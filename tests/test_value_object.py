from ddd_nginx.value_object import ValueObject


class TheValueObject(ValueObject):

    def __init__(self, name):
        super(TheValueObject, self).__init__()
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, ValueObject):
            return NotImplemented

        return self.name == other.name


def test_value_object_compare():
    a_value_object = TheValueObject("name")
    b_value_object = TheValueObject("name")

    assert a_value_object.same_as(b_value_object)
