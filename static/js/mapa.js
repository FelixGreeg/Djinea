function salida_capas(map, options) {
    var openmaps = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}{r}.png', {
        attribution: '© OpenStreetMap contributors',
        fullscreenControl: true,
        fullscreenControlOptions: {
            position: 'topleft'
        }
    }).addTo(map);

    var edomexshp = new L.GeoJSON.AJAX("{% url 'edomex' %}", {
        style: function colors(feature) {
            switch (feature.properties.nomgeo) {
                case 'Aculco':
                    return {
                        color: 'orange',
                        fillOpacity: 0.3
                    };
                    break;
                case 'Zumpango':
                    return {
                        color: 'green',
                        fillOpacity: 0.3
                    };
                    break;
                case 'Metepec':
                    return {
                        color: 'yellow',
                        fillOpacity: 0.3
                    };
                    break;

            };
        },
        onEachFeature: function (feature, layer) {
            layer.bindPopup(feature.properties.nomgeo.toString());
        }

    });

    var geojsonFeatureIcon = [{
        "type": "Feature",
        "properties": {
            "simbologia": "L.icon"
        },
        "geometry": {
            "type": "Point"
        }
    }
    ];

    var greenIcon = L.icon({
        iconUrl: "static/img/esc.png",
        iconSize: [30, 40],
        iconAnchor: [15, 40],
        shadowSize: [35, 50],
        shadowAnchor: [0, 55],
        //popupAnchor: [0, -40]
    });


    function estiloIcon(feature, latlng) {
        return L.marker(latlng, {
            icon: greenIcon
        })
    };

    var puntos = new L.GeoJSON.AJAX("{% url 'unidades' %}", {

        onEachFeature: function (feature, layer) {
            layer.bindPopup('<h3><img src="static/img/icono.png "> Unidad Operativa</h3> <hr>' + feature.properties.Tipo_Unidad_Operativa + '<br/>' + feature.properties.Nombre_Unidad_Operativa + '<br/>' + feature.properties.Domicilio.toString());
        },
        pointToLayer: estiloIcon
    });

    edomexshp.addTo(map);
    puntos.addTo(map);

    var baseLayers = {
        "OpenStreetMap": openmaps
    }

    var groupedOverlays = {
        "Capas": {
            "Municipios": edomexshp,
            "Unidades": puntos
        }
    };

    L.control.groupedLayers(baseLayers, groupedOverlays, {
        collapsed: true,
        position: 'topright'
    }).addTo(map);

    var Icono = L.icon({
        iconUrl: "static/img/ruta.png",
        iconSize: [30, 40],
        iconAnchor: [15, 40],
        shadowSize: [35, 50],
        shadowAnchor: [0, 55],
        popupAnchor: [0, -40]
    });

    var ruta = L.Routing.control({
        waypoints: [
            inicio = L.latLng(19.286548, -99.676456),
            fin = L.latLng(19.685383, -99.128567)
        ],
        language: 'es',
        routeWhileDragging: true,
        show: false,
        geocoder: L.Control.Geocoder.nominatim(),
        createMarker: function (i, inicio, n) {
            return L.marker(inicio.latLng, {
                draggable: true,
                bounceOnAdd: false,
                opacity: 0.9,
                icon: Icono,
                bounceOnAddOptions: {
                    duration: 2000,
                    height: 800,
                    function() {
                        (bindPopup(myPopup).openOn(map))
                    }
                }
            }).bindPopup('Selecciona la ruta' + "   " + i);
        }

    }).addTo(map)


    var itineraryShown = false;
    var controlContainer = ruta.getContainer();
    var legendClickArea = document.createElement("DIV");
    legendClickArea.classList.add('legendClickArea');
    controlContainer.appendChild(legendClickArea);
    legendClickArea.onclick = function () {
        if (itineraryShown)
            ruta.hide();
        else {
            ruta.show();
        }
        itineraryShown = !itineraryShown;
    };

    L.control.locate().addTo(map);

     L.control.fullscreen({
        position: 'topleft', 
        title: 'Pantalla completa', 
        titleCancel: 'Salir pantalla completa', 
        content: null, 
        forceSeparateButton: true, 
        forcePseudoFullscreen: true, 
        fullscreenElement: false 
    }).addTo(map);
    map.on('enterFullscreen', function () {
        console.log('entered fullscreen');
    });
    map.on('exitFullscreen', function () {
        console.log('exited fullscreen');
    });
    map.toggleFullScreen();

}