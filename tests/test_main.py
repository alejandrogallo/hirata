import logging
import hirata
import copy
logging.basicConfig(level=logging.DEBUG)

def test_1():

    print("")
    line = "[ - 1.0 + 1.0 * P( h3 h4 p2 p1 => h3 h4 p1 p2 ) + 1.0 * P( h3 h4 p2 p1 => h4 h3 p2 p1 ) - 1.0 * P( h3 h4 p2 p1 => h4 h3 p1 p2 ) ] * f ( h3 p2 ) * y ( h4 p1 )\n"

    h_line = hirata.HirataLine(line)

    assert h_line is not None
    assert len(h_line.get_prefactors()) == 4
    assert len(h_line.get_postfactors()) == 2
    assert h_line.get_summation_indices() == None
    assert h_line.get_free_indices() == " h3 p2 h4 p1"
    assert hirata.get_hp_combination(h_line.get_postfactors()[1]) == "hp"

    cc4s_line = hirata.hirata_to_cc4s(h_line)
    lines = hirata.cc4s_to_cpp(cc4s_line)

def test_2():

    print("")
    line = "[ - 1.0 + 1.0 * P( h3 h4 p2 p1 => h3 h4 p1 p2 ) ] * Sum ( h5 ) * v ( h3 h4 h5 p2 ) * y ( h5 p1 )\n"

    h_line = hirata.HirataLine(line)

    assert h_line is not None
    assert len(h_line.get_prefactors()) == 2
    assert len(h_line.get_postfactors()) == 3
    assert h_line.get_summation_indices() == " h5 "
    assert h_line.get_free_indices() == " h3 h4 p2 p1"
    assert hirata.get_hp_combination(h_line.get_postfactors()[1]) == "hhhp"

    cc4s_line = hirata.hirata_to_cc4s(h_line)
    lines = hirata.cc4s_to_cpp(cc4s_line)

def test_3():

    print("")
    line = "[ + 0.5 ] * Sum ( p3 p4 h5 h6 ) * t ( p3 p4 h5 h6 ) * v ( h6 h2 p3 p4 ) * y ( h5 p1 )\n"

    h_line = hirata.HirataLine(line)

    assert h_line is not None
    assert len(h_line.get_prefactors()) == 1
    assert len(h_line.get_postfactors()) == 4
    assert h_line.get_summation_indices() == " p3 p4 h5 h6 "
    assert h_line.get_free_indices() == " h2 p1"
    assert hirata.get_hp_combination(h_line.get_postfactors()[1]) == "pphh"

    cc4s_line = hirata.hirata_to_cc4s(h_line)
    lines = hirata.cc4s_to_cpp(cc4s_line)

def test_4():

    print("")
    line = "[ + 1.0 - 1.0 * P( p6 p4 p5 h1 h2 h3 => p5 p4 p6 h1 h2 h3 ) - 1.0 * P( p6 p5 p4 h1 h2 h3 => p4 p5 p6 h1 h2 h3 ) - 1.0 * P( p6 p4 p5 h1 h2 h3 => p6 p4 p5 h1 h3 h2 ) + 1.0 * P( p6 p4 p5 h1 h2 h3 => p5 p4 p6 h1 h3 h2 ) + 1.0 * P( p6 p5 p4 h1 h2 h3 => p4 p5 p6 h1 h3 h2 ) + 1.0 * P( p6 p4 p5 h1 h2 h3 => p6 p4 p5 h2 h3 h1 ) - 1.0 * P( p6 p4 p5 h1 h2 h3 => p5 p4 p6 h2 h3 h1 ) - 1.0 * P( p6 p5 p4 h1 h2 h3 => p4 p5 p6 h2 h3 h1 ) ] * Sum ( h9 h10 p7 p8 ) * t ( p7 h1 ) * t ( p8 h2 ) * t ( p6 h9 ) * t ( p4 p5 h10 h3 ) * v ( h9 h10 p7 p8 )\n"

    h_line = hirata.HirataLine(line)

    assert h_line is not None
    assert len(h_line.get_prefactors()) == 9
    assert len(h_line.get_postfactors()) == 6
    assert h_line.get_summation_indices() == " h9 h10 p7 p8 "
    #assert(h_line.get_free_indices() == " p4 p5 h3 p6 h1 h2")
    assert hirata.get_hp_combination(h_line.get_postfactors()[1]) == "ph"
    assert hirata.get_hp_combination(h_line.get_postfactors()[2]) == "ph"
    assert hirata.get_hp_combination(h_line.get_postfactors()[3]) == "ph"
    assert hirata.get_hp_combination(h_line.get_postfactors()[4]) == "pphh"
    assert hirata.get_hp_combination(h_line.get_postfactors()[5]) == "hhpp"

    cc4s_line = hirata.hirata_to_cc4s(h_line)
    lines = hirata.cc4s_to_cpp(cc4s_line)

