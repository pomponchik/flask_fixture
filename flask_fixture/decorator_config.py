import inspect
from typing import Type
from dataclasses import dataclass, fields

from flask_fixture.errors import NotExpectedConfigFieldError
from flask_fixture.collection_of_importing_modules import modules
from flask_fixture.collection_of_configs import configs



def config(Class: Type) -> Type:
    Class = dataclass(Class)
    modules.add(inspect.getmodule(Class).__name__)

    fields_of_reference = {field.name: (field.default, field.default_factory) for field in fields(ReferenceConfig)}
    fields_of_new_class = {field.name: (field.default, field.default_factory) for field in fields(Class)}

    data = {}

    for field_name, field_value in fields_of_new_class.items():
        if field_name not in fields_of_reference:
            available_fields = ', '.join([f'"{x}"' for x in fields_of_reference])
            raise NotExpectedConfigFieldError(f'Option "{field_name}" is not provided. Available options: {available_fields}.')
        value = field_value[0] or field_value[1]() if field_value[1] else None
        data[field_name] = value

    configs.update(data)
    
    return Class


@config
class ReferenceConfig:
    template_folder: str = 'templates'
