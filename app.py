from flask import Flask, request, jsonify, url_for, render_template, send_from_directory, abort
from build_graph_headless import build_graph
import re,os
app = Flask(__name__)

@app.route('/')
def home():
    # Render the home page
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    url = request.form['url']
    depth = request.form['depth']
    return jsonify({'redirectURL':url_for('result', url=url, depth=depth)})

@app.route('/result')
@app.route('/result')
def result():
    # Retrieve query parameters
    url = request.args.get('url')
    depth = request.args.get('depth')
    id_match = re.search(r"open.spotify.com/user/([^?]+)\?si=", url)
    id = id_match.group(1) if id_match else "no_found"  # Adjusted default case
    build_graph(int(depth), id)  # Assuming sync execution
    # Ensure the file exists
    filepath = os.path.join(app.root_path, 'static/graphs', f'{id}.html')
    if os.path.exists(filepath):
        return send_from_directory('static/graphs', f'{id}.html')
    else:
        return abort(404)
@app.route('/graphs/<path:filename>')
def custom_static(filename):
    filepath = os.path.join(app.root_path, 'static/graphs', filename)
    if os.path.exists(filepath):
        return send_from_directory('static/graphs', filename)
    else:
        # Log error or notify as necessary
        return abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=23232)
