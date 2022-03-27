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


ol1 = ['to deliver precise and effective communication of the insights hidden in the data through appropiraite graphical or pictorial representations',
       'to find out the hot zone of terrorism',
       'to identify and highlight the geographical and temporal patterns of the terrorism',
       'What all security issues and insights you can derive by EDA']



key_points = ['Strong security should be provided to the countries like Iraq, Pakistan, Afghanistan and India and also for middle East Regions and cities like Bhagdad, Karachi, Lima etc.',
              'Safety measures have to be take regarding explosives, as bombing explosions are the most commonly used weapon type used by terrorsits.',
              'Strong security should be provided to Private citizens and Property, Military,Police etc as they are main target in terrorism.']


general_analysis = [ 'We obsevered that terrorist attack increase over the years in general year 2014 saw most terrorist attacks',
                    'Top four countries who faced most terrorist attacks are Iraq, Pakistan, Afghanistan and India',
                    'Middle East & North Africa, South Aisa and South America were most vurnable to terrorist attacks',
                    'Top three Weapon used in attacks were Bombing/Explosion, Armed Assault and Assassination',
                    'Year 2014, 2015 and 2016 faced more casuality',
                    'Iraq country has highest number of attacks (24636)',
                    'Middle and East Africa region has highest number of attacks (50474)',
                    'Explosives are the most weapon used by terrorsits (92426).',
                    'From the analysis we can see that on 2014 the number of terrorist activities were the highest in Iraq Country (16806)',
                    'Private citizens and Property were the main targets in terrorism activity (43510)',
                    'Bombing and Explosion methods were most commonly used in terrorism activity (82255).',
                    'Taliban is most Notorious group with highest number of terrorist activitiies (7478)',
                    '84% of the terrorist attacks in 1970 were carried out on the American continent. In 1970, the Middle East and North Africa, currently the center of wars and terrorist attacks, faced only one terrorist attack'
                    ]

region_based_analysis = [
                        'In South Asia region Top three country who faced attacks are Pakistan, Afghanistan and India',
                        'Top Three country who faaced more terrorist attacks Japan, China and Taiwan in East Asia',
                        'UK, Spain and France were most suffered from terrorist attack in Western Europe',
                        'Terrorist most favourable country for attack in Middle East & North Africa region were Iraq, Turkey and Yemen',
                        'Colombia, Peru and Chile were more vulnerable for terrorist attack in South America region',
                        'Easily attackable country in Sub-Saharan Africa region were Somalia, Nigeria and South Africa'
                        ]

india_analysis = [
                   ' More Attack faced in year 2016, 2015, 2014.',
                   'Bombing/Explosion and Firearms most favourable weapon for attack.',
                   'Casuality in year 2006, 2008 and 1991 were more.',
                   'Most terrorist attcks at target place Private Citizen & Property, Police and Government.',
                   'J&K, Assam and Punjab faced more casuality.',
                   'Max number of terrorist attact in states J&K , Assam and Manipur.'
                 ]



