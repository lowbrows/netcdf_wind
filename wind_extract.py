#python 2.7
import numpy
import netCDF4 as n
import csv

#Controls
filename= "ascat_20180226_004200.nc"

#Create the name for the csv file
clist= filename.split(".")
csvfilename= clist[0]+".csv"

#create the netCDF dataset
windDS= n.Dataset("ascat_20180226_004200.nc")


#Create the lists of variable data
wind_speed = windDS.variables["wind_speed"]
wind_dir= windDS.variables["wind_dir"]
time_set = windDS.variables["time"]
lat_set = windDS.variables["lat"]
lon_set = windDS.variables["lon"]

#explore the data
print("The len of wind_speed: ", len(wind_speed)) 
print("The len of wind_dir: ", len(wind_dir[0]))
print("The len of time_set: ", len(time_set[0]))
print("The len of lat_set: ", len(lat_set[0]))
print("The len of lon_set: ", len(lon_set[0]))

print("The type of wind_speed: ", type(wind_speed[0]))
print("The type of wind_dir: ", type(wind_dir[0]))
print("The type of time_set: ", type(time_set[0]))
print("The type of lat_set: ", type(lat_set[0]))
print("The type of lon_set: ", type(lon_set[0]))

#_____Create the lists of seperate variable values________
lat_list=[]

for i in range(len(wind_speed)):
    for p in lat_set[i-1]:
        lat_list.append(p)
#______________________________________
lon_list=[]

for i in range(len(wind_speed)):
    for p in lon_set[i-1]:
        lon_list.append(p)
#______________________________
time_list=[]

for i in range(len(wind_speed)):
    for p in time_set[i-1]:
        time_list.append(p)
#_________________________
speed_list=[]

for i in range(len(wind_speed)):
    for p in wind_speed[i-1]:
        speed_list.append(p*0.01)
print("speed: ",speed_list[0:5])


dir_list=[]

for i in range(len(wind_speed)):
    for p in wind_dir[i-1]:
        dir_list.append(p*0.1)

print("wind direction: ", dir_list[0:5])


with open(csvfilename, 'wb') as csvfile:
    writer= csv.writer(csvfile, dialect='excel', delimiter=',')
    writer.writerow(["lat", "lon", "time", "speed", "direction"])
    for i in range(len(dir_list)):
        writer.writerow([lat_list[i], lon_list[i], time_list[i], speed_list[i], dir_list[i]])

#garbage collection
del wind_speed, wind_dir, time_set, lat_set, lon_set, lat_list, lon_list,time_list,
speed_list, dir_list

