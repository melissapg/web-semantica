import pandas as pd

foodon_codes = pd.read_csv('data/csv/foodon_codes.csv', encoding='utf-8')
tbca = pd.read_csv('data/csv/tbca.csv')


# Função para formatar os valores de acordo com a métrica
def format_value(value, metric):
    if pd.notna(value) or value not in ['tr', 'nan', 'null', 'NA', 'None']:
        return f"{value} {metric}"
    return value

columns_to_format = tbca.columns[7:47]
for col in columns_to_format:
    # Converter colunas numéricas para strings (se necessário)
    if tbca[col].dtype == 'object':
        tbca[col] = tbca[col].str.replace(',', '.')
    metric = col.split('(')[-1].rstrip(')')
    tbca[col] = tbca[col].apply(lambda x: format_value(x, metric))

# converte para minuscula
tbca['nome_cientifico'] = tbca['nome_cientifico'].str.lower()
foodon_codes['NarrowSynonym'] = foodon_codes['NarrowSynonym'].str.lower()
merged_df = tbca.merge(foodon_codes, left_on='nome_cientifico', right_on='NarrowSynonym', how='left')

merged_df.drop(columns=['nome_ingles', 'grupo', 'marca', 'url', 'Energia (kJ)', 'Carboidrato disponível (g)',
                        'Gordura de adição (g)', 'Proteína animal (g)', 'Proteína vegetal (g)', 'Colesterol (g)',
                        'Code', 'NarrowSynonym'], inplace=True)

merged_df.rename(columns={'Cod': 'codigo_FoodOn'}, inplace=True)
merged_df.drop_duplicates(subset=['nome', 'nome_cientifico'], inplace=True)

merged_df.to_csv("data/csv/food_composition.csv", index=False, encoding='utf-8')