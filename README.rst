A Descriptor class implementing weakref properties in Python 2/3
================================================================

Add a property that acts like a normal attribute,
but keeps a weak reference to anything that is assigned
to it.

Example:

    First let's define WeakValue using WeakProperty
    and SomeClass that will be weakly referenced::

        >>> import weakref_property
        >>> import gc

        >>> class WeakValue(object):
        ...     value = weakref_property.WeakProperty('value')

        >>> class SomeClass(object):
        ...     pass

    You can assign and retrieve a value::

        >>> a = SomeClass()
        >>> obj = WeakValue()
        >>> obj.value = a
        >>> obj.value  # doctest: +ELLIPSIS
        <__main__.SomeClass object at ...>

    But it is kept as a weakref, so it can get collected.
    If it is collected, the property returns None::

        >>> del a
        >>> gc.collect()  # force gc to collect `a` object
        0
        >>> print(obj.value)
        None

    You can also delete the value completelly::

        >>> del obj.value
        >>> obj.value
        Traceback (most recent call last):
            ...
        AttributeError: 'WeakValue' object has no attribute 'value'

    Sadly, weakrefs do not work on tuples, ints
    and not-subclassed lists and dicts::

        >>> obj.value = []
        Traceback (most recent call last):
            ...
        TypeError: cannot create weak reference to 'list' object
