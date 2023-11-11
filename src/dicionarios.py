#criando dicionários

dicionario = {}
dicionario = dict()

dicionario = {'nome': 'Ana', 'idade': 20, 'altura': 1.77}

print(dicionario['idade'])

#adicionando elementos

dicionario['programador'] = True
print(dicionario)
dicionario['altura'] = 2
print(dicionario)

#iterando sobre um dicionario

#percorre as chaves do dicionário
for chave in dicionario:
    print(chave, dicionario[chave])

#verifica se a chave existe no dicionário
print('peso' in dicionario)
print('altura' in dicionario)