from flask import Flask
from flask import Response, render_template
from flask import request
import json
from ASpeakGrammar import checkGrammar

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        title='Home Page'
    )

@app.route('/check-grammar', methods=['GET', 'POST'])
def upload():
    try:
        strLine = request.json['inputText']
        jObj = checkGrammar(strLine)

    except Exception as e:
        print (e)

    return Response(json.dumps(jObj), mimetype='application/json')


@app.route('/test', methods=['GET', 'POST'])
def res_massage():
    return "Hello User!"


if __name__ == '__main__':
    app.run(port=5000, debug=True)
