# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup

with open('C:/Users/student/Desktop/PythonPractice/US08621662_20140107.XML','r') as f:
    xml = f.read()
    
soup = BeautifulSoup(xml,'lxml')

print(soup.find('invention-title').get_text())