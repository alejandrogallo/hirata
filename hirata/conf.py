
PARTICLE_INDICES = dict(
    p1="a", p2="b", p3="c", p4="d", p5="e", p6="f", p7="g", p8="h",
    p9="A", p10="B", p11="C", p12="D", p13="E", p14="F", p15="G", p16="H",
)

HOLE_INDICES = dict(
    h1="i", h2="j", h3="k", h4="l", h5="m", h6="n", h7="o", h8="p",
    h9="I", h10="J", h11="K", h12="L", h13="M", h14="N", h15="O", h16="P",
)

# This is just for the main name
TENSOR_NAME_TRANSLATON = dict(
    x="R{hpindices}",
    y="L{hpindices}",
    v="V{hpindices}",
    f="F{hpindices}",
    t="T{hpindices}",
    t1="T1{hpindices}",
    t2="T2{hpindices}",
    t3="T3{hpindices}",
)

# Up to 4 indices, for less we will just get the first two characters of every
# case
TENSOR_INDICES_TRANSLATION = dict(
    # Doubles

    hhhh="ijkl", phhh="aijk", hphh="iajk", hhph="ijak", hhhp="ijka",
    pphh="abij", phph="aibj", phhp="aijb", hpph="iabj", hphp="iajb",
    hhpp="ijab", ppph="abci", pphp="abic", phpp="aibc", hppp="iabc",
    pppp="abcd", hhhhhh="ijklmn",

    # Triples
    hhhhhp="ijklma", hhhhph="ijklam", hhhhpp="ijklab", hhhphh="ijkalm",
    hhhphp="ijkalb", hhhpph="ijkabl", hhhppp="ijkabc", hhphhh="ijaklm",
    hhphhp="ijaklb", hhphph="ijakbl", hhphpp="ijakbc", hhpphh="ijabkl",
    hhpphp="ijabkc", hhppph="ijabck", hhpppp="ijabcd", hphhhh="iajklm",
    hphhhp="iajklb", hphhph="iajkbl", hphhpp="iajkbc", hphphh="iajbkl",
    hphphp="iajbkc", hphpph="iajbck", hphppp="iajbcd", hpphhh="iabjkl",
    hpphhp="iabjkc", hpphph="iabjck", hpphpp="iabjcd", hppphh="iabcjk",
    hppphp="iabcjd", hpppph="iabcdj", hppppp="iabcde", phhhhh="aijklm",
    phhhhp="aijklb", phhhph="aijkbl", phhhpp="aijkbc", phhphh="aijbkl",
    phhphp="aijbkc", phhpph="aijbck", phhppp="aijbcd", phphhh="aibjkl",
    phphhp="aibjkc", phphph="aibjck", phphpp="aibjcd", phpphh="aibcjk",
    phpphp="aibcjd", phppph="aibcdj", phpppp="aibcde", pphhhh="abijkl",
    pphhhp="abijkc", pphhph="abijck", pphhpp="abijcd", pphphh="abicjk",
    pphphp="abicjd", pphpph="abicdj", pphppp="abicde", ppphhh="abcijk",
    ppphhp="abcijd", ppphph="abcidj", ppphpp="abcide", pppphh="abcdij",
    pppphp="abcdie", ppppph="abcdei", pppppp="abcdef",

    hhhhhhh="ijklmno", hhhhhhp="ijklmna", hhhhhph="ijklman", hhhhhpp="ijklmab",
    hhhhphh="ijklamn", hhhhphp="ijklamb", hhhhpph="ijklabm", hhhhppp="ijklabc",
    hhhphhh="ijkalmn", hhhphhp="ijkalmb", hhhphph="ijkalbm", hhhphpp="ijkalbc",
    hhhpphh="ijkablm", hhhpphp="ijkablc", hhhppph="ijkabcl", hhhpppp="ijkabcd",
    hhphhhh="ijaklmn", hhphhhp="ijaklmb", hhphhph="ijaklbm", hhphhpp="ijaklbc",
    hhphphh="ijakblm", hhphphp="ijakblc", hhphpph="ijakbcl", hhphppp="ijakbcd",
    hhpphhh="ijabklm", hhpphhp="ijabklc", hhpphph="ijabkcl", hhpphpp="ijabkcd",
    hhppphh="ijabckl", hhppphp="ijabckd", hhpppph="ijabcdk", hhppppp="ijabcde",
    hphhhhh="iajklmn", hphhhhp="iajklmb", hphhhph="iajklbm", hphhhpp="iajklbc",
    hphhphh="iajkblm", hphhphp="iajkblc", hphhpph="iajkbcl", hphhppp="iajkbcd",
    hphphhh="iajbklm", hphphhp="iajbklc", hphphph="iajbkcl", hphphpp="iajbkcd",
    hphpphh="iajbckl", hphpphp="iajbckd", hphppph="iajbcdk", hphpppp="iajbcde",
    hpphhhh="iabjklm", hpphhhp="iabjklc", hpphhph="iabjkcl", hpphhpp="iabjkcd",
    hpphphh="iabjckl", hpphphp="iabjckd", hpphpph="iabjcdk", hpphppp="iabjcde",
    hppphhh="iabcjkl", hppphhp="iabcjkd", hppphph="iabcjdk", hppphpp="iabcjde",
    hpppphh="iabcdjk", hpppphp="iabcdje", hppppph="iabcdej", hpppppp="iabcdef",
    phhhhhh="aijklmn", phhhhhp="aijklmb", phhhhph="aijklbm", phhhhpp="aijklbc",
    phhhphh="aijkblm", phhhphp="aijkblc", phhhpph="aijkbcl", phhhppp="aijkbcd",
    phhphhh="aijbklm", phhphhp="aijbklc", phhphph="aijbkcl", phhphpp="aijbkcd",
    phhpphh="aijbckl", phhpphp="aijbckd", phhppph="aijbcdk", phhpppp="aijbcde",
    phphhhh="aibjklm", phphhhp="aibjklc", phphhph="aibjkcl", phphhpp="aibjkcd",
    phphphh="aibjckl", phphphp="aibjckd", phphpph="aibjcdk", phphppp="aibjcde",
    phpphhh="aibcjkl", phpphhp="aibcjkd", phpphph="aibcjdk", phpphpp="aibcjde",
    phppphh="aibcdjk", phppphp="aibcdje", phpppph="aibcdej", phppppp="aibcdef",
    pphhhhh="abijklm", pphhhhp="abijklc", pphhhph="abijkcl", pphhhpp="abijkcd",
    pphhphh="abijckl", pphhphp="abijckd", pphhpph="abijcdk", pphhppp="abijcde",
    pphphhh="abicjkl", pphphhp="abicjkd", pphphph="abicjdk", pphphpp="abicjde",
    pphpphh="abicdjk", pphpphp="abicdje", pphppph="abicdej", pphpppp="abicdef",
    ppphhhh="abcijkl", ppphhhp="abcijkd", ppphhph="abcijdk", ppphhpp="abcijde",
    ppphphh="abcidjk", ppphphp="abcidje", ppphpph="abcidej", ppphppp="abcidef",
    pppphhh="abcdijk", pppphhp="abcdije", pppphph="abcdiej", pppphpp="abcdief",
    ppppphh="abcdeij", ppppphp="abcdeif", pppppph="abcdefi", ppppppp="abcdefg",

)

