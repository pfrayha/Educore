from educore.manager_interfaces import IPeopleManager

from flask import render_template, flash, redirect, url_for
from ..forms.guardian_forms import AddOrEditGuardianForm
from ..forms.student_forms import AddOrEditStudentForm

import logging

logging.basicConfig(filename = 'logging.log', level=logging.INFO, format='date:' + '%(asctime)s' + ' name:'+'%(name)s'+' message:'+'%(message)s')
logger = logging.getLogger('people')

class PeopleManager(IPeopleManager):
    @staticmethod
    def get_registration_form(model, id=None):
        from ..models import Guardian, Student
        from app import db
        
        if model == 'guardian':
            guardian = db.session.query(Guardian).get_or_404(id) if id else None
            form = AddOrEditGuardianForm(obj=guardian)
            return render_template('people/add_or_edit_guardian.html', form=form, guardian=guardian)
        elif model == 'student':
            student = db.session.query(Student).get_or_404(id) if id else None
            form = AddOrEditStudentForm(obj=student)
            form.guardian_id.choices = [(t.id, t.name) for t in Guardian.query.order_by("name")]
            return render_template('people/add_or_edit_student.html', form=form, student=student)

    @staticmethod
    def submit_registration_form(model, id=None):
        from ..models import Guardian, Student
        from app import db

        if model == 'guardian':
            if id:
                guardian = db.session.query(Guardian).get_or_404(id)
                form = AddOrEditGuardianForm(obj=guardian)
                if form.validate_on_submit():
                    guardian.name = form.name.data
                    guardian.email = form.email.data
                    guardian.cpf = form.cpf.data
                    guardian.cellphone = form.cellphone.data
                    guardian.housephone = form.housephone.data
                    
                    guardian.address_number = form.address_number.data
                    guardian.address_street = form.address_street.data
                    guardian.address_complement = form.address_complement.data
                    guardian.address_neighborhood = form.address_neighborhood.data
                    guardian.address_city = form.address_city.data
                    guardian.address_uf = form.address_uf.data
                    guardian.address_cep = form.address_cep.data

                    new_guardian = False
                    action = 'editado'
            else:
                logger.error("Attempted to create guardian")
                form = AddOrEditGuardianForm()
                guardian = Guardian(
                    name = form.name.data,
                    email = form.email.data,
                    cpf = form.cpf.data,
                    cellphone = form.cellphone.data,
                    housephone = form.housephone.data,

                    address_number = form.address_number.data,
                    address_street = form.address_street.data,
                    address_complement = form.address_complement.data,
                    address_neighborhood = form.address_neighborhood.data,
                    address_city = form.address_city.data,
                    address_uf = form.address_uf.data,
                    address_cep = form.address_cep.data
                )
                new_guardian = True
                action = 'criado'

            try:
                msg=None
                db.session.add(guardian) if new_guardian else None
                db.session.commit()

            # except IntegrityError as ie:
            #     logger.info(ie)
            #     msg = str(ie)
            # except DataError as de:
            #     logger.info(de)
            #     msg = str(de)
            except Exception as e:
                logger.error(e)
                msg = str(e)
            finally:
                if msg:
                    db.session.rollback()
                    logger.info(msg)
                    return render_template('errors/500.html', msg=msg)

            flash( f'Responsável {action} com sucesso')
            # redirect to usuarios page
            return redirect(url_for(f'people.list_people',model='guardian'))

        elif model == 'student':
            student = db.session.query(Student).get_or_404(id) if id else None
            form = AddOrEditStudentForm(obj=student)
            if id:
                form.guardian_id.choices = [(t.id, t.name) for t in Guardian.query.order_by("name")]
                if form.validate_on_submit():
                    
                    student.name = form.name.data
                    student.guardian_id = form.guardian_id.data

                    new_student = False
                    action = 'editado'
            else:
                student = Student(
                    name = form.name.data,
                    guardian_id = form.guardian_id.data
                )
                new_student = True
                action = 'criado'

            try:
                msg=None
                db.session.add(student) if new_student else None
                db.session.commit()

            # except IntegrityError as ie:
            #     logger.info(ie)
            #     msg = str(ie)
            # except DataError as de:
            #     logger.info(de)
            #     msg = str(de)
            except Exception as e:
                logger.error(e)
                msg = str(e)
            finally:
                if msg:
                    db.session.rollback()
                    logger.info(msg)
                    return render_template('errors/500.html', msg=msg)

            flash( f'Aluno {action} com sucesso')
            # redirect to usuarios page
            return redirect(url_for(f'people.list_people',model='student'))

    @staticmethod
    def list_people(model):
        if model == 'student':
            from app import db
            from ..models import Student

            students = db.session.query(Student).all()

            return render_template('people/list_students.html',students=students)
    
    @staticmethod
    def delete_person(model, id):
        if model == 'student':
            from app import db
            from ..models import Student

            target = db.session.query(Student).get_or_404(id)

        elif model == 'guardian':
            from app import db
            from ..models import Guardian

            target = db.session.query(Guardian).get_or_404(id)
        
        else: 
            target = None

        try:
            msg = None
            if target:
                db.session.delete(target)
                db.session.commit()

        # except IntegrityError as ie:
        #     logger.info(ie)
        #     msg = str(ie)
        # except DataError as de:
        #     logger.info(de)
        #     msg = str(de)
        except Exception as e:
            logger.error(e)
            msg = str(e)
        finally:
            if msg:
                db.session.rollback()
                logger.info(msg)
                return render_template('errors/500.html', msg=msg)
            
            return redirect(url_for(f'people.list_people',model=model))