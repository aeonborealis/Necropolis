# An Introduction to Data Science and Data Analysis using Python

# the Purpose of this document is to introduce to us the role of a data scientist and the techniques of data Analysis
# Data Analysts use programming tools to mine large ammounts of complex information and find relevant information from this data

# The desirable skills for a data analyst to have are
# Domain Expertise, Programming Skills, Statistical Insight, Visualization Skills, Storytelling/Narrative Skills

# In this document we will go over downloading and cleaning a dataset
# then we  will move on to analysis and visualization 

# Know about and understand the use of Kaggle for data set acquisition 
# Through out this document we will be utilizing multiple tools, but this document is written in Python and specific to Python 

# Lets get started: what is a CSV file?

# A CSV file is a comma-seperated-value file. This file format was developed for use with the language Fortran 77, approved in 1978. 
# The specifications for this file format was covered in the RFC 4180. It goes over 4 basic features of the CSV file: 

# 1. Is plaintext using character encoding such as ASCII
# 2. Consists of records, typically one record per line
# 3. The records are  divided into fields seperated by delimiters (typical delimiters: characters such as comma, semicolon, or tab)
# 4. Every Record has the same sequence of fields

# CSV files are best used for large arrays of data, such as data sets, data bases and relational databases

# After downloading the dataset, you will need to read the .csv file as a data frame in Python
# You can do this using the Pandas Library
# In order to import the Pandas Library for python, you can utilize the following code to create a Python Data Frame using python 

import pandas as pd
df = pd.read_csv('diabetes.csv)

# In looking at the above code we first simply imported pandas as pd
# The next line establishes the data frame with python by opening up the file and reading it through pandas

# To check the head of the data frame, run:

df.head()

# doing this displays the csv file in a mode similar to an excel spreadsheet, so to speak, it visually represents the csv file 
# in a format that seperates the fields in accordance with the head of the data, the head contains these 'field headers' 

# when looking at the data above we will need to understand the relationship this data has to the fields being presented, 
# meaning as a data scientist we have to intuit or better yet, understand what the data represents, this understanding will inform how we 
# process clean and visualize the data, it ultimately informs the relavant information to be extracted from the data
# bare with me, in order to be a data 'scientist' we have to develop a frame work for knowing and understanding how fields of data
# are related to each other, this is not something that the data informs us of, but is something we come to the data with. 

# Pandas Profiling 

# This is a very useful tool that can be used by analysts. It generates an analysis report on the data help, this helps to understand
# correlations between variables. 

# To generate a pandas profiling report, run the following lines od code;

import pandas_profiling as pp
pp.ProfileReports(df)

# this report will give you several statstical information on the dataset
# running this pandas report will yield great amount of information regarding the data, specifically finding redundencies. 

# This report is saves a lot of time and is great report to run to preliminary analyze the values being studied

# Tools for Data Analysis: Correlation Matrix
# A correlation matrix gives us a better understanding of the correlation between the variables in the dataset. 

# The most helpful Python Libraries for cleaning data are: 
# + NumpPy
# + Pandas
# + Matplotlib
# + Datacleaner
# + Dora
# + Seaborn
# + Arrow
# + Scrubadub

# commands for pandas that can help in data analysis
# NA and NaN are the standard missing value representations by Pandas
# the isna() function returns true if a value is missing 
# you can comebing the isna() with the sum() 
# to fill the missing values: fillna()

# pandas can also handle textual data and date and time data, using str and dt respectively

# for example we have a list of names ages. 
# we want to use the str and split function to take the first and last name and split them up into two different fields 
# we can use the following code to do so:

df[['First_name', 'Last_name']] = df['Name'].str.split(' ', expand=True)

# Look at the function above, we are calling the data frame to take two values to be derived from the data frame, 
# specifically from the Name Field we are searching for Space which would inform us the 'split' between a first and last name

# Another Example would be our ability to use this kind of interpolation with date data

# For example we get a series of dates that are in the format 'year-month-day'  
# using dt we can split this into different colomns: 

df['month] = df.col_a.dt.month
df['dayofweek'] = df.col_a.dt.dayofweek

# with the code above we can see what we are doing is taking the information contained within the structure of 'year-month-date' 
# then we are creating new colomns with this data and labeling them as

# Data Visualization 

# After we have a decent understanding of the variables we can try to find the relationship between them 
# We will be using the following three libraries to get the job done:
# 1. Matplotlib
# 2. Seaborn
# 3. Plotpy

# Visualizing the outcome variable 
# First runt the following lines of code to import Matplotlib, Seaborn, Numpy and Plotly after installation: 

# Visualization Imports

import matplotlib.pyplot as plt
import searborn as sns
color = sns.color_palette()
get_ipython() .run_line_magic('matplotlib', 'inline')
import Plotpy.offline as py
py.init_notebook_mode(connected=True)
import plotpy.graph_objs as go 
import plotpy.tools as tls
import plotly.expresss as px 
import numpy as np

# Next, run the following lines of code to create a pie chart visualizing the outcome variable: 

dist = df['Outcome'].value_counts()
colors = ['mediumturquoise', 'darkorange']
trace = go.Pie(values=np.array(dist)), labels=dist.index)
layout = go.Layout(title='Diabetes Outcome')
data = [trace]
fig = go.Figure(trace, layout)
fig.update_traces(marker=dict(colors=colors,
line=dict(color='#000000', width=2)))
fig.show()

# We can use the above code as a template for when we would like to create charts and visualizations 

# Similar to the correlation matrix that we discussed we can create one using the following code usng Plotly

def df_to_plotly(df):
    return {'z': df.values.tolist(), 
            'x': df.columns.tolist(),
            'y': df.index.tolist() }

import plotly.graph_objects as go 
dfNew = df.corr()
fig = go.Figure(data=go.Heatmap(df_to_plotly(dfNew)))
fig.show()

# This allows us to identify correlation between different sets of data, this could be extremely useful for establishing correlated data pairs

# In order to understand correlations between vraiables we will create some plots:
# Visualize Glucose levels and insulin 

fig = px.scatter(df, x='Glucose', y='Insulin')
fig.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='Glucose and Insulin')
fig.show()

# the above code runs a plot that shows the correlation between the variables glucose and insulin

# Now we will visualize the variables outcome and age. We will create a boxplot to do so

fig = px.box(df, x='Outcome', y='Age')
fig.update_traces(marker_color="midnightblue",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='Age and Outcome')
fig.show()

# Finally we will visualize BMI and Outcome using the following code: 

plot = sns.boxplot(x='Outcome',y="BMI",data=df)

# The two above samples show us how we can easily 

# The last part of this analysis that we want to cover is the story telling
# At first you must be wondering, why is storytelling an important skill for a data scientist to have?
# because interpreting data is all about positing narratives or stories that speak to the correlations of that data
# Often times the people who we are explaining the correlations in relevant data towards are not well versed in data science
# this would include managers and CEOs, people who actively make decisions based on the data that you are providing
# In those roles often time it will be much more helpful to establish a narrative that explains why you are seeing the data you are seeing


