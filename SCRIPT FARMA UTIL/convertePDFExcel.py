import camelot
import pandas as pd

# Caminho para o arquivo PDF
pdf_file = r"C:\Users\Nícolas Nasário\Downloads\PDF\PEDIDO KOLESTON.pdf"

# Extrair todas as tabelas do PDF
tabelas = camelot.read_pdf(pdf_file, pages='all')

# Verificar quantas tabelas foram encontradas
print(f'{len(tabelas)} tabelas encontradas.')

# Criar um writer do Excel para salvar as tabelas
with pd.ExcelWriter(r"C:\Users\Nícolas Nasário\Downloads\PDF\PEDIDO KOLESTON.xlsx", engine='openpyxl') as writer:
    for idx, tabela in enumerate(tabelas):
        # Converter cada tabela em DataFrame
        df = tabela.df
        # Salvar cada tabela em uma aba separada
        df.to_excel(writer, sheet_name=f'Tabela_{idx+1}', index=False)

print("PDF convertido para Excel com sucesso!")