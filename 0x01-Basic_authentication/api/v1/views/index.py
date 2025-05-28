from flask import jsonify
from api.v1.views import app_views
from flask import abort

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized():
    """Endpoint to test 401 error handler"""
    abort(401)
