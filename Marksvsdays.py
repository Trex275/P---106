import plotly.express as px
import csv
import numpy as np

with open("Student Marks vs Days Present.csv") as csv_file: 
    df = csv.DictReader(csv_file)


with open("cups of coffee vs hours of sleep.csv") as csv_file:  
    df = csv.DictReader(csv_file)

def getDataSource(data_path):
    studentmarks = []
    hoursslept = []
    with open(data_path) as csv_file:
          csv_reader = csv.DictReader(csv_file)
          for row in csv_reader:
              studentmarks.append(float(row["Student Marks"]))
              hoursslept.append(float(row["Hours Slept"]))
    return {"x" : studentmarks, "y": hoursslept}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("the value of corrrelations is ", correlation)


def setup():
    data_path  = "P106\Student Marks vs Days Present.csv - cups of coffee vs hours of sleep.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
setup()