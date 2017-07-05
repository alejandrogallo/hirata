
PARTICLE_INDICES = dict(
    p1="a",
    p2="b",
    p3="c",
    p4="d",
    p5="e",
    p6="f",
    p7="g",
    p8="h"
)

HOLE_INDICES = dict(
    h1="i",
    h2="j",
    h3="k",
    h4="l",
    h5="m",
    h6="n",
    h7="o",
    h8="p"
)

# This is just for the main name
TENSOR_NAME_TRANSLATON = dict(
    x="R{hpindices}",
    y="L{hpindices}",
    v="V{hpindices}",
    f="F{hpindices}",
    t="T{hpindices}"
)

# Up to 4 indices, for less we will just get the first two characters of every
# case
TENSOR_INDICES_TRANSLATION = dict(
    hhhh="ijkl",

    phhh="aijk",
    hphh="iajk",
    hhph="ijak",
    hhhp="ijka",

    pphh="abij",
    phph="aibj",
    phhp="aijb",
    hpph="iabj",
    hphp="iajb",
    hhpp="ijab",

    ppph="abci",
    pphp="abic",
    phpp="aibc",
    hppp="iabc",

    pppp="abcd",
)
