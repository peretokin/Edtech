#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


s = pd.read_csv('/Users/alexandrperetokin/Downloads/ramen.csv')#https://www.kaggle.com/residentmario/ramen-ratings


# In[ ]:





# In[ ]:





# In[4]:


s.loc[s['Stars'] == 'Unrated']


# In[5]:


s = s.drop([32,122,993])


# In[6]:


s['Stars'] = s['Stars'].astype(float)


# In[ ]:





# In[8]:


s = s.loc[s.Stars > 4]#оставляем только высокий балл 


# In[9]:


ss = s.groupby(s['Style']).agg(['count', 'mean'])
ss


# In[11]:



ss.loc[ss.Stars['count'] > 6]#отсеиваем маленькие выборки


# In[12]:


plt.bar(ss.loc[ss.Stars['count'] > 6].index,ss.loc[ss.Stars['count'] > 6].Stars['count'])# показывает количество разной упаковки


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




