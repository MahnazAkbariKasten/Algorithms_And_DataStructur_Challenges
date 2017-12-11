
# coding: utf-8

# # Zulily test
# ## Homepage Conversion

# In[23]:


import pandas as pd
import matplotlib as mp
import seaborn as sb
get_ipython().magic('matplotlib inline')


# In[8]:


dates = pd.date_range('6/4/2007', periods=12)


# In[7]:


cells = [ [7823, 796, 2910, 289],
[5611,541,3049,262],
[5092,533,2775,280],
[16407,1001,3266,191],
[4072,416,1980,188],
[2802,268,1512,129],
[3277,323,1408,134],
[8159,808,2709,258],
[5331,517,2802,258],
[5217,542,2720,272],
[15922,1099,3119,205],
[4360,415,2091,182]
]


# In[6]:


df = pd.DataFrame(cells, index=dates, columns=['visits-A', 'Orders-A', 'visits-B', 'Orders-B'])
df


# In[12]:


totals = df.sum()
totals


# ## A) What is the overall conversion rate for Homepage version A?

# In[16]:


conv_rate_A = totals['Orders-A'] / totals['visits-A']
conv_rate_A


# ## B) What is the overall conversion rate for Homepage version B?

# In[17]:


conv_rate_B = totals['Orders-B'] / totals['visits-B']
conv_rate_B


# ## C) Which version of the home page would you recommend rolling out with to maximize the number of orders?						

# Version B has higher conversion rate.

# ## D) What % more orders can you expect to get by using the version you answered in #3 above, vs the other version?

# In[21]:


(conv_rate_B - conv_rate_A) / conv_rate_B


# ## E) What is a little strange about this data? Why is this happening?

# In[27]:


df.plot(dates, 'visits-A')
df.plot(dates, 'visits-B')

# The day(s) before banner show, the orders drops significantly in version-A while it's a still pretty high for version-B.
# A hypotysis is that if we switch to version-B, the banner-effect wouldn't be that significant.