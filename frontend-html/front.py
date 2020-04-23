from flask import Flask, request, jsonify,render_template,redirect, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
here=""
@app.route('/')
def form():
    return render_template('form.html')

@app.route("/addrec", methods=['GET','POST'])
def addrec():
	if request.method == 'POST':
		Id = request.form['Id']
		nm = request.form['nm']
		nm1 = request.form['nm1']
		print(request.form)
		here=request.form
		print(type(here))
		print(dict(here))
		requests.post('http://172.22.0.3:5000/test',json=dict(here))
		print("id=",Id)
		print('nm=',nm)
		print('nm1=',nm1)
	print("nothing/n")
	return jsonify(here),200

if __name__ == "__main__":
    app.run(debug= True,port=5001,host="0.0.0.0")
