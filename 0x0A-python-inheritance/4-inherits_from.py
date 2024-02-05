#!/usr/bin/python3
"""Defines the inherits_from function."""


def inherits_from(obj, a_class):
    """Checks if (obj) is a sub-class of (a_class)"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
