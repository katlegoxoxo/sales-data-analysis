#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd  


df = pd.read_csv("mf.txt", sep="\t")  # use sep="\t" if it's tab-separated
df.head()


# In[2]:


# Show the entire dataset (be careful if it's very large)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df


# In[3]:


# Count missing values in each column
df.isnull().sum()


# In[4]:


# Show the entire dataset (be careful if it's very large)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df


# In[5]:


# Show the entire dataset (be careful if it's very large)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df


# In[6]:


# Show the entire dataset (be careful if it's very large)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df


# In[7]:


df = pd.read_csv("mf.txt", sep="\t", skip_blank_lines=True)


# In[8]:


# Show the entire dataset (be careful if it's very large)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df


# In[9]:


# Count missing values in each column
df.isnull().sum()


# In[10]:


# Count duplicates
df.duplicated().sum()



# In[11]:


# Remove duplicates (if any)
df = df.drop_duplicates()


# In[12]:


df.dtypes


# In[13]:


# Convert to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# Confirm conversion
df.dtypes


# In[14]:


# Shape of dataset after cleaning
df.shape

# Display first 5 rows
df.head()


# In[15]:


total_revenue = df['Revenue'].sum()
print("Total Revenue:", total_revenue)


# In[16]:


avg_units_sold = df['Units_Sold'].mean()
print("Average Units Sold per Order:", avg_units_sold)


# In[17]:


revenue_per_region = df.groupby('Region')['Revenue'].sum()
print("Revenue per Region:\n", revenue_per_region)


# In[18]:


revenue_per_rep = df.groupby('Sales_Rep')['Revenue'].sum()
top_sales_rep = revenue_per_rep.idxmax()
top_sales_amount = revenue_per_rep.max()
print(f"Top Sales Rep: {top_sales_rep} with Revenue: {top_sales_amount}")


# In[19]:


units_per_product = df.groupby('Product')['Units_Sold'].sum()
top_3_products = units_per_product.sort_values(ascending=False).head(3)
print("Top 3 Products by Units Sold:\n", top_3_products)


# In[ ]:




