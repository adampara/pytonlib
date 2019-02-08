#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def is_interactive():
    import __main__ as main
    return not hasattr(main, '__file__')

