# Biblioteca utilizado para realizar as funções com Regex
import re

class Telefone:
    # Caso o telefone seja válido, transforma ele em um número, caso não sejá retorna um erro
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número inválido, a quantidade de caracteres não corresponde com a exigida")

    def __str__(self):
        return self.formata_numero()

    # Busca o telefone em meio as informações, utilizando um padrão que foi passado
    def valida_telefone(self, telefone):
        padrao = ("([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})")
        retorno_padrao = re.findall(padrao, telefone)
        if retorno_padrao:
            return True
        else:
            return False

    # Faz a formatação dos números de telefone
    def formata_numero(self):
        padrao = ("([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})")
        buscatell = re.search(padrao, self.numero)
        formatacao = f"+{buscatell.group(1)} ({buscatell.group(2)}) {buscatell.group(3)}-{buscatell.group(4)}"
        return formatacao




