import pandas as pd
from datetime import datetime
import time
import pyperclip

fileDB = (f'C:\\TSC\\Data\\Cuentas_GMAIL.xlsx')
day = int(datetime.now().strftime("%d"))
hour = int(time.strftime("%H"))
accounts = []

try:

    data = pd.read_excel(fileDB, skiprows=0, sheet_name="Cuentas")
    df = pd.DataFrame(data)
    columnas = ['Dia', 'Cuenta', 'Contraseña']
    def buscar():
        info = df[df['Dia']==day]
        return(info)

    df_seleccionados = buscar()[columnas]
    
    for index, row in df_seleccionados.iterrows():
        account = (row['Cuenta'])
        accounts.append(account)

    if hour < 12:
        pyperclip.copy(accounts[0])

    else:
        pyperclip.copy(accounts[1])

except Exception as e:
    print(e)