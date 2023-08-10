import logging
from pythonjsonlogger import jsonlogger
#import time

logPath = '/home/brian/python-scripts/logs/'

logging.basicConfig(format='%(asctime)s',filename=logPath + "linktapLog.log", level=logging.DEBUG, filemode='w')

eventsLogger = logging.getLogger('eventsLogger')
formatter = jsonlogger.JsonFormatter()
fileHandler = logging.FileHandler(logPath + "linktapEvents.log",mode='w')
fileHandler.setFormatter(formatter)
eventsLogger.addHandler(fileHandler)

from flask import Flask, request

app = Flask(__name__)

@app.route('/linktapEvent', methods=['POST'])
def linktapEvent():

    if request.method == 'POST':
        print("Data received from webhook is: ", request.json)
        eventsLogger.debug(request.json)
        return "Webhook received!"
@app.route('/status', methods=['GET'])
def status():

    if request.method == 'GET':
        return "Listener is up"

app.run(host='0.0.0.0', port=7001)
