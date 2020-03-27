# 使用dash进行股票可视化交互
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc 
import dash_html_components as html
from datetime import datetime as dt 
from pandas_datareader.data import DataReader
import tushare as ts

# 创建一个应用
app = dash.Dash()
# 设置layout
app.layout = html.Div([
    html.H1('k线图'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': '探路者', 'value':'300005'},
            {'label': '莱美药业', 'value':'300006'},
            {'label': '汉威科技', 'value':'300007'},
            {'label': '天海防务', 'value':'300008'},
            {'label': '安科生物', 'value':'300009'},
        ],
        value='300005'
    ),
    dcc.Graph(id='my-graph')
])

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = ts.get_k_data(selected_dropdown_value, ktype='30')
    return {
        'data':[
            {
            'x': df.index,
            'y':df.close
            }
        ]
    }

if __name__ == '__main__':
    app.run_server(host="0.0.0.0")