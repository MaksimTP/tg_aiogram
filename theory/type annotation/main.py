from typing import List,Dict,Any

# Аннотация переменных

name: str = 'Tommy'
age: int = 24
height_in_meters: float = 1.7
colleagues: List[str] = ['Alicia', 'John']


# Аннотация функций

def conv_c_to_f(celcius_temp: float) -> float:
    return (celcius_temp * 1.8) + 32


def ppprint(text: str) -> None:
    print(text)

# Специальные типы

# Any

result: Any = 'SUCCESS'

result = 10

state: str = 'PENDING'

state = result