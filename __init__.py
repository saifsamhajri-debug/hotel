import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configure app
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///hotel.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Hotel configuration
    app.config['HOTEL_NAME'] = os.getenv('HOTEL_NAME', 'فندق النجوم الذهبية')
    app.config['HOTEL_LOGO'] = os.getenv('HOTEL_LOGO', 'img/logo.png')
    app.config['CURRENCY'] = os.getenv('CURRENCY', 'ريال')

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Configure login
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'الرجاء تسجيل الدخول للوصول إلى هذه الصفحة'
    login_manager.login_message_category = 'info'

    # Register blueprints
    from hotel.routes.main import main_bp
    from hotel.routes.auth import auth_bp
    from hotel.routes.admin import admin_bp
    from hotel.routes.room import room_bp
    from hotel.routes.booking import booking_bp
    from hotel.routes.customer import customer_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(room_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(customer_bp)

    # Add context processor for templates
    @app.context_processor
    def inject_now():
        return {
            'now': datetime.now(),
            'hotel_name': app.config['HOTEL_NAME'],
            'hotel_logo': app.config['HOTEL_LOGO'],
            'currency': app.config['CURRENCY']
        }

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
