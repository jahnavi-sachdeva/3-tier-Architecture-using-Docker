from flask import Flask, request, jsonify,render_template,redirect, url_for
import requests
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']='172.22.0.2'
app.config['MYSQL_USER']='root'
app.config["MYSQL_PASSWORD"]=''
app.config["MYSQL_DB"]='flaskapp'

mysql=MySQL(app)
CORS(app)


@app.route("/test",methods=['GET','POST'])
def test():
	cur=mysql.connection.cursor()
	data=request.get_json()
	print("JSON:")
	print(data)
	Id=data['Id']
	nm=data['nm']
	email=data['nm1']
	print(Id,nm,email)
	query="INSERT INTO users VALUES({},'{}','{}')".format(Id,nm,email)
	print(query)
	cur.execute(query)
	cur.execute("SELECT * FROM users")
	fetchdata=cur.fetchall()
	print(fetchdata)
	mysql.connection.commit()
	cur.close()
	return data
if __name__ == "__main__":
    app.run(debug= True,port=5000,host='0.0.0.0')
