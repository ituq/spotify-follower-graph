from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from build_graph_headless import build_graph
import re
app = Flask(__name__)

@app.route('/')
def home():
    # Render the home page
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    url = request.form['url']
    depth = request.form['depth']
    # Instead of returning JSON, redirect to the 'result' route with query parameters
    return redirect(url_for('result', url=url, depth=depth))

@app.route('/result')
def result():
    # Retrieve query parameters
    url = request.args.get('url')
    depth = request.args.get('depth')
    id_match=re.search(r"https://open.spotify.com/user/([a-zA-Z0-9]+)",url)
    id=id_match if id_match else "no found"
    # Render 'result.html' template with the data
    build_graph(depth,id)
    return redirect(url_for('custom_static', filename=f'{id}.html'))
@app.route('/graphs/<path:filename>')
def custom_static(filename):
    return send_from_directory('static/graphs', filename)
if __name__ == '__main__':
    app.run(debug=True)
