import numpy as np

#You have a temperature data for 5 cities (Mumbai,Delhi,Bangalor,Chennai & Kolkata) for the last 5 days.
temp_data=np.array([
    [32,34,30,31,35], #mumbai
    [28,29,27,30,31], #Delhi
    [29,28,30,31,29], #bangalore
    [33,34,35,32,33], #chennai
    [30,31,28,29,30], #kolkata
]
)

# 1.Calculare dailey average temp for each city
daily_avg_temp=np.mean(temp_data,axis=1)
print("Daily average temperature for each city in India", daily_avg_temp)

#Output: Daily average temperature for each city in India [32.4 29.  29.4 33.4 29.6]

# 2..Find the city with the highest average temperature
avg_temp=np.mean(temp_data,axis=1)
city_highest_avg_temp=np.argmax(avg_temp) #argmax means aggregate max
cities=["Mumbai","Delhi","Bangalore","Chennai","Kolkata"]
print("City with the highest avg temperature is:",cities[city_highest_avg_temp])

#Output: City with the highest avg temperature is: Chennai

# 3...Calculate the temp anomalies for each city
temp_anomalies=temp_data-daily_avg_temp[:,np.newaxis]
print(temp_anomalies)

#Output: [[-0.4  1.6 -2.4 -1.4  2.6]
 #        [-1.   0.  -2.   1.   2. ]
 #        [-0.4 -1.4  0.6  1.6 -0.4]
 #        [-0.4  0.6  1.6 -1.4 -0.4]
 #        [ 0.4  1.4 -1.6 -0.6  0.4]]
