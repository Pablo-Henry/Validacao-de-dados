from cep import BuscaEndereco
cep = "06813180"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)
