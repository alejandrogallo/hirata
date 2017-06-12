( - 1.0 + 1.0 * P("klab", "lkab") )     *  Fai["km"]              * Labij["mlab"] // H22 (m) -> klab
( - 1.0 + 1.0 * P("klba", "klab") )     *  Fai["eb"]              * Labij["klea"] // H22 (e) -> klba
( - 0.5 )     *  Vabij["klmn"]          * Labij["nmab"] // H22 (mn) -> klab
( + 1.0 - 1.0 * P("klba", "klab") - 1.0 * P("klba", "lkba") + 1.0 * P("klba", "lkab") ) *  Vabij["kenb"] * Labij["nlea"] // H22 ne -> kbla
( - 0.5 )     *  Vabij["efab"]          * Labij["klfe"] // H22 ef -> abkl
( + 0.5 - 0.5 * P("klba", "klab") )     *  Tabij["efop"]          * Vabij["klfb"]       * Labij["poea"] // H22 efop -> klba
( - 0.25 )    *  Tabij["efop"]          * Vabij["klef"]           * Labij["poab"] // H22 
( - 0.5 + 0.5 * P("klab", "lkab") )     *  Tabij["efop"]          * Vabij["pkab"]       * Labij["olfe"]
( - 1.0 + 1.0 * P("klba", "klab") + 1.0 * P("klba", "lkba") - 1.0 * P("klba", "lkab") ) *  Tabij["efop"] * Vabij["pkfb"] * Labij["olea"]
( + 0.5 - 0.5 * P("klab", "lkab") )     *  Tabij["efop"]          * Vabij["pkef"]       * Labij["olab"]
( - 0.25 )    *  Tabij["efop"]          * Vabij["opab"]           * Labij["klfe"]
( - 0.5 + 0.5 * P("klba", "klab") )     *  Tabij["efop"]          * Vabij["opfb"]       * Labij["klea"]
