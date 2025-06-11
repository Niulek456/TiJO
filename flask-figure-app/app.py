from flask import Flask, render_template, request, jsonify
from services import FigureService

app = Flask(__name__)
service = FigureService()

@app.route('/')
def index():
    return render_template('index.html', figure_colors=service.get_all_colors())

@app.route('/change-color', methods=['POST'])
def change_color():
    data = request.get_json()
    if service.set_color(data.get('figure_type'), data.get('new_color')):
        return jsonify({"status": "success", "figure_colors": service.get_all_colors()})
    return jsonify({"status": "error", "message": "invalid figure type"}), 400

@app.route('/change-color-all', methods=['POST'])
def change_color_all():
    data = request.get_json()
    service.set_color_all(data.get('new_color'))
    return jsonify({"status": "success", "figure_colors": service.get_all_colors()})
