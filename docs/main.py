import os
import sys
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)

# Database setup
from frontend_app.database import db
db.init_app(app)

# Import routes
from frontend_app.routes import main_routes
app.register_blueprint(main_routes)

# Run the application
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        app.run(debug=True)
    else:
        app.run(debug=False)