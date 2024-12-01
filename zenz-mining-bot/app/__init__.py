# app/__init__.py  
from flask import Flask  

def create_app():  
    app = Flask(__name__)  
    app.config.from_object('app.config')  

    # Importing the bot functionality  
    from .bot import main as bot_main  
    bot_main.start()  # Start the bot in a separate thread or process  

    # Importing routes  
    from .web_app import main as web_app_main  
    app.register_blueprint(web_app_main)  

    return app

# app/__init__.py  
from flask import Flask  
from .bot import start_bot  # Ensure you import your bot startup logic  

def create_app():  
    app = Flask(__name__)  

    # Load configurations  
    app.config.from_object('app.config')  

    # Register blueprints or routes if you have any  
    # from .web_app import main as web_app_blueprint  
    # app.register_blueprint(web_app_blueprint)  

    return app  

if __name__ == '__main__':  
    app = create_app()  
    app.run(debug=True)  
    start_bot()