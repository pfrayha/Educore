from educore.manager_interfaces import IPeopleManager

from flask import render_template, flash, redirect, url_for
from sqlalchemy.exc import InternalError, DataError, IntegrityError

from ..forms.neam_forms import AddOrEditAlunoAprendizForm, AddOrEditVoluntarioForm

import logging

logging.basicConfig(filename = 'logging.log', level=logging.INFO, format='date:' + '%(asctime)s' + ' name:'+'%(name)s'+' message:'+'%(message)s')
logger = logging.getLogger('neam_people')

class NeamPeopleManager(IPeopleManager):
    @staticmethod
    def get_registration_form(model, id=None):
        from ..models import Pessoa
        from ..utils import valida_cpf_cep_matricula, formata_strings, formata_lista
        from app import db
        if not id:
            add_aluno = True

            if(model == 'aluno' or model == 'aprendiz'):
                form = AddOrEditAlunoAprendizForm()
            else:
                form = AddOrEditVoluntarioForm()

            # load usuario template
            return render_template('people/add_or_edit_pessoa.html', action="Add", add_aluno=add_aluno, tipo=model, form=form, title="Add Aluno")
        else:
            add_aluno = False
            pessoa = db.session.query(Pessoa).get_or_404(id)

            if(pessoa.tipo == 'aluno' or pessoa.tipo == 'aprendiz'):
                form = AddOrEditAlunoAprendizForm(obj=pessoa)
            else:
                form = AddOrEditVoluntarioForm(obj=pessoa)

            form.nome.data = pessoa.nome
            form.email.data = pessoa.email
            form.celular.data = pessoa.celular
            form.foto.data = pessoa.foto
            form.sexo.data = pessoa.sexo
            form.data_ingresso.data = pessoa.data_ingresso

            if pessoa.tipo == 'aluno' or pessoa.tipo == 'aprendiz':
                form.data_nascimento.data = pessoa.data_nascimento
                form.identificador_tipo.data = pessoa.identificador_tipo
                form.identificador_numero.data = pessoa.identificador_numero
                form.identificador_complemento.data = pessoa.identificador_complemento
                form.endereco_numero.data = pessoa.endereco_numero
                form.endereco_rua.data = pessoa.endereco_rua
                form.endereco_complemento.data = pessoa.endereco_complemento
                form.endereco_bairro.data = pessoa.endereco_bairro
                form.endereco_cidade.data = pessoa.endereco_cidade
                form.endereco_uf.data = pessoa.endereco_uf
                form.endereco_cep.data = pessoa.endereco_cep
                form.nome_responsavel.data = formata_lista(pessoa.nome_responsavel)
                form.telefone_responsavel.data = formata_lista(pessoa.telefone_responsavel)
                form.profissao_responsavel.data = formata_lista(pessoa.profissao_responsavel)
                form.dificuldade.data = formata_lista(pessoa.dificuldade)
                form.serie.data = pessoa.serie
                form.escolaridade_nivel.data = pessoa.escolaridade_nivel
                form.escolaridade_turno.data = pessoa.escolaridade_turno
                form.nome_instituicao.data = pessoa.nome_instituicao
            else:
                form.curso_puc.data = pessoa.curso_puc
                form.matricula_puc.data = pessoa.matricula_puc

            if pessoa.desligamento_data:
                form.desligamento_data.data = pessoa.desligamento_data
                form.desligamento_motivo.data = pessoa.desligamento_motivo
                form.desligamento_destino.data = pessoa.desligamento_destino
                desligado = True
            else:
                desligado = False

            return render_template('people/add_or_edit_pessoa.html', action="Edit",
                           add_aluno=add_aluno,desligado=desligado, form=form,
                           pessoa=pessoa,tipo=pessoa.tipo, title="Edit Aluno")


    @staticmethod
    def submit_registration_form(model, id=None):
        from ..models import Pessoa
        from ..utils import valida_cpf_cep_matricula, formata_strings, formata_lista
        from app import db

        if not id:
            if(model == 'aluno' or model == 'aprendiz'):
                form = AddOrEditAlunoAprendizForm()
            else:
                form = AddOrEditVoluntarioForm()

            if form.validate_on_submit():
                logger.error("Called validate")

                if form.foto.data:
                    img_64b = base64.b64encode(form.foto.data.read())
                else:
                    img_64b = None

                if isinstance(form, AddOrEditAlunoAprendizForm):
                    pessoa = Pessoa(nome=form.nome.data, email=form.email.data, foto=img_64b, celular=form.celular.data, sexo=form.sexo.data, data_nascimento=form.data_nascimento.data, data_ingresso=form.data_ingresso.data, identificador_tipo=form.identificador_tipo.data, identificador_numero=form.identificador_numero.data, identificador_complemento=form.identificador_complemento.data, endereco_numero=form.endereco_numero.data, endereco_rua=form.endereco_rua.data, endereco_complemento=form.endereco_complemento.data, endereco_bairro=form.endereco_bairro.data, endereco_cidade=form.endereco_cidade.data, endereco_uf=form.endereco_uf.data, endereco_cep=form.endereco_cep.data, tipo=model, nome_responsavel= '{"'+form.nome_responsavel.data+'"}', telefone_responsavel='{"'+form.telefone_responsavel.data+'"}', profissao_responsavel='{"'+form.profissao_responsavel.data+'"}', dificuldade='{"'+form.dificuldade.data+'"}', serie=form.serie.data, escolaridade_nivel=form.escolaridade_nivel.data, escolaridade_turno=form.escolaridade_turno.data, nome_instituicao=form.nome_instituicao.data)
                else:
                    pessoa = Pessoa(nome=form.nome.data, email=form.email.data, foto=img_64b, celular=form.celular.data, sexo=form.sexo.data, data_ingresso=form.data_ingresso.data, desligamento_data = form.desligamento_data.data, desligamento_motivo = form.desligamento_motivo.data, curso_puc=form.curso_puc.data, matricula_puc=form.matricula_puc.data, tipo=model)

                logger.error(f"Created pessoa {pessoa.nome}")
                if pessoa.tipo == 'voluntario':
                    if not valida_cpf_cep_matricula(pessoa.matricula_puc, 'Mat'):
                        return render_template('errors/500.html', msg="Matrícula PUC inválida! Ela deve conter 7 dígitos!")
                    pessoa.matricula_puc = formata_strings(pessoa.matricula_puc)
                else:
                    if (pessoa.endereco_cidade == None) or (pessoa.endereco_cep == None) or (pessoa.endereco_bairro == None) or (pessoa.endereco_rua == None) or (pessoa.endereco_numero == None):
                        return render_template('errors/500.html', msg="Todos os campos referentes ao endereço devem ser preenchidos.")
                    pessoa.identificador_numero = formata_strings(pessoa.identificador_numero)
                    pessoa.endereco_cep = formata_strings(pessoa.endereco_cep)
                    pessoa.endereco_bairro = pessoa.endereco_bairro.strip().title()

                logger.error("Passed address check")

                if pessoa.identificador_tipo == 'CPF' and not valida_cpf_cep_matricula(pessoa.identificador_numero, 'CPF'):
                    return render_template('errors/500.html', msg='CPF inválido! Ele deve conter 11 dígitos!')

                logger.error("Passed CPF check")

                if pessoa.tipo!='voluntario' and not valida_cpf_cep_matricula(pessoa.endereco_cep, 'CEP'):
                    logger.error("Failed CEP check")
                    return render_template('errors/500.html', msg="CEP inválido! Ele deve conter 8 dígitos!")

                logger.error("Passed CEP check")

                if pessoa.nome_instituicao == '':
                    pessoa.nome_instituicao = None

                msg = None
                try:
                    logger.error("Adding pessoa")
                    db.session.add(pessoa)
                    logger.error("Added pessoa")
                    db.session.commit()
                except IntegrityError as ie:
                    logger.info(ie)
                    if 'matricula_puc_key' in str(ie):
                        msg = 'A matrícula do voluntário já foi cadastrada.'
                    elif 'pessoa_email_key' in str(ie):
                        msg = 'Este email já foi cadastrado.'
                    else:
                        msg = "genericoPessoa"
                except DataError as de:
                    logger.info(de)
                    if 'responsável completos' in str(de):
                        msg = 'Um aprendiz ou aluno deve possuir os dados do seu responsável completos.'
                    elif 'instituição de origem' in str(de): 
                        msg = 'Um aluno ou aprendiz deve possuir os dados da sua instituição de origem.'
                    elif 'voluntário deve possuir' in str(de):
                        msg = 'Um voluntário deve possuir os dados de matrícula e curso na PUC.'
                    else:
                        msg = "genericoPessoa"
                except Exception as e:
                    logger.info(e)
                    msg = "genericoPessoa"
                finally:
                    if msg:
                        db.session.rollback()
                        logger.info(msg)
                        return render_template('errors/500.html', msg=msg)


                # flash( pessoa.tipo+' criado com sucesso')
                # redirect to usuarios page
                return redirect(url_for('people.list_people',model=model))
        else:
            pessoa = db.session.query(Pessoa).get_or_404(id)

            if(pessoa.tipo == 'aluno' or pessoa.tipo == 'aprendiz'):
                form = AddOrEditAlunoAprendizForm(obj=pessoa)
            else:
                form = AddOrEditVoluntarioForm(obj=pessoa)

            if form.validate_on_submit():

                if form.foto.data:
                    img_64b = base64.b64encode(form.foto.data.read())
                    pessoa.foto = img_64b

                pessoa.nome = form.nome.data
                pessoa.email = form.email.data
                pessoa.celular = form.celular.data
                pessoa.sexo = form.sexo.data
                pessoa.data_ingresso = form.data_ingresso.data
                
                if form.desligamento_data.data:
                    pessoa.desligamento_data = form.desligamento_data.data
                    pessoa.desligamento_motivo = form.desligamento_motivo.data
                    pessoa.desligamento_destino = form.desligamento_destino.data

                if pessoa.tipo == 'aluno' or pessoa.tipo == 'aprendiz':
                    pessoa.data_nascimento = form.data_nascimento.data
                    pessoa.identificador_tipo = form.identificador_tipo.data
                    pessoa.identificador_numero = form.identificador_numero.data
                    pessoa.identificador_complemento = form.identificador_complemento.data
                    pessoa.endereco_numero = form.endereco_numero.data
                    pessoa.endereco_rua = form.endereco_rua.data
                    pessoa.endereco_complemento = form.endereco_complemento.data
                    pessoa.endereco_bairro = form.endereco_bairro.data
                    pessoa.endereco_cidade = form.endereco_cidade.data
                    pessoa.endereco_uf = form.endereco_uf.data
                    pessoa.endereco_cep = form.endereco_cep.data
                    pessoa.nome_responsavel = '{"'+ form.nome_responsavel.data+'"}'
                    pessoa.telefone_responsavel = '{"' + form.telefone_responsavel.data +'"}'
                    pessoa.profissao_responsavel =  '{"' + form.profissao_responsavel.data +'"}'
                    pessoa.dificuldade =  '{"' + form.dificuldade.data +'"}'
                    pessoa.serie = form.serie.data
                    pessoa.escolaridade_nivel = form.escolaridade_nivel.data
                    pessoa.escolaridade_turno = form.escolaridade_turno.data
                    pessoa.nome_instituicao = form.nome_instituicao.data
                    if (pessoa.endereco_cidade == None) or (pessoa.endereco_cep == None) or (pessoa.endereco_bairro == None) or (pessoa.endereco_rua == None) or (pessoa.endereco_numero == None):
                        return render_template('errors/500.html', msg="Todos os campos referentes ao endereço devem ser preenchidos.") 
                    # Formata as strings do formulario (tira '.', '-' e espaços no fim)
                    pessoa.identificador_numero = formata_strings(pessoa.identificador_numero)
                    pessoa.endereco_cep = formata_strings(pessoa.endereco_cep)
                    pessoa.endereco_bairro = pessoa.endereco_bairro.strip().title()
                else:
                    pessoa.curso_puc = form.curso_puc.data
                    pessoa.matricula_puc = form.matricula_puc.data
                    pessoa.matricula_puc = formata_strings(pessoa.matricula_puc)
                    if not valida_cpf_cep_matricula(pessoa.matricula_puc, 'Mat'):
                        return render_template('errors/500.html', msg="Matrícula PUC inválida! Ela deve conter 7 dígitos!")

                # verifica se tamanho do CPF e CEP são válidos
                if pessoa.identificador_tipo == 'CPF' and not valida_cpf_cep_matricula(pessoa.identificador_numero, 'CPF'):
                    return render_template('errors/500.html', msg='CPF inválido! Ele deve conter 11 dígitos!')

                if pessoa.tipo!='voluntario' and not valida_cpf_cep_matricula(pessoa.endereco_cep, 'CEP'):
                    return render_template('errors/500.html', msg="CEP inválido! Ele deve conter 8 dígitos!")

                if pessoa.nome_instituicao == '':
                    pessoa.nome_instituicao = None
                
                msg = None
                try:
                    db.session.commit()
                    flash('%s editado com sucesso.' % pessoa.tipo)
                except IntegrityError as ie:
                    logger.info(ie)
                    if 'matrícula' in str(ie):
                        msg = 'A matrícula do voluntário já foi cadastrada.'
                    elif 'pessoa_email_key' in str(ie):
                        msg = 'Este email já foi cadastrado.'
                    else:
                        msg = "genericoPessoa"
                except DataError as de:
                    logger.info(de)
                    if 'responsável completos' in str(de):
                        msg = 'Um aprendiz ou aluno deve possuir os dados do seu responsável completos.'
                    elif 'instituição de origem' in str(de): 
                        msg = 'Um aluno ou aprendiz deve possuir os dados da sua instituição de origem.'
                    elif 'voluntário deve possuir' in str(de):
                        msg = 'Um voluntário deve possuir os dados de matrícula e curso na PUC.'
                    else:
                        msg = "genericoPessoa"
                except Exception as e:
                    logger.info(e)
                    msg = "genericoPessoa"
                finally:
                    if msg:
                        db.session.rollback()
                        logger.info(msg)
                        return render_template('errors/500.html', msg=msg)

                # redirect to the alunos page
                return redirect(url_for('people.list_people',model=model))