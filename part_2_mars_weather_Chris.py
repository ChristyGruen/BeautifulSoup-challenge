#!/usr/bin/env python
# coding: utf-8

# # Module 12 Challenge
# ## Deliverable 2: Scrape and Analyze Mars Weather Data

# In[1]:


# #magic
# %matplotlib


# In[2]:


# Import relevant libraries
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplcursors
import pandas as pd
from datetime import datetime
from datetime import timezone


# In[3]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Step 1: Visit the Website
# 
# Use automated browsing to visit the [Mars Temperature Data Site](https://data-class-mars-challenge.s3.amazonaws.com/Mars/index.html). Inspect the page to identify which elements to scrape. Note that the URL is `https://data-class-mars-challenge.s3.amazonaws.com/Mars/index.html`.
# 
#    > **Hint** To identify which elements to scrape, you might want to inspect the page by using Chrome DevTools to discover whether the table contains usable classes.
# 

# In[4]:


# Visit the website
# https://data-class-mars-challenge.s3.amazonaws.com/Mars/index.html
url = 'https://data-class-mars-challenge.s3.amazonaws.com/Mars/index.html'
browser.visit(url)


# ### Step 2: Scrape the Table
# 
# Create a Beautiful Soup object and use it to scrape the data in the HTML table.
# 
# Note that this can also be achieved by using the Pandas `read_html` function. However, use Beautiful Soup here to continue sharpening your web scraping skills.

# In[5]:


# Create a Beautiful Soup Object
html = browser.html
soup = soup(html,"html.parser")


# In[6]:


# Extract all rows of data
tempdata = soup.find_all('table',class_='table')

for tdata in tempdata:
    temphead = tdata.find_all('th')
    tempdict= tdata.find_all('tr',class_='data-row')
    print('-----------------')
    print(temphead)
    print(tempdict)


# ### Step 3: Store the Data
# 
# Assemble the scraped data into a Pandas DataFrame. The columns should have the same headings as the table on the website. Here’s an explanation of the column headings:
# 
# * `id`: the identification number of a single transmission from the Curiosity rover
# * `terrestrial_date`: the date on Earth
# * `sol`: the number of elapsed sols (Martian days) since Curiosity landed on Mars
# * `ls`: the solar longitude
# * `month`: the Martian month
# * `min_temp`: the minimum temperature, in Celsius, of a single Martian day (sol)
# * `pressure`: The atmospheric pressure at Curiosity's location

# In[7]:


# # Create an empty list
# lheaders = []
# lrows = []
# # Loop through the scraped data to create a list of rows
# tempdata = soup.find_all('table',class_='table')


# for tdata in tempdata:
#     temphead = tdata.find_all('th')
#     lheaders.append(temphead)
#     tempdict= tdata.find_all('tr',class_='data-row')
#     lrows.append(tempdict)
#     print(lheaders)
#     print(lrows)


# In[8]:



# Create an empty list
# Loop through the scraped data to create a list of column names
colnames = []
tempheaders = soup.find_all('table',class_='table')
for tr in tempheaders:
    th = tr.find_all('th')
    row = [tr.text for tr in th]
    colnames.append(row)
colnamesflat = [item for sublist in colnames for item in sublist]
colnamesflat


# In[9]:


# Create an empty list
# Loop through the scraped data to create a list of rows

lrows = []
tempdata = soup.find_all('tr',class_='data-row')
for tr in tempdata:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    lrows.append(row)

lrows


# In[10]:


browser.quit()


# In[11]:


# Create a Pandas DataFrame by using the list of rows and a list of the column names
# Confirm DataFrame was created successfully
mdf= pd.DataFrame(lrows,columns = colnamesflat)
mdf


# ### Step 4: Prepare Data for Analysis
# 
# Examine the data types that are currently associated with each column. If necessary, cast (or convert) the data to the appropriate `datetime`, `int`, or `float` data types.
# 
#   > **Hint** You can use the Pandas `astype` and `to_datetime` methods to accomplish this task.
# 

