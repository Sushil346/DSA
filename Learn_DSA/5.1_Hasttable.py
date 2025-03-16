#5.1)  nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem

nyc_weather=[]
with open("Data/nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        date = tokens[0]
        temp = tokens[1]
        nyc_weather.append([date, temp])


nyc_weather

avg_temp_week = sum( float(data[1]) for data in nyc_weather[1:8]) /7
avg_temp_week


temp_list = [float(data[1]) for data in nyc_weather[1:] ]
max(temp_list)


# Using Hashtable for python i.e. Dictionary
weather_nyc = {}
with open("Data/nyc_weather.csv","r") as wf:
    for line in wf:
        tokens = line.split(',')
        date = tokens[0]
        temp = tokens[1]
        weather_nyc.append
        

print(weather_nyc)
