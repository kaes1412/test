from flask import Flask, render_template
import MySQLdb
import time
import json

app = Flask(__name__)

@app.route("/")
def main():
	return render_template ('index.html')

@app.route("/showData")
def showData():
	start = time.time()
	response = {}

	db = MySQLdb.connect("localhost","root","root","TestDB")	
	cursor = db.cursor()

	sql = "SELECT * FROM News "

	cursor.execute(sql)
	result =  cursor.fetchall()

	datas = []
	for row in result:
			Judul = row [0]
			Isi= row [1]
			Penulis= row [2]

			datas.append(result)
	# return "datas"
	end = time.time()
	response['status'] ='success'
	response['data'] = datas
	response['elapsedtime'] =end - start

	return json.dumps(response)

@app.route("/insertData")
def insertData():
	return render_template ('insert.html')

@app.route("/submit")
def submit(data):
	start = time.time()
	Judul = data.get("Judul")
	Isi = data.get("Isi")
	Penulis = data.get("Penulis")
	response = {}

	db = MySQLdb.connect("localhost","root","root","TestDB")	
	cursor = db.cursor()

	sql = "INSERT INTO News(Judul, isi, penulis) VALUES ('"+Judul+"','"+Isi+"', '"+Penulis+"')"

	try:
		cursor.execute(sql)
		result =  cursor.fetchall()
		db.commit()
	except:

	   db.rollback()

	# disconnect from server
	db.close()
	response['status'] ='success'
	response['description'] = 'data inserted'
	response['elapsedtime'] =end - start

	return json.dumps(response)



if __name__ == "__main__":
	app.run(host='0.0.0.0')
