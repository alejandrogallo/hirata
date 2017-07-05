import logging
import hirata
import copy
logging.basicConfig(level=logging.DEBUG)

#######################################################################################################

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

#######################################################################################################

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

#####################################################################################

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

