# WebScrapingToDataframe
Python script for scraping project descriptions from Innovation Norway website.<br>
Project descriptions are in Norwegian.<br>
Results are saved as csv file 'description_.csv'.

Jupyter notebook: reads csv file and cleans the description columns.<br>
Concatenates the columns into one text per project.<br>
Creates a clean dataframe with result.<br>
Number of rows: 149.<br>
Creating Bag of Words.<br>
Lemmatization, and inspecting most frequent nouns in bag of words.<br>
Using spaCy language model in Norwegian bokmål.<br>

We would like to be able to search through the projects by theme for example 'havvind', 'helse', 'bistand', 'afrika', etc.<br>
The projects should be tagged automatically.<br>

Also we would like to be able to find projects which are similar to a selected one for instance.<br>

Python version: 3.74<br>
