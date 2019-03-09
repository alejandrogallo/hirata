from hirata import HirataLine, Cc4sLine
import os


def test_E():
    # [ + 1.0 ] * Sum ( h1 p2 ) * f ( h1 p2 ) * t ( p2 h1 )
    # [ + 0.25 ] * Sum ( h3 h4 p1 p2 ) * t ( p1 p2 h3 h4 ) * v ( h3 h4 p1 p2 )
    infile = "cisd/E.in"
    assert(os.path.exists(infile))
    with open(infile) as f:
        lines = f.readlines()
    assert(len(lines) == 2)
    hl_singles = HirataLine(lines[0])
    hl_doubles = HirataLine(lines[1])
    assert(hl_singles is not None and hl_doubles is not None)

    assert(hl_singles.free_indices == "")
    assert(hl_singles.summation_indices == " h1 p2 ")
    assert(hl_singles.prefactors == ["+ 1.0 "])
    assert(
        hl_singles.postfactors ==
        ['Sum ( h1 p2 )', 'f ( h1 p2 )', 't ( p2 h1 )']
    )
    assert(str(hl_singles) == lines[0].replace('\n', ''))
    cl_singles = Cc4sLine(hl_singles)
    assert(cl_singles.free_indices == " ")
    assert(cl_singles.summation_indices == " i b ")
    assert(cl_singles.prefactors == ["+ 1.0 "])
    assert(cl_singles.postfactors == ['Fia["ib"]', 'Tai["bi"]'])
    assert(cl_singles.to_cpp() == ['( + 1.0  ) * Fia["ib"] * Tai["bi"];'])


    assert(hl_doubles.free_indices == "")
    assert(hl_doubles.summation_indices == " h3 h4 p1 p2 ")
    assert(hl_doubles.prefactors == ["+ 0.25 "])
    assert(
        hl_doubles.postfactors ==
        ['Sum ( h3 h4 p1 p2 )', 't ( p1 p2 h3 h4 )', 'v ( h3 h4 p1 p2 )']
    )
    assert(str(hl_doubles) == lines[1].replace('\n', ''))
    cl_doubles = Cc4sLine(hl_doubles)
    assert(cl_doubles.summation_indices == " k l a b ")
    assert(cl_doubles.prefactors == ["+ 0.25 "])
    assert(cl_doubles.postfactors == ['Tabij["abkl"]', 'Vijab["klab"]'])
    assert(
        cl_doubles.to_cpp() == ['( + 0.25  ) * Tabij["abkl"] * Vijab["klab"];']
    )


def test_T2():
    """
    [ + 1.0 ] * v ( p3 p4 h1 h2 )
    [ - 1.0 + 1.0 * P( p4 p3 h1 h2 => p3 p4 h1 h2 ) + 1.0 * P( p4 p3 h1 h2 => p4 p3 h2 h1 ) - 1.0 * P( p4 p3 h1 h2 => p3 p4 h2 h1 ) ] * f ( p4 h1 ) * t ( p3 h2 )
    [ - 1.0 + 1.0 * P( p3 p4 h1 h2 => p4 p3 h1 h2 ) ] * Sum ( h5 ) * t ( p3 h5 ) * v ( h5 p4 h1 h2 )
    [ + 1.0 - 1.0 * P( p3 p4 h2 h1 => p3 p4 h1 h2 ) ] * Sum ( p5 ) * t ( p5 h2 ) * v ( p3 p4 h1 p5 )
    [ - 1.0 + 1.0 * P( p3 p4 h1 h2 => p3 p4 h2 h1 ) ] * Sum ( h5 ) * f ( h5 h1 ) * t ( p3 p4 h5 h2 )
    [ - 1.0 + 1.0 * P( p4 p3 h1 h2 => p3 p4 h1 h2 ) ] * Sum ( p5 ) * f ( p4 p5 ) * t ( p5 p3 h1 h2 )
    [ + 0.5 ] * Sum ( h5 h6 ) * t ( p3 p4 h5 h6 ) * v ( h5 h6 h1 h2 )
    [ + 1.0 - 1.0 * P( p3 p4 h2 h1 => p4 p3 h2 h1 ) - 1.0 * P( p3 p4 h2 h1 => p3 p4 h1 h2 ) + 1.0 * P( p3 p4 h2 h1 => p4 p3 h1 h2 ) ] * Sum ( h6 p5 ) * t ( p5 p3 h6 h2 ) * v ( h6 p4 h1 p5 )
    [ + 0.5 ] * Sum ( p5 p6 ) * t ( p5 p6 h1 h2 ) * v ( p3 p4 p5 p6 )
    [ - 1.0 ] * e ( ) * t ( p3 p4 h1 h2 )
    """
    infile = "cisd/T2.in"
    assert(os.path.exists(infile))
    with open(infile) as f:
        lines = f.readlines()
    assert(len(lines) == 10)

    hl1 = HirataLine(lines[0])
    assert(set(hl1.free_indices.split()) == set("p3 p4 h1 h2".split()))
    assert(hl1.summation_indices == '')
    assert(hl1.prefactors == ["+ 1.0 "])
    assert(hl1.postfactors == ['v ( p3 p4 h1 h2 )'])
    assert(str(hl1) == lines[0].replace('\n', ''))
    cl1 = Cc4sLine(hl1)
    assert(set(cl1.free_indices.split()) == set(["c", "d", "i", "j"]))
    assert(cl1.summation_indices == "")
    assert(cl1.prefactors == ["+ 1.0 "])
    assert(cl1.postfactors == ['Vabij["cdij"]'])
    assert(cl1.to_cpp() == ['( + 1.0  ) * Vabij["cdij"];'])

    hl8 = HirataLine(lines[7])
    assert(set(hl8.free_indices.split()) == set("p3 p4 h1 h2".split()))
    assert(hl8.summation_indices == ' h6 p5 ')
    assert(
        hl8.prefactors == [
            '+ 1.0 ',
            '- 1.0 * P( p3 p4 h2 h1 => p4 p3 h2 h1 ) ',
            '- 1.0 * P( p3 p4 h2 h1 => p3 p4 h1 h2 ) ',
            '+ 1.0 * P( p3 p4 h2 h1 => p4 p3 h1 h2 ) '
        ]
    )
    assert(
        hl8.postfactors ==
        ['Sum ( h6 p5 )', 't ( p5 p3 h6 h2 )', 'v ( h6 p4 h1 p5 )']
    )
    assert(str(hl8) == lines[7].replace('\n', ''))
    cl8 = Cc4sLine(hl8)
    assert(set(cl8.free_indices.split()) == set(["c", "d", "i", "j"]))
    assert(cl8.summation_indices == " n e ")
    assert(
        cl8.prefactors ==
        ['+ 1.0 ',
        '- 1.0 * P( c d j i => d c j i ) ',
        '- 1.0 * P( c d j i => c d i j ) ',
        '+ 1.0 * P( c d j i => d c i j ) ']
    )
    assert(cl8.postfactors == ['Tabij["ecnj"]', 'Viajb["ndie"]'])
    assert(
        cl8.to_cpp() == [
            '( + 1.0  ) * Tabij["ecnj"] * Viajb["ndie"];',
            '( - 1.0  ) * Tabij["ednj"] * Viajb["ncie"];',
            '( - 1.0  ) * Tabij["ecni"] * Viajb["ndje"];',
            '( + 1.0  ) * Tabij["edni"] * Viajb["ncje"];'
        ]
    )
