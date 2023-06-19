import taipy as tp

text = "Original text"

page = """
# Getting started with Taipy GUI

My text: <|{text}|>

<|{text}|input|>
<br/>

<|Run local|button|on_action=on_button_action|>
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
    tp.run(gui, title="Taipy Demo", use_reloader=True)
else:
    # Execute by _Gunicorn_, for production environment.
    app = tp.run(gui, title="Taipy Demo", run_server=False)
