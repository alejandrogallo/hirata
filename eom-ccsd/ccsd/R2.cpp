( - 1.0 + 1.0 * P("dcij", "cdij") )     *  Viajk["mdij"]          * Rai["cm"]
( + 1.0 - 1.0 * P("cdij", "cdji") )     *  Vabic["cdie"]          * Rai["ej"]
( - 1.0 + 1.0 * P("cdij", "cdji") )     *  Fij["mi"]              * Rabij["cdmj"]
( - 1.0 + 1.0 * P("dcij", "cdij") )     *  Fab["de"]              * Rabij["ecij"]
( + 0.5 )     *  Vijkl["mnij"]          * Rabij["cdmn"]
( + 1.0 - 1.0 * P("dcij", "cdij") - 1.0 * P("dcij", "dcji") + 1.0 * P("dcij", "cdji") ) *  Viajb["mdif"] * Rabij["fcmj"]
( + 0.5 )     *  Vabcd["cdef"]          * Rabij["efij"]
( - 1.0 + 1.0 * P("dcij", "cdij") )     *  Tai["dm"]              * Vijkl["mnij"]       * Rai["cn"]
( - 1.0 + 1.0 * P("dcji", "cdji") + 1.0 * P("dcji", "dcij") - 1.0 * P("dcji", "cdij") ) *  Tai["ej"]     * Viajb["ndie"] * Rai["cn"]
( - 1.0 + 1.0 * P("cdij", "dcij") + 1.0 * P("cdij", "cdji") - 1.0 * P("cdij", "dcji") ) *  Tai["cm"]     * Viajb["mdif"] * Rai["fj"]
( + 1.0 - 1.0 * P("cdij", "cdji") )     *  Tai["ei"]              * Vabcd["cdef"]       * Rai["fj"]
( + 0.5 - 0.5 * P("cdji", "cdij") )     *  Tai["ej"]              * Vijka["noie"]       * Rabij["cdno"]
( + 1.0 - 1.0 * P("dcij", "cdij") - 1.0 * P("dcij", "dcji") + 1.0 * P("dcij", "cdji") ) *  Tai["dm"]     * Vijka["mnig"] * Rabij["gcnj"]
( + 1.0 - 1.0 * P("cdij", "cdji") )     *  Tai["en"]              * Vijka["noie"]       * Rabij["cdoj"]
( + 1.0 - 1.0 * P("dcij", "cdij") - 1.0 * P("dcij", "dcji") + 1.0 * P("dcij", "cdji") ) *  Tai["ei"]     * Viabc["ndeg"] * Rabij["gcnj"]
( - 0.5 + 0.5 * P("cdij", "dcij") )     *  Tai["cm"]              * Viabc["mdfg"]       * Rabij["fgij"]
( - 1.0 + 1.0 * P("dcij", "cdij") )     *  Tai["en"]              * Viabc["ndeg"]       * Rabij["gcij"]
( - 1.0 + 1.0 * P("cdji", "cdij") )     *  Tabij["cdmj"]          * Vijka["mnig"]       * Rai["gn"]
( + 1.0 - 1.0 * P("dcji", "cdji") - 1.0 * P("dcji", "dcij") + 1.0 * P("dcji", "cdij") ) *  Tabij["ednj"] * Vijka["noie"] * Rai["co"]
( + 0.5 - 0.5 * P("cdij", "cdji") )     *  Tabij["cdmn"]          * Vijka["mnig"]       * Rai["gj"]
( + 1.0 - 1.0 * P("cdij", "dcij") )     *  Tabij["ecij"]          * Viabc["ndeg"]       * Rai["gn"]
( - 0.5 + 0.5 * P("dcij", "cdij") )     *  Tabij["efij"]          * Viabc["odef"]       * Rai["co"]
( + 1.0 - 1.0 * P("cdij", "dcij") - 1.0 * P("cdij", "cdji") + 1.0 * P("cdij", "dcji") ) *  Tabij["ecni"] * Viabc["ndeg"] * Rai["gj"]
( + 0.5 - 0.5 * P("dcij", "cdij") )     *  Tabij["edij"]          * Vijab["noeh"]       * Rabij["hcno"]
( + 0.25 )    *  Tabij["efij"]          * Vijab["opef"]           * Rabij["cdop"]
( - 0.5 + 0.5 * P("cdij", "cdji") )     *  Tabij["cdmi"]          * Vijab["mngh"]       * Rabij["ghnj"]
( - 1.0 + 1.0 * P("dcij", "cdij") + 1.0 * P("dcij", "dcji") - 1.0 * P("dcij", "cdji") ) *  Tabij["edni"] * Vijab["noeh"] * Rabij["hcoj"]
( - 0.5 + 0.5 * P("cdij", "cdji") )     *  Tabij["efoi"]          * Vijab["opef"]       * Rabij["cdpj"]
( + 0.25 )    *  Tabij["cdmn"]          * Vijab["mngh"]           * Rabij["ghij"]
( + 0.5 - 0.5 * P("dcij", "cdij") )     *  Tabij["edno"]          * Vijab["noeh"]       * Rabij["hcij"]
( - 1.0 + 1.0 * P("dcji", "cdji") + 1.0 * P("dcji", "dcij") - 1.0 * P("dcji", "cdij") ) *  Tai["ej"]     * Tai["dn"]     * Vijka["noie"] * Rai["co"]
( + 1.0 - 1.0 * P("cdij", "cdji") )     *  Tai["cm"]              * Tai["dn"]           * Vijka["mnig"]  * Rai["gj"]
( - 1.0 + 1.0 * P("dcij", "cdij") )     *  Tai["ei"]              * Tai["fj"]           * Viabc["odef"]  * Rai["co"]
( - 1.0 + 1.0 * P("cdij", "dcij") + 1.0 * P("cdij", "cdji") - 1.0 * P("cdij", "dcji") ) *  Tai["ei"]     * Tai["cn"]     * Viabc["ndeg"] * Rai["gj"]
( + 0.5 )     *  Tai["ei"]              * Tai["fj"]               * Vijab["opef"]       * Rabij["cdop"]
( + 1.0 - 1.0 * P("dcij", "cdij") - 1.0 * P("dcij", "dcji") + 1.0 * P("dcij", "cdji") ) *  Tai["ei"]     * Tai["dn"]     * Vijab["noeh"] * Rabij["hcoj"]
( + 1.0 - 1.0 * P("cdij", "cdji") )     *  Tai["ei"]              * Tai["fo"]           * Vijab["opef"]  * Rabij["cdpj"]
( + 0.5 )     *  Tai["cm"]              * Tai["dn"]               * Vijab["mngh"]       * Rabij["ghij"]
( - 1.0 + 1.0 * P("dcij", "cdij") )     *  Tai["dm"]              * Tai["fo"]           * Vijab["mofh"]  * Rabij["hcij"]
( - 1.0 + 1.0 * P("cdji", "cdij") )     *  Tabij["cdmj"]          * Tai["fi"]           * Vijab["mofh"]  * Rai["ho"]
( - 1.0 + 1.0 * P("dcji", "cdji") + 1.0 * P("dcji", "dcij") - 1.0 * P("dcji", "cdij") ) *  Tabij["ednj"] * Tai["gi"]     * Vijab["npeg"] * Rai["cp"]
( + 0.5 - 0.5 * P("cdij", "cdji") )     *  Tabij["cdmn"]          * Tai["gi"]           * Vijab["mngh"]  * Rai["hj"]
( + 1.0 - 1.0 * P("cdij", "dcij") )     *  Tabij["ecij"]          * Tai["dn"]           * Vijab["noeh"]  * Rai["ho"]
( - 0.5 + 0.5 * P("dcij", "cdij") )     *  Tabij["efij"]          * Tai["do"]           * Vijab["opef"]  * Rai["cp"]
( + 1.0 - 1.0 * P("dcij", "cdij") )     *  Tabij["edij"]          * Tai["fo"]           * Vijab["opef"]  * Rai["cp"]
( - 1.0 + 1.0 * P("cdij", "dcij") + 1.0 * P("cdij", "cdji") - 1.0 * P("cdij", "dcji") ) *  Tabij["ecni"] * Tai["do"]     * Vijab["noeh"] * Rai["hj"]
( - 1.0 + 1.0 * P("cdij", "cdji") )     *  Tabij["cdmi"]          * Tai["fo"]           * Vijab["mofh"]  * Rai["hj"]
( - 1.0 + 1.0 * P("dcij", "cdij") )     *  Tai["ei"]              * Tai["fj"]           * Tai["do"]      * Vijab["opef"] * Rai["cp"]
( + 1.0 - 1.0 * P("cdij", "cdji") )     *  Tai["ei"]              * Tai["cn"]           * Tai["do"]      * Vijab["noeh"] * Rai["hj"]
