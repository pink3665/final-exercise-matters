
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

import numpy as np


# In[3]:

import matplotlib.pyplot as plt


# In[4]:

df = pd.read_csv("gapminder_gdp_americas.csv")


# In[5]:

df.mean()


# In[8]:

ax = df.mean().plot(kind='bar', title="Average GDP per year across all countries", figsize=(20,8), fontsize=7)


# In[9]:

ax.set_xlabel("Year", fontsize=12)


# In[10]:

ax.set_ylabel("Average GDP across all countries", fontsize=12)


# In[11]:

plt.show()


# In[ ]:



