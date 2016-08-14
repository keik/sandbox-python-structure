# -*- coding: utf-8 -*-

from sandbox_python_structure import f


def test_parse_no_subarg():
    ret = f()
    assert ret == 'hi'
