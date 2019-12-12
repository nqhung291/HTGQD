from flask import request, jsonify
from app import app, mongo
from app.schemas import validate_candidate
from bson import json_util, ObjectId
import json


@app.route('/candidate', methods=['GET', 'POST', 'PUT'])
def candidate_list():
    if request.method == 'GET':
        query = request.args
        query_db = remove_empty_query(query)
        if query_db:
            query_str = dict()
            if query_db.get('name'):
                query_str['name'] = {'$regex': str(query_db.get('name')), '$options': 'i'}
            if query_db.get('gpa'):
                query_str['gpa'] = {'$gte': float(query_db.get('gpa'))}
            if query_db.get('english'):
                query_str['english'] = {'$gte': float(query_db.get('english'))}
            if query_db.get('major'):
                query_str['major'] = {'$regex': str(query_db.get('major')), '$options': 'i'}
            if query_db.get('university'):
                query_str['university'] = {'$regex': str(query_db.get('university')), '$options': 'i'}
            if query_db.get('salary'):
                query_str['salary'] = {'$lte': float(query_db.get('salary'))}
            if query_db.get('is_rated'):
                query_str['is_rated'] = bool(int(query_db.get('is_rated')))

            # page_size = query.get('page_size', 10)
            # page = query.get('page') - 1
            result = mongo.db.htgqd.find(query_str)
            # total = result.cout()
        else:
            result = mongo.db.htgqd.find({})
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
        try:
            mongo.db.htgqd.find_one_and_update({'_id': ObjectId(oid=str(candidate_id))}, {
                '$set': {
                    'attitude': data['attitude'],
                    'team_work': data['team_work'],
                    'communication_skill': data['communication_skill'],
                    'experience': data['experience'],
                    'is_rated': True
                }
            })
            return jsonify({'code': '00', 'message': 'Candidate updated successfully'})
        except Exception as e:
            print(e)
            return jsonify({'code': '99', 'message': 'Error'})


@app.route("/university", methods=['GET', 'POST'])
def univesityList():
    if request.method == 'GET':
        db_result = mongo.db.university.find({})
        data = [university for university in db_result]
        return json.dumps(data, default=json_util.default), 200
    if request.method == 'POST':
        data = json.loads(request.data, encoding='utf-8')
        print(data)
        mongo.db.university.insert_many(data['university'])
        return jsonify({'code': '00', 'message': 'University added successfully'})


def remove_empty_query(query):
    query_db = {}
    for k, v in query.items():
        if v:
            query_db[k] = v
    return query_db
