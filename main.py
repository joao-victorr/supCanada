from IPython.display import display
import pandas as pd

# Caminho para o arquivo Excel
file_path = "teste.xlsx"

# Lendo o arquivo Excel
table = pd.read_excel(file_path)

# Contar a frequência de cada tipo  # Contar a frequência de cada categoria
category_counts = table['type'].value_counts()

# Selecionar as 10 primeiras categorias com mais produtos
# top_10_categories = category_counts.head(20)

# Exibir as 10 categorias com mais produtos
# print(top_10_categories)

category_counts.to_excel("category.xlsx")

# Exibir a tabela modificada
# display(table)
