from app import create_app, db
from flask_script import Manager, Server
from app.models import Pitch, Review
from flask_migrate import Migrate, MigrateCommand


app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    '''
    run unit tests
    :return:
    '''

    import unittest

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db, Pitch = Pitch, Review = Review )


if __name__ == '__main__':
    manager.run()