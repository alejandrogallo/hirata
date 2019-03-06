from hirata import HirataLine, Cc4sLine


def test_ccsdt():
    rawline = (
        "[ + 0.5 - 0.5 * P( p4 p5 p6 h2 h3 h11 => p5 p4 p6 h2 h3 h11 )"
        " - 0.5 * P( p4 p6 p5 h2 h3 h11 => p6 p4 p5 h2 h3 h11 ) "
        "+ 0.5 * P( p4 p5 p6 h3 h2 h11 => p4 p5 p6 h11 h3 h2 ) "
        "- 0.5 * P( p4 p5 p6 h3 h2 h11 => p5 p4 p6 h11 h3 h2 ) "
        "- 0.5 * P( p4 p6 p5 h3 h2 h11 => p6 p4 p5 h11 h3 h2 ) "
        "+ 0.5 * P( p4 p5 p6 h2 h3 h11 => p4 p5 p6 h11 h2 h3 ) "
        "- 0.5 * P( p4 p5 p6 h2 h3 h11 => p5 p4 p6 h11 h2 h3 ) "
        "- 0.5 * P( p4 p6 p5 h2 h3 h11 => p6 p4 p5 h11 h2 h3 ) ] * "
        "Sum ( h9 h10 p7 p8 ) * "
        "t ( p7 p8 p4 h9 h2 h3 ) * "
        "t ( p5 p6 h10 h11 ) * "
        "v ( h9 h10 p7 p8 )\n"
    )
    hl = HirataLine(rawline)
    assert(len(hl.get_prefactors()) == 9)
    assert(hl.get_prefactors() ==
        ["+ 0.5 ", "- 0.5 * P( p4 p5 p6 h2 h3 h11 => p5 p4 p6 h2 h3 h11 ) ",
        "- 0.5 * P( p4 p6 p5 h2 h3 h11 => p6 p4 p5 h2 h3 h11 ) ",
        "+ 0.5 * P( p4 p5 p6 h3 h2 h11 => p4 p5 p6 h11 h3 h2 ) ",
        "- 0.5 * P( p4 p5 p6 h3 h2 h11 => p5 p4 p6 h11 h3 h2 ) ",
        "- 0.5 * P( p4 p6 p5 h3 h2 h11 => p6 p4 p5 h11 h3 h2 ) ",
        "+ 0.5 * P( p4 p5 p6 h2 h3 h11 => p4 p5 p6 h11 h2 h3 ) ",
        "- 0.5 * P( p4 p5 p6 h2 h3 h11 => p5 p4 p6 h11 h2 h3 ) ",
        "- 0.5 * P( p4 p6 p5 h2 h3 h11 => p6 p4 p5 h11 h2 h3 ) "]
    )
    assert(len(hl.get_postfactors()) == 4)
    assert(
        hl.get_postfactors() ==
        [
        'Sum ( h9 h10 p7 p8 )',
        't ( p7 p8 p4 h9 h2 h3 )',
        't ( p5 p6 h10 h11 )',
        'v ( h9 h10 p7 p8 )'
        ]
    )
    assert(hl.summation_indices == ' h9 h10 p7 p8 ')
    assert(
        set(hl.free_indices.split()) == set('h11 h2 h3 p4 p5 p6'.split())
    )
    assert(str(hl) == rawline.replace('\n', ''))

    cc4sline = Cc4sLine(hl)
    # assert(
        # cc4sline.postfactors ==
        # ['Tabcijk["ghdIjk"]', 'Tabij["efJK"]', 'Vijab["IJgh"]']
    # )
