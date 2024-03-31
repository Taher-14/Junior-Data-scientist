#!/usr/bin/env python
# coding: utf-8

# # Packages

# In[168]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


# # Datasets

# In[169]:


df_crime=pd.read_csv("E:\Datasets\Datacamp\Analyzing Crime in Los Angeles Project\crimes.csv",parse_dates=["DATE OCC","Date Rptd"],
dtype={"TIME OCC":str})


# # Explaination for each column

# In[ ]:


###### Column	Description
# 'DR_NO'	Division of Records Number: Official file number made up of a 2-digit year, area ID, and 5 digits.
# 'Date Rptd'	Date reported - MM/DD/YYYY.
# 'DATE OCC'	Date of occurrence - MM/DD/YYYY.
# 'TIME OCC'	In 24-hour military time.
# 'AREA NAME'	The 21 Geographic Areas or Patrol Divisions are also given a name designation that references a landmark or the surrounding community that it is responsible for. For example, the 77th Street Division is located at the intersection of South Broadway and 77th Street, serving neighborhoods in South Los Angeles.
# 'Crm Cd Desc'	Indicates the crime committed.
# 'Vict Age'	Victim's age in years.
# 'Vict Sex'	Victim's sex: F: Female, M: Male, X: Unknown.
# 'Vict Descent'	Victim's descent:
# A - Other Asian
# B - Black
# C - Chinese
# D - Cambodian
# F - Filipino
# G - Guamanian
# H - Hispanic/Latin/Mexican
# I - American Indian/Alaskan Native
# J - Japanese
# K - Korean
# L - Laotian
# O - Other
# P - Pacific Islander
# S - Samoan
# U - Hawaiian
# V - Vietnamese
# W - White
# X - Unknown
# Z - Asian Indian
# 'Weapon Desc'	Description of the weapon used (if applicable).
# 'Status Desc'	Crime status.
# 'LOCATION'	Street address of the crime.


# # EDA

# In[186]:


df_crime.head(2)
df_crime.info()


# ## Which hour has the highest frequency of crimes

# ### Extracting hour column

# In[187]:


df_crime["crime_hour"]=df_crime["TIME OCC"].str[0:2].astype(int)
df_crime.head(2)


# # Which hour has the highest frequency of crimes

# In[236]:


df_crime["crime_hour"].value_counts()


# In[192]:


sns.countplot(x="crime_hour",data=df_crime)
peak_crime_hour=12


# ### Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59am)

# In[238]:


Area_high_crime=df_crime[df_crime["crime_hour"].isin([22,23,24,0,1,2,3])]
Area_high_crime.head(2)


# In[239]:


peak_area_night=Area_high_crime.groupby("AREA NAME").agg({"crime_hour":"count"}).sort_values("crime_hour",ascending=False)
peak_area_night
peak_night_crime_location="Central"


# ### Identify the number of crimes committed against victims by age group (0-17, 18-25, 26-34, 35-44, 45-54, 55-64, 65+).

# In[232]:


age_labels=["0-17","18-25", "26-34", "35-44","45-54","55-64","65+"]
age_bins=[0,17,25,34,44,54,64,np.inf]
df_crime["victim_ages"]=pd.cut(df_crime["Vict Age"],labels=age_labels,bins=age_bins)
df_crime.head(2)


# In[240]:


df_crime["victim_ages"].value_counts()


# In[ ]:




