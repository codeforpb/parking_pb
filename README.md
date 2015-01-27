Parken in Paderborn
==========

Inspiriert von http://codefor.de/projekte/2014-04-19-dd-freieparkplaetze.html

Um die App auf einem Server zu hosten ist eine Installation von [scrapy](https://scrapy.org) notwendig, damit regelmäßig neue Daten geholt werden können. Die Web-App selbst wurde mit jekyll erstellt, damit diese lokal getestet werden kann. Sie ist jedoch von jekyll-Funktionen (templating, etc.) unabhängig.

Die aufbereiteten Rohdaten sind über http://parking_pb.gigantic.io/newest.json (aktuellste Belegung als json) und http://parking_pb.gigantic.io/history.csv ("Belegungslog") abrufbar.

Crawler
-------

Der crawler benutzt [scrapy](https://scrapy.org), um [die Seite der Stadt](http://www9.paderborn.de/ParkInfoSPB/ParkInfoSPB/default.aspx) in eine json-Datei zu konvertieren. Diese wird anschließend im Verzeichnis web_app abgelegt. Es gibt hier zwei Hilfs-Skripte - crawl.sh und crawlAndLog.sh. Letzteres "loggt" die Parkplatzbelegung zusätzlich in eine Datei, deren Name ein Unix-Timestamp ist.

Web App
-------

Zeigt eine osm-Karte an und später darauf die Parkplätze inklusive deren Belegung. Nutzt [OpenLayers](http://wiki.openstreetmap.org/wiki/OpenLayers), [jquery-csv](https://code.google.com/p/jquery-csv/), und [jQuery](http://code.jquery.com/).
