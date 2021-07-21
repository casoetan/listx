from flask import Flask, request, jsonify
from listx.service import ListxService
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/api/listx")
    def index():
        path = request.args.get('path')
        if not path:
            return "No path provided"
        service = ListxService(path)
        path_items = service.get_path_items()
        return jsonify(list(path_items))

    return app
