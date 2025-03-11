import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Product': ['Smartphone', 'Laptop', 'Headset', 'Mouse', 'Keyboard', 
                'Shirt', 'Jeans', 'Shoes', 'Watch', 'Purse'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics',
                  'Clothes', 'Clothes', 'Clothes', 'Accessory' ,'Clothes',],
    'Current Stock': np.random.randint(5, 50, 10),
    'Sales per Day': np.random.uniform(0.5, 5, 10),
    'Restock Time (days)': np.random.randint(3, 15, 10)
}

df = pd.DataFrame(data)


df['Reorder Point']  = df['Sales per Day'] * df['Restock Time (days)'] #calculating the reorder point
df['Needs Restocking'] =  df['Current Stock'] < df['Reorder Point'] #identifying products thhat need restocking
print(df) #visualization of df
'''
#create a file of this df in a csv file
df.to_csv('product_data.csv', index=False) #Save the df as a CSV file
print("CSV file 'product_data.csv' has been created successfully!")

'''


#visualization of products that need restocking
plt.figure(figsize=(12, 6))
sns.barplot(x='Product', y='Current Stock', hue='Needs Restocking', data=df, palette={True: 'red', False: 'green'})
plt.axhline(df['Reorder Point'].max(), color='gray', linestyle='--', label='Maximum Reorder Point') #This is useful because it shows the product with the highest demand relative to its restocking time
plt.xlabel('Product')
plt.ylabel('Current Stock')
plt.title('Current Stock vs Restocking Need')
plt.xticks(rotation=45)
plt.legend()
plt.show()









