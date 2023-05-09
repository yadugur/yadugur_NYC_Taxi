#!/usr/bin/env python
# coding: utf-8

# In[22]:


import csv
import datetime
import matplotlib.pylab as plt
#Read the input data file

f = open('trip_data_3.csv', 'r')
data = csv.reader(f)


# In[3]:


n=0
for row in data:
    if n>0:
        break
    else:
        print(row)
    n+=1


# In[4]:


#Question 1
min_datetime='2013-03-01 00:00:18'
max_datetime='2013-03-01 00:00:18'
no_of_rows=0
for i in data:
    if i[5]<min_datetime:
        min_datetime=i[5]
    if i[6]>max_datetime:
        max_datetime=i[6]
    no_of_rows=no_of_rows+1
print(f'The datetime range varies from {min_datetime} to {max_datetime}')
print(f"The number of rows in the file are {no_of_rows}")


# In[5]:


# Question 3
n=0
for row in data:
    if n%100000==0:
        print (row)
        n+=1
    else:
        n+=1
        continue


# In[6]:


# Question 5

min_lat=40.645164
max_lat=40.772614
min_lon=-73.913925
max_lon=-73.776703

for row in data:
    try:
        if float(row[10]) < min_lon:
            min_lon = row[10]
        if float(row[12]) < min_lon:
            min_lon = row[12]
        if float(row[12]) > max_lon:
            max_lon = row[12]
        if float(row[12]) > max_lon:
            max_lon = row[12]
        if float(row[11]) < min_lat:
            min_lat = row[11]
        if float(row[13]) < min_lat:
            min_lat = row[13]
        if float(row[11]) > max_lat:
            max_lat = row[11]
        if float(row[13]) > max_lat:
            max_lat = row[13]
    except Exception as e:
        continue
print(f"The min and max of long is {min_lon} and {max_lon}")
print(f"The min and max of lat is {min_lat} and {max_lat}")


# In[7]:


# Question 6
from math import radians, cos, sin, asin, sqrt

def haversine_distance(lat1, lon1, lat2, lon2):


    R = 3959.87433 # this is in miles.  For Earth radius in kilometers use 6372.8 km

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))

    return R * c


# In[8]:


lon1 = -73.987343
lat1 = 40.645164
lon2 = -73.776703
lat2 = 40.772614
print('The average trip distance calculated is '+str(haversine_distance(lat1, lon1, lat2, lon2)))


# In[9]:


# Histogram
trip_distance={'0-5':0,'5-10':0,'10-15':0,'15-20':0}
n=0
for row in data:
    if n==0:
        n+=1
        continue
    else:
        temp=float(row[9])
        if (temp>0) and (temp<5):
            trip_distance['0-5']+=1
        elif (temp>5) and (temp<10):
            trip_distance['5-10']+=1
        elif (temp>10) and (temp<15):
            trip_distance['10-15']+=1
        elif (temp>15) and (temp<20):
            trip_distance['15-20']+=1
print(trip_distance)
req_list=trip_distance.items()
req_list=sorted(req_list)
print (req_list)
x, y = zip(*req_list)
print (x,y)


# In[10]:


# Question 7 

trip_time=[]
n=0
for i in data:
    if (i[8] in trip_time)or (n==0):
        n=n+1
        continue
    else:
        trip_time.append(i[8])
        n=n+1
print(f"The distinct values in trip time is {trip_time}")

No_of_passengers=[]
n=0
for i in data:
    if (i[7] in No_of_passengers)or (n==0):
        n=n+1
        continue
    else:
        No_of_passengers.append(i[7])
        n=n+1
print(f"The distinct values in no of passengers is {No_of_passengers}")

trip_dist=[]
n=0
for i in data:
    if (i[9] in trip_dist)or (n==0):
        n=n+1
        continue
    else:
        trip_dist.append(i[9])
        n=n+1
print(f"The distinct values in trip distance is {trip_dist}")

