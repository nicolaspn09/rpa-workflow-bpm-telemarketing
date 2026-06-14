#python -m pip install llama-parse
import os
from llama_parse import LlamaParse

#Salva na variável de ambiente
os.environ["LLAMA_CLOUD_API_KEY"] = "llx-KDzlAf55u5jSaemsCy69wburm5tZxDJlWkFzlk7edwd9xnCm"

#caminho_arquivo = r"C:\Users\ACER\OneDrive\Cursos online\Treinamento Python - Hashtag\Códigos\Llama\resultado.pdf"
caminho_arquivo = r"C:\Users\Nícolas Nasário\Downloads\PDF\PEDIDO KOLESTON.pdf"

#Resultado
#documentos = LlamaParse(result_type = "markdown", parsing_instruction="This file contais text and table, I'd like to get only the tables from the text").load_data(caminho_arquivo) #Formatos: markdown ou text
documentos = LlamaParse(result_type = "markdown", language="pt", parsing_instruction="Você é um especialista em leitura de imagens, vou te enviar um texto extraído de um arquivo em PDF, é composto por uma tabela com os itens, em que temos um cabeçalho com o número do pedido, cotação do cliente, CNPJ e, logo abaixo, uma tabela com os itens, quero que você me retorne em cada linha de EAN: EAN, número do pedido (ou cotação), CNPJ, desconto do item, a descrição dos itens, a quantidade de todos os itens cotados e o valor total de cada item. Um ponto importante: Essas informações devem formar uma linha a cada item da tabela, pode acontecer de o pedido estar em uma página e o restante, em outra página, você deve perceber isso e fazer a unificação com o pedido da página anterior. Exemplos de dados: #EAN: 7890123456789 (o EAN costuma ter 13 dígitos), #Número do pedido: 123456 (geralmente são 6 dígitos), #CNPJ: 82.873.068/0001-40 (normalmente com 14 dígitos, separados pelos caracteres '.', '/' ou '-'), #Quantidade: geralmente um valor decimal (fica ao lado do valor do item). O retorno que quero na sua saída é o seguinte: EAN: x | Número do pedido: x | CNPJ: x | Desconto: x | Descrição do item: x | Quantidade: x | Valor do item: x.").load_data(caminho_arquivo) #Formatos: markdown ou text

lista_textos = []

for i, pagina in enumerate(documentos):
    texto_pagina = pagina.text
    texto_pagina = texto_pagina.replace("# Relatório de Itens", "")
    lista_textos.append(texto_pagina)
    print(pagina.text)
    # with open(rf"C:\Users\ACER\OneDrive\Cursos online\Treinamento Python - Hashtag\Códigos\Llama\Extração\Pagina_{i + 1}.md", "w", encoding="utf-8") as arquivo:
    #     arquivo.write(pagina.text)