# WebScrapingToDataframe
Python script for scraping project descriptions from Innovation Norway website. 
Project descriptions are in Norwegian.
Results are saved as csv file 'description_.csv'.

Jupyter notebook: reads csv file and cleans the description columns.
Concatenates the columns into one text per project. 
Creates a clean dataframe with result.
Number of rows: 149.

We would like to be able to search through the projects by theme for example 'havvind', 'helse', 'bistand', 'afrika', etc.
The projects should be tagged automatically.

Also we would like to be able to find projects which are similar to a selected one for instance.

Python version: 3.74
