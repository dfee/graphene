from ..field import Field
from ..objecttype import ObjectType
from ..scalars import ID
from ..utils import (
    LazyType,
    get_type,
)


class Container:
    class MyObject(ObjectType):
        id = ID()


def test_lazy_type():
    dotted_path = Container.__module__
    dotted_attributes = 'Container.MyObject'

    lt = LazyType(dotted_path, dotted_attributes)
    assert get_type(lt) == Container.MyObject


def test_related_lazy_type():
    dotted_path = Container.__module__
    dotted_attributes = 'Container.MyObject'

    class ParentObject(ObjectType):
        related = Field(LazyType(
            dotted_path,
            dotted_attributes,
        ))

    assert ParentObject.related.type == Container.MyObject
