import re
from typing import Tuple


def compose_message(message: bytes) -> bytes:
    return b'start' + message + b'stop'


def decompose_message(message: bytes) -> list[bytes]:
    pattern = b'start' + b'(.*?)' + b'stop'
    pat = re.compile(pattern)
    return pat.findall(message)


def get_first_byte_from_list(byte_list: list[bytes]) -> bytes:
    return byte_list[0]


def get_first_key_from_dict(test_dict: dict[str, int]) -> str:
    for key in test_dict.keys():
        return key


def get_first_value_from_dict(test_dict: dict[str, int]) -> int:
    for value in test_dict.values():
        return value


def sets_and_tuples(test_set: set[float]) -> Tuple[float, int]:
    assert type(test_set) == set
    return tuple([1.2, 3])


def is_a_good_string(greeting: str) -> bool:
    return 'Good Morning' in greeting
