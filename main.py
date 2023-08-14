from taipy.gui import Gui, notify

import pandas as pd

text = "Original text"
col1 = "first col"
col2 = "second col"
col3 = "third col"

ballon_img = "./img/Ballon_15_20.png"

section_1 = """
<h1 align="center">Getting started with Taipy GUI</h1>

<|layout|columns=1 2 2|
<|
My text: <|{text}|>
<|{text}|input|>
|>

<|
<center>
<|Press Me|button|on_action=on_button_action|>  
**Ein Button:** <|{col1}|>
</center>
|>

<|
<center>
<|{ballon_img}|image|height=30%|width=30%|label=This is one ballon|>
</center>
|>

|>
"""

section_2 = '''

##Darstellung Gas-Verbrauch
<|{dataset}|chart|mode=line|x=Datum|y[1]=Verbrauch|y[2]=Betriebsstunden|yaxis[2]=y2|layout={layout}|color[1]=green|color[2]=blue|>

'''
layout = {
    "xaxis": {
        # Force the title of the x axis
        "title": "Time-Range"
    },
    "yaxis": {
        # Force the title of the first y axis
        "title": "Verbrauch",
        # Place the first axis on the left
        "side": "left"
    },
    "yaxis2": {
        # Second axis overlays with the first y axis
        "overlaying": "y",
        # Place the second axis on the right
        "side": "right",
        # and give it a title
        "title": "Betriebsstunden"
    },
    "legend": {
        # Place the legend above chart
        "yanchor": "middle"
    }
}

def on_button_action(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return
    
def get_data(path: str):
    dataset = pd.read_csv(path)
    dataset["Datum"] = pd.to_datetime(dataset["Datum"], dayfirst=True).dt.date
    return dataset

gui = Gui(page=section_1 + section_2)
dataset = get_data("./dataset.csv")

if __name__ == '__main__':
    # Execute by the _Python_ interpretor, for debug only.
    Gui.run(gui, title="Taipy Demo", use_reloader=True, dark_mode=True, port=5001, flask_log=False)
else:
    # Execute by _Gunicorn_, for production environment.
    app = Gui.run(gui, title="Taipy Demo", run_server=False)
