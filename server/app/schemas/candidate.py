from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

candidate_schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "email": {
            "type": "string",
            "format": "email"
        },
        "major": {
            "type": "string"
        },
        "gpa": {
            "type": "number"
        },
        "english": {
            "type": "number"
        },
        "university": {
            "type": "string"
        },
        "attitude": {
            "type": "number"
        },
        "team_work": {
            "type": "number"
        },
        "communication_skill": {
            "type": "number"
        },
        "experience": {
            "type": "number"
        },
        "salary_range": {
            "type": "object",
            "properties": {
                "min": {
                    "type": "number"
                },
                "max": {
                    "type": "number"
                }
            },
            "required": [
                "min",
                "max"
            ]
        }
    },
    "required": [
        "name",
        "email",
        "major",
        "gpa",
        "english",
        "university",
        "salary_range"
    ],
    "additionalProperties": {"type": "number"}
}


def set_default(data):
    if data.get('gpa'):
        data['gpa'] *= 2.5
    if data.get('english'):
        data['english'] /= 100

    data['attitude'] = data.get('attitude', 0)
    data['team_work'] = data.get('team_work', 0)
    data['communication_skill'] = data.get('communication_skill', 0)
    data['experience'] = data.get('experience', 0)
    return data


def validate_candidate(data):
    try:
        validate(set_default(data), candidate_schema)
    except ValidationError as e:
        return {'ok': False, 'message': e}
    except SchemaError as e:
        return {'ok': False, 'message': e}
    return {'ok': True, 'data': data}
