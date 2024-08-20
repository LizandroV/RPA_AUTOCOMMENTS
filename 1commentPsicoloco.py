import pandas as pd
import random
import pyperclip

fileDB = (f'C:\\TSC\\Data\\Cuentas_GMAIL.xlsx')
randid = random.randint(1,150)

try:

    data = pd.read_excel(fileDB, skiprows=0, sheet_name="FrasesPsicologo")
    df = pd.DataFrame(data)
    columnas = ['ID', 'Comment']
    def buscar():
        info = df[df['ID']==randid]
        return(info)

    df_seleccionados = buscar()[columnas]
    
    for index, row in df_seleccionados.iterrows():
        comment = (row['Comment'])
    pyperclip.copy(comment)

except Exception as e:
    print(e)