#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Задача анализа - выяснить есть ли связь между количеством пищи для человека и количеством корма для скота


# In[ ]:





# In[491]:


import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from scipy import stats
from scipy.stats import iqr
import seaborn as sns


# In[492]:


sp = pd.read_csv('/Users/alexandrperetokin/Downloads/fao.csv')#https://www.kaggle.com/dorbicycle/world-foodfeed-production


# In[493]:


sp


# sp

# In[494]:


sp['total'] = sp.T[10:-2].sum()#вводим сумму по странам


# In[497]:


ag = sp.groupby(['Area', 'Element']).sum()#группировка по странам и виду производства 


# In[613]:





# In[498]:


ag = ag.reset_index(level=['Area', 'Element'])#делаем из индексов,столбцы для дальнейшено анализа


# In[ ]:





# In[499]:


ag.to_excel("feed.xlsx")#Проверка


# In[614]:


a = ag.iloc[0::2]#разделяем виды производства


# In[621]:


a


# In[623]:


a['index'] = a.index##создаем дополнительные индексы в виде столбца, чтобы индексы не сбивались в процессе анализа


# In[625]:


b = ag.iloc[1::2]# создаем переменную, которая связана с производством продовольствия для людей.


# In[626]:


b['index'] = b.index


# In[509]:


np.corrcoef(b['total'],a['total'])#смотрим наличеие корреляции 


# In[510]:


scipy.stats.pearsonr(b['total'],a['total'])#Смотрим наличие корреляции и значимость
#Модель значима, кэффициент 0,84 говорит о наличии сильной связи 


# In[642]:


plt.scatter(b['total'],a['total'],color = 'hotpink')#строим коррел модель
#plt.xlim(0, 20000000);
plt.ylabel('Количество корма для скота',fontsize=13)
plt.xlabel('Количество продовольствия для людей', fontsize=13)
plt.suptitle('Взаимосвязь количества корма и количества продовольствия', fontsize=18)


# In[ ]:


#На графике видны ярко выраженные выбросы, от них стоит избавиться


# In[527]:


iq = iqr(a['total'])
a1 = a[a.total <= 
(np.percentile(a['total'],75)+(3*iq))]#вычисляем наблюдения, которые не являются выбросами.

a1.set_index('index',inplace=True)#возвращаем индекс из столбца на место


# In[584]:


ii = iqr(b['total'])
b1 = b[b.total >= 
       (np.percentile(b['total'],75)+(3*ii))]#вычисляем наблюдения, являются выбросами

b1.set_index('index',inplace=True)  


# In[644]:


m = b1.index
o = a1.index
z = m & o


# In[532]:


a2 = a1.drop([51,75,120])# убираем все точки переменной а, которые пересекаются с выбросами переменной b


# In[534]:


iq = iqr(a['total'])

a3 = a[a.total >= 
       (np.percentile(a['total'],75)+(3*iq))]#Проделываем те же манипуляции, но для переменой b

a3.set_index('index',inplace=True)


# In[536]:


ii = iqr(b['total'])
b3 = b[b.total <= 
       (np.percentile(b['total'],75)+(3*ii))]
b3.set_index('index',inplace=True)


# In[539]:


a3.index & b3.index


# In[541]:


b4 = b3.drop([29,112,129,162])


# In[575]:


y =  b4.merge(a2, how = 'outer')
y.drop_duplicates(subset =["Area"],
                     keep = False, inplace = True)#проверка правильности рассчетов


# In[578]:


scipy.stats.pearsonr(b4['total'],a2['total'])#Смотрим наличие корреляции и значимость новой модели


# In[ ]:


#Значимость как и сила связи упала, это значит, что некоторые удаленные выбросы не портили модель


# In[ ]:


#Поэтому было решено убрать только 3 очевидных выброса.


# In[595]:


b1.total.sort_values()


# In[603]:


b5 = b.drop([36,74,166])


# In[604]:


a5 = a.drop([36,74,166])


# In[612]:


scipy.stats.pearsonr(b5['total'],a5['total'])#Смотрим наличие корреляции и значимость для самой новой модели


# In[646]:


plt.scatter(b5['total'],a5['total'],color = 'hotpink')#строим коррел модель
#plt.xlim(0, 20000000);
plt.ylabel('Количество корма для скота',fontsize=13)
plt.xlabel('Количество продовольствия для людей', fontsize=13)
plt.suptitle('Взаимосвязь количества корма и количества продовольствия', fontsize=18)


# In[ ]:


# убрав 3 выброса, модель не стала сущетсвенно качественней. Тем не менее результат анализа показал,
#что есть сильная линейная связь между количеством корма для скота и количеством продовольствия для людей.
#Можно сделать вывод, что увеличивая количество корма для скота, количество человеческой еды также вырастет


# In[ ]:




