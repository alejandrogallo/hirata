( - 0.5 )  *  Vabij["jclm"] * Labij["mlca"]
( - 0.5 )  *  Vabij["cdma"] * Labij["mjdc"]

// These are zero because we have hartree fock orbitals
//( + 1.0 )  *  Fai["cl"]     * Labij["ljca"]
//( + 0.5 )  *  Fai["jc"]     * Tabij["dcmn"] * Labij["nmda"]
//( + 0.5 )  *  Fai["ka"]     * Tabij["denk"] * Labij["njed"]
//( + 1.0 )  *  Fai["kd"]     * Tabij["ednk"] * Labij["njea"]

( - 0.5 )  *  Tabij["cdmn"] * Vabij["njoa"] * Labij["omdc"]
( - 1.0 )  *  Tabij["cdmn"] * Vabij["njod"] * Labij["omca"]
( - 0.25 ) *  Tabij["cdmn"] * Vabij["mnoa"] * Labij["ojdc"]
( - 0.5 )  *  Tabij["cdmn"] * Vabij["mnod"] * Labij["ojca"]
( - 0.5 )  *  Tabij["cdmn"] * Vabij["jgda"] * Labij["nmgc"]
( - 0.25 ) *  Tabij["cdmn"] * Vabij["jgcd"] * Labij["nmga"]
( - 1.0 )  *  Tabij["cdmn"] * Vabij["ngda"] * Labij["mjgc"]
( - 0.5 )  *  Tabij["cdmn"] * Vabij["ngcd"] * Labij["mjga"]
