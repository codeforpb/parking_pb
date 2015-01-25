        var map, select, markers;
        var projection = new OpenLayers.Projection("EPSG:4326");

        var styleMap = new OpenLayers.StyleMap({'default':{
                    pointerEvents: "visiblePainted",
                    externalGraphic: "img/parking_lot_marker_${bg}.png",
                    graphicWidth: 64,
                    graphicHeight: 18,
                    label : '${free}/${count}',
                    fontColor: '#000',
                    fontSize: "12px",
                    fontFamily: "Courier New, monospace",
                    fontWeight: "bold"
                }});

        function init(){
            var options = {
                projection: new OpenLayers.Projection("EPSG:900913"),
                displayProjection: new OpenLayers.Projection("EPSG:4326")
            };
            map = new OpenLayers.Map('map', options);
            var mapnik = new OpenLayers.Layer.OSM("OpenStreetMap (Mapnik)");
            map.addLayer(mapnik);
 
            var lonLat = transformCoordinates(8.75456929206848, 51.71960448493701);
            map.setCenter(lonLat, 15);

            loadParkingData(map,mapnik);
        }

        function transformCoordinates(lon, lat){
            var projectionObj =  map.getProjectionObject();
            return new OpenLayers.LonLat(lon, lat)
                                 .transform(projection, projectionObj);
        }

        function loadParkingData(map,mapnik){
            var xhr = new XMLHttpRequest();




            xhr.onreadystatechange = function()
            {
                if (xhr.readyState== 4 && xhr.status == 200){
                    showParkingData(xhr.responseText);
                }
            }
            xhr.open("GET", "newest.json", true);
            xhr.send(null);
        }

        function showParkingData(responseText){
            var renderer = OpenLayers.Util.getParameters(window.location.href).renderer;
            renderer = (renderer) ? [renderer] : OpenLayers.Layer.Vector.prototype.renderers;

            var vectorLayer = new OpenLayers.Layer.Vector("Parkplätze", {
                styleMap: styleMap,
                renderers: renderer
            });

            var array = JSON.parse(responseText);
            var size = new OpenLayers.Size(50,18);
            var offset = new OpenLayers.Pixel(-(size.w/2), -size.h);
 
            map.addControl(new OpenLayers.Control.LayerSwitcher());

            for (var i = 0; i < array.length; i++) {
                var parkingLot = array[i];
                addParkingLotToMap(vectorLayer, parkingLot);
            }

            map.addLayer(vectorLayer);
        }

       function addParkingLotToMap(vectorLayer, parkingLot){
             var free = parkingLot.free;
             var count = parkingLot.count;
             var projectionObj =  map.getProjectionObject();

             var point = new OpenLayers.Geometry.Point(parkingLot.lon, parkingLot.lat).transform(projection,projectionObj);
             var pointFeature = new OpenLayers.Feature.Vector(point);
             pointFeature.attributes = {
                name: parkingLot.name,
                free: parkingLot.free,
                count: parkingLot.count,
                bg: getColor(free, count)
            };
            vectorLayer.addFeatures([pointFeature]);
       }

        function getColor(free, count){
            if(free == '?'){
                return 'white'; 
            }

            var freeRatio = free/count;                 
            if (freeRatio < 0.25) {
                return 'red';
            }
            else if (freeRatio < 0.75) {
                return 'yellow';
            }
            else {
                return 'green';
            }
        }
