# Teste com cpf_cnpj2

from cpf_cnpj2 import Documento

cpf_cnpj = int(input("Informe o Número do seu CPF ou CNPJ (Somente Números): "))
cpf_cnpj = str(cpf_cnpj)

if len(cpf_cnpj) == 11:
    obj_cpf = Documento.cria_documento(cpf_cnpj)
    print(obj_cpf)

elif len(cpf_cnpj) == 14:
    obj_cnpj = Documento.cria_documento(cpf_cnpj)
    print(obj_cnpj)

else:
    raise ValueError("Documento inválido!!")







# Teste com cpf_cnpj
# from cpf_cnpj import Cpf_Cnpj
#
# cpf_cnpj1 = input("Informe o tipo de Document: <CPF> - <CNPJ>")
#
# if cpf_cnpj1 == "CPF":
#     cpf = int(input("Informe o Número do seu CPF(Somente Números): "))
#     obj_cpf1 = Cpf_Cnpj(cpf, "CPF")
#     print(obj_cpf1)
# elif cpf_cnpj1 == "CNPJ":
#     cnpj = int(input("Informe o Número do seu CNPJ(Somente Números): "))
#     obj_cnpj1 = Cpf_Cnpj(cnpj, "CNPJ")
#     print(obj_cnpj1)
# else:
#     raise ValueError("Documento inválido")

































