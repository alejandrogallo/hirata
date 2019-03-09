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

    assert(hl_doubles.free_indices == "")
    assert(hl_doubles.summation_indices == " h3 h4 p1 p2 ")
    assert(hl_doubles.prefactors == ["+ 0.25 "])
    assert(
        hl_doubles.postfactors ==
        ['Sum ( h3 h4 p1 p2 )', 't ( p1 p2 h3 h4 )', 'v ( h3 h4 p1 p2 )']
    )
    assert(str(hl_doubles) == lines[1].replace('\n', ''))

