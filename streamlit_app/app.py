# app.py
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load the dataset
import os
csv_path = os.path.join(os.path.dirname(__file__), 'Studio Ghibli Films.csv')
movie_data = pd.read_csv(csv_path)


#movie_data = pd.read_csv('Studio Ghibli Films.csv')

# Clean Revenue column
movie_data['Revenue'] = movie_data['Revenue'].replace('[\$,]', '', regex=True).astype(float)
movie_data['Budget'] = movie_data['Budget'].replace('[\$,]', '', regex=True).astype(float)


# Streamlit UI
st.title('Studio Ghibli Revenue Analysis')

st.markdown("""

# Hi! 
I will be analysing the revenue of all the full-length films made by the famous Japanese film studio, Studio Ghibli. I will be examining the revenue across various features such as genre, director, screenwriter, length, and more. I am also currently building a small ML model based on this data, to predict some of the revenues. For now, I'll start with importing the libraries needed for analysis.

These are the questions I will look at: 

**Preliminary:** 
* How does the dataset look like?
* What are the datatypes of the values and do they need to be converted to another type?
* Are there missing values?

**Basic:** 
* Which movies were the highest-performing in terms of box-office revenue?
* Which genres were the highest-performing?

**Analysis:** 
* What is the ROI per movie?
* Does a higher budget indicate higher revenue?
* Which decade had the highest revenue per movie, and how has it changed over the years?

**(In Progress) Machine Learning Implementation:**
* I'll be using a Random Forest model to predict the revenue of the movies, since it appears to not only depend on the budget, during a preliminary scan of the data. 

 """)

# Q1 - Highest Performing Movies
st.markdown(""" # Q1. Which movies were the most successful at the Box Office? """) 

# Sorting movies by revenue
highestRevenue_movies = movie_data.sort_values(by='Revenue', ascending=False)
highestRevenue_movies_graph = highestRevenue_movies[['Name', 'Revenue']].head()

# Display the table
st.write(highestRevenue_movies_graph)

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Create a barplot
sns.barplot(data=highestRevenue_movies_graph, x='Revenue', y='Name', palette='viridis', ax=ax)

# To include the revenue numbers in a readable way
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))

# Title and labels
ax.set_title('Highest Performing Studio Ghibli Movies')
ax.set_xlabel('Revenue ($)')
ax.set_ylabel('Movie')

# Display the plot in Streamlit
st.pyplot(fig)

st.markdown("""
# Q2. Which genres were the most succesful? 
             """)

# Sorting movies by revenue
highestRevenue_movies = movie_data.sort_values(by='Revenue', ascending=False)

# Selecting the top movies by revenue, using 'Genre 1' instead of 'Name'
highestRevenue_movies_graph = highestRevenue_movies[['Genre 1', 'Revenue']].head()

# Creating a figure and axis for the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Creating the bar plot
sns.barplot(data=highestRevenue_movies_graph, x='Revenue', y='Genre 1', palette='viridis', ax=ax)

# To include the revenue numbers in a readable format
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))

# Adding the title and labels
ax.set_title('Highest Performing Studio Ghibli Movie Genres')
ax.set_xlabel('Revenue ($)')
ax.set_ylabel('Genre')

# Display the plot
st.pyplot(fig)

st.markdown("""
            There is an error bar running through Fantasy and Animation. This suggests that there is a lot of variability in the 
            revenue made by these genres. This might mean that genre is not a perfect measure of box office success, and may not help much in the prediction of it. 
            """)


st.markdown("""

# Q3. Who directed the top performing movies?
Miyazaki is the most well-known, but how is the 
            distribution among the directors?
            
            """)

# Grouping by Director and sorting by average revenue
topRevenue_byDirector = movie_data.groupby('Director')['Revenue'].mean().sort_values(ascending=False).head()

# Creating a figure and axis for the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Creating the bar plot
sns.barplot(x=topRevenue_byDirector.values, y=topRevenue_byDirector.index, palette='mako', ax=ax)

# Adding the title and labels
ax.set_title('Top Directors by Average Revenue')
ax.set_xlabel('Average Revenue ($)')
ax.set_ylabel('Director')

# Display the plot in Streamlit
st.pyplot(fig)

st.markdown("""
            # Q4. Does a higher budget indicate higher success?
            
            """)

# Creating a figure and axis for the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Creating the scatter plot
sns.scatterplot(data=movie_data, x='Budget', y='Revenue', hue='Name', palette='tab10', ax=ax)

# Adding the title and labels
ax.set_title('Budget vs. Revenue')
ax.set_xlabel('Budget ($)')
ax.set_ylabel('Revenue ($)')

# Adding the legend
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot in Streamlit
st.pyplot(fig)

st.markdown("""
There seems to be slight correlation so a 
            line of best fit can be drawn to see further. 
            """)
