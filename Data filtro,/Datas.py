# Biblioteca utilizado para facilitar na estração de Horas e Dias/meses/ano
from datetime import datetime, timedelta

class Data:
    def __init__(self):
        self.momento_cadastro = datetime.today()       # Aciona a biblioteca de datas

# Retorna o mes na qual o cliente realizou um possivel cadastro
    def mes_cadastro(self):
        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto",
                 "Setembro", "Outubro", "Novembro", "Dezembro"]

        mes_de_cadastro = self.momento_cadastro.month - 1
        return meses[mes_de_cadastro]

    def __str__(self):
        return self.data_formatada()


# Retorna o dia da semana na qual o cliente relizou um possivel cadastro
    def dia_cadastro(self):
        dia = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"]

        dia_de_cadastro = self.momento_cadastro.weekday()
        return dia[dia_de_cadastro]

# comandos fornecidos pela biblioteca para formatar a data
    # %d - dia/ %m - mês/ %Y - ano      %H - hora   %M - minutos
    def data_formatada(self):
        data_f = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_f