#CREATING UI FOR EDA
def create_app_ui():
    
    main_layout = html.Div(
        [
            html.H2( 
                children = 'EXPLORATORY DATA ANALYSIS (EDA) on GLOBAL TERRORISM DATASET (GTD) ',
                id='Main_title',
                style = {
                'textAlign' : 'center','color' : '#000','font-family' :' Verdana' ,'fontstyle' : 'bold' , 'font-weight':'bold'}),
            html.Br(),html.Br(),html.Br(),
            html.H4(children = '1. INTRODUCTION', style = {
                'color' : '#000','font-family' :' Verdana' ,'fontstyle' : 'bold','letter-spacing':'2px' }),
            html.Br(),
            html.Div([
                html.P('The scope of this project is to drill down the terrorist events around the world from 1970 through 2015'),
                html.P("The primary objectives are")]),
            html.Br(),
            html.Div(
                className="OL1",
                children=[
                html.Ul(id='my-list', children=[html.Li(i) for i in ol1])], style = {' line-height':'1.6'} ),
            html.Br(),
            html.Div(),
            html.Br(),
            html.H2(children = 'WORLD ANALYSIS', style = {'align':'centre'} ),
             html.H4(children ='TERROR ACTIVITIES EACH YEAR'), html.Br(),
                 html.Div([html.Img(src='/assets/terroract_each_year.png')]), html.Br(),
                 html.P('The graphs shows that there was a drastic increase in terrorism in year 2014, with more than 16000 attacks.'),
            html.Br(),html.Br(),
            html.Div([
                html.H4(children ='HOT ZONES OF TERRORISM (by Country)'),
                html.Br(),
                html.Div([
                    html.P(children = 'From the above analysis we conclude that city of Baghdadh highest number of attacks.'),])
            ]),
            html.Br(),
                html.Div([
                html.Img(src='/assets/affected_countries.png')]),
                html.Br(),
                
    
                 html.H4(children ='HOT ZONES OF TERRORISM (by City)'), html.Br(),
                 html.Div([html.Img(src='/assets/affected_cities.png')]), html.Br(),
                 html.P('From the graph below, it is evident, Iraq country has highest number of attacks.'),
                 html.P('Total Attacks = 24636'),
                 html.Br(),html.Br(),html.Br(),
                 
                 html.H4(children ='TERRORIST ACTIVITIES BY REGION IN EACH YEAR THROUGH AREA PLOT'), html.Br(),
                 html.Div([html.Img(src='/assets/area_plot.png')]), html.Br(),
                
                 
             
                 html.H4(children ='NUMBER OF PEOPLE ATTACKED Vs KILLED'), html.Br(),html.Br(),
                 html.Div([html.Img(src='/assets/attack_kill.png')]), html.Br(),
                 
                 
                  
                 html.H4(children ='ACTIVITY OF TOP TERRORIST GROUPS'), html.Br(),
                 html.Div([html.Img(src='/assets/act_terror.png')]), html.Br(),
                 
                 html.H4(children ='MOSTLY TARGETTED REGIONS '), html.Br(),
                 html.Div([html.Img(src='/assets/favt.png')]), html.Br(),
                 
                 html.H4(children ='MOST USED ATTACK TYPE'), html.Br(),
                 html.Div([html.Img(src='/assets/tp2.png')]), html.Br(),
                 html.H5('Percentage Calculated: '),
                 html.Div([html.Img(src='/assets/pie.png')]), html.Br(),
                 
   #-------------------ATTACK TYPE  BASED ON REGION--------------------------------              
                 html.H4(children ='ATTACK TYPE BASED ON REGION'), 
                 html.P('Let us check out the type of attack carried out in in each country.'),
                 html.Div([html.Img(src='/assets/attacktypeVsRegion.png') ]), html.Br(),
    
    #------------------- KILL COUNT BASED ON REGION-------------------------------- 
                 html.H4(children ='KILL COUNT BASED ON REGION'), 
                 html.H5('1. South Asia'),
                 html.Div([html.Img(src='/assets/south_asia.png') ]), html.Br(),
                 
                
                 html.H5('2. East Asia'),
                 html.Div([html.Img(src='/assets/east_asia.png') ]), html.Br(),
                 
                 html.H5('3. Western Europe'),
                 html.Div([html.Img(src='/assets/western_europe.png') ]), html.Br(),
                 
                 html.H5('4. Middle East & North Africa'),
                 html.Div([html.Img(src='/assets/middle_east&north_africa.png') ]), html.Br(),
                 
                 html.H5('5. South America'),
                 html.Div([html.Img(src='/assets/south_america.png') ]), html.Br(),
                
                 
                 html.H5('6. North America'),
                 html.Div([html.Img(src='/assets/north_america.png') ]), html.Br(),
                 
                  html.H5('7. Sub-Saharan Africa'),
                 html.Div([html.Img(src='/assets/sub_saharan_africa.png') ]), html.Br(),
                 
                 html.H4('CASUALITIES EACH YEAR'),
                 html.Div([html.Img(src='/assets/casualities _each_year.png') ]), html.Br(),
 #------------------------------------------------------------------------------------


#INDIA ANALAYIS
            html.H2(children = 'INDIA ANALYSIS', style = {'align':'centre'} ),                
                 
             html.H4('Attacks Each year'),
                 html.Div([html.Img(src='/assets/india_attacks_year.png') ]), html.Br(),
                 
                 html.H4('WEAPONS USED'),
                 html.Div([html.Img(src='/assets/major_weapon _used.png') ]), html.Br(),
                 
                 html.H4('CASUALITIES'),
                 html.Div([html.Img(src='/assets/ind_casualities.png') ]), html.Br(),
                 
                 html.H4('TARGET TYPE'),
                 html.Div([html.Img(src='/assets/india_target_type.png') ]), html.Br(),
                 
                 html.H4('CASUALITIES PER STATE'),
                 html.Div([html.Img(src='/assets/india_casuaities_state.png') ]), html.Br(),
                 
                
               
                 
#-----------------------CONCLUSION, KEY POINTS, NOTE-------------------------                 
                 
                #-----GENERAL ANALYSIS-------------
                 html.Br(),html.Br(),
                 html.H4(children ='CONCLUSION' , style = {'fontweight':'bold'}), html.Br(),
                 html.H5(children = 'General Analysis' , style = {'font-weight':'bold'}),html.Br(),
                 html.Div(
                 className="GENERAL-ANALYSIS",
                 children=[
                 html.Ul(id='my-list1',children=[html.Li(i) for i in general_analysis])], ),
                 html.Br(),html.Br(),
                 
                 #INDIA ANALYSIS
                 html.H5(children = 'India Analysis' , style = {'font-weight':'bold'}),html.Br(),
                 html.Div(
                 className="INDIA-ANALYSIS",
                 children=[
                 html.Ul(id='my-list2',children=[html.Li(i) for i in india_analysis])], ),
                 html.Br(),html.Br(),
                 
                 
                 html.H4(children ='KEY POINT' , style = {'fontweight':'bold'}), html.Br(),
                 html.Div(
                 className="key_points",
                 children=[
                 html.Ul(id='my-list3',children=[html.Li(i) for i in key_points ] )],),
                 html.Br(),html.Br(),
                 html.H3('NOTE'),html.Br(),
                 html.P('Terrorist acts in the Middle East and northern Africa have been seen to have fatal consequences. The Middle East and North Africa are seen to be the places of serious terrorist attacks. In addition, even though there is a perception that Muslims are supporters of terrorism, Muslims are the people who are most damaged by terrorist attacks. If you look at the graphics, it appears that Iraq, Afghanistan and Pakistan are the most damaged countries. All of these countries are Muslim countries.')
             
             
             ],style={'align':'center','color' : '#28282B','font-family' :' Verdana', 'margin':'70px','line-height':'20px'})#End of first div and method
   
          
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
fig_size[0]=10
fig_size[1]=10
plt.rcParams["figure.figsize"] = fig_size
plt.bar(index, values, color = colors, width = 0.9)
plt.ylabel('Killed People', fontsize=15)
plt.xlabel('Countries', fontsize = 15)
plt.xticks(index, labels, fontsize=15, rotation=90)
plt.title('Number of people killed by countries', fontsize = 15)
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
fig_size[0]=10
fig_size[1]=10
plt.rcParams["figure.figsize"] = fig_size
plt.bar(index, values, color = colors, width = 0.9)
plt.ylabel('Killed People', fontsize=15)
plt.xlabel('Countries', fontsize = 15)
plt.xticks(index, labels, fontsize=15, rotation=90)
plt.title('Number of people killed by countries', fontsize = 15)
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
fig_size[0]=10
fig_size[1]=10
plt.rcParams["figure.figsize"] = fig_size
plt.bar(index, values, color = colors, width = 0.9)
plt.ylabel('People KIlled', fontsize=15)
plt.xlabel('Countries', fontsize = 15)
plt.xticks(index, labels, fontsize=15, rotation=90)
plt.title('Number of people killed by countries', fontsize = 15)
plt.show()


