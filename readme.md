# How to build Web using mvc with python writen by Songjiang Zhang
## Build development environment
    1 create root folder FlaskWeb
    2 cd Flaskweb then python -m venv env : [env is your develop environment include packages]
    3 activate env : [run env\scripts\activate]
    4 install any required packages like Flask, Bootstrap, WTForm etc.
## Project structure Tree
    FlaskWeb 
            --env
            --app : [every app have it's fold structure include model,view,and page]
                --auth : [auth app root] 
                --main : [Website app root]
                    --__init__.py : [init Blueprint for main package]
                    --forms.py : [Webpage form declare]
                    --views.py : [include route ]
                    --erros.py
                --static
                --templates : [all the page of App in this fold because using templates]
                --__init__.py : [
                            **init required object **
                            bootsrap = Bootstrap()
                            moment = Moment()
                            db = SQLAlchemy()
                            login_manager = LoginManager()
                            login_manager.login_view = 'userverify.login'
            
                            **construct object**
                            def app_create(config_name):
                                app = Flask(__name__)
                                app.config.from_object(config[config_name])
                                config[config_name].init_app(app)
                            
                                bootsrap.init_app(app)
                                moment.init_app(app)
                                db.init_app(app)
                                login_manager.init_app(app)
                                
                                from .main import blue 
                                app.register_blueprint(blue)
                                from .auth import userverify
                                app.register_blueprint(userverify,url_prefix='/auth')
                                ]
                --models.py
            --migritions
            --tests
            --__init__.py ：init function，and represent a package
            --manage.py : program main() entry,because using . and .. relative reference,
                            main() function just reside in the top level of Flaskweb. 
            --test.py : test main() like manage.py
            --requirement.txt
            --readme.md
## DB create -- manage.py

    python manage.py shell
    from manage import db
    db.create_all()

## DB init -- manage.py

    python manage.py shell
    from manage import db,User
    u = User()
    u.email ='songjiangzhang@hotmail.com'
    u.username = 'zsj'
    u.password = '1234'
    db.session.add(u)
    db.session.commit()

## Run App
    python manage.py runserver
## Tips
* all main() point of app exit in the top level of flaskweb,for example test.py is testcase main entry, tests fold include many testcases. manage.py is app main entry.



### Privacy Statement
The [Microsoft Enterprise and Developer Privacy Statement]() describes the privacy statement of this software.
### License
MIT © songjiangzhang@hotmail.com