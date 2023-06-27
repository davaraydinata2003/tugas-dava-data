#!/usr/bin/env python
# coding: utf-8

# In[1]:


def houseRobber(houses, currentIndex):
    if currentIndex >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex + 2)
        skipFirstHouse = houseRobber(houses, currentIndex+1)
        return max(stealFirstHouse, skipFirstHouse)


# In[2]:


houses = [6,7,1,30,8,2,4]


# In[3]:


print(houseRobber(houses, 0))


# In[ ]:




