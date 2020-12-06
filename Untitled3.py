#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[15]:


sp = pd.read_csv('/Users/alexandrperetokin/Downloads/fao.csv')#https://www.kaggle.com/dorbicycle/world-foodfeed-production


# sp

# In[33]:


sp['total'] = sp.T[10:-2].sum()#вводим сумму по странам


# In[21]:


ag = sp.groupby(['Area', 'Element']).sum()#группировка по странам и виду производства 


# In[28]:


a = ag.iloc[0::2]#разделяем виды производства


# In[10]:


b = ag.iloc[1::2]


# In[31]:


np.corrcoef(b['total'],a['total'])#смотрим наличеие корреляции 


# In[32]:


plt.scatter(b['total'],a['total'])#строим регрессионую модель


# In[ ]:





# In[ ]:





# In[ ]:




