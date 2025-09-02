import pandas as pd
import os


def verify_email_sent_by_line_csv(index, path_file_imports: str):
    try:
        df = pd.read_csv(path_file_imports, sep=';', encoding='utf-8')
        
        # Verificar se o índice é válido
        if index >= len(df):
            return False
        
        # Verificar se a coluna 'Enviado' existe
        if 'Enviado' not in df.columns:
            return False
        
        line_email_sent = df.loc[index, 'Enviado']
        return line_email_sent == 'SIM'
        
    except Exception as e:
        print(f"Erro ao verificar email: {e}")
        return False
    
    