# import seaborn as sns
# import matplotlib.pyplot as plt
#%matplotlib inline
import requests      
import pandas as pd
import numpy as np
import plotly.express as px

        
def graphics():
    lst=pd.read_html('https://www.mohfw.gov.in/')
    dfs=lst[0]
    dfs.drop(columns=['S. No.'],inplace=True)
    dfs=dfs.rename(columns={'Name of State / UT':'State','Total Confirmed cases (Including 77 foreign Nationals)':'Cases',
                         'Cured/Discharged/Migrated':'Cured','Death':'Death'})
    dfs.replace("Nagaland#","Nagaland",inplace=True)
    dfs.drop(index=[33,34,35],inplace=True)
    data=dfs[dfs['Cases'].astype(str).astype(int) > 300]
    
    
    fig = px.pie(data, values='Cases', names='State',
                 title='Population of American continent',
                 hover_data=['Death'], labels={'Death':'Death'})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig.show()

# temp=graphics()
# temp    