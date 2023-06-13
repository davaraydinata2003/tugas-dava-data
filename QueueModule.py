#!/usr/bin/env python
# coding: utf-8

# In[24]:


import queue as q

customQueue = q.Queue(maxsize=3)
print(customQueue.empty())
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.full())
print(customQueue.get())
print(customQueue.qsize())


# In[ ]:





# In[ ]:





# In[ ]:




