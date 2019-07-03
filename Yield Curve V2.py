#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import time
import plotly.graph_objs as go 
import dash
import dash_core_components as dcc 
import dash_html_components as html 
import requests
import re
import dash_table



# In[2]:



url = "https://quote.cnbc.com/quote-html-webservice/quote.htm?partnerId=2&requestMethod=quick&exthrs=1&noform=1&fund=1&output=jsonp&symbols=US1M|US3M|US6M|US1Y|US2Y|US3Y|US5Y|US7Y|US10Y|US30Y&callback=quoteHandler1"

res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page,'html.parser')
text = soup.find_all(text = True)
text = str(text)

text2 = re.split(':|,"',text)


indices = [i for i, x in enumerate(text2)if x == r'last"']
indices2 = [i + 1 for i in indices]

yields = [text2[i] for i in indices2]

a = [i.replace('"', '') for i in yields]

yields2 = [float(i) for i in a]

yields2

df = pd.DataFrame({'Term': ['1 MO','3 MO','6 MO','1 YR', '2 YR', '3 YR', '5 YR', '7 YR', '10 YR', '30 YR'],
                  'Yields':yields2})






# In[4]:



app = dash.Dash()

x_values = df['Term']
y_values = df['Yields']


app.layout = html.Div([
            dcc.Graph(
                    id = 'live-curve',
                    figure = {'data':[
                        go.Scatter(x= x_values,
                                    y = y_values,
                                    mode = 'lines+markers')], 
                                    'layout':go.Layout(title = 'United States Treasury Curve')})
            
                                
                    ])


# In[ ]:





# In[ ]:


if __name__ == '__main__':
    app.run_server()


# In[ ]:


## html.Div(
                   

