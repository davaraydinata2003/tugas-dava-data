#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value/weight


# In[9]:


def knapsackMethod(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse = True)
    usedCapacity = 0
    totalValue = 0
    for i in items:
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalValue += i.value
        else:
            unusedWeight = capacity - usedCapacity
            value = i.ratio * unusedWeight
            usedCapacity += unusedWeight
            totalValue += value
            
        if usedCapacity == capacity:
            break
    print("Total value obtiened: "+str(totalValue))


# In[10]:


item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)
clist = [item1, item2, item3]


# In[11]:


knapsackMethod(clist, 50)


# In[ ]:




