import json
import os
import socket
from flask import Flask
from db_util import read_data_from_db

app = Flask(__name__)

@app.route('/healthcheck')
def hello():
    return 'OK',200

@app.route('/getallusers')
def get_all_users():
    user_data_result = read_data_from_db('select * from user_data')
    if user_data_result is None:
        return 'Failed to retrieve data',500
    print("User data is fetched from DB")
    all_user_data =  [r._asdict() for r in user_data_result]
    #print(all_user_data)
    return json.dumps(all_user_data,default=str)

@app.route('/getbackendhost')
def get_backend_host():
    return socket.gethostname()

@app.route('/getactiveorpassive')
def get_active_or_passive():
    return os.getenv('HOST_TYPE')

if __name__ == "__main__":
    app.run(debug=True)