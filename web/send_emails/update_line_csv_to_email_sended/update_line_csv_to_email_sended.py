import pandas as pd

def update_line_csv_to_email_sended(index):
    df = pd.read_csv('import/jobs.csv', sep=';', encoding='utf-8')
    df['Enviado'] = df['Enviado'].astype('string')
    
    df.loc[index, 'Enviado'] = 'SIM'
    df.fillna('', inplace = True)
    
    df.to_csv('import/jobs.csv', index=False , encoding='utf-8', sep=';')

