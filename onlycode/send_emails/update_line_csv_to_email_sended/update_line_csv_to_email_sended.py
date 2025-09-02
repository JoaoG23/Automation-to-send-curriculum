import pandas as pd
import os

def update_line_csv_to_email_sended(index, path_file_imports: str):
    try:
        df = pd.read_csv(path_file_imports, sep=';', encoding='utf-8')
        
        # Verificar se o índice é válido
        if index >= len(df):
            print(f"Índice {index} fora do range do DataFrame")
            return False
        
        # Verificar se a coluna 'Enviado' existe
        if 'Enviado' not in df.columns:
            print("Coluna 'Enviado' não encontrada no CSV")
            return False
        
        # Atualizar a linha
        df.loc[index, 'Enviado'] = 'SIM'
        
        # Salvar o arquivo
        df.to_csv(path_file_imports, sep=';', index=False, encoding='utf-8')
        return True
        
    except Exception as e:
        print(f"Erro ao atualizar CSV: {e}")
        return False

