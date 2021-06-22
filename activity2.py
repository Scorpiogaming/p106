import csv
import numpy as np
import plotly.express as px
def plotfigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="Days Present",y='Marks In Percentage')
        fig.show()
def getdatasource(data_path):
    mip=[]
    dp=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            mip.append(float(row['Marks In Percentage']))
            dp.append(float(row['Days Present']))
    return {'x':mip,'y':dp}
def fc(ds):
    cr=np.corrcoef(ds['x'],ds['y'])
    print ("cr is"+str(cr[0,1]))
def setup():
    data_path='SDP.csv'
    ds=getdatasource(data_path)
    fc(ds)
    plotfigure(data_path)
setup()