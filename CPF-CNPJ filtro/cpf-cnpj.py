# Biblioteca que contém um válidador de cpf/cnpj e uma máscara de formatação já criada
from validate_docbr import CPF, CNPJ

class Cpf_Cnpj:
    def __init__(self, documento, tipo_de_documento):
        self.tipo_de_documento = tipo_de_documento
        documento = str(documento)
        if self.tipo_de_documento == "CPF":
    # Se o cpf tiver 11 caracteres o cpf é válido
            if self.validador_de_cpf(documento):
                self.cpf = documento
            else:
    # Caso o cpf não tenha a quantidade necessária de digitos cpf inválido
                raise ValueError("CPF Inválido!")
        # Se o cnpj tiver 11 caracteres o cnpj é válido
        elif self.tipo_de_documento == "CNPJ":
            if self.validador_de_cnpj(documento):
                self.cnpj = documento
            else:
                # Caso o cnpj não tenha a quantidade necessária de digitos cnpj inválido
                raise ValueError("CNPJ Inválido!")


    # Válida a quantidade de caracteres necessárias para ser um cpf
    def validador_de_cpf(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            validador.validate(cpf)
            return True
        else:
            raise ValueError("Quantidade de caracteres inválida")


    # Válida a quantidade de caracteres necessárias para ser um cnpj
    def validador_de_cnpj(self, cnpj):
        if len(cnpj) == 14:
            validador_cnpj = CNPJ()
            validador_cnpj.validate(cnpj)
            return True
        else:
            raise ValueError("Quantidade de caracteres inválida")


    # Formata o cpf EX: 000.000.000-00
    def formata_cpf(self):
        formatacao_cpf = CPF()
        return formatacao_cpf.mask(self.cpf)


    # Formata o cpf EX: 000.000.000-00
    def formata_cnpj(self):
        formatacao_cnpj = CNPJ()
        return formatacao_cnpj.mask(self.cnpj)


    # Retorna/Imprime a formatação do cpf
    def __str__(self):
        if self.tipo_de_documento == "CPF":
            return self.formata_cpf()
        elif self.tipo_de_documento == "CNPJ":
            return self.formata_cnpj()




