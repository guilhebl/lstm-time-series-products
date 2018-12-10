import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_name = 'data/mercari_train.tsv'
df = pd.read_csv(file_name, sep = '\t')

msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]

train.head()
train.info()
train.price.describe()

plt.subplot(1, 2, 1)
(train['price']).plot.hist(bins=50, figsize=(12, 6), edgecolor = 'white', range = [0, 250])
plt.xlabel('price', fontsize=12)
plt.title('Price Distribution', fontsize=12)
plt.subplot(1, 2, 2)
np.log(train['price']+1).plot.hist(bins=50, figsize=(12,6), edgecolor='white')
plt.xlabel('log(price+1)', fontsize=12)
plt.title('Price Distribution', fontsize=12)

train['shipping'].value_counts() / len(train)

shipping_fee_by_buyer = train.loc[df['shipping'] == 0, 'price']
shipping_fee_by_seller = train.loc[df['shipping'] == 1, 'price']
fig, ax = plt.subplots(figsize=(18,8))
ax.hist(shipping_fee_by_seller, color='#8CB4E1', alpha=1.0, bins=50, range = [0, 100],
       label='Price when Seller pays Shipping')
ax.hist(shipping_fee_by_buyer, color='#007D00', alpha=0.7, bins=50, range = [0, 100],
       label='Price when Buyer pays Shipping')
plt.xlabel('price', fontsize=12)
plt.ylabel('frequency', fontsize=12)
plt.title('Price Distribution by Shipping Type', fontsize=15)
plt.tick_params(labelsize=12)
plt.legend()

print('The average price is {}'.format(round(shipping_fee_by_seller.mean(), 2)), 'if seller pays shipping');
print('The average price is {}'.format(round(shipping_fee_by_buyer.mean(), 2)), 'if buyer pays shipping')

fig, ax = plt.subplots(figsize=(18,8))
ax.hist(np.log(shipping_fee_by_seller+1), color='#8CB4E1', alpha=1.0, bins=50,
       label='Price when Seller pays Shipping')
ax.hist(np.log(shipping_fee_by_buyer+1), color='#007D00', alpha=0.7, bins=50,
       label='Price when Buyer pays Shipping')
plt.xlabel('log(price+1)', fontsize=12)
plt.ylabel('frequency', fontsize=12)
plt.title('Price Distribution by Shipping Type', fontsize=15)
plt.tick_params(labelsize=12)
plt.legend()

print('There are', train['category_name'].nunique(), 'unique values in category name column')
top_cat_names = train['category_name'].value_counts()[:10]
print('Top Categories', top_cat_names)

print('There are', train['name'].nunique(), 'unique values in name column')
top_names = train['name'].value_counts()[:10]
print('Top Products', top_names)

print('There are', train['brand_name'].nunique(), 'unique values in brand column')
top_brands = train['brand_name'].value_counts()[:10]
print('Top Brands', top_brands)

price_by_condition_1 = train.loc[df['item_condition_id'] == 1, 'price']
price_by_condition_2 = train.loc[df['item_condition_id'] == 2, 'price']
price_by_condition_3 = train.loc[df['item_condition_id'] == 3, 'price']

fig, ax = plt.subplots(figsize=(18,8))
ax.hist(price_by_condition_1, color='#8CB4E1', alpha=1.0, bins=50, range = [0, 100], label='New')
ax.hist(price_by_condition_2, color='#CD5C5C', alpha=0.7, bins=50, range = [0, 100], label='Like New')
ax.hist(price_by_condition_3, color='#0A7D00', alpha=0.7, bins=50, range = [0, 100], label='Good')

plt.xlabel('price', fontsize=12)
plt.ylabel('frequency', fontsize=12)
plt.title('Price Distribution by Condition Type', fontsize=15)
plt.tick_params(labelsize=12)
plt.legend()

