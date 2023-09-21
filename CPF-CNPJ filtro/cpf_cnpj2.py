from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Documento Inválido!")


class Cpf:
    def __init__(self, documento):
        if self.validador_de_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def validador_de_cpf(self, documento):
        validador_cpf = CPF()
        return validador_cpf.validate(documento)

    # Formata o cpf EX: 000.000.000-00
    def formata_cpf(self):
        formatacao_cpf = CPF()
        return formatacao_cpf.mask(self.cpf)

    # Retorna/Imprime a formatação do cpf
    def __str__(self):
        return self.formata_cpf()



class Cnpj:
    def __init__(self, documento):
        if self.validador_de_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ Inválido!")


    def validador_de_cnpj(self, cnpj):
            validador_cnpj = CNPJ()
            return validador_cnpj.validate(cnpj)

    # Formata o cnpj
    def formata_cnpj(self):
        formatacao_cnpj = CNPJ()
        return formatacao_cnpj.mask(self.cnpj)

    def __str__(self):
        return self.formata_cnpj()

