#  <span style="color:tan"> **Module 12 Web Scraping Challenge**  </span>
### Chris Gruenhagen 27Dec2022
**Homework Log**

The xxx homework is located in the xx directory in the xx repository.  The xx homework consists of a jupyter notebook "xx" and output files located in the "output_data" directory (xx.csv file and xx png files).

---
### **Purpose**

The purpose of this homework was to:
1. Scrape the titles and preview text from Mars news articles from the https://redplanetscience.com/ website.  Store data in a JSON file and a MongoDB database.
2. Scrape and analyze Mars weather data from an html table on the https://data-class-mars-challenge.s3.amazonaws.com/Mars/index.html site.

### **Study Format**

In this study, data on a single day (Nov 6, 2022) from over 500 random cities of varying distances from the equator were evaluated to visualize the potential relationships between latitude and temperature, humidity, cloudiness, and wind speed in both the Northern and Southern hemispheres. Data was obtained from OpenWeather https://openweathermap.org/.

Limitations:  This dataset was generated on a single day so it does not capture day to day variation, and it relies on data from cities which are generally located in more liveable locations by latitude.  Comparisons between the northern and southern hemispheres may be impacted by differences in the number of cities (northern = 393, southern = 168) and ranges of latitude evaluated (northern 0 to 77, southern 0 to -55).

Exclusions: At the beginning of the study, 611 random cities were selected from the citipy library. While pulling additional weather data from OpenWeather, 50 cities were excluded due to errors in data processing, leaving a dataset of 561 cities for analysis.

### **Attribution**
‘Mars news articles provided by’
https://redplanetscience.com/

‘Mars temperature data provided by’
https://data-class-mars-challenge.s3.amazonaws.com/Mars/index.html


### Conclusions

What is the weather like as we approach the equator?

Based on the data collected on 561 random cities on November 6, 2022 from OpenWeather https://openweathermap.org/, temperature increases and wind speed appears to decrease as we approach the equator.  Humidity and cloudiness did not appear to be correlated with latitude.

### **Analysis**
### *Requirement 1:  Create Plots to showcase the relationship between weather variables and latitude across the globe.*

Worldwide Latitude vs Temperature
![Alt text](/WeatherPy_VacationPy/output_data/Fig1.png "Latitude vs Temp")

Worldwide Latitude vs Humidity
![Alt text](/WeatherPy_VacationPy/output_data/Fig2.png "Latitude vs Humidity")

Worldwide Latitude vs Cloudiness
![Alt text](/WeatherPy_VacationPy/output_data/Fig3.png "Latitude vs Cloudiness")

Worldwide Latitude vs Wind Speed

![Alt text](/WeatherPy_VacationPy/output_data/Fig4.png "Latitude vs Wind Speed")
---
### *Requirement 2: Compute Linear Regression for Each Relationship in the Northern and Southern Hemispheres.*

Latitude vs Temperature in the Northern and Southern Hemispheres
![Alt text](/WeatherPy_VacationPy/output_data/North_Lat_vs_Max%20Temp.png "Northern Latitude vs Humidity")
![Alt text](/WeatherPy_VacationPy/output_data/South_Lat_vs_Max%20Temp.png "Southern Latitude vs Humidity")

        **Discussion about the linear relationship:**
         In the northern hemisphere, there is a very strong negative correlation (r = -0.84) between latitude and max temperature.  In the southern hemisphere, there is a moderate correlation (r = 0.53) between latitude and max temperature.  In both hemispheres, the max temperature increases as you approach the equator (latitude = 0). 
         
         The northern latitude appears to have a greater temperature difference (-33C to 33C) than the southern latitude (9C to 33C), but the city locations in the northern latitudes also span a much greater range of latitudes (lat 0 to 77) than the cities in the southern latitudes (lat 0 to -55). Additional data and/or analysis would be required to evaluate differences between the two hemispheres.
         


