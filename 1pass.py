import pandas as pd
from datetime import datetime
import time
import pyperclip

fileDB = (f'C:\\TSC\\Data\\Cuentas_GMAIL.xlsx')
day = int(datetime.now().strftime("%d"))
hour = int(time.strftime("%H"))
passwords = []

try:

    data = pd.read_excel(fileDB, skiprows=0, sheet_name="Cuentas")
    df = pd.DataFrame(data)
    columnas = ['Dia', 'Cuenta', 'Contraseña']
    def buscar():
        info = df[df['Dia']==day]
        return(info)

    df_seleccionados = buscar()[columnas]
    
    for index, row in df_seleccionados.iterrows():
        psw = (row['Contraseña'])
        passwords.append(psw)

    if hour < 12:
        pyperclip.copy(passwords[0])

    else:
        pyperclip.copy(passwords[1])

except Exception as e:
    print(e)