price_by_brand_Nike = train.loc[df['brand_name'] == 'Nike', 'price']
price_by_brand_VictoriaSecret = train.loc[df['brand_name'] == 'Victoria\'s Secret', 'price']
price_by_brand_LuLaRoe = train.loc[df['brand_name'] == 'LuLaRoe', 'price']
price_by_brand_Apple = train.loc[df['brand_name'] == 'Apple', 'price']
price_by_brand_FOREVER_21 = train.loc[df['brand_name'] == 'FOREVER 21', 'price']
price_by_brand_Nintendo = train.loc[df['brand_name'] == 'Nintendo', 'price']
price_by_brand_Lululemon = train.loc[df['brand_name'] == 'Lululemon', 'price']
price_by_brand_MichaelKors = train.loc[df['brand_name'] == 'Michael Kors', 'price']
price_by_brand_AmericanEagle = train.loc[df['brand_name'] == 'American Eagle', 'price']

fig, ax = plt.subplots(figsize=(18,8))
ax.hist(price_by_brand_Nike, color='#FAF0E6', alpha=1.0, bins=50, range = [0, 100], label='Nike')
ax.hist(price_by_brand_VictoriaSecret, color='#EE82EE', alpha=1.0, bins=50, range = [0, 100], label='VictoriaSecret')
ax.hist(price_by_brand_LuLaRoe, color='#4682B4', alpha=1.0, bins=50, range = [0, 100], label='LuLaRoe')
ax.hist(price_by_brand_Apple, color='#000000', alpha=1.0, bins=50, range = [0, 100], label='Apple')
ax.hist(price_by_brand_FOREVER_21, color='#DAA520', alpha=1.0, bins=50, range = [0, 100], label='FOREVER 21')
ax.hist(price_by_brand_Nintendo, color='#8B4513', alpha=1.0, bins=50, range = [0, 100], label='Nintendo')
ax.hist(price_by_brand_MichaelKors, color='#778899', alpha=1.0, bins=50, range = [0, 100], label='Michael Kors')
ax.hist(price_by_brand_AmericanEagle, color='#32CD32', alpha=1.0, bins=50, range = [0, 100], label='American Eagle')

plt.xlabel('price', fontsize=12)
plt.ylabel('frequency', fontsize=12)
plt.title('Price Distribution by Top 10 most popular Brands', fontsize=15)
plt.tick_params(labelsize=12)
plt.legend()
plt.show()

print('There are %d items that do not have a category name.' %train['category_name'].isnull().sum())
print('There are %d items that do not have a brand name.' %train['brand_name'].isnull().sum())
print('There are %d items that do not have a description.' %train['item_description'].isnull().sum())

print('There are', train['name'].nunique(), 'unique values in name column')
top_names = train['name'].value_counts()[:10]
print('Top Names', top_names)

price_by_name_CoachPurse = train.loc[df['name'] == 'Coach purse', 'price']
price_by_name_Dress = train.loc[df['name'] == 'Dress', 'price']
price_by_name_Lularoe_TC_leggings = train.loc[df['name'] == 'Lularoe TC leggings', 'price']
price_by_name_Romper = train.loc[df['name'] == 'Romper', 'price']
price_by_name_Nike = train.loc[df['name'] == 'Nike', 'price']
price_by_name_Vans = train.loc[df['name'] == 'Vans', 'price']

fig, ax = plt.subplots(figsize=(18,8))
ax.hist(price_by_name_CoachPurse, color='#FAF0E6', alpha=1.0, bins=50, range = [0, 100], label='Coach purse')
ax.hist(price_by_name_Dress, color='#EE82EE', alpha=1.0, bins=50, range = [0, 100], label='Dress')
ax.hist(price_by_name_Lularoe_TC_leggings, color='#4682B4', alpha=1.0, bins=50, range = [0, 100], label='Lularoe TC leggings')
ax.hist(price_by_name_Romper, color='#000000', alpha=1.0, bins=50, range = [0, 100], label='Romper')
ax.hist(price_by_name_Nike, color='#DAA520', alpha=1.0, bins=50, range = [0, 100], label='Nike')
ax.hist(price_by_name_Vans, color='#8B4513', alpha=1.0, bins=50, range = [0, 100], label='Vans')

plt.xlabel('price', fontsize=12)
plt.ylabel('frequency', fontsize=12)
plt.title('Price Distribution by Top 6 Most popular Item Names', fontsize=15)
plt.tick_params(labelsize=12)
plt.legend()
plt.show()
