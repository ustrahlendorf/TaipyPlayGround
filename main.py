import taipy as tp

gui = tp.Gui(page="# Getting started with *Taipy*")

if __name__ == '__main__':
    # Execute by the _Python_ interpretor, for debug only.
    tp.run(gui, title="Taipy Demo")
else:
    # Execute by _Gunicorn_, for production environment.
    app = tp.run(gui, title="Taipy Demo", run_server=False)
