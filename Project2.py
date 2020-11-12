#!/usr/bin/env python
# coding: utf-8

# ### Question 1. The data set need cleaning. Decide what to do with missing values and extra attributes.

# **Answer - Cleaning the data required accordingly. Some examples of data cleaning that I cleaned is dropping NaN, considering speed limit only divisble by 5, etc.**

# In[129]:


import pandas as pd
import datetime
from pandas import DataFrame
import matplotlib.pyplot as plt

df = pd.read_csv('Traffic_Crashes_Crashes.csv')
#cleaning all the data for the columns that using
df['CRASH_YEAR'] = pd.DatetimeIndex(df['CRASH_DATE']).year #seperating crash year from crash date
df = df[df['INJURIES_FATAL'].notnull()] #dropping NaN
df = df[df['WEATHER_CONDITION'] != 'UNKNOWN'] #dropping unknown
df = df[df['ROAD_DEFECT'] != 'UNKNOWN'] #dropping unknown
df = df[df['LIGHTING_CONDITION'] != 'UNKNOWN'] #dropping unknown
df.HIT_AND_RUN_I = df.HIT_AND_RUN_I.fillna('N') #replacing all the empty space to N("No")
df.INTERSECTION_RELATED_I = df.HIT_AND_RUN_I.fillna('N') #replacing all the empty space to N("No")
newdf = df[df['POSTED_SPEED_LIMIT'] % 5 !=  0].index # Cleaning speed limit data
df.drop(newdf, inplace=True) #Cleaning speed limit data
print(df)


# ### Question 2. Some attributes are more useful if you break them into several attributes. An example of this is already included in the data set where the time, day, and month of the crash are given as separate attributes. These attributes allow you to compare crashes based on the day of the week, time, or month (season). Are there other attributes that you can break down into smaller attributes to gain more information from?
# 

# **Answer - I did break CRASH_DATE attribute into smaller chuck by only getting the CRASH_YEAR since I wanted to check the fatality by year.**

# ### Question 3. What are some insights about the crashes and date/time? You can look into season, day of the week, day/night, lightning, weather, etc.

# **Answer - I am comparing the crash by weather condition in june and january, and trying to get the insights if the weather plays any role to number of crash. By looking at the below graph we can say even though the total number of crashes is less in clear weather in winter compared to summer but still most 
# crashes are happening in clear weather.**

# In[122]:


data = df[['CRASH_MONTH','CRASH_DAY_OF_WEEK','WEATHER_CONDITION']]
crashJune = data.loc[(df['CRASH_MONTH'] == 6)]
crashJune = crashJune.groupby(['WEATHER_CONDITION' ])['WEATHER_CONDITION'].count()
print(crashJune)

crashJune.plot(x ='WEATHER_CONDITION', title ='Crash number by weather in June', kind = 'bar')


# In[123]:


data = df[['CRASH_MONTH','CRASH_DAY_OF_WEEK','WEATHER_CONDITION']]
crashJan = data.loc[(df['CRASH_MONTH'] == 1)]
crashJan = crashJan.groupby(['WEATHER_CONDITION' ])['WEATHER_CONDITION'].count()
print(crashJan)

crashJan.plot(x ='WEATHER_CONDITION', title ='Crash number by weather in January', kind = 'bar')


# ### Question 4. Has number of deadly crashes increased recently? Look at the data over the years. Can you identify any significant increase/decrease?
# 

# **Answer - Yes, we can clearly see the deadly crashes has constantly been increasing year by year. There was a sudden increase in 2017 compared to 2016. In 2019, it dropped little bit in comparison to 2018.**

# In[116]:


deadly = df[['CRASH_YEAR', 'INJURIES_FATAL']]
deadly = deadly.groupby(['CRASH_YEAR' ])['INJURIES_FATAL'].sum()
print(deadly)

deadly.plot(x ='CRASH_YEAR', title ='Crash fatality by years', kind = 'bar')


# ### Question 5. Investigate number and type of injuries based on the speed limit.