Latitude vs Humidity in the Northern and Southern Hemispheres
![Alt text](/WeatherPy_VacationPy/output_data/North_Lat_vs_Humidity.png "Northern Hemisphere Latitude vs Humidity") 
![Alt text](/WeatherPy_VacationPy/output_data/South_Lat_vs_Humidity.png "Southern Hemisphere Latitude vs Humidity")

        **Discussion about the linear relationship:** 
        In the northern hemisphere, there is a very weak to weak correlation (r = 0.24) between latitude and humidity. In the southern hemisphere, there is a weak correlation (r =0.32) between latitude and humidity.  Humidity varies widely across latitudes in both hemispheres, from 13 to 100%. 

Latitude vs Cloudiness in the Northern and Southern Hemispheres
![Alt text](/WeatherPy_VacationPy/output_data/North_Lat_vs_Cloudiness.png "Northern Hemisphere Latitude vs Cloudiness") 
![Alt text](/WeatherPy_VacationPy/output_data/South_Lat_vs_Cloudiness.png "Southern Hemisphere Latitude vs Cloudiness")

        **Discussion about the linear relationship:** 
        In both the northern and southern hemispheres, there is a weak correlation (r = 0.28, r = 0.33) between latitude and cloudiness. Cloudiness varies widely across latitudes in both hemispheres, from 0 to 100%.

Latitude vs Wind Speed in the Northern and Southern Hemispheres
![Alt text](/WeatherPy_VacationPy/output_data/North_Lat_vs_Wind%20Speed.png "Northern Hemisphere Latitude vs Wind Speed") 
![Alt text](/WeatherPy_VacationPy/output_data/South_Lat_vs_Wind%20Speed.png "Southern Hemisphere Latitude vs Wind Speed")

        **Discussion about the linear relationship:** 
        In the northern hemisphere, there is a very weak to weak correlation (r = 0.22) between latitude and wind speed. In the southern hemisphere, there is a weak negative correlation (r = - 0.29) between latitude and wind speed.  Although wind speed varies widely across latitudes in both hemispheres (0-14 m/s), the average wind speed in both hemispheres appear to decrease as you approach the equator (latitude = 0).
---

# &#x1F469;&#x200D;&#x1F680; &#x1F680; &#x1f311; &#x1F47D; &#x1F6F8; &#x1F30E; &#x1F6F8; &#x1F47D; &#x1f311;&#x1F680; &#x1F469;&#x200D;&#x1F680;
     emoji & format references:
        https://emojipedia.org
        https://www.markdownguide.org/basic-syntax/


***See below for original homework instructions***
# <span style="color:tan"> Module 12 Web Scraping Challenge </span>
Due Jan 4, 2023 by 11:59pm 

Points 100 

Submitting a text entry box or a website url
_________________________________________________________
## <span style="color:red"> **Background**  </span>

You’re now ready to take on the full web-scraping and data analysis project for the mission to Mars. You’ve learned to identify HTML elements on a page, identify their id and class attributes, and use this knowledge to extract information via both automated browsing with Splinter and HTML parsing with Beautiful Soup. You’ve also learned to scrape various types of information. These include HTML tables and recurring elements, like multiple news articles on a webpage.

As you work on this Challenge, remember that you’re strengthening the same core skills that you’ve been developing until now: collecting data, organizing and storing data, analyzing data, and then visually communicating your insights.

##  <span style="color:orange"> **What You're Creating** </span>

This new assignment consists of two technical products. You will submit the following deliverables:

* Deliverable 1: Scrape titles and preview text from Mars news articles. Optionally export the data into a JSON file or a MongoDB database.

* Deliverable 2: Scrape and analyze Mars weather data, which exists in a table.

##  <span style="color:yellow"> **Files** </span>

Download the following files to help you get started:

Module 12 Challenge files

https://static.bc-edx.com/data/dl-1-1/m12/lms/starter/Starter_Code.zip

##  <span style="color:green">  **Instructions** </span>

### ***Deliverable 1: Scrape Titles and Preview Text from Mars News***

Open the Jupyter Notebook in the starter code folder named part_1_mars_news.ipynb. You will work in this code as you follow the steps below to scrape the Mars News website.

