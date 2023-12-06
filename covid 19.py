import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv', parse_dates=['Date'])
df['Total Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)

# Worldwide cases
worldwide_df = df.groupby(['Date']).sum()
w = worldwide_df.plot(figsize=(16, 10))
w.set_xlabel('Date')
w.set_ylabel('# of cases worldwide')
w.title.set_text('Worldwide Covid-19 Insight')
plt.show()

# India total cases
ind_df = df[df['Country'] == 'India'].groupby(['Date']).sum()

# Plotting Worldwide vs India Total Cases
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(worldwide_df['Total Cases'], label='Worldwide')
ax.plot(ind_df['Total Cases'], label='India')
ax.set_xlabel('Date')
ax.set_ylabel('# of Total cases')
ax.set_title('Worldwide vs India Covid-19 Insight')
plt.legend(loc='upper left')

# India daily Cases and Deaths
ind_df['Daily Confirmed'] = ind_df['Confirmed'].sub(ind_df['Confirmed'].shift())
ind_df['Daily Deaths'] = ind_df['Deaths'].sub(ind_df['Deaths'].shift())

# Plotting India Daily Cases and Deaths
fig, ax = plt.subplots(figsize=(20, 8))
ax.bar(ind_df.index, ind_df['Daily Confirmed'], color='b', label='India Daily Confirmed Cases')
ax.bar(ind_df.index, ind_df['Daily Deaths'], color='r', label='India Daily Deaths')
ax.set_xlabel('Date')
ax.set_ylabel('# of People affected')
ax.set_title('India Daily Cases and Deaths')
plt.legend(loc='upper left')
plt.show()

from datetime import date, timedelta 
yesterday = date.today() - timedelta(days=1)
yesterday.strftime('%Y-%m-%d')
today_df= df[df['Date'] == yesterday]
top_10 = today_df.sort_values(['Confirmed'],ascending = False)[:10]
top_10.head()
