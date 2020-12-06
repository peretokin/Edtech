#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[55]:


s = pd.read_csv('/Users/alexandrperetokin/Downloads/ramen.csv')#https://www.kaggle.com/residentmario/ramen-ratings


# In[ ]:





# In[ ]:





# In[56]:


s.loc[s['Stars'] == 'Unrated']


# In[57]:


s = s.drop([32,122,993])#убираем позиции без рейтинга, чтобы далее перевести в float


# In[58]:


s['Stars'] = s['Stars'].astype(float) # переводим в float


# In[59]:


s.loc[s['Stars'] == 0] #


# In[60]:


s.groupby(s['Style']).agg(['count', 'mean'])
s


# In[61]:


ss


# In[64]:


ss.loc[ss.Stars['count'] > 6]#отсеиваем слишком маленьие значения


# In[62]:


graph1 = plt.bar(ss.loc[ss.Stars['count'] > 6].index,ss.loc[ss.Stars['count'] > 6].Stars['count'])# показывает количество разной упаковки


# In[63]:


graph2 = plt.bar(ss.loc[ss.Stars['count'] > 6].index,ss.loc[ss.Stars['count'] > 6].Stars['mean'])#сравнение средних


# In[ ]:





# In[ ]:





# In[ ]:




