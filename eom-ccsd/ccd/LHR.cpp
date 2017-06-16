
//R1

( - 1.0 ) * Lai["ib"] *  Fij["ki"]     * Rai["bk"]
( + 1.0 ) * Lai["ib"] *  Fab["bc"]     * Rai["ci"]
( - 1.0 ) * Lai["ib"] *  Viajb["kbid"] * Rai["dk"]
( + 1.0 ) * Lai["ib"] *  Tabij["cbli"] * Vijab["lmcf"] * Rai["fm"]
( - 0.5 ) * Lai["ib"] *  Tabij["cdmi"] * Vijab["mncd"] * Rai["bn"]
( - 0.5 ) * Lai["ib"] *  Tabij["cblm"] * Vijab["lmcf"] * Rai["fi"]

// from eomd
// R1
( + 0.5 ) * Lai["ib"] *  Vijka["klie"] * Rabij["ebkl"]  // H21 (kle) -> bi
( + 0.5 ) * Lai["ib"] *  Viabc["kbde"] * Rabij["deki"]  // H21 (dek) -> bi








//R2


//( - 1.0 + 1.0 * P("dcij", "cdij") )     *  Viajk["mdij"]          * Rai["cm"]
( - 1.0 )     * Labij ["ijcd"] *  Viajk["mdij"]          * Rai["cm"]
( + 1.0 )     * Labij ["ijcd"] *  Viajk["mcij"]          * Rai["dm"]

//( + 1.0 - 1.0 * P("cdij", "cdji") )     *  Vabic["cdie"]          * Rai["ej"]
( + 1.0 )     * Labij ["ijcd"] *  Vabic["cdie"]          * Rai["ej"]
( - 1.0 )     * Labij ["ijcd"] *  Vabic["cdje"]          * Rai["ei"]

// Because of HF not there
//( - 1.0 + 1.0 * P("dcij", "cdij") )     *  Fai["mf"]              * Tabij["fdij"]       * Rai["cm"]
//( - 1.0 )     * Labij ["ijcd"] *  Fai["mf"]              * Tabij["fdij"]       * Rai["cm"]
//( + 1.0 )     * Labij ["ijcd"] *  Fai["mf"]              * Tabij["fcij"]       * Rai["dm"]
//( + 1.0 - 1.0 * P("cdij", "cdji") )     *  Fai["mf"]              * Tabij["cdmi"]       * Rai["fj"]
//( + 1.0 )     * Labij ["ijcd"] *  Fai["mf"]              * Tabij["cdmi"]       * Rai["fj"]
//( - 1.0 )     * Labij ["ijcd"] *  Fai["mf"]              * Tabij["cdmj"]       * Rai["fi"]

//( - 1.0 + 1.0 * P("cdji", "cdij") )     *  Tabij["cdmj"]          * Vijka["mnig"]       * Rai["gn"]
( - 1.0 )     * Labij ["ijcd"] *  Tabij["cdmj"]          * Vijka["mnig"]       * Rai["gn"]
( + 1.0 )     * Labij ["ijcd"] *  Tabij["cdmi"]          * Vijka["mnjg"]       * Rai["gn"]

//( + 1.0 - 1.0 * P("dcji", "cdji") - 1.0 * P("dcji", "dcij") + 1.0 * P("dcji", "cdij") ) *  Tabij["ednj"] * Vijka["noie"] * Rai["co"]
( + 1.0 ) * Labij ["ijcd"] *  Tabij["ednj"] * Vijka["noie"] * Rai["co"]
( - 1.0 ) * Labij ["ijcd"] *  Tabij["ecnj"] * Vijka["noie"] * Rai["do"]
( - 1.0 ) * Labij ["ijcd"] *  Tabij["edni"] * Vijka["noje"] * Rai["co"]
( + 1.0 ) * Labij ["ijcd"] *  Tabij["ecnj"] * Vijka["noie"] * Rai["do"]

//( + 0.5 - 0.5 * P("cdij", "cdji") )     *  Tabij["cdmn"]          * Vijka["mnig"]       * Rai["gj"]
( + 0.5 )     * Labij ["ijcd"] *  Tabij["cdmn"]          * Vijka["mnig"]       * Rai["gj"]
( - 0.5 )     * Labij ["ijcd"] *  Tabij["cdmn"]          * Vijka["mnjg"]       * Rai["gi"]

//( + 1.0 - 1.0 * P("cdij", "dcij") )     *  Tabij["ecij"]          * Viabc["ndeg"]       * Rai["gn"]
( + 1.0 )     * Labij ["ijcd"] *  Tabij["ecij"]          * Viabc["ndeg"]       * Rai["gn"]
( - 1.0 )     * Labij ["ijcd"] *  Tabij["edij"]          * Viabc["nceg"]       * Rai["gn"]

//( - 0.5 + 0.5 * P("dcij", "cdij") )     *  Tabij["efij"]          * Viabc["odef"]       * Rai["co"]
( - 0.5 )     * Labij ["ijcd"] *  Tabij["efij"]          * Viabc["odef"]       * Rai["co"]
( + 0.5 )     * Labij ["ijcd"] *  Tabij["efij"]          * Viabc["ocef"]       * Rai["do"]

//( + 1.0 - 1.0 * P("cdij", "dcij") - 1.0 * P("cdij", "cdji") + 1.0 * P("cdij", "dcji") ) *  Tabij["ecni"] * Viabc["ndeg"] * Rai["gj"]
( + 1.0 ) * Labij ["ijcd"] *  Tabij["ecni"] * Viabc["ndeg"] * Rai["gj"]
( - 1.0 ) * Labij ["ijcd"] *  Tabij["edni"] * Viabc["nceg"] * Rai["gj"]
( - 1.0 ) * Labij ["ijcd"] *  Tabij["ecnj"] * Viabc["ndeg"] * Rai["gi"]
( + 1.0 ) * Labij ["ijcd"] *  Tabij["ednj"] * Viabc["nceg"] * Rai["gi"]





