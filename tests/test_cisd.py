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

