import requests #bibliotaca para acesso de api
class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.validador_cep(cep):
            self.cep = cep
        else:
            raise ValueError("O CEP é Inválido!!")

    def __str__(self):
        return self.formata_cep()

    def validador_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formata_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

# Cria uma URL passando para ela o cep na qual a gente deseja
    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        print(url)
        r = requests.get(url)
# Json() um método utilizado para fazer requests mais facilmente
# Utilizando o Json() conseguimos retornar as informações passadas no return com mais facilidade
        dados = r.json()
        return (dados['bairro'], dados['localidade'], dados['uf'])