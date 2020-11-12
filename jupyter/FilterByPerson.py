#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os


# In[2]:


os.listdir()


# In[3]:


table = pd.read_excel("ChildObservation_MasterFile.xlsx")


# In[4]:


table.head()


# In[9]:



target_rows = [table[table.TargetPerson.astype(str).str.contains('193')], table[table.present1.astype(str).str.contains('193')],
              table[table.present2.astype(str).str.contains('193')],table[table.present3.astype(str).str.contains('193')],
              table[table.present4.astype(str).str.contains('193')],table[table.present5.astype(str).str.contains('193')],
              table[table.present6.astype(str).str.contains('193')],table[table.present7.astype(str).str.contains('193')],
              table[table.present8.astype(str).str.contains('193')],table[table.present9.astype(str).str.contains('193')],
              table[table.present10.astype(str).str.contains('193')],table[table.present11.astype(str).str.contains('193')],
              table[table.present12.astype(str).str.contains('193')]]
df_193 = pd.concat(target_rows)


# In[10]:


df_193.head()


# In[11]:


df_193.to_excel(r'FilterByPerson/CO_193.xlsx', index = False)


# In[ ]:




