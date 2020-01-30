# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 13:20:14 2020

@author: Samrat
"""
#Importing all the Important Packages required for Web Scraping
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as Soup

#Creating columns
col = ['Name','Company','City','Ratings','Summary','Date']

#Creating a data File Name indeed where I'm going to save the Scrapped Data.
indeed = pd.DataFrame(columns = col)

#Creating a loop to scrapped first 1000 pages
for page in range(0,1000):
    urls = "https://www.indeed.com/jobs?q=Software+Engineer&l=94115&radius=25&start="
    url = urls + str(page*10)
    P_url = requests.get(url)
    P_html = P_url.text
    P_soup = Soup(P_html, "html.parser")
    containers = P_soup.findAll("div", {"data-tn-component": "organicJob"}) 
    #print(len(containers))
    #print(Soup.prettify(containers[0]))
    container = containers[0]
    for container in containers:
        Name = container.findAll("a",{"class": "jobtitle turnstileLink"})
        name = Name[0].text.strip()

        Company = container.findAll("span",{"class":"company"})
        comp = Company[0].text.strip()
    
        City =  container.findAll('span',{"class":"location accessible-contrast-color-location"})
        city = City[0].text.strip()
       
    
        ratings = container.findAll("span",{"class":"ratingsDisplay"})
        if len(ratings) != 0:
          rat = ratings[0].text.strip()
          #print(rat)
        else:
          rat = "NaN"
        
        Summ = container.findAll("div",{"class":"summary"})
        summ = Summ[0].text.strip()
        #print(summ)
    
        date = container.findAll('span',{"class":"date"})
        dat = date[0].text.strip()
        #print(dat)
        

        data = pd.DataFrame([[name, comp, city, rat, summ, dat]])
        data.columns = col
        indeed = indeed.append(data, ignore_index = True)
#Printing the Final Datasets of 10 thousand Profiles
print(indeed)    
#Saving the DataSet in the Local Drive E:, you can save according to your local storage.
indeed.to_excel('E:\Indeeds.xls')
  