# Creating a figure and axis for the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Creating the regression plot
sns.regplot(data=movie_data, x='Budget', y='Revenue', robust=True, ax=ax)

# Adding the title and labels
ax.set_title('Budget vs. Revenue (Regression)')
ax.set_xlabel('Budget ($)')
ax.set_ylabel('Revenue ($)')

# Display the plot in Streamlit
st.pyplot(fig)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Create the regression plot
sns.regplot(data=movie_data, x='Budget', y='Revenue', scatter_kws={'s': 60}, robust=True, ax=ax)

# Add movie names on the plot
for i, row in movie_data.iterrows():
    ax.text(row['Budget'], row['Revenue'], row['Name'], fontsize=8, alpha=0.7)

# Add title and labels
ax.set_title('Does Higher Budget Indicate Higher Revenue?')
ax.set_xlabel('Budget ($)')
ax.set_ylabel('Revenue ($)')

# Adjust layout
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(fig)

st.markdown("""
The big outliers seem to be 'The Tale of Princess Kaguya'( having a big budget but comparatively lesser revenue), and 'Spirited Away' (having a lesser budget comparitely with a high revenue amount). 

*The Tale of Princess Kaguya* had a much higher budget than the box office revenue. This is one of the most expensive studio ghibli films, having a budget of $49,300,000 .This budget is only topped by The Boy and the Heron, the recent release of 2023. 

Despite its budget, it could not perform more than its budget. Perhaps the reason could lie in the differentiating factors between this movie and the other films from the Studio. It was animated using watercolor-like style, and a slower, thoughtful pace.
            
            """)

st.markdown("""

# Q5. Which movies had the highest ROI? (Return on investment)
            """)

# Calculate ROI
movie_data['ROI'] = (movie_data['Revenue'] - movie_data['Budget']) / movie_data['Budget']

# Ensure that any NaN values from the calculation (due to missing 'Revenue' or 'Budget') are handled
movie_data = movie_data.dropna(subset=['ROI'])

# Get the top 5 movies with the highest ROI
highest_ROI = movie_data.sort_values(by='ROI', ascending=False).head()

# Create the figure and axis for plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the data
sns.barplot(data=highest_ROI, x='ROI', y='Name', palette='deep', ax=ax)

# Add titles and labels
ax.set_title('Top 5 Studio Ghibli movies: highest ROI')
ax.set_xlabel('ROI')
ax.set_ylabel('Movie')

# Pass the figure to st.pyplot
st.pyplot(fig)

st.markdown("""
*Spirited Away*, *Howl's moving castle*, *Princess Monoke*, are all 
part of the top five box-office performing movies of the studio. (q1)
            """)

st.markdown("""

# Q6. Which decade had the highest revenue per movie on average? 
           """)


import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Calculate the decade for each movie
movie_data['Decade'] = (movie_data['Year'] // 10) * 10

# Calculate average revenue per decade
decade_revenue = movie_data.groupby('Decade')['Revenue'].mean().sort_index()

# Create the figure and axis for plotting
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the data
sns.lineplot(x=decade_revenue.index, y=decade_revenue.values, marker='o', ax=ax)

# Add titles and labels
ax.set_title('Average Revenue per Movie by Decade')
ax.set_xlabel('Decade')
ax.set_ylabel('Average Revenue ($)')
ax.set_xticks(decade_revenue.index)

# Pass the figure to st.pyplot
st.pyplot(fig)

st.markdown("""

The movies in the 2000's had the highest average movie revenue by a lot, followed by the 2010's, then the 1990's, then the 1980's.

2000's performance is because of breakthrough successes like *Howl's Moving Castle*, *Spirited Away*, and *Ponyo*, which are the top three box office performing movies from Studio Ghibli. But it is important to note 2010's also had successes like T*he Secret World of Arrietty* and *The Wind Rises*, and it still had a much higher average revenue than the 1990's and the 1980's.

Information about the 2020's is still limited, but it looks promising as the film that was released in 2023: *The Boy and the Heron*, is the fourth highest Box Office Performing movie of the Studio, amassing a $172,766,713 revenue.

After the 2000's, the films performed much better than before. This is perhaps because of the exposure to international audiences. The increase in popularity of Japanese films and animations have increased, providing a larger audience for the newer releases.
            
            """)

st.markdown("""# Future Work

**Adjust for Inflation**: Analyze revenues in inflation-adjusted terms for a fair comparison.

**Explore Movie Count**: Examine whether fewer releases in the 2010s contributed to the revenue decline.

**Global Market Influence**: Investigate how Ghibli's expansion to international markets impacted revenues.

**Adjust for Impact**: Using BoxOffice Revenue is an imperfect metric of success. For example, *My Neighbour Totoro*, had lesser Box Office than its budget, but it has since become one of the most iconic films, in the era of streaming and global audience. This should be accounted for in the future.
""")

st.markdown(""" ## Thank you for Reading! """)