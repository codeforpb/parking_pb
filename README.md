parking_pb
==========

Inspiriert von http://codefor.de/projekte/2014-04-19-dd-freieparkplaetze.html

Crawler
-------

Der crawler benutzt [https://scrapy.org](scrapy), um [http://www9.paderborn.de/ParkInfoSPB/ParkInfoSPB/default.aspx](die Seite der Stadt) in eine json-Datei zu konvertieren. Diese wird anschließend im Verzeichnis web_app abgelegt. Es gibt hier zwei Hilfs-Skripte - crawl.sh und crawlAndLog.sh. Letzteres "loggt" die Parkplatzbelegung zusätzlich in eine Datei, deren Name ein Unix-Timestamp ist.

Web App
-------

Zeigt eine osm-Karte an und später darauf die Parkplätze inklusive deren Belegung. Nutzt [http://wiki.openstreetmap.org/wiki/OpenLayers](OpenLayers), [https://code.google.com/p/jquery-csv/](jquery-csv), und [http://code.jquery.com/](jQuery).
