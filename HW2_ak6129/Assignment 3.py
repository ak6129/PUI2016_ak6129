
# coding: utf-8

# In[7]:

from __future__ import print_function
import os
import sys
import csv
import numpy as np
import pylab as pl
import pandas as pd 
get_ipython().magic('pylab inline')


# In[8]:

env


# In[9]:

DFDATA  = os.getenv('DFDATA')
PUI2016 = os.getenv('PUI2016')

print(DFDATA)


# In[10]:

df1 = pd.read_csv(DFDATA + '/kku6-nxdu/1414245945/kku6-nxdu')


# In[12]:

df1.columns
print(df1)


# In[13]:

df1.head()


# In[14]:

df2 = df1 [["COUNT MALE", "COUNT PARTICIPANTS"]]


# In[15]:

df2.head()


# In[19]:

plt.plot(df2, 'o')
plt.xlabel('COUNT MALE')
plt.ylabel('COUNT PARTICIPANTS')
plt.title('Plot COUNT')
plt.text(0, -75, 'compare males vs participants')
plt.show


# In[ ]:



