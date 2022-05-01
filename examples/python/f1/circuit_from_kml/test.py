#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Put parent folder in the pythonpath
import sys,os,inspect

import matplotlib.pyplot as plt
sys.path.append("../../")
import fastest_lap
from fastest_lap import KMH

# In[2]:


# Load vehicle
vehicle=fastest_lap.load_vehicle("car","limebeer-2014-f1","/home/kktse/src/fastest-lap/database/vehicles/f1/limebeer-2014-f1.xml");


# In[ ]:

fastest_lap.circuit_from_kml(
    "/home/kktse/src/fastest-lap/database/tracks/lfg/LFG_Left.kml",
    "/home/kktse/src/fastest-lap/database/tracks/lfg/LFG_Right.kml",
    500,
    "/home/kktse/src/fastest-lap/database/tracks/lfg/mytrack.xml"
)


# In[ ]:




