import os
from app import app_create, db
from app.models import Role, User
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = app_create('default')

manager = Manager(app)

migrate = Migrate(app, db)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)



if __name__ == '__main__':
    manager.run()
