import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3eba733fa9f2c06726496269a61178a6"
# Your Auth Token from twilio.com/console
auth_token = "8ba968b091b74445de33ae3151d06ae8"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        Vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        Vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguem bateu a meta. Vendedor:{Vendedor} , Vendas: {Vendas}')
        message = client.messages.create(
            to="+5541998239594",
            from_="+19388887041",
            body=f'No mês de {mes} alguem bateu a meta. vendedor:{Vendedor} , vendas: {Vendas}')
        print(message.sid)
