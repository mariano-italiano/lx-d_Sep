from flask import Flask, request
from flask_restx import Api, Resource, fields
import socket

app = Flask(__name__)
api = Api(app, version='1.0', title='Python-Api Swagger',
          description='A simple API for Python-Api demo application\nAuthor: Marcin Kujawski', doc='/api', prefix='/api')

# Define a namespaces
record = api.namespace('record', description='Record operations')
counter = api.namespace('counter', description='Manage Counter')

# Define a models
record_model = api.model('Records', {
    'id': fields.Integer(readOnly=True, description='The record unique identifier'),
    'name': fields.String(required=True, description='The record name'),
    'description': fields.String(required=True, description='The record description')
})

counter_model = api.model('Counter', {
   'counter': fields.Integer(readOnly=True, description='The counter value')
})


# Define data for records array
RECORDS = [
    {'id': 1, 'name': 'record1', 'description': 'This is example record'},
]

# Define counter
COUNTER = 0

# Counter API
@counter.route('/api/info')
class Counter(Resource):
    @counter.marshal_list_with(counter_model)
    def get(self):
        '''Get the current value of the counter'''
        return {"counter": COUNTER}
    @counter.expect(counter_model)
    @counter.marshal_with(counter_model, code=201)
    def post(self):
        '''Increase the value of the counter by 1'''
        global counter
        COUNTER += 1
        return {"counter": COUNTER}, 201

# Record API
@record.route('/api/records')
class RecordList(Resource):
    '''Shows a list of all records, and lets you POST to add new records'''

    @record.marshal_list_with(record_model)
    def get(self):
        '''List all records'''
        return RECORDS

    @record.expect(record_model)
    @record.marshal_with(record_model, code=201)
    def post(self):
        '''Create a new record'''
        record = {
            'id': RECORDS[-1]['id'] + 1,
            'name': request.json['name'],
            'description': request.json['description']
        }
        RECORDS.append(record)
        return record, 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
