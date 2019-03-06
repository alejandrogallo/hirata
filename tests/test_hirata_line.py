from hirata import HirataLine

def test_ccsdt():
    rawline = (
        "[ + 0.5 - 0.5 * P( p4 p5 p6 h2 h3 h1 => p5 p4 p6 h2 h3 h1 )"
        " - 0.5 * P( p4 p6 p5 h2 h3 h1 => p6 p4 p5 h2 h3 h1 ) + "
        "0.5 * P( p4 p5 p6 h3 h2 h1 => p4 p5 p6 h1 h3 h2 ) - "
        "0.5 * P( p4 p5 p6 h3 h2 h1 => p5 p4 p6 h1 h3 h2 ) - "
        "0.5 * P( p4 p6 p5 h3 h2 h1 => p6 p4 p5 h1 h3 h2 ) + "
        "0.5 * P( p4 p5 p6 h2 h3 h1 => p4 p5 p6 h1 h2 h3 ) - "
        "0.5 * P( p4 p5 p6 h2 h3 h1 => p5 p4 p6 h1 h2 h3 ) - "
        "0.5 * P( p4 p6 p5 h2 h3 h1 => p6 p4 p5 h1 h2 h3 ) ] * "
        "Sum ( h9 h10 p7 p8 ) * "
        "t ( p7 p8 p4 h9 h2 h3 ) * "
        "t ( p5 p6 h10 h1 ) * "
        "v ( h9 h10 p7 p8 )\n"
    )
    hl = HirataLine(rawline)
