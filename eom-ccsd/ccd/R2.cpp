( - 1.0 + 1.0 * P("dcij", "cdij") )     *  Vabij["mdij"]          * Rai["cm"]
( + 1.0 - 1.0 * P("cdij", "cdji") )     *  Vabij["cdie"]          * Rai["ej"]
( - 1.0 + 1.0 * P("cdij", "cdji") )     *  Fai["mi"]              * Rabij["cdmj"]
( - 1.0 + 1.0 * P("dcij", "cdij") )     *  Fai["de"]              * Rabij["ecij"]
( + 0.5 )     *  Vabij["mnij"]          * Rabij["cdmn"]
( + 1.0 - 1.0 * P("dcij", "cdij") - 1.0 * P("dcij", "dcji") + 1.0 * P("dcij", "cdji") ) *  Vabij["mdif"] * Rabij["fcmj"]
( + 0.5 )     *  Vabij["cdef"]          * Rabij["efij"]
( - 1.0 + 1.0 * P("dcij", "cdij") )     *  Fai["mf"]              * Tabij["fdij"]       * Rai["cm"]
( + 1.0 - 1.0 * P("cdij", "cdji") )     *  Fai["mf"]              * Tabij["cdmi"]       * Rai["fj"]
( - 1.0 + 1.0 * P("cdji", "cdij") )     *  Tabij["cdmj"]          * Vabij["mnig"]       * Rai["gn"]
( + 1.0 - 1.0 * P("dcji", "cdji") - 1.0 * P("dcji", "dcij") + 1.0 * P("dcji", "cdij") ) *  Tabij["ednj"] * Vabij["noie"] * Rai["co"]
( + 0.5 - 0.5 * P("cdij", "cdji") )     *  Tabij["cdmn"]          * Vabij["mnig"]       * Rai["gj"]
( + 1.0 - 1.0 * P("cdij", "dcij") )     *  Tabij["ecij"]          * Vabij["ndeg"]       * Rai["gn"]
( - 0.5 + 0.5 * P("dcij", "cdij") )     *  Tabij["efij"]          * Vabij["odef"]       * Rai["co"]
( + 1.0 - 1.0 * P("cdij", "dcij") - 1.0 * P("cdij", "cdji") + 1.0 * P("cdij", "dcji") ) *  Tabij["ecni"] * Vabij["ndeg"] * Rai["gj"]
( + 0.5 - 0.5 * P("dcij", "cdij") )     *  Tabij["edij"]          * Vabij["noeh"]       * Rabij["hcno"]
( + 0.25 )    *  Tabij["efij"]          * Vabij["opef"]           * Rabij["cdop"]
( - 0.5 + 0.5 * P("cdij", "cdji") )     *  Tabij["cdmi"]          * Vabij["mngh"]       * Rabij["ghnj"]
( - 1.0 + 1.0 * P("dcij", "cdij") + 1.0 * P("dcij", "dcji") - 1.0 * P("dcij", "cdji") ) *  Tabij["edni"] * Vabij["noeh"] * Rabij["hcoj"]
( - 0.5 + 0.5 * P("cdij", "cdji") )     *  Tabij["efoi"]          * Vabij["opef"]       * Rabij["cdpj"]
( + 0.25 )    *  Tabij["cdmn"]          * Vabij["mngh"]           * Rabij["ghij"]
( + 0.5 - 0.5 * P("dcij", "cdij") )     *  Tabij["edno"]          * Vabij["noeh"]       * Rabij["hcij"]