# **Answer - I am comparing incapacitating, non-incapacitating and fatal injuries by the speed limit. After finding the data, I don't see any major difference incomparison to speed limit with the injuries. Speed limit 30 has the highest number of injury.**

# In[107]:


incap = df[['POSTED_SPEED_LIMIT', 'INJURIES_INCAPACITATING']]
incap = incap.groupby(['POSTED_SPEED_LIMIT' ])['INJURIES_INCAPACITATING'].sum()
print(incap)

incap.plot(x ='POSTED_SPEED_LIMIT', title ='INJURIES INCAPACITATING BY SPEED LIMIT', kind = 'bar')


# In[104]:


nonIncap = df[['POSTED_SPEED_LIMIT', 'INJURIES_NON_INCAPACITATING']]
nonIncap = nonIncap.groupby(['POSTED_SPEED_LIMIT' ])['INJURIES_NON_INCAPACITATING'].sum()
print(nonIncap)

nonIncap.plot(x ='POSTED_SPEED_LIMIT', title ='INJURIES NON-INCAPACITATING BY SPEED LIMIT', kind = 'bar')


# In[126]:


fatalInjury = df[['POSTED_SPEED_LIMIT', 'INJURIES_FATAL']]
fatalInjury = fatalInjury.groupby(['POSTED_SPEED_LIMIT' ])['INJURIES_FATAL'].sum()
print(fatalInjury)
fatalInjury.plot(x ='POSTED_SPEED_LIMIT', title ='INJURIES FATAL BY SPEED LIMIT', kind = 'bar')


# ### Question 6. Is there a relationship between hit and run crashes and number of fatal injuries?

# **Answer - Firstly, there were empty rows that I replaced to N("No") since I assume that means those cases weren't hit and run. As shown below, there are some cases in which hit and run crashes let into fatal injuries**

# In[100]:


hitRun = df[['HIT_AND_RUN_I', 'INJURIES_FATAL']]
hitRun = hitRun.groupby(['HIT_AND_RUN_I' ])['INJURIES_FATAL'].sum()
print(hitRun)
hitRun.plot(x ='HIT_AND_RUN_I', y ='INJURIES_FATAL', title ='INJURIES FATAL BY SPEED LIMIT', kind = 'pie')


# ### Question 7.  Do intersection-related crashes result in more fatal injuries?
# 

# **Answer - There were empty rows that I replaced to N("No") since I assume that means those cases weren't intersection-related crashes. As shown below, there are some cases in which intersection-related crashes let into fatal injuries**

# In[101]:


interRelated = df[['INTERSECTION_RELATED_I', 'INJURIES_FATAL']]
interRelated = interRelated.groupby(['INTERSECTION_RELATED_I' ])['INJURIES_FATAL'].sum()
print(interRelated)
interRelated.plot(x ='INTERSECTION_RELATED_I', y ='INJURIES_FATAL', title ='INJURIES FATAL BY SPEED LIMIT', kind = 'pie')


# ### Question 8. Try to include visualization with your answer to these questions.
# 

# **Answer - I have included visualization for the work that I have done.**

# ### Question 9. Come up with at least two more interesting insights and visualize them. (Suggestions: Season/weather/road condition and fatalities, or hit and run, ... } )
# 

# **1.I am getting the insight if the road defect have any affect to crashes. By looking at the graph, we can say that mostly no defects are reason for crashes.**

# **2.I am getting the insight in what lighting condition more crashes are 
# happening. From the graph, we can tell that more crashes are in daylight
# compared that to darkness.**

# In[130]:


rdDefect = df[['ROAD_DEFECT']]
rdDefect = rdDefect.groupby(['ROAD_DEFECT'])['ROAD_DEFECT'].count()
print(rdDefect)
rdDefect.plot(x ='ROAD_DEFECT', title ='crash count by road defect', kind = 'bar')


# In[131]:


lightCond = df[['LIGHTING_CONDITION']]
lightCond = lightCond.groupby(['LIGHTING_CONDITION'])['LIGHTING_CONDITION'].count()
print(cras)
lightCond.plot(x ='LIGHTING_ONDITION', title ='crash count by lighting condition', kind = 'bar')

