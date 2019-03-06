from hirata.cc4s import *


def test_get_hp_combination():
    assert(
        get_hp_combination("h193 asdflkj p3 h4 124") == "hph"
    )
    assert(get_hp_combination("h3 p13 h23 p1 h2 1p h12 31p3") == "hphphhp")


def test_get_converted_hp_combination():
    assert(get_converted_hp_combination("th193 asdflkj p3 h4 12p4") == "iajb")
    assert(get_converted_hp_combination("h123 p41 h1 p4 p41 h2") == "iajbck")
    assert(get_converted_hp_combination("h212312") == "i")
    assert(get_converted_hp_combination("h12 p3 h4 h1 p1 h2 p1") == "hphhphp")
