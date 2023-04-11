from flask import Flask, request, render_template
import requests
import json



app = Flask(__name__, template_folder='Templates')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        val = str(request.args.get('text'))
        data = json.dumps({"sender": "Rasa", "message": val})
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        res = requests.post('http://localhost:5005/webhooks/rest/webhook', data=data, headers=headers)
        res = res.json()
        val = res[0]['text']
    return render_template('index.html', val=val)


@app.route('/result', methods=['POST', 'GET'])
def res_json():
    if request.method == "POST":
        text = request.form.get('query')
        payload = {"sender": "Rasa", "text": text}
        headers = {'content-type': 'application/json'}
        response = requests.post('http://localhost:5005/model/parse', json=payload, headers=headers)
        result = response.json()
        return result


if __name__ == '__main__':
    app.run(debug=True)
