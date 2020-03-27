import os
from flask_migrate import MigrateCommand
from flask_script import Manager


from App import create_app

app = create_app()
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

manager = Manager(app)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()
