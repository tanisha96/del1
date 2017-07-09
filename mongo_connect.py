from flask import Flask
from flask_pymongo import PyMongo
#from flask import jsonify
#from flask import request

#from paris's video
'''
from pymongo import MongoClient

mongodb_host = 'localhost'
mongodb_port = '27017'

client = MongoClient(mongodb_host + ':' + mongodb_port)
db = client['mongo-test']
print (db)
'''	
#end of paris's video

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'sales101'
app.config['MONGO_URI'] = 'mongodb://tan:shouting123@ds139072.mlab.com:39072/sales101'

#app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'
mongo = PyMongo(app)

@app.route('/add')
def add():
	#with app.app_context():
	s = mongo.db.salesdb
	s.insert({'timestamp':'100010001000',
		'pid': '10001000',
		'sid': '1001',
		'city': 'Mumbai',
		'state': 'Maharashtra',
		'qty': '1',
		'price': '40'})
	s.insert({'timestamp':'100010001021',
		'pid': '10001001',
		'sid': '1012',
		'city': 'Pune',
		'state': 'Maharashtra',
		'qty': '1',
		'price': '50'})
	return 'Added item!'

print('hey there! ')
@app.route('/findstuff')
def findstuff():
	with app.app_context():
		s = mongo.db.salesdb
		print('hey')
		#item = s.find_one({'city':'Mumbai'})
		#item = s.find_one(entity1['city'] : value['value'])
		item = s.find_one( { 'qty': '2' } )
		price = float(item['qty']) * float(item['price'])
		print(price)
	return 'The required item is: ' + item['pid'] + ', shopID= ' + item['sid'] + 'and the total sales are: {}' .format(price)

@app.route('/update')
def update():
	with app.app_context():
		s = mongo.db.salesdb
		state = s.find_one({'city':'Mumbai'})
		#return 'The required item is: ' + item['pid'] + ', shopID= ' + item['sid']
		state['city'] = 'Nagpur'
		s.save(state)
	return 'update succeed!'


print('comprehending answer function: ')
ans = findstuff()
print('ans' + ans)


if __name__ == '__main__':
	app.run(debug=True)


