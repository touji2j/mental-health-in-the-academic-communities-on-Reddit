#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx 
import matplotlib.pyplot as plt 
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'notebook')
sns.set()


# In[8]:


G = nx.Graph()
G.add_edge(0,1)
G.add_edge(1,2)
G.add_edge(2,0)


# In[9]:


plt.figure()

nx.draw_networkx(G)


# In[10]:


#directional graphs 

G1 = nx.DiGraph()
G1.add_edge(1,2)
G1.add_edge(1,3)


# In[11]:


plt.figure()


nx.draw_networkx(G1)


# In[ ]:




