( - 0.5 )  *  Vabij["jclm"] * Labij["mlca"] // H21 (mlc) -> aj
( - 0.5 )  *  Vabij["cdma"] * Labij["mjdc"] // H21 (mdc) -> aj

// These are zero because we have hartree fock orbitals
//( + 1.0 )  *  Fai["cl"]     * Labij["ljca"]
//( + 0.5 )  *  Fai["jc"]     * Tabij["dcmn"] * Labij["nmda"]
//( + 0.5 )  *  Fai["ka"]     * Tabij["denk"] * Labij["njed"]
//( + 1.0 )  *  Fai["kd"]     * Tabij["ednk"] * Labij["njea"]

( - 0.5 )  *  Tabij["cdmn"] * Vabij["njoa"] * Labij["omdc"] // H21 (mncdo) -> aj
( - 1.0 )  *  Tabij["cdmn"] * Vabij["njod"] * Labij["omca"] // H21 (mncdo) -> aj
( - 0.25 ) *  Tabij["cdmn"] * Vabij["mnoa"] * Labij["ojdc"] // H21 (mncdo) -> aj
( - 0.5 )  *  Tabij["cdmn"] * Vabij["mnod"] * Labij["ojca"] // H21 (mncdo) -> aj
( - 0.5 )  *  Tabij["cdmn"] * Vabij["jgda"] * Labij["nmgc"] // H21 (mncdg) -> aj
( - 0.25 ) *  Tabij["cdmn"] * Vabij["jgcd"] * Labij["nmga"] // H21 (mncdg) -> aj
( - 1.0 )  *  Tabij["cdmn"] * Vabij["ngda"] * Labij["mjgc"] // H21 (mncdg) -> aj
( - 0.5 )  *  Tabij["cdmn"] * Vabij["ngcd"] * Labij["mjga"] // H21 (mncdg) -> aj