rate_code=[] 


# In[11]:


# Question 8 

min_passno=1
max_passno=1
for row in data:
    try:
        if int(row[7]) < min_passno:
            min_passno = int(row[7])
        if int(row[7]) > max_passno:
            max_passno = int(row[7])
    except Exception as e:
        continue
print(min_passno, max_passno)

min_ratecode=1
max_ratecode=1
for row in data:
    try:
        if int(row[3]) < min_ratecode:
            min_ratecode = int(row[3])
        if int(row[3]) > max_ratecode:
            max_ratecode = int(row[3])
    except Exception as e:
        continue
print(min_ratecode, max_ratecode)

min_triptime=1
max_triptime=1
for row in data:
    try:
        if int(row[8]) < min_triptime:
            min_triptime = int(row[8])
        if int(row[8]) > max_triptime:
            max_triptime = int(row[8])
    except Exception as e:
        continue
print(min_triptime, max_triptime)

min_tripdist=1
max_tripdist=1
for row in data:
    try:
        if int(row[9]) < min_tripdist:
            min_triptime = int(row[9])
        if int(row[9]) > max_tripdist:
            max_triptime = int(row[9])
    except Exception as e:
        continue
print(min_tripdist, max_tripdist)


# In[14]:


# Question 9 

avg_pass_count = {}
n = 0
for row in data:
    if n == 0:
        n += 1
        continue
    else:
        datetimeobj = datetime.datetime.strptime(row[5], "%Y-%m-%d %H:%M:%S")
        pass_count = int(row[7])
        if datetimeobj.hour not in avg_pass_count:
            avg_pass_count[datetimeobj.hour] = pass_count
        else:
            avg_pass_count[datetimeobj.hour] += pass_count

# Process and plot the data
keys = sorted(avg_pass_count)
for i in keys:
    print(i, avg_pass_count[i])

if avg_pass_count:  # Check if avg_pass_count is not empty
    req_list = avg_pass_count.items()
    req_list = sorted(req_list)
    x, y = zip(*req_list)
    y_list = list(y)
    y_list = [z / 30 for z in y_list]
    y = tuple(y_list)
    print(x, y)
    plt.plot(x, y)
    plt.xlabel('Hour of the day')
    plt.ylabel('Passenger count')
    plt.title('Chart')
    plt.show()


# In[18]:


# Question 10 
outFile= "subset_file.csv"
f2 = open(outFile,'w')
f2.write("")
f2.close()
f2 = open(outFile,'a')
writer_obj = csv.writer(f2, lineterminator='\n')
n=0
for i in data:
    if n==999 or n==0:
        writer_obj.writerow(i)
        n=1
    else:
        n=n+1

f2.close()


# In[21]:


# Question 11
avg_pass_count = {}
with open('subset_file.csv', 'r') as f3:
    data_input = csv.reader(f3)
    n = 0
    for row in data_input:
        if n == 0:
            n += 1
            continue
        else:
            datetimeobj = datetime.datetime.strptime(row[5], "%Y-%m-%d %H:%M:%S")
            pass_count = int(row[7])
            if datetimeobj.hour not in avg_pass_count:
                avg_pass_count[datetimeobj.hour] = pass_count
            else:
                avg_pass_count[datetimeobj.hour] += pass_count

keys = sorted(avg_pass_count)
for i in keys:
    print(i, avg_pass_count[i])

if avg_pass_count:  # Check if avg_pass_count is not empty
    req_list = avg_pass_count.items()
    req_list = sorted(req_list)
    if req_list:  # Check if req_list is not empty
        x, y = zip(*req_list)
        y_list = list(y)
        y_list = [z / 30 for z in y_list]
        y = tuple(y_list)
        print(x, y)
        plt.plot(x, y)
        plt.xlabel('Hour of the day')
        plt.ylabel('Passenger count')
        plt.title('Chart')
        plt.show()


# In[ ]:




