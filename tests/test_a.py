# -*- coding: utf-8 -*-

from a import f


def test_parse_no_subarg():
    ret = f()
    assert ret == 'hi'
