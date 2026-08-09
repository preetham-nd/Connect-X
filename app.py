from flask import Flask

from config import Config
from extensions import db


def create_app(config_class=Config):

    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )
    app.config.from_object(config_class)

    db.init_app(app)


    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.admin import admin_bp
    from routes.profile import profile_bp
    from routes.posts import posts_bp
    from routes.likes import likes_bp
    from routes.comments import comments_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(likes_bp)
    app.register_blueprint(comments_bp)


    @app.context_processor
    def inject_current_user():
        from flask import session
        from models.user import User
        user_id = session.get("user_id")
        current_user = db.session.get(User, user_id) if user_id else None
        return {"current_user": current_user}

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=app.config.get("DEBUG", False), port=5001)
