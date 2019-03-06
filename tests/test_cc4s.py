from hirata.cc4s import *


def test_get_hp_combination():
    assert(
        get_hp_combination("h193 asdflkj p3 h4 124") == "hph"
    )
