from fastjsonschema import compile as compile_schema

from src.ingredient import Ingredient

validate = compile_schema({
    'type': 'object',
    'required': ['ingredientes'],
    'properties': {
        'ingredientes': {
            'type': 'array',
            'minItems': 1,
            'items': [
                {
                    'type': 'string',
                    'enum': Ingredient.get_all_ingredients_names_list()
                }
            ]
        }
    }
})


def validate_payload(payload):
    """ @throws JsonSchemaException """
    validate(payload)
