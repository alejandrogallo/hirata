
// R1
( + 0.5 ) * Lai["ib"] *  Vabij["klie"] * Rabij["ebkl"]  // H21 (kle) -> bi
( + 0.5 ) * Lai["ib"] *  Vabij["kbde"] * Rabij["deki"]  // H21 (dek) -> bi

// R2
//( - 1.0 + 1.0 * P("cdij", "cdji") ) * Labij ["ijcd"] * Fai["mi"] * Rabij["cdmj"] // m -> cdij
( - 1.0 ) * Labij ["ijcd"] * Fij["mi"] * Rabij["cdmj"] // m -> cdij
( + 1.0 ) * Labij ["ijcd"] * Fij["mj"] * Rabij["cdmi"] // m -> cdij

//( - 1.0 + 1.0 * P("dcij", "cdij") ) * Labij["ijdc"] * Fai["de"] * Rabij["ecij"] // e -> dcij
( - 1.0 ) * Labij["ijdc"] * Fab["de"] * Rabij["ecij"] // e -> dcij
( + 1.0 ) * Labij["ijdc"] * Fab["ce"] * Rabij["edij"] // e -> dcij

//( + 1.0 - 1.0 * P("dcij", "cdij") - 1.0 * P("dcij", "dcji") + 1.0 * P("dcij", "cdji") ) * Labij["ijcd"] * Vabij["mdif"] * Rabij["fcmj"] //mf dcij
( + 1.0 ) * Labij["ijcd"] * Vabij["mdif"] * Rabij["fcmj"] //mf dcij
( - 1.0 ) * Labij["ijcd"] * Vabij["mcif"] * Rabij["fdmj"] //mf dcij
( - 1.0 ) * Labij["ijcd"] * Vabij["mdjf"] * Rabij["fcmi"] //mf dcij
( + 1.0 ) * Labij["ijcd"] * Vabij["mcjf"] * Rabij["fdmi"] //mf dcij

//( + 0.5 - 0.5 * P("dcij", "cdij") ) * Labij["ijcd"] * Tabij["edij"] * Vabij["noeh"] * Rabij["hcno"] // ohne -> cdij
( + 0.5 ) * Labij["ijcd"] * Tabij["edij"] * Vabij["noeh"] * Rabij["hcno"] // ohne -> cdij
( - 0.5 ) * Labij["ijcd"] * Tabij["ecij"] * Vabij["noeh"] * Rabij["hdno"] // ohne -> cdij

//( - 0.5 + 0.5 * P("cdij", "cdji") ) * Labij["ijcd"] * Tabij["cdmi"] * Vabij["mngh"] * Rabij["ghnj"] // mngh -> cdij
( - 0.5 ) * Labij["ijcd"] * Tabij["cdmi"] * Vabij["mngh"] * Rabij["ghnj"] // mngh -> cdij
( + 0.5 ) * Labij["ijcd"] * Tabij["cdmj"] * Vabij["mngh"] * Rabij["ghni"] // mngh -> cdij

//( - 1.0 + 1.0 * P("dcij", "cdij") + 1.0 * P("dcij", "dcji") - 1.0 * P("dcij", "cdji") ) * Labij["ijcd"] * Tabij["edni"] * Vabij["noeh"] * Rabij["hcoj"] // enho -> cdij
( - 1.0 ) * Labij["ijcd"] * Tabij["edni"] * Vabij["noeh"] * Rabij["hcoj"] // enho -> cdij
( + 1.0 ) * Labij["ijcd"] * Tabij["ecni"] * Vabij["noeh"] * Rabij["hdoj"] // enho -> cdij
( + 1.0 ) * Labij["ijcd"] * Tabij["ednj"] * Vabij["noeh"] * Rabij["hcoi"] // enho -> cdij
( - 1.0 ) * Labij["ijcd"] * Tabij["ecnj"] * Vabij["noeh"] * Rabij["hdoi"] // enho -> cdij

//( - 0.5 + 0.5 * P("cdij", "cdji") ) * Labij["ijcd"] * Tabij["efoi"] * Vabij["opef"] * Rabij["cdpj"] // efop -> cdij
( - 0.5 ) * Labij["ijcd"] * Tabij["efoi"] * Vabij["opef"] * Rabij["cdpj"] // efop -> cdij
( + 0.5 ) * Labij["ijcd"] * Tabij["efoj"] * Vabij["opef"] * Rabij["cdpi"] // efop -> cdij

//( + 0.5 - 0.5 * P("dcij", "cdij") ) * Labij["ijcd"] * Tabij["edno"] * Vabij["noeh"] * Rabij["hcij"] // noeh -> cdij
( + 0.5 ) * Labij["ijcd"] * Tabij["edno"] * Vabij["noeh"] * Rabij["hcij"] // noeh -> cdij
( - 0.5 ) * Labij["ijcd"] * Tabij["ecno"] * Vabij["noeh"] * Rabij["hdij"] // noeh -> cdij


( + 0.5 )  * Labij["ijcd"] * Vabij["mnij"] * Rabij["cdmn"] // mn -> cdij
( + 0.5 )  * Labij["ijcd"] * Vabij["cdef"] * Rabij["efij"] // ef -> cdij
( + 0.25 ) * Labij["ijcd"] * Tabij["efij"] * Vabij["opef"] * Rabij["cdop"] // efop -> cdij
( + 0.25 ) * Labij["ijcd"] * Tabij["cdmn"] * Vabij["mngh"] * Rabij["ghij"] // mngh -> cdij
