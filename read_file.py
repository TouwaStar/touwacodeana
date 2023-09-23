import importlib
import string
from types import FunctionType, ModuleType
from typing import Any, Dict, Generic, Iterable, get_origin, get_args
from random import choice, randint, seed, randbytes, uniform
seed()


checked_module: ModuleType = importlib.import_module("tests.test_files.test_functions_positive")


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(choice(letters) for i in range(length))
    return result_str


def is_matching_type(value_one, value_two) -> bool:
    try:
        result = isinstance(value_one, value_two)
    except:
        result = isinstance(value_one, get_origin(value_two))

    if not result:
        raise TypeError(f"Types dont match! {value_one} vs {value_two}")
    return True


def return_random_value(of_type: Any):
    if of_type == bytes:
        return randbytes(randint(0, 255))
    if of_type == str:
        return get_random_string(randint(0, 255))
    if of_type == int:
        return randint(0, 255)
    if of_type == float:
        return uniform(0, 255.0)


for name, item in checked_module.__dict__.items():
    if type(item) == FunctionType:
        kwargs: dict[str, Any] = {}
        retval = None
        for arg_name, arg_type in item.__annotations__.items():
            if arg_name == 'return':
                retval = arg_type
                continue
            if isinstance(arg_type, Iterable):
                container = arg_type()
                for i in range(0, randint(0, 255)):
                    if isinstance(container, dict):
                        container[return_random_value(get_args(arg_type)[0])] = return_random_value(get_args(arg_type)[1])
                    elif isinstance(container, set):
                        container.add(return_random_value(get_args(arg_type)[0]))
                    else:
                        container.append(return_random_value(get_args(arg_type)[0]))
                kwargs[arg_name] = container
            else:
                kwargs[arg_name] = return_random_value(arg_type)

        result = item(**kwargs)
        print(is_matching_type(result, retval))
