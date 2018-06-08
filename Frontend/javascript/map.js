var map; //Will contain map object.
var marker = false; ////Has the user plotted their location marker? 
        
//Function called to initialize / create the map.
//This is called when the page has loaded.



function initMap() {
 
    //The center location of our map.
    var centerOfMap = new google.maps.LatLng(lat, lng);
    var styles = [
        {
            featureType: 'water',
            elementType: 'geometry',
            stylers: [
                { hue: '#6699ff' },
                { saturation: 100 },
                { lightness: 8 },
                { visibility: 'on' }
            ]
        },{
            featureType: 'landscape',
            elementType: 'geometry',
            stylers: [
                { hue: '#44ff88' },
                { saturation: 100 },
                { lightness: -19 },
                { visibility: 'simplified' }
            ]
        },{
            featureType: 'poi',
            elementType: 'labels',
            stylers: [
                { hue: '#aaaacc' },
                { saturation: -42 },
                { lightness: -6 },
                { visibility: 'on' }
            ]
        },{
            featureType: 'road',
            elementType: 'geometry',
            stylers: [
                { hue: '#666666' },
                { saturation: -100 },
                { lightness: 50 },
                { visibility: 'simplified' }
            ]
        },{
            featureType: 'road',
            elementType: 'labels',
            stylers: [
                { hue: '#777777' },
                { saturation: -100 },
                { lightness: -27 },
                { visibility: 'simplified' }
            ]
        }
    ];
    //Map options.
    var options = {
      mapTypeControlOptions: {
         mapTypeIds: [ 'Styled']
      },
      center: centerOfMap, //Set center.
      zoom: 16, //The zoom value.
      mapTypeId: 'Styled',
    };

    //Create the map object.
    var div = document.getElementById('map');
    var map = new google.maps.Map(div, options);
    var styledMapType = new google.maps.StyledMapType(styles, { name: 'Styled' });
    map.mapTypes.set('Styled', styledMapType);
 
    if(marker === false){
        //Create the marker.
        marker = new google.maps.Marker({
            position: centerOfMap,
            map: map,
            draggable: true //make it draggable
        });
        //Listen for drag events!
        google.maps.event.addListener(marker, 'dragend', function(event){
            markerLocation();
        });
    }
    //Listen for any clicks on the map.
    google.maps.event.addListener(map, 'click', function(event) {                
        //Get the location that the user clicked.
        var clickedLocation = event.latLng;
        //If the marker hasn't been added.
        if(marker === false){
            //Create the marker.
            marker = new google.maps.Marker({
                position: clickedLocation,
                map: map,
                draggable: true //make it draggable
            });
            //Listen for drag events!
            google.maps.event.addListener(marker, 'dragend', function(event){
                markerLocation();
            });
        } else{
            //Marker has already been added, so just change its location.
            marker.setPosition(clickedLocation);
        }
        //Get the marker's location.
        markerLocation();
    });
}
        
//This function will get the marker's current location and then add the lat/long
//values to our textfields so that we can save the location.
function markerLocation(){
    //Get location.
    var currentLocation = marker.getPosition();
    //Add lat and lng values to a field that we can save.
    document.getElementById('lat').value = currentLocation.lat(); //latitude
    document.getElementById('lng').value = currentLocation.lng(); //longitude

    console.log(currentLocation.lat()); //latitude
    console.log(currentLocation.lng()); //longitude
    
}
        
        
//Load the map when the page has finished loading.
google.maps.event.addDomListener(window, 'load', initMap);