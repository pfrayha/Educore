def converte_data(data):
	
	data_convertida = [None]*10

	data_convertida[2] = '/'
	data_convertida[5] = '/'

	for i in range(0,10):
		if(i < 4):
			data_convertida[i+6] = str(data)[i]

		if(i > 4 and i < 7):
			data_convertida[i-2] = str(data)[i]

		if(i > 7 and i < 10):
			data_convertida[i-8] = str(data)[i]

	return ''.join(data_convertida)


def formata_lista(lst):
    s1 = ""
    if lst:
        for item in lst:
            if item!="" and (item[0] == "'" or item[0] == "["):
                s1+=item.split("'")[1]+','
            else:
                s1+=item
    if s1!="" and s1[-1] == ",":
        s1 = s1[:-1]
    return s1


def formata_strings(num):

    str = num.replace('.', '')
    str = str.replace('-', '')
    str = str.replace(' ', '')

    return str

def valida_cpf_cep_matricula(num, tipo):

    if tipo == 'CPF' and len(num) != 11:
            return False
    elif tipo == 'CEP' and len(num) != 8:
            return False
    elif tipo == 'Mat' and len(num)>0 and len(num) != 7: 
            return False

    return True

def separa_lista(lst):
    s1 = ""
    if lst:
        for item in lst:
            s1+=item + ','
    if s1!="" and s1[-1] == ",":
        s1 = s1[:-1]
    return s1

# select pk_nome_atividade_neam from cursa where pk_matricula_neam_pessoa = x
# select pk_nome_evento from participa where pk_matricula_neam_pessoa = x

