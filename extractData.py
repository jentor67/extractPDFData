#!/usr/bin/python3
"""
File: extractData.py
Author: John Major
Date: 2025-10-30
Description:  Extract specific data from a list of PDFs
"""

import fitz
import glob
import os
import module
import csv

# set global position
xg = 0
yg = 0

# create a list
dataRows =[]

# create a list header record
line = [
    "HeartFlowRep",
    "phyNameX",
    "phyName",
    "NPI",
    "siteNameX",
    "siteName",
    "address",
    "city",
    "state",
    "zipCode",
    "website",
    "email",
    "phone",
    "fax",
    "fullName",
    "Title",
    "dateOf"]

# add header record to dataRows list
dataRows.append(line)


# define class
ext = module.pdfTools()

# set the extension to be used
pdfFiles = (".pdf",".PDF")

# set the directory
directory_path = "input"

# gather files
Files = sum([glob.glob(os.path.join(directory_path, "*" + x))
             for x in pdfFiles],[])


# open each file and gather info
for File in Files:
    # open pdf
    doc = fitz.open("test.pdf")
    # set page
    page = doc[0]
    
    # assign values to each variable 
    HeartFlowRep = ext.getText(page, xg+37, yg+300, 400)
    phyNameX = ext.getText(page, xg+35, yg+375, 15)
    phyName = ext.getText(page, xg+118, yg+375, 280)
    NPI = ext.getText(page, xg+450, yg+375, 100)
    siteNameX = ext.getText(page, xg+35, yg+405, 15)
    siteName = ext.getText(page, xg+118, yg+405, 450)
    address = ext.getText(page, xg+72, yg+438, 230)
    city = ext.getText(page, xg+330, yg+438, 120)
    state = ext.getText(page, xg+474, yg+438, 25)
    zipCode = ext.getText(page, xg+525, yg+438, 55)
    website = ext.getText(page, xg+70, yg+465, 500)
    email = ext.getText(page, xg+65, yg+522, 230)
    phone = ext.getText(page, xg+340, yg+522, 100)
    fax = ext.getText(page, xg+473, yg+522, 100)
    fullName = ext.getText(page, xg+100, yg+665, 250)
    Title = ext.getText(page, xg+382, yg+665, 200)
    dateOf = ext.getText(page, xg+482, yg+695, 135)

    # close pdf
    doc.close()

    # append variables to a list
    line = [
    HeartFlowRep,
    phyNameX,
    phyName,
    NPI,
    siteNameX,
    siteName,
    address,
    city,
    state,
    zipCode,
    website,
    email,
    phone,
    fax,
    fullName,
    Title,
    dateOf]

    # append line values to dataRows
    dataRows.append(line)

# create file and and add data to csv
with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerows(dataRows)


