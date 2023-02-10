# coding=UTF-8

"""
ogr2osm translation rules for Sondrio address data

Copyright (C) 2022 Andrea Musuruane <musuruan@gmail.com>

The data are availble under the CC-BY 4.0 license with an ODbL addendum:
https://wikimediaitalia.nws.netways.de/index.php/s/HZ2P6KSMF2mf94X

Spatial Reference: EPSG:32632 (WGS 84 / UTM zone 32N)

Requires ogr2osm v1.0.0:
https://github.com/roelderickx/ogr2osm

Run with:
ogr2osm -e 32632 -t civici.py -f Civici_OSM.shp
"""

import ogr2osm

class TranslateCivici(ogr2osm.TranslationBase):

    def filter_tags(self, attrs):
        if not attrs:
            return

        tags = {}

        tags["addr:housenumber"] = attrs["CIVICO"].lower()
        tags["addr:street"] = attrs["NOME_VIA"]
        tags["addr:postcode"] = attrs["CAP"]
        tags["addr:city"]= attrs["NOME_COM"]

        if attrs["CIVICO_OLD"] != "" and attrs["NOMEVIAOLD"] != "":
            tags["old_addr:housenumber"] = attrs["CIVICO_OLD"]
            tags["old_addr:place"] = attrs["NOMEVIAOLD"]

        return tags
 	
