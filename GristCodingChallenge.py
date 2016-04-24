# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 17:39:51 2016

@author: siddhujz
"""
import json

#Read the input json file
#with open('test.json') as data_file:
with open('apply-20-challenge.json') as data_file:
    data = json.load(data_file)

#Number of Rows in the dataset
rows = len(data)
#Number of Columns in the dataset
columns = len(data[0])

#Initialize a sum matrix - this contains the maximum sum at each position
sum = [[0 for x in range(rows)] for x in range(columns)] 
#Initialize a Path matrix - to obtain the path of the maximum sum
path = [["" for x in range(rows)] for x in range(columns)] 

for i in range(0, rows):
    for j in range(0, columns):
        #for the first element in the dataset
        if i == 0 and j == 0:
            sum[i][j] = data[i][j]
        #for the first row elements in the dataset
        elif i == 0:
            sum[i][j] = sum[i][j - 1] + data[i][j]
            path[i][j] = "R"
        #for the first column elements in the dataset
        elif j == 0:
            sum[i][j] = sum[i - 1][j] + data[i][j]
            path[i][j] = "D"
        #For any other element in the dataset
        else:
            #tSum is the sum value obtained by moving from the top row(previous row) downwards
            #lSum is the sum value obtained by moving from the left column(previous column) towards right
            tSum = sum[i - 1][j] + data[i][j]
            lSum = sum[i][j - 1] + data[i][j]
            sum[i][j] = max(tSum, lSum)
            if sum[i][j] == lSum:
                path[i][j] = "R"
            else:
                path[i][j] = "D"

print("Maximum Sum =",sum[rows - 1][columns - 1])

pathStr = ""
i = rows - 1
j = columns - 1
#Loop to obtain the path which gave the maximum sum
while i != 0 or j != 0:
    if path[i][j] == "D":
        pathStr = "D" + pathStr
        i = i - 1
    else:
        pathStr = "R" + pathStr
        j = j - 1

print("path =",pathStr)

