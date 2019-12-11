from flask import request, jsonify
from app import app, mongo
from app.schemas import validate_candidate
from bson import json_util, ObjectId
import json


@app.route('/candidate', methods=['GET', 'POST', 'PUT'])
def candidate_list():
    if request.method == 'GET':
        query = request.args
        result = mongo.db.htgqd.find(query)
        return_data = [person for person in result]
        return json.dumps(return_data, default=json_util.default), 200

    data = json.loads(request.data, encoding='utf-8')
    if request.method == 'POST':
        validated = validate_candidate(data)
        if validated['ok']:
            mongo.db.htgqd.insert_one(data)
            return jsonify({'code': '00', 'message': 'Candidate created successfully'})
        return jsonify({'code': '99', 'message': 'Error'})


@app.route('/candidate/<candidate_id>', methods=['GET', 'PUT'])
def candidate(candidate_id):
    if request.method == 'GET':
        query = request.args
        result = mongo.db.htgqd.find_one(query)
        return json.dumps(result, default=json_util.default), 200

    data = json.loads(request.data, encoding='utf-8')
    if request.method == 'PUT':
        mongo.db.htgqd.find_one_and_update({'_id': ObjectId(oid=str(candidate_id))}, {
            '$set': {
                'attitude': data['attitude'],
                'team_work': data['team_work'],
                'communication_skill': data['communication_skill'],
                'experience': data['experience']
            }
        })
        return jsonify({'code': '00', 'message': 'Candidate updated successfully'})