1. Use automated browsing to visit the Mars NASA news site Links to an external site.. Inspect the page to identify which elements to scrape.

    HINT: To identify which elements to scrape, you might want to inspect the page by using Chrome Dev Tools.
2. Create a Beautiful Soup object and use it to extract text elements from the website.

3. Extract the titles and preview text of the news articles that you scraped. Store the scraping results in Python data structures as follows:

    * Store each title-and-preview pair in a Python dictionary. And, give each dictionary two keys: title and preview. An example is the following:

        {'title': "Mars Rover Begins Mission!",
      'preview': "NASA's Mars Rover begins a multiyear mission to collect data about the little-explored planet."}
    * Store all the dictionaries in a Python list.

    * Print the list in your notebook.

4. Optionally, store the scraped data in a file or database (to ease sharing the data with others). To do so, export the scraped data to either a JSON file or a MongoDB database.

### ***Deliverable 2: Scrape and Analyze Mars Weather Data***

Open the Jupyter Notebook in the starter code folder named part_2_mars_weather.ipynb. You will work in this code as you follow the steps below to scrape and analyze Mars weather data.

1. Use automated browsing to visit the Mars Temperature Data Site Links to an external site.. Inspect the page to identify which elements to scrape. Note that the URL is https://data-class-mars-challenge.s3.amazonaws.com/Mars/index.html.

    HINT: To identify which elements to scrape, you might want to inspect the page by using Chrome DevTools to discover whether the table contains usable classes.

2. Create a Beautiful Soup object and use it to scrape the data in the HTML table. Note that this can also be achieved by using the Pandas read_html function. However, use Beautiful Soup here to continue sharpening your web scraping skills.

3. Assemble the scraped data into a Pandas DataFrame. The columns should have the same headings as the table on the website. Here’s an explanation of the column headings:

    * id: the identification number of a single transmission from the Curiosity rover
    * terrestrial_date: the date on Earth
    * sol: the number of elapsed sols (Martian days) since Curiosity landed on Mars
    * ls: the solar longitude
    * month: the Martian month
    * min_temp: the minimum temperature, in Celsius, of a single Martian day (sol)
    * pressure: The atmospheric pressure at Curiosity's location

4. Examine the data types that are currently associated with each column. If necessary, cast (or convert) the data to the appropriate datetime, int, or float data types.

5. Analyze your dataset by using Pandas functions to answer the following questions:
    1. How many months exist on Mars?
    2. How many Martian (and not Earth) days worth of data exist in the scraped dataset?
    3. What are the coldest and the warmest months on Mars (at the location of Curiosity)? To answer this question:
        * Find the average the minimum daily temperature for all of the months.
        * Plot the results as a bar chart.
    4. Which months have the lowest and the highest atmospheric pressure on Mars? To answer this question:
        * Find the average the daily atmospheric pressure of all the months.
        * Plot the results as a bar chart.
    5. About how many terrestrial (Earth) days exist in a Martian year? To answer this question:
        * Consider how many days elapse on Earth in the time that Mars circles the Sun once.
        * Visually estimate the result by plotting the daily minimum temperature.
6. Export the DataFrame to a CSV file.


##  <span style="color:blue"> **Requirements** </span>
### ***Deliverable 1: Scrape Titles and Preview Text from Mars News (40 points)***
* Automated browsing (with Splinter) was used to visit the Mars news site, and the HTML code was extracted (with Beautiful Soup) (10 points)

* The titles and preview text of the news articles were scraped and extracted (20 points)

* The scraped information was stored in the specified Python data structure—specifically, a list of dictionaries (10 points)

### ***Deliverable 2: Scrape and Analyze Mars Weather Data (60 points)***
* The HTML table was extracted into a Pandas DataFrame. Splinter and Beautiful Soup were used to scrape the data. The columns have the correct headings and data types (15 points)

* The data was analyzed to answer all five listed questions, with data visualizations provided when specified (40 points)

* The DataFrame was exported into a CSV file (5 points)


## <span style="color:indigo"> **References**  </span>

© 2020 - 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.