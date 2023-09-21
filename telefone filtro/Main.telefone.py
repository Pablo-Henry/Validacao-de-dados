from Telefone_Regex import Telefone
# import re
telefone = "551194692887"
print(len(telefone))


# padrao = ("([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([-]?)([0-9]{4})")
#
# buscaltell = re.search(padrao, telefone)

telefone_obj = Telefone(telefone)

print(telefone_obj)











# []	Define um range ou um grupo de caracteres	[0-9]; [a-z]; [abc]
# *	Marca nenhuma, uma ou mais ocorrências	sol*
# {}	Quantidade de repetições de uma ocorrência definida	[abc]{5}
# \d	Qualquer número de 0 até 9	\d{3,4}
# \w	Qualquer número de a té 9 letra de a até z ou _	\w{10}
# |	Um ou outro	@$
# ()	Captura e agrupa	(\w{4})



