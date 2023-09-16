from typing import Type
from dataclasses import dataclass, fields

from flask_fixture.errors import NotExpectedConfigFieldError
from flask_fixture.state_storage.collection_of_configs import configs


def config(Class: Type) -> Type:
    Class = dataclass(Class)

    class_fields = {field.name: field.default for field in fields(Class)}

    for field_name, field_value in class_fields.items():
        if field_name not in configs:
            available_fields = ', '.join([f'"{x}"' for x in configs])
            raise NotExpectedConfigFieldError(f'Option "{field_name}" is not provided. Available options: {available_fields}.')
        configs[field_name] = field_value

    return Class
