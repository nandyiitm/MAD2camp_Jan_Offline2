from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'daklsfkdlasfkldlakdsl'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

from models import db, User
db.init_app(app)

from routes import api
api.init_app(app)

if __name__ == '__main__':

    with app.app_context():

        db.create_all()

        is_admin_exists = User.query.filter_by(role='admin').first() is not None

        if not is_admin_exists:
            admin_user = User(username='admin', email='admin@gmail.com', password='1234', role='admin')
            db.session.add(admin_user)
            db.session.commit()
            print('Admin user created with email: admin@gmail.com and password: 1234')
        else:
            print('Admin user already exists with email: admin@gmail.com and password: 1234')

    app.run(debug=True)