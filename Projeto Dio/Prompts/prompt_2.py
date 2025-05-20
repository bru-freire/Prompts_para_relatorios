import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados (substitua os caminhos pelos seus arquivos locais, se necessário)
ali = pd.read_csv("Meganium_Sales_Data_-_AliExpress.csv")
etsy = pd.read_csv("Meganium_Sales_Data_-_Etsy.csv")
shopee = pd.read_csv("Meganium_Sales_Data_-_Shopee.csv")

# Adicionar coluna de origem do marketplace
ali['Marketplace'] = 'AliExpress'
etsy['Marketplace'] = 'Etsy'
shopee['Marketplace'] = 'Shopee'

# Combinar todos os dados
df = pd.concat([ali, etsy, shopee], ignore_index=True)

# Converter datas (opcional se quiser análises temporais depois)
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Agrupar por país e produto, somando as quantidades
grouped = df.groupby(['delivery_country', 'product_sold'])['quantity'].sum().reset_index()

# Para cada país, pegar o produto com maior quantidade vendida
top_sellers = grouped.sort_values(['delivery_country', 'quantity'], ascending=[True, False])
top_sellers = top_sellers.groupby('delivery_country').first().reset_index()

# Visualização com Seaborn
plt.figure(figsize=(12, 6))
sns.barplot(data=top_sellers, x='delivery_country', y='quantity', hue='product_sold')
plt.title("Console mais vendido por país")
plt.xlabel("País")
plt.ylabel("Quantidade vendida")
plt.xticks(rotation=45)
plt.legend(title="Console")
plt.tight_layout()
plt.show()