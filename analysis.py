# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 12:30:27 2022

@author: SARA
"""


import pandas as pd
import webbrowser
import dash
import dash_html_components as html
import pandas as pd
import dash_core_components as dcc
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go



#import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


#VARIABLES DECLARATIO
app = dash.Dash()
df = pd.read_csv("global_terror.csv")
df2 = pd.read_csv("india_terror.csv")


ol1 = ['to find out the hot zone of terrorism',
       'to identify and highlight the geographical and temporal patterns of the terrorism',
       'What all security issues and insights you can derive by EDA?',
       'to discover the main parameters of a successful terrorist attack,and ']

conclusion = ['Iraq country has highest number of attacks (24636)',
              'Middle and East Africa region has highest number of attacks (50474)',
              'Explosives are the most weapon used by terrorsits (92426).',
              'From the analysis we can see that on 2014 the number of terrorist activities were the highest in Iraq Country (16806)',
              'Private citizens and Property were the main targets in terrorism activity (43510)',
              'Bombing and Explosion methods were most commonly used in terrorism activity (82255).',
              'Taliban is most Notorious group with highest number of terrorist activitiies (7478)',
              '84% of the terrorist attacks in 1970 were carried out on the American continent. In 1970, the Middle East and North Africa, currently the center of wars and terrorist attacks, faced only one terrorist attack']

key_points = ['Strong security should be provided to the countries like Iraq, Pakistan, Afghanistan and India and also for middle East Regions and cities like Bhagdad, Karachi, Lima etc.',
              'Safety measures have to be take regarding explosives, as bombing explosions are the most commonly used weapon type used by terrorsits.',
              'Strong security should be provided to Private citizens and Property, Military,Police etc as they are main target in terrorism.']





#CREATING UI FOR EDA
def create_app_ui():
    
    main_layout = html.Div(
        [
            html.H2( 
                children = 'EXPLORATORY DATA ANALYSIS (EDA) on GLOBAL TERRORISM DATABASE (GTD) ',
                id='Main_title',
                style = {
                'textAlign' : 'center','color' : '#000','font-family' :' Verdana' ,'fontstyle' : 'bold' , 'font-weight':'bold'}),
    
            html.H4(children = '1. INTRODUCTION', style = {
                'color' : '#000','font-family' :' Verdana' ,'fontstyle' : 'bold','letter-spacing':'2px' }),
            html.Div([
                html.P('The scope of this project is to drill down the terrorist events around the world from 1970 through 2015'),
                html.P("The primary objectives are")]),
            
            html.Div(
                className="OL1",
                children=[
                html.Ul(id='my-list', children=[html.Li(i) for i in ol1])],),
            
            html.Div(),
            
             html.H4(children ='TERROR ACTIVITIES EACH YEAR'), html.Br(),
                 html.Div([html.Img(src='/assets/terroract_each_year.png')]), html.Br(),
                 html.P('The graphs shows that there was a drastic increase in terrorism in year 2014, with more than 16000 attacks.'),
            html.Div([
                html.H4(children ='HOT ZONES OF TERRORISM (by Country)'),
                html.Br(),
                html.Div([
                    html.P(children = 'From the above analysis we conclude that city of Baghdadh highest number of attacks.'),])
            ]),
            
                html.Div([
                html.Img(src='/assets/affected_countries.png')]),
                html.Br(),
                
    
                 html.H4(children ='HOT ZONES OF TERRORISM (by City)'), html.Br(),
                 html.Div([html.Img(src='/assets/affected_cities.png')]), html.Br(),
                 html.P('From the graph below, it is evident, Iraq country has highest number of attacks.'),
                 html.P('Total Attacks = 24636'),
                 
                 html.H4(children ='TERRORIST ACTIVITIES BY REGION IN EACH YEAR THROUGH AREA PLOT'), html.Br(),
                 html.Div([html.Img(src='/assets/area_plot.png')]), html.Br(),
                
                 
             
                 html.H4(children ='NUMBER OF PEOPLE ATTACKED Vs KILLED'), html.Br(),
                 html.Div([html.Img(src='/assets/attack_kill.png')]), html.Br(),
                 
                 html.H4(children ='NUMBER OF PEOPLE KILLED IN EACH COUNTRY'), html.Br(),html.Br(),
                 html.Div([html.Img(src='/assets/no_of_peoplekilledbycountry.png')]), html.Br(),
                 html.Div([html.Img(src='/assets/no_of_peoplekilledbycountry2.png')]), html.Br(),
                 html.Div([html.Img(src='/assets/no_of_peoplekilledbycountry.3png.png')]), html.Br(),
                  
                 html.H4(children ='ACTIVITY OF TOP TERRORIST GROUPS'), html.Br(),
                 html.Div([html.Img(src='/assets/act_terror.png')]), html.Br(),
                 
                 html.H4(children ='MOSTLY TARGETTED REGIONS '), html.Br(),
                 html.Div([html.Img(src='/assets/favt.png')]), html.Br(),
                 
                 html.H4(children ='MOST USED ATTACK TYPE'), html.Br(),
                 html.Div([html.Img(src='/assets/tp2.png')]), html.Br(),
                 
                 html.H4(children ='ATTACK TYPE BASED ON REGION'), 
                 html.P('Let us check out the type of attack carried out in in each country.'),
                 html.Div([html.Img(src='/assets/attacktypeVsRegion.png')]), html.Br(),
                 
                 
                 html.H4(children ='CONCLUSION' , style = {'fontweight':'bold'}), 
                 html.Div(
                 className="Conclusion",
                 children=[
                 html.Ul(id='my-list2',children=[html.Li(i) for i in conclusion ])],),
                 
                 html.H4(children ='KEY POINT' , style = {'fontweight':'bold'}), 
                 html.Div(
                 className="key_points",
                 children=[
                 html.Ul(id='my-list3',children=[html.Li(i) for i in key_points ])],),
                 
                 html.H3('NOTE'),
                 html.P('Terrorist acts in the Middle East and northern Africa have been seen to have fatal consequences. The Middle East and North Africa are seen to be the places of serious terrorist attacks. In addition, even though there is a perception that Muslims are supporters of terrorism, Muslims are the people who are most damaged by terrorist attacks. If you look at the graphics, it appears that Iraq, Afghanistan and Pakistan are the most damaged countries. All of these countries are Muslim countries.')
             
             
             ],style={'color' : '#000','font-family' :' Verdana', 'margin':'70px'})#End of first div and method
   
          
    return main_layout



#Terrorist Activities Each Year
plt.subplots(figsize=(15,6))
sns.countplot('iyear',data=df,palette='GnBu',edgecolor=sns.color_palette('PuBuGn_r',7))
plt.xticks(rotation=60)
plt.title('Number Of Terrorist Activities Each Year')
plt.show()



#Hot zones of terrorism (by Country)
plt.subplots(figsize=(18,6))
sns.barplot(df['country_txt'].value_counts()[:15].index,df['country_txt'].value_counts()[:15].values,palette='plasma_r')
plt.title('Top Affected Countries')
plt.show()

#Hot zones of terrorism (by City)
plt.subplots(figsize=(18,6))
sns.barplot(df['city'].value_counts()[1:15].index,df['city'].value_counts()[1:15].values,palette='gnuplot2_r')
plt.title('Top Affected Cities')
plt.show()


# Terrorist Activities by Region in each Year through Area Plot 
pd.crosstab(df.iyear, df.region_txt).plot(kind='area',figsize=(15,6))
plt.title('Terrorist Activities by Region in each Year')
plt.ylabel('Number of Attacks')
plt.show()


#Attacks vs Killed
coun_terror=df['country_txt'].value_counts()[:15].to_frame()
coun_terror.columns=['Attacks']
coun_kill=df.groupby('country_txt')['nkill'].sum().to_frame()
coun_terror.merge(coun_kill,left_index=True,right_index=True,how='left').plot.bar(width=0.9)
fig=plt.gcf()
fig.set_size_inches(18,6)
plt.show()


#Activity of top terrorist group
top_groups10=df[df['gname'].isin(df['gname'].value_counts()[1:11].index)]
pd.crosstab(top_groups10.iyear,top_groups10.gname).plot(color=sns.color_palette('magma',10))
fig=plt.gcf()
fig.set_size_inches(18,6)
plt.show()





#Favorite Targets
plt.subplots(figsize=(15,6))
sns.countplot(df['targtype1_txt'],palette='inferno',order=df['targtype1_txt'].value_counts().index)
plt.xticks(rotation=90)
plt.xlabel('TARGET')
plt.title('Favorite Targets')
plt.show()





#AttackType vs Region
pd.crosstab(df.region_txt,df.attacktype1_txt).plot.barh(stacked=True,width=1,color=sns.color_palette('RdYlGn',9))
fig=plt.gcf()
fig.set_size_inches(12,8)
plt.show()



#Favorite attack type
f,ax=plt.subplots(1,2,figsize=(10,10))
ind_groups=df['gname'].value_counts()[1:11].index
ind_groups=df[df['gname'].isin(ind_groups)]
sns.countplot(y='gname',data=ind_groups,ax=ax[0])
ax[0].set_title('Top Terrorist Groups')
sns.countplot(y='attacktype1_txt',data=df,ax=ax[1])
ax[1].set_title('Favorite Attack Types')
plt.subplots_adjust(hspace=0.3,wspace=0.6)
ax[0].tick_params(labelsize=15)
ax[1].tick_params(labelsize=15)
f.set_figwidth(15)
f.set_figheight(10)
plt.show()



#Number of Killed in Terrorist Attacks by Countries -------1
countryData = df.loc[:,'country_txt']
import numpy as np
killData = df.loc[:,'nkill']
# countyData
countryKillData = pd.concat([countryData, killData], axis=1)
countryKillFormatData = countryKillData.pivot_table(columns='country_txt', values='nkill', aggfunc='sum')
countryKillFormatData
fig_size = plt.rcParams["figure.figsize"]
fig_size[0]=25
fig_size[1]=25
plt.rcParams["figure.figsize"] = fig_size

labels = countryKillFormatData.columns.tolist()
labels = labels[:50] #50 bar provides nice view
index = np.arange(len(labels))
transpoze = countryKillFormatData.T
values = transpoze.values.tolist()
values = values[:50]
values = [int(i[0]) for i in values] # convert float to int
colors = ['red', 'green', 'blue', 'purple', 'yellow', 'brown', 'black', 'gray', 'magenta', 'orange'] # color list for bar chart bar color 
fig, ax = plt.subplots(1, 1)
ax.yaxis.grid(True)
fig_size = plt.rcParams["figure.figsize"]
fig_size[0]=15
fig_size[1]=15
plt.rcParams["figure.figsize"] = fig_size
plt.bar(index, values, color = colors, width = 0.9)
plt.ylabel('Killed People', fontsize=20)
plt.xlabel('Countries', fontsize = 20)
plt.xticks(index, labels, fontsize=18, rotation=90)
plt.title('Number of people killed by countries', fontsize = 20)
# print(fig_size)
plt.show()





#Number of Killed in Terrorist Attacks by Countries -------2
labels = countryKillFormatData.columns.tolist()
labels = labels[50:101]
index = np.arange(len(labels))
transpoze = countryKillFormatData.T
values = transpoze.values.tolist()
values = values[50:101]
values = [int(i[0]) for i in values]
colors = ['red', 'green', 'blue', 'purple', 'yellow', 'brown', 'black', 'gray', 'magenta', 'orange']
fig, ax = plt.subplots(1, 1)
ax.yaxis.grid(True)
fig_size = plt.rcParams["figure.figsize"]
fig_size[0]=15
fig_size[1]=15
plt.rcParams["figure.figsize"] = fig_size
plt.bar(index, values, color = colors, width = 0.9)
plt.ylabel('Killed People', fontsize=20)
plt.xlabel('Countries', fontsize = 20)
plt.xticks(index, labels, fontsize=18, rotation=90)
plt.title('Number of people killed by countries', fontsize = 20)
plt.show()




#Number of Killed in Terrorist Attacks by Countries -------3
labels = countryKillFormatData.columns.tolist()
labels = labels[152:206]
index = np.arange(len(labels))
transpoze = countryKillFormatData.T
values = transpoze.values.tolist()
values = values[152:206]
values = [int(i[0]) for i in values]
colors = ['red', 'green', 'blue', 'purple', 'yellow', 'brown', 'black', 'gray', 'magenta', 'orange']
fig, ax = plt.subplots(1, 1)
ax.yaxis.grid(True)
fig_size = plt.rcParams["figure.figsize"]
fig_size[0]=15
fig_size[1]=15
plt.rcParams["figure.figsize"] = fig_size
plt.bar(index, values, color = colors, width = 0.9)
plt.ylabel('Killed People', fontsize=20)
plt.xlabel('Countries', fontsize = 20)
plt.xticks(index, labels, fontsize=18, rotation=90)
plt.title('Number of people killed by countries', fontsize = 20)
plt.show()


#----------------------------------------------------

















#-------------------------------------------------------



def open_browser():
    
    webbrowser.open_new('http://127.0.0.1:8050/')

def main():
    
    
    open_browser()
    
    project_name = "Terrorism Analysis and Finding Insights" 
    
    global app
    app.layout = create_app_ui()
    app.title = project_name
   
    app.run_server() 
  
    print('Execution Ended')
    app = None
    project_name = 'None'


if __name__ == '__main__':
    main()
