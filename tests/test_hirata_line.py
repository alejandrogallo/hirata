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
    assert(len(cc4sline.postfactors) == 3)
    assert(len(cc4sline.prefactors) == 9)
    assert(cc4sline.summation_indices == " I J g h ")
    assert(set(cc4sline.free_indices.split()) == set(" K j k d e f ".split()))
    assert(
        cc4sline.postfactors ==
        ['Tabcijk["ghdIjk"]', 'Tabij["efJK"]', 'Vijab["IJgh"]']
    )
    assert(
        cc4sline.prefactors ==
        [
            '+ 0.5 ',
            '- 0.5 * P( d e f j k K => e d f j k K ) ',
            '- 0.5 * P( d f e j k K => f d e j k K ) ',
            '+ 0.5 * P( d e f k j K => d e f K k j ) ',
            '- 0.5 * P( d e f k j K => e d f K k j ) ',
            '- 0.5 * P( d f e k j K => f d e K k j ) ',
            '+ 0.5 * P( d e f j k K => d e f K j k ) ',
            '- 0.5 * P( d e f j k K => e d f K j k ) ',
            '- 0.5 * P( d f e j k K => f d e K j k ) '
        ]
    )

    cpp_lines = cc4sline.to_cpp()
    assert(cpp_lines ==
    [
        '( + 0.5  ) * Tabcijk["ghdIjk"] * Tabij["efJK"] * Vijab["IJgh"];',
        '( - 0.5  ) * Tabcijk["gheIjk"] * Tabij["dfJK"] * Vijab["IJgh"];',
        '( - 0.5  ) * Tabcijk["ghfIjk"] * Tabij["edJK"] * Vijab["IJgh"];',
        '( + 0.5  ) * Tabcijk["ghdIkK"] * Tabij["efJj"] * Vijab["IJgh"];',
        '( - 0.5  ) * Tabcijk["gheIkK"] * Tabij["dfJj"] * Vijab["IJgh"];',
        '( - 0.5  ) * Tabcijk["ghfIkK"] * Tabij["edJj"] * Vijab["IJgh"];',
        '( + 0.5  ) * Tabcijk["ghdIKj"] * Tabij["efJk"] * Vijab["IJgh"];',
        '( - 0.5  ) * Tabcijk["gheIKj"] * Tabij["dfJk"] * Vijab["IJgh"];',
        '( - 0.5  ) * Tabcijk["ghfIKj"] * Tabij["edJk"] * Vijab["IJgh"];'
    ])

