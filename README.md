Parken in Paderborn
==========

Inspiriert wurde dieses Projekt von http://codefor.de/projekte/2014-04-19-dd-freieparkplaetze.html - Parking PB zeigt diese App eine maximal 15 Minuten alte Belegung der Parkplätze in Paderborn an. Die Stadt selbst die geöffneten Parkplätze nur in einer Tabelle [0], nicht jedoch auf einer Karte. Es gibt eine von der Parkplatzanzeige erreichbare Karte -- diese ist jedoch nicht zoombar und zeigt auch nicht alle Parkplätze an. 

Diese Probleme wurden mit Parking PB gelöst: die aktuelle Belegung der Parkplätze wird direkt auf einer Karte angezeigt, die beliebig gezoomt werden kann. 

Ein weiteres Ziel, an dem gearbeitet wird, ist die Sammlung "historischer Parkplatzdaten". Diese Daten könnten genutzt werden, um Parkplatzbelegungen im Voraus zu schätzen und ggf. für Navigationssysteme zu nutzen.

Um dies alles zu bewerkstelligen, werden ca. alle 15 Minuten die Daten von den Seiten Stadt geparst und gecachet. Da nicht bekannt ist, wie oft die Daten der Stadt aktualisiert werden, wurde erst ein relativ großes Parsing-Intervall gewählt. Zum Parsen wird scrapy genutzt [1]. Die Daten werden hierbei als csv und als json exportiert und über die Web-Anwendung verfügbar gemacht. 

Die Web-Anwendung selbst besteht ausschließlich aus einer Karte, die dynamisch die aktuelle Belegung nachlädt und anzeigt. Es ist jedoch möglich, die Rohdaten über Direktlinks zu bekommen:

 * Web-Anwendung: http://parking_pb.gigantic.io/
 * Aktuelle Belegung: http://parking_pb.gigantic.io/newest.json
 * Historische Daten, buggy: http://parking_pb.gigantic.io/history.csv

[0] http://www.paderborn.de/microsite/asp/parken_in_der_city/freie_Parkplaetze.php?p=4,1
[1] https://scrapy.org

Technisches
-----------

Um die App auf einem Server zu hosten ist eine Installation von [scrapy](https://scrapy.org) notwendig, damit regelmäßig neue Daten geholt werden können. Die Web-App selbst wurde mit jekyll erstellt, damit diese lokal getestet werden kann. Sie ist jedoch von jekyll-Funktionen (templating, etc.) unabhängig.

Die aufbereiteten Rohdaten sind über http://parking_pb.gigantic.io/newest.json (aktuellste Belegung als json) und http://parking_pb.gigantic.io/history.csv ("Belegungslog") abrufbar.

Crawler
-------

Der crawler benutzt [scrapy](https://scrapy.org), um [die Seite der Stadt](http://www9.paderborn.de/ParkInfoSPB/ParkInfoSPB/default.aspx) in eine json-Datei zu konvertieren. Diese wird anschließend im Verzeichnis web_app abgelegt. Es gibt hier zwei Hilfs-Skripte - crawl.sh und crawlAndLog.sh. Letzteres "loggt" die Parkplatzbelegung zusätzlich in eine Datei, deren Name ein Unix-Timestamp ist.

Web App
-------

Zeigt eine osm-Karte an und später darauf die Parkplätze inklusive deren Belegung. Nutzt [OpenLayers](http://wiki.openstreetmap.org/wiki/OpenLayers), [jquery-csv](https://code.google.com/p/jquery-csv/), und [jQuery](http://code.jquery.com/).