// from eomd
// R2
//( - 1.0 + 1.0 * P("cdij", "cdji") ) * Labij ["ijcd"] * Fai["mi"] * Rabij["cdmj"] // m -> cdij
( - 1.0 ) * Labij ["ijcd"] * Fij["mi"] * Rabij["cdmj"] // m -> cdij
( + 1.0 ) * Labij ["ijcd"] * Fij["mj"] * Rabij["cdmi"] // m -> cdij

//( - 1.0 + 1.0 * P("dcij", "cdij") ) * Labij["ijdc"] * Fai["de"] * Rabij["ecij"] // e -> dcij
( - 1.0 ) * Labij["ijdc"] * Fab["de"] * Rabij["ecij"] // e -> dcij
( + 1.0 ) * Labij["ijdc"] * Fab["ce"] * Rabij["edij"] // e -> dcij

//( + 1.0 - 1.0 * P("dcij", "cdij") - 1.0 * P("dcij", "dcji") + 1.0 * P("dcij", "cdji") ) * Labij["ijcd"] * Viajb["mdif"] * Rabij["fcmj"] //mf dcij
( + 1.0 ) * Labij["ijcd"] * Viajb["mdif"] * Rabij["fcmj"] //mf dcij
( - 1.0 ) * Labij["ijcd"] * Viajb["mcif"] * Rabij["fdmj"] //mf dcij
( - 1.0 ) * Labij["ijcd"] * Viajb["mdjf"] * Rabij["fcmi"] //mf dcij
( + 1.0 ) * Labij["ijcd"] * Viajb["mcjf"] * Rabij["fdmi"] //mf dcij

//( + 0.5 - 0.5 * P("dcij", "cdij") ) * Labij["ijcd"] * Tabij["edij"] * Vijab["noeh"] * Rabij["hcno"] // ohne -> cdij
( + 0.5 ) * Labij["ijcd"] * Tabij["edij"] * Vijab["noeh"] * Rabij["hcno"] // ohne -> cdij
( - 0.5 ) * Labij["ijcd"] * Tabij["ecij"] * Vijab["noeh"] * Rabij["hdno"] // ohne -> cdij

//( - 0.5 + 0.5 * P("cdij", "cdji") ) * Labij["ijcd"] * Tabij["cdmi"] * Vijab["mngh"] * Rabij["ghnj"] // mngh -> cdij
( - 0.5 ) * Labij["ijcd"] * Tabij["cdmi"] * Vijab["mngh"] * Rabij["ghnj"] // mngh -> cdij
( + 0.5 ) * Labij["ijcd"] * Tabij["cdmj"] * Vijab["mngh"] * Rabij["ghni"] // mngh -> cdij

//( - 1.0 + 1.0 * P("dcij", "cdij") + 1.0 * P("dcij", "dcji") - 1.0 * P("dcij", "cdji") ) * Labij["ijcd"] * Tabij["edni"] * Vijab["noeh"] * Rabij["hcoj"] // enho -> cdij
( - 1.0 ) * Labij["ijcd"] * Tabij["edni"] * Vijab["noeh"] * Rabij["hcoj"] // enho -> cdij
( + 1.0 ) * Labij["ijcd"] * Tabij["ecni"] * Vijab["noeh"] * Rabij["hdoj"] // enho -> cdij
( + 1.0 ) * Labij["ijcd"] * Tabij["ednj"] * Vijab["noeh"] * Rabij["hcoi"] // enho -> cdij
( - 1.0 ) * Labij["ijcd"] * Tabij["ecnj"] * Vijab["noeh"] * Rabij["hdoi"] // enho -> cdij

//( - 0.5 + 0.5 * P("cdij", "cdji") ) * Labij["ijcd"] * Tabij["efoi"] * Vijab["opef"] * Rabij["cdpj"] // efop -> cdij
( - 0.5 ) * Labij["ijcd"] * Tabij["efoi"] * Vijab["opef"] * Rabij["cdpj"] // efop -> cdij
( + 0.5 ) * Labij["ijcd"] * Tabij["efoj"] * Vijab["opef"] * Rabij["cdpi"] // efop -> cdij

//( + 0.5 - 0.5 * P("dcij", "cdij") ) * Labij["ijcd"] * Tabij["edno"] * Vijab["noeh"] * Rabij["hcij"] // noeh -> cdij
( + 0.5 ) * Labij["ijcd"] * Tabij["edno"] * Vijab["noeh"] * Rabij["hcij"] // noeh -> cdij
( - 0.5 ) * Labij["ijcd"] * Tabij["ecno"] * Vijab["noeh"] * Rabij["hdij"] // noeh -> cdij


( + 0.5 )  * Labij["ijcd"] * Vijkl["mnij"] * Rabij["cdmn"] // mn -> cdij
( + 0.5 )  * Labij["ijcd"] * Vabcd["cdef"] * Rabij["efij"] // ef -> cdij
( + 0.25 ) * Labij["ijcd"] * Tabij["efij"] * Vijab["opef"] * Rabij["cdop"] // efop -> cdij
( + 0.25 ) * Labij["ijcd"] * Tabij["cdmn"] * Vijab["mngh"] * Rabij["ghij"] // mngh -> cdij
