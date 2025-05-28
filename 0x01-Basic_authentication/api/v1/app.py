from flask import Flask, jsonify
from api.v1.views import app_views
from flask import abort

app = Flask(__name__)
app.register_blueprint(app_views)

# Add this new error handler
@app.errorhandler(401)
def unauthorized_error(error):
    """Handler for 401 Unauthorized"""
    return jsonify({"error": "Unauthorized"}), 401
