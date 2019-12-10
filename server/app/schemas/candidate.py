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
        "teamWork": {
            "type": "number"
        },
        "communicationSkill": {
            "type": "number"
        },
        "experience": {
            "type": "number"
        },
        "salaryRange": {
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
        "attitude",
        "teamWork",
        "communicationSkill",
        "experience",
        "salaryRange"
    ]
}


def validate_candidate(data):
    try:
        validate(data, candidate_schema)
    except ValidationError as e:
        return {'ok': False, 'message': e}
    except SchemaError as e:
        return {'ok': False, 'message': e}
    return {'ok': True, 'data': data}
