import pandas as pd


def verify_email_sent_by_line_csv(index):
    df = pd.read_csv('import/jobs.csv', sep=';', encoding='utf-8')
    
    line_email_sent = df.loc[index, 'Enviado']
    
    if line_email_sent == 'SIM':
        return True    
    return False
    
    