#--------------------NEW ADDS--------------------------------

#-------1------------------

region_country_group = df.groupby(['region_txt'])
def region_base_attack(regionName, color='winter'):
    region = region_country_group.get_group(regionName)['country_txt']
    plt.figure(figsize=(10,7))
    plt.xticks(rotation=90)
    sns.countplot(x=region, palette=color)
region_base_attack('South Asia')
region_base_attack('East Asia', 'summer')
region_base_attack("Western Europe", 'rainbow')
region_base_attack("Middle East & North Africa", "gist_rainbow_r")
region_base_attack('South America', "inferno_r")
region_base_attack('North America', "tab20b_r")
region_base_attack("Sub-Saharan Africa", "autumn")



#--------2-----------------
plt.figure(figsize=(10,10))
df['attacktype1_txt'].value_counts().plot.pie(autopct ="%1.1f%%")
plt.show()

#-------------FUNCTIONS------------
def generalCountPlot(x=None, data=None, pattel='autumn'):
    plt.figure(figsize=(12,7))
    plt.xticks(rotation=90)
    sns.countplot(x=x, data=data, palette=pattel)
def generalBarPlot(x=None, y=None, data=None, color='Paired', estimator=np.mean):
    plt.figure(figsize=(12,7))
    plt.xticks(rotation=90)
    sns.barplot(x=x, y=y, data=data, palette=color, estimator=estimator)
def generalPointPlot(x=None, y=None, data=None, color='Paired', estimator=np.mean, hue=None):
    plt.figure(figsize=(12,7))
    plt.xticks(rotation=90)
    sns.pointplot(x=x, y=y, data=df, palette=color, estimator=estimator, hue=hue)


#----Casualities-----

generalBarPlot(x='iyear', y='nkill', data=df, color="Oranges", estimator=np.sum)

#-----------------------------------------------
#-----------INDIA ANALYSIS-------------

generalCountPlot('iyear',df2,"Wistia" )

generalCountPlot('weaptype1_txt',df2,"nipy_spectral" )
generalPointPlot('iyear', 'nkill', df2,"magma_r" , np.sum)
generalCountPlot('targtype1_txt', df2,"bwr")

generalBarPlot('provstate', 'nkill', df2,"gnuplot" , np.sum)




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
