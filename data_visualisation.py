# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar

cardiff = pd.read_csv('cardiffdata.csv')
berporth = pd.read_csv('aberporthdata.csv')
oxford = pd.read_csv('oxforddata.csv')
eastbourne = pd.read_csv('eastbournedata.csv')
valley = pd.read_csv('valleydata.csv')
# normalised 
cardiff_n =  cardiff[cardiff['year']>= 2014]
berporth_n = berporth[berporth['year']>= 2014]
oxford_n = oxford[oxford['year']>= 2014]
eastbourne_n = eastbourne[eastbourne['year']>=2014]
valley_n = valley[valley['year']>= 2014]
# further normalised to 2 columns
cardiff_n_o = cardiff_n.iloc[:, [0, 5]] 
berporth_n_o = berporth_n.iloc[:, [0, 5]] 
oxford_n_o = oxford_n.iloc[:, [0, 5]] 
eastbourne_n_o = eastbourne_n.iloc[:, [0, 5]] 
valley_n_o = valley_n.iloc[:, [0, 5]] 
# Now i will avarage the rainfall for each year witihn the rain column for
# each dataset.
# cardiff
cardiff_n_o['rain'] = cardiff_n_o['rain'].str.extract(pat='(\d+)',expand=False)
cardiff_n_o['rain'] = cardiff_n_o['rain'].astype(float)
c = cardiff_n_o.groupby('year')['rain'].mean().reset_index()
# Aberporth
berporth_n_o['rain'] = berporth_n_o['rain'].astype(float)
b = berporth_n_o.groupby('year')['rain'].mean().reset_index()
# oxford
oxford_n_o['rain'] = oxford_n_o['rain'].astype(float)
o = oxford_n_o.groupby('year')['rain'].mean().reset_index()
# eastbourne
eastbourne_n_o['rain'] = eastbourne_n_o['rain'].str.extract(pat='(\d+)',expand=False)
eastbourne_n_o['rain'] = eastbourne_n_o['rain'].astype(float)
e = eastbourne_n_o.groupby('year')['rain'].mean().reset_index()
# valoley
valley_n_o['rain'] = valley_n_o['rain '].astype(float)
v = eastbourne_n_o.groupby('year')['rain'].mean().reset_index()
# line plot
plt.figure(figsize=(12,6), facecolor= 'c' )
plt.plot( c['year'], c['rain'] ,marker=".", label = "Cardif weather station")
plt.plot(b['year'], b['rain'],marker=".", label= "Aberporth weather station")
plt.plot(o['year'], o['rain'],marker=".", label= "oxford weather station")
plt.plot(e['year'], e['rain'] ,marker=".", label= "Eastbourne weather station")
plt.plot(v['year'], v['rain'],marker=".", label= "Valley weather staion")
plt.legend()
plt.xticks(c['year'])
plt.grid()
plt.title("Avarage annual rainfall over the last ten years from different areas of England", fontsize = 15)
plt.xlabel("rain over the last 10 years", fontsize = 12)
plt.ylabel("rain in millimeters", fontsize = 14)
plt.savefig('line_plot.png', dpi = 300)
plt.show()
# bar chart reprsenting maximum temperature recorded for each weather station in the year 2022
cardiff_month_conversion = cardiff['month'] = cardiff['month'].apply(lambda x: calendar.month_abbr[x])
x = cardiff.loc[cardiff['year'] == 2022]
berporth_month_conversion = berporth['month'] = berporth['month'].apply(lambda x: calendar.month_abbr[x])
y = berporth.loc[berporth['year'] == 2022]
oxford_month_conversion = oxford['month'] = oxford['month'].apply(lambda x: calendar.month_abbr[x])
z = oxford.loc[oxford['year'] == 2022]
eastbourne_month_conversion = eastbourne['month'] = eastbourne['month'].apply(lambda x: calendar.month_abbr[x])
i = eastbourne.loc[eastbourne['year'] == 2022]
valley_month_conversion = valley['month'] = valley['month'].apply(lambda x: calendar.month_abbr[x])
j = valley.loc[valley['year'] == 2022]
# bar plot
plt.figure(figsize=(17,10),facecolor='aquamarine')
plt.tight_layout()
plt.title("subplot with maximun temperature recorded in the uk for the year 2022 from different weather stations")

plt.subplot(2,2,1)
plt.title("Cardiff weather station")
plt.bar(x.iloc[:,1], x.iloc[:,2],color='red')
plt.yticks(np.arange(0,28, step=1.5, dtype = "float"  ))
plt.grid(axis="y")
plt.xlabel("maximum temperature each month for year 2022")
plt.ylabel('temperature in Celcius')

plt.subplot(2,2,2)
plt.bar(i.iloc[:,1], i.iloc[:,2], color='tab:cyan')
plt.title( "Eastbourne weather station")
plt.yticks(np.arange(0,28, step=1.5, dtype = "float"  ))
plt.grid(axis="y")
plt.xlabel("maximum temperature each month for year 2022")
plt.ylabel('temperature in Celcius')

plt.subplot(2,2,3)
plt.bar(j.iloc[:,1], j.iloc[:,2], color='b')
plt.title("Valley weather station")
plt.yticks(np.arange(0,28, step=1.5, dtype = "float"  ))
plt.grid(axis="y")
plt.xlabel("maximum temperature each month for year 2022")
plt.ylabel('temperature in Celcius')

plt.subplot(2,2,4)
plt.bar(z.iloc[:,1], z.iloc[:,2], color='mediumseagreen')
plt.title("Oxford weather station")
plt.yticks(np.arange(0,28, step=1.5, dtype = "float"  ))
plt.grid(axis="y")
plt.xlabel("maximum temperature each month for year 2022")
plt.ylabel('temperature in Celcius')
plt.savefig('bar_plot', dpi = 300)
plt.show()
# pie plot, rainfall represented for year 2022 from oxford weather station
plt.figure(figsize=(12,8) , facecolor='mediumseagreen')
ts = {"fontsize":18}
plt.pie(z.iloc[:,5], labels=(z.iloc[:,1]),textprops=ts,radius=0.8 ,labeldistance=1.25,pctdistance=1.1, wedgeprops = { 'linewidth' : 5, 'edgecolor' : 'white'}, autopct='%1.1f%%')
plt.axis('equal')
m = plt.ylabel('rainfall percentage for each month of year 2022',labelpad=5)
plt.legend()
plt.savefig('pie_plot', dpi = 300)
plt.show()

print(z)