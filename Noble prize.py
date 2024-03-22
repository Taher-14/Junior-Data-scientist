#!/usr/bin/env python
# coding: utf-8

# # Packages

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm , t
import numpy as np


# # Datasets

# In[77]:


df=pd.read_csv(r"E:\Datasets\Datacamp\Nobel prize project\nobel.csv")


# # Top gender won nobel prize

# In[78]:


gender=df["sex"].value_counts()
top_gender=gender.sort_values(ascending=False).index[0]
top_gender


# # Which country has more nobel prize winners ? 

# In[79]:


country=df["birth_country"].value_counts()
top_country=country.sort_values(ascending=False).index[0]
top_country


# # Which decade has the most american winners ? 

# In[150]:


df["decade"]=(np.floor(df["year"]/10)*10).astype(int)
df["US_winners"]=df["birth_country"]=="United States of America"
decade_usa=df.groupby("decade")["US_winners"].mean()
m_decade_usa=decade_usa.sort_values(ascending=False).index[0]
max_decade_usa=int(m_decade_usa)
max_decade_usa


# # Which decade has the most female winners 

# In[151]:


df["female_winners"]=df["sex"]=="Female"
female_max=df.groupby("decade")["female_winners"].sum()
max_female_winners=female_max.sort_values(ascending=False)
max_female_winners


# In[82]:


max_female_dict={max_female_winners.index[0]:max_female_winners.values[0]}
max_female_dict


# # Who is the first women won nobel prize

# In[100]:


women=df[df["female_winners"]]
women_winners=women.groupby("full_name").agg({"year":"min"})
first_woman_name=women_winners.sort_values("year").index[0]
first_woman_name


# # Which cateorgy has the first women won nobel prize 

# In[131]:


W=women[women["full_name"]=="Marie Curie, née Sklodowska"]
w_ascending=W.sort_values("year")
w_ascending
first_record=w_ascending.set_index("category")
first_woman_category=first_record.index[0]
first_woman_category


# # who won nobel prize multiple times

# In[152]:


winners=df["full_name"].value_counts()
winners
winners_more_than_one_time=winners[winners>=2].index
repeat_list=list(winners_more_than_one_time)
repeat_list


# In[ ]:




