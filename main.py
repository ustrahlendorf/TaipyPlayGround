import taipy as tp

text = "Original text"
col1 = "first col"
col2 = "second col"
col3 = "third col"

page = """
<h1 align="center">Getting started with Taipy GUI</h1>

My text: <|{text}|>

<|{text}|input|>
<br/>

<center>
<|Press Me|button|on_action=on_button_action|>
</center>


<|layout|gap=50px|columns=1fr 2fr 1fr|
<|{text}|>
<|{col2}|>
<|{col3}|>
|>

<center>
![Mein Ballon](./img/Ballon_15_20.png)
</center>

"""

def on_button_action(state):
    tp.gui.notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return

gui = tp.Gui(page)

if __name__ == '__main__':
    # Execute by the _Python_ interpretor, for debug only.
    tp.run(gui, title="Taipy Demo", use_reloader=True, dark_mode=True, port=5001, flask_log=True)
else:
    # Execute by _Gunicorn_, for production environment.
    app = tp.run(gui, title="Taipy Demo", run_server=False)
