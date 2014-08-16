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

from setuptools import setup


setup(
    name="weakref_property",
    version="0.1",
    url="https://github.com/popotam/python-weakref-property",
    py_modules=['weakref_property'],
    author="Paweł Sobkowiak",
    author_email="pawel.sobkowiak@gmail.com",
    license="GPLv3",
    description="A Descriptor class implementing weakref properties in Python",
    keywords=['weakref', 'property', 'descriptor'],
    zip_safe=True,
)
