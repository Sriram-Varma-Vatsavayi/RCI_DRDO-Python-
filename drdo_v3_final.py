#!/usr/bin/env python
# coding: utf-8

# In[1]:
from IPython import get_ipython

get_ipython().system('pip install psutil')
get_ipython().system('pip install fpdf')


# In[2]:


import psutil
import platform
import socket
import fpdf


# In[3]:


from datetime import datetime


# In[4]:


print("="*40,"System Information","=" *40)
name = platform.uname()
host = socket.gethostname()

pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)
def test_connection():
    try:
        socket.create_connection(('Google.com', 80))
        return True
    except OSError:
        return False

system_name = name.system
node_name = name.node
release_name = name.release
version_name = name.version
machine_name = name.machine
processor_name = name.processor
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host)

#pdf.write("="*40," End ","="*40)
#pdf.output("drdo.pdf")

print("System Name: "+system_name)
print("Node Name: "+node_name)
print("Release Name: "+release_name)
print("Version Name: "+version_name)
print("Machine Name: "+machine_name)
print("Processor Name: "+processor_name)
print("Host Name: "+host_name)
print("IP Address: "+ip_address)
if(test_connection()==True):
    wifi_status = "Connected to wifi"
else:
    wifi_status = "Not Connected to wifi"
print("Wifi Status: "+wifi_status)

#l1=[system_name,node_name,release_name,version_name,machine_name,processor_name,host_name,ip_address]
d1= {'System Name: ': system_name,'node name: ': node_name,'release name: ': release_name,'Version Name: ':version_name,'Machine Name: ': machine_name,'Processor Name: ':processor_name,"Host Name: ":host_name,"IP Address: ":ip_address,"Wifi Connectivity: ":wifi_status}
# for i in l1:
#     pdf.write(10,str(i))
#     pdf.ln()
values = d1.values()
keys = d1.keys()
items = d1.items()
for keys,values in d1.items():
    pdf.write(10,str(keys+" "+values))
    pdf.ln()
pdf.output("drdov3.pdf")


# In[ ]:




