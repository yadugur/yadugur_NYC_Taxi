```python
import csv
import datetime
import matplotlib.pylab as plt
#Read the input data file

f = open('trip_data_3.csv', 'r')
data = csv.reader(f)
```


```python
n=0
for row in data:
    if n>0:
        break
    else:
        print(row)
    n+=1

```

    ['medallion', ' hack_license', ' vendor_id', ' rate_code', ' store_and_fwd_flag', ' pickup_datetime', ' dropoff_datetime', ' passenger_count', ' trip_time_in_secs', ' trip_distance', ' pickup_longitude', ' pickup_latitude', ' dropoff_longitude', ' dropoff_latitude']



```python
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
```

    The datetime range varies from 2013-03-01 00:00:00 to 2013-04-01 01:16:32
    The number of rows in the file are 15749227

```python
# Question 2

    Name - Description
    medallion - A taxi medallion, also known as a CPNC, is a transferable permit in the United States allowing a taxicab driver to operate
    hack_license - license or other authority issued by a governmental agency authorizing a person to drive a taxicab in service to customers in that area.
    rate_code - Rate Code means a numerical code designated by AHCCCS to indicate a member's eligibility category
    vendor_id - a code indicating the provider associated with the trip record
    pickup_datetime - date and time when the meter was engaged
    dropoff_datetime - date and time when the meter was disengaged
    passenger count - the number of passengers in the vehicle (driver entered value)
    pickup longitude - the longitude where the meter was engaged
    pickup latitude - the latitude where the meter was engaged
    dropoff_longitude - the longitude where the meter was disengaged
    dropoff_latitude - the latitude where the meter was disengaged
    store_and_fwd_flag- This flag indicates whether the trip record was held in vehicle memory before sending to the vendor because the vehicle did not have a connection to the server (Y=store and forward; N=not a store and forward trip)
    trip_time_in_secs - (target) duration of the trip in seconds

```



```python
# Question 3
n=0
for row in data:
    if n%100000==0:
        print (row)
        n+=1
    else:
        n+=1
        continue
```
```python
# Question 4


    Name - MySQL data types / len
    medallion - varchar(30)
    hack_license - varchar(30)
    rate_code - int(5)
    vendor_id - text(5)
    pickup_datetime - datetime
    dropoff_datetime - datetime
    passenger count - int(5)
    pickup longitude - decimal(5,10)
    pickup latitude - decimal(5,10)
    dropoff_longitude - decimal(5,10)
    dropoff_latitude - decimal(5,10)
    store_and_fwd_flag- text(5)
    trip_time_in_secs - int(10)

```

```python
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
```

    The min and max of long is -73.913925 and -73.776703
    The min and max of lat is 40.645164 and 40.772614



```python
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
```


```python
lon1 = -73.987343
lat1 = 40.645164
lon2 = -73.776703
lat2 = 40.772614
print('The average trip distance calculated is '+str(haversine_distance(lat1, lon1, lat2, lon2)))
```

    The average trip distance calculated is 14.119779173262613



```python
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

```

    {'0-5': 0, '5-10': 0, '10-15': 0, '15-20': 0}
    [('0-5', 0), ('10-15', 0), ('15-20', 0), ('5-10', 0)]
    ('0-5', '10-15', '15-20', '5-10') (0, 0, 0, 0)



```python
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
```

    The distinct values in trip time is []
    The distinct values in no of passengers is []
    The distinct values in trip distance is []



```python
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
```

    1 1
    1 1
    1 1
    1 1



```python
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

```


```python
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
```


```python
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

```


```python
# Observation

    1-Though the passenger count scale is different for both the graphs, we can observe that the trend has been pretty much same for both the datasets
    2-For both the graphs, we can find the max passenger count was around 20:00 hrs.
    3-The passenger count was at its minimum at 5:00 in the morning.

```
