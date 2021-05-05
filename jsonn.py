#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json

with open("test.json", "w") as file:
    json.dump({"x": 10, "y": 20}, file)


with open("test.json", "r") as file:
     data = json.load(file)



data



# In[ ]:




