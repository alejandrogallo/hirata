from hirata.cc4s import *
import hirata.conf as conf


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


def test_transform_tensor_indices():
    assert(transform_tensor_indices("(a b i j k l)") == '["abijkl"]')


def test_translate_indices():
    import re
    # assert(not re.match(r"(h1)([^0-9]*)$", "h10"))
    # assert(re.match(r"(h10)([^0-9]*)$", "h10"))
    # assert(re.match(r"(h1)([^0-9]+)", "t(h1 h3)"))
    # assert(not re.match(r"(h1)([^0-9]*)", "t(h10 h3)"))
    for case in [conf.PARTICLE_INDICES, conf.HOLE_INDICES]:
        for hp in case.keys():
            assert(translate_indices(hp+" ").strip() == case[hp])
    assert(
        translate_indices("t(h1 h3 p2 p1)")
        == "t(i k b a)"
    )
    assert(
        translate_indices("as dfasdf adfasdf (h13 h1 h3 p12 p1)")
        == "as dfasdf adfasdf (M i k D a)"
    )

def test_translate_tensor_names():

    assert(
        translate_tensor_names("t(h1 h3 p2 p1)")
        == "Tijab(h1 h3 p2 p1)"
    )

    assert(
        translate_tensor_names("t(h11 h3 p12 p1 h3 p3)")
        == "Tijabkc(h11 h3 p12 p1 h3 p3)"
    )
