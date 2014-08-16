#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Paweł Sobkowiak <pawel.sobkowiak@gmail.com>
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the the GNU General Public License version 3, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the applicable version of the GNU General Public
# License for more details.
#.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
:mod:`weakref_property` -- Descriptor class implementing weakref properties.
============================================================================

Please, take a look at WeakProperty class' docstring.

"""

import weakref
import types

__version__ = "0.1"



class WeakProperty(object):
    """Descriptor class implementing weakref properties.

    Add a property that acts like a normal attribute,
    but keeps a weak reference to anything that is assigned
    to it.

    First let's define WeakValue using WeakProperty
    and SomeClass that will be weakly referenced:

        >>> import weakref_property
        >>> import gc

        >>> class WeakValue(object):
        ...     value = weakref_property.WeakProperty('value')

        >>> class SomeClass(object):
        ...     pass

    You can assign and retrieve a value:

        >>> a = SomeClass()
        >>> obj = WeakValue()
        >>> obj.value = a
        >>> obj.value  # doctest: +ELLIPSIS
        <__main__.SomeClass object at ...>

    But it is kept as a weakref, so it can get collected.
    If it is collected, the property returns None.

        >>> del a
        >>> gc.collect()  # force gc to collect `a` object
        0
        >>> obj.value

    You can also delete the value completelly:

        >>> del obj.value
        >>> obj.value
        Traceback (most recent call last):
            ...
        AttributeError: 'WeakValue' object has no attribute 'value'

    Sadly, weakrefs do not work on list, dict, tuple and int:

        >>> obj.value = []
        Traceback (most recent call last):
            ...
        TypeError: cannot create weak reference to 'list' object

    """
    def __init__(self, attrname, callback=None):
        self.attrname = attrname
        self.callback = callback

    def __get__(self, obj, objtype=None):
        try:
            return obj.__dict__[self.attrname]()
        except KeyError:
            raise AttributeError("'{}' object has no attribute '{}'".format(
                obj.__class__.__name__, self.attrname))

    def __set__(self, obj, value):
        if isinstance(value, types.MethodType) \
                and hasattr(weakref, 'WeakMethod'):
            ref = weakref.WeakMethod(value, self.callback)
        else:
            ref = weakref.ref(value, self.callback)
        obj.__dict__[self.attrname] = ref

    def __delete__(self, obj):
        try:
            del obj.__dict__[self.attrname]
        except KeyError:
            raise AttributeError("'{}' object has no attribute '{}'".format(
                obj.__class__.__name__, self.attrname))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
