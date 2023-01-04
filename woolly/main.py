from typing import List

class FooBar():
    """Class Variables"""
    x: str = 'x'
    y: int = 1
    z: float = 1.0

    def __init__(self, a, b, c) -> None:
        """Instance Variables"""
        self.a = a
        self.b = b
        self.c = c


def analyzeClass(object: any) -> List:
    """Get the attributes and attribute types of a class

    Args:
        _class (any): A class to analyze

    Returns:
        List[any]: A list of attributes and their types {name:type}
    """
    class_variables = [attribute for attribute in dir(object)
                        if not attribute.startswith('__')
                        and not callable(getattr(object, attribute))]

    class_types = [type(getattr(object, name)).__name__ for name in dir(object)
                        if not name.startswith('__')]

    return list(map(list, zip(class_variables, class_types)))

def fuzzer(_type: any) -> any:
    """Return a random value based on type
    """
    match _type:
        case int():
            return 1
        case float():
            return 1.0
        case str():
            return 'a'
        case bool():
            return True
        case _:
            raise Exception("Unknown type")

if __name__ == '__main__':
    type_info = analyzeClass(FooBar(1, 2.00, 3))