# In[12]:


# Examine data type of each column
mdf.dtypes


# In[13]:


# Change data types for data analysis
mdf['sol'] = mdf['sol'].astype('int') 
mdf['ls'] = mdf['ls'].astype('int')
mdf['month'] = mdf['month'].astype('int')


# In[14]:


# Change data types for data analysis
mdf['min_temp'] = mdf['min_temp'].astype('float')
mdf['pressure'] = mdf['pressure'].astype('float')


# In[15]:


# Change data types for data analysis
mdf.terrestrial_date = pd.to_datetime(mdf.terrestrial_date)
mdf['Date']=mdf['terrestrial_date'].dt.date


# In[16]:


# Confirm type changes were successful by examining data types again
mdf.dtypes


# In[17]:


mdf


# ### Step 5: Analyze the Data
# 
# Analyze your dataset by using Pandas functions to answer the following questions:
# 
# 1. How many months exist on Mars?
# 2. How many Martian (and not Earth) days worth of data exist in the scraped dataset?
# 3. What are the coldest and the warmest months on Mars (at the location of Curiosity)? To answer this question:
#     * Find the average the minimum daily temperature for all of the months.
#     * Plot the results as a bar chart.
# 4. Which months have the lowest and the highest atmospheric pressure on Mars? To answer this question:
#     * Find the average the daily atmospheric pressure of all the months.
#     * Plot the results as a bar chart.
# 5. About how many terrestrial (Earth) days exist in a Martian year? To answer this question:
#     * Consider how many days elapse on Earth in the time that Mars circles the Sun once.
#     * Visually estimate the result by plotting the daily minimum temperature.
# 

# In[18]:


# 1. How many months are there on Mars?
nmonths = mdf.month.nunique()
print(f' There are {nmonths} months on Mars.')


# In[19]:


# 2. How many Martian days' worth of data are there?
#sol = number of elapsed sols (Martian days)since Curiosity landed on Mars

datasol = mdf.sol.nunique()
print(f" There are {datasol} Martian days' worth of data.")


# In[20]:


# 3. What is the average low temperature by month?
avlowt = mdf.groupby('month')['min_temp'].mean().reset_index()
avlowt


# In[45]:


# Plot the average temperature by month
monthtemp = mdf.groupby('month')['min_temp'].mean().plot(legend = True, title = "Average Martian Temperature by Month")
monthtemp




# In[56]:


# Plot the average temperature by month
fig,ax = plt.subplots()
ln, =ax.plot(mdf.groupby('month')['min_temp'].mean())
ln.set_color('purple')
plt.title('Average Minimum Martian Temperature by Month')
plt.xlabel ('Martian Month')
plt.ylabel('Degrees Celsius')
plt.grid()
mplcursors.cursor(hover=True)

plt.show()


# In[23]:


# Identify the coldest and hottest months in Curiosity's location
avtemp = mdf.groupby('month')['min_temp'].mean().sort_values().reset_index()
raspberry = len(avtemp.month)-1

print('----------------------')
print(f' The coldest month is {avtemp.month[0]} with an average temperature of {round(avtemp.min_temp[0],2)} degrees Celsius.')
print('----------------------')
print(f' The hottest month is {avtemp.month[raspberry]} with an average temperature of {round(avtemp.min_temp[raspberry],2)} degrees Celsius.')
print('----------------------')


# In[24]:


# 4. Average pressure by Martian month
avpressure = mdf.groupby('month')['pressure'].mean().reset_index()
avpressure


# In[25]:


# Plot the average pressure by month
avpressplot = mdf.groupby('month')['pressure'].mean().plot.bar(x='month', y='pressure', legend = True, title = "Average Martian Pressure by Month")


# In[26]:


# Identify the coldest and hottest months in Curiosity's location
avpress = mdf.groupby('month')['pressure'].mean().sort_values().reset_index()
plum= len(avpress.month)-1

print('----------------------')
print(f' The month with the lowest pressure is {avpress.month[0]} with an average pressure of {round(avpress.pressure[0],2)}.')
print('----------------------')
print(f' The month with the highest pressure is {avpress.month[plum]} with an average pressure of {round(avpress.pressure[11],2)}.')
print('----------------------')


# In[27]:


#visual estimation of number of earth days in a Martian year

visdays = mdf.plot(x = 'terrestrial_date',y = 'ls',legend = True, figsize=[30,10],title = "Terrestrial Days per Martian Year")
visdays.xaxis.set_major_locator(mdates.MonthLocator())

mplcursors.cursor(visdays)
plt.show()


# In[28]:


import matplotlib.pyplot as plt
import numpy as np
import mplcursors

data = np.outer(range(10), range(1, 5))

fig, ax = plt.subplots()
lines = ax.plot(data)
ax.set_title("Click somewhere on a line.\nRight-click to deselect.\n"
             "Annotations can be dragged.")
fig.tight_layout()

mplcursors.cursor(lines)

plt.show()


# In[29]:


#visual estimation of number of earth days in a Martian year
# Plot the average temperature by month

lines = mdf.plot(x = 'terrestrial_date',y = 'ls',legend = True, figsize=[30,10],title = "Terrestrial Days per Martian Year")
lines.xaxis.set_major_locator(mdates.MonthLocator())


lines.set_title("Click somewhere on a line.\nRight-click to deselect.\n"
             "Annotations can be dragged.")


mplcursors.cursor(lines)

plt.show()


# In[30]:


# Calculate number of earth days in Martian year
# iterate through the dataframe to find the first and last days of Curiosity's first full year on Mars
#FDOYindex = first day of year index
#LDOYindex = last day of year index
#ls goes from 0 to 359 per solar orbit, i.e. year
prevls = 0

for index, row in mdf.iterrows():
    if row['ls'] == 0:
        FDOYindex = index
        break

for index, row in mdf.iterrows():
    if row['ls'] >= prevls:
        prevls=row['ls']
        LDOYindex = index
    if row['ls'] == 0 and index > FDOYindex+1:
        break

print(FDOYindex)
print(LDOYindex)
    


# In[31]:


# Calculate number of earth days in Martian year
# to calculate days between dates
# https://pynative.com/python-difference-between-two-dates/#:~:text=Use%20the%20strptime(date_str%2C%20format,as%20per%20the%20corresponding%20format%20.&text=To%20get%20the%20difference%20between,result%20is%20a%20timedelta%20object.
#ls 0 to 359 signifies one Martian year
# 2015-06-18 terrestrial_date, sol = 1018, ls = 359, index = 924 (last measurement of 1st full Martian year for Curiosity) 2013-08-01 terrestrial_date, ls = 0, sol = 351, index = 304 (first measurement of 1st full Martian year for Curiosity)
# 687 days per google

floof = mdf['Date'][FDOYindex]
print(f"The first terrestrial_date of Curiosity's first full year on Mars is {floof}.")
poof = mdf['Date'][LDOYindex]
print(f"The last terrestrial_date of Curiosity's first full year on Mars is {poof}.")


# difference between dates in timedelta
delta = poof - floof
print(f'The difference is {delta.days} days.')
print(f'Total number of days in a Martian year is {delta.days+1} days.')


# On average, the third month has the coldest minimum temperature on Mars, and the eighth month is the warmest. But it is always very cold there in human terms!
# 
# 

# Atmospheric pressure is, on average, lowest in the sixth month and highest in the ninth.

# The distance from peak to peak is roughly 1425-750, or 675 days. A year on Mars appears to be about 675 days from the plot. Internet search confirms that a Mars year is equivalent to 687 earth days.

# ### Step 6: Save the Data
# 
# Export the DataFrame to a CSV file.

# In[32]:


# Write the data to a CSV
mdf.to_csv('MarsWeather.csv', index = False)
#option to save to resources folder
# mdf.to_csv('Resources/MarsWeather.csv', index = False)


# In[33]:


browser.quit()


# In[ ]:




