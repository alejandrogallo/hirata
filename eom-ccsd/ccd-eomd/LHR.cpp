
// R1
( + 0.5 ) * Lai["ib"] *  Vabij["klie"] * Rabij["ebkl"]  // H21 (kle) -> bi
( + 0.5 ) * Lai["ib"] *  Vabij["kbde"] * Rabij["deki"]  // H21 (dek) -> bi

// R2
( - 1.0 + 1.0 * P("cdij", "cdji") )     *  Fai["mi"]              * Rabij["cdmj"] // m -> cdij
( - 1.0 + 1.0 * P("dcij", "cdij") )     *  Fai["de"]              * Rabij["ecij"] // e -> dcij
( + 0.5 )     *  Vabij["mnij"]          * Rabij["cdmn"] // mn -> cdij
( + 1.0 - 1.0 * P("dcij", "cdij") - 1.0 * P("dcij", "dcji") + 1.0 * P("dcij", "cdji") ) *  Vabij["mdif"] * Rabij["fcmj"] //mf dcij
( + 0.5 )     *  Vabij["cdef"]          * Rabij["efij"] // ef -> cdij
( + 0.5 - 0.5 * P("dcij", "cdij") )     *  Tabij["edij"]          * Vabij["noeh"]       * Rabij["hcno"] // ohne -> cdij
( + 0.25 )    *  Tabij["efij"]          * Vabij["opef"]           * Rabij["cdop"] // efop -> cdij
( - 0.5 + 0.5 * P("cdij", "cdji") )     *  Tabij["cdmi"]          * Vabij["mngh"]       * Rabij["ghnj"] // mngh -> cdij
( - 1.0 + 1.0 * P("dcij", "cdij") + 1.0 * P("dcij", "dcji") - 1.0 * P("dcij", "cdji") ) *  Tabij["edni"] * Vabij["noeh"] * Rabij["hcoj"] // enho -> cdij
( - 0.5 + 0.5 * P("cdij", "cdji") )     *  Tabij["efoi"]          * Vabij["opef"]       * Rabij["cdpj"] // efop -> cdij
( + 0.25 )    *  Tabij["cdmn"]          * Vabij["mngh"]           * Rabij["ghij"] // mngh -> cdij
( + 0.5 - 0.5 * P("dcij", "cdij") )     *  Tabij["edno"]          * Vabij["noeh"]       * Rabij["hcij"] // noeh -> cdij
