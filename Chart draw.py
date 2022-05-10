import pandas as pd
import plotly.graph_objects as go
from plotly.offline import iplot
from plotly.subplots import make_subplots

df = pd.read_csv('Prices.csv')

df['date'] = pd.to_datetime(df['date'])

fig = make_subplots(rows=2,cols=1,shared_xaxes=True,subplot_titles=('Bitcoin Ptice (USD)'))
# Candle Sticks
fig.add_trace(go.Candlestick(x=df['date'],
                             open=df['open'],
                             close=df['close'],
                             high=df['high'],
                             low=df['low'],
                             name='CandleStick'),
              row=1,col=1)

# Middle Bound
fig.add_trace(go.Scatter(x=df['date'],
                         y=df['bb_bbm'],
                         line_color='orange',
                         name='Middle Bound'),
              row=1,col=1)

# Upper Bound
fig.add_trace(go.Scatter(x = df['date'],
                         y = df['bb_bbh'],
                         line_color = 'indigo',
                         line = {'dash': 'dash'},
                         name = 'Upper Bound',
                         opacity = 0.5),
              row = 1, col = 1)

# Lower Bound
fig.add_trace(go.Scatter(x = df['date'],
                         y = df['bb_bbl'],
                         line_color = 'indigo',
                         line = {'dash': 'dash'},
                         fill = 'tonexty',
                         name = 'Lower bound',
                         opacity = 0.5),
              row = 1, col = 1)

# Volume Plot
fig.add_trace(go.Bar(x = df['date'], y = df['volume'], showlegend=False), 
              row = 2, col = 1)

fig.update_layout(template='plotly_dark')
fig.update_yaxes(type='log')
fig.update(layout_xaxis_rangeslider_visible=False)

fig.show()
