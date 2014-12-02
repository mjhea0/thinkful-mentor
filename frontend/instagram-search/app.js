$(document).ready(function () {
    console.log("dom is ready!");
    $('#map-canvas').hide();
    $('#search').hide();

    $("#location").on("submit", function (event) {
        $('#map-canvas').show();
        initialize();
        $("#location").hide();
        $("#tag").hide();
    });

    $("#tag").on("submit", function (event) {
        $('#search').show();
        $("#location").hide();
        $("#tag").hide();
    });

    //Get lat/long coordinates from location clicked on the map
    function placeMarker(location) {
            var marker = new google.maps.Marker({
            position: location,
            map: map
        });
        LAT = location.k;
        LNG = location.B;
        }
    // Get Location ID from lat/long coordinates
    function getLocation() {
        console.log(LAT, LNG);
        var client_id = '813efa314de94e618290bc8bfcbbb1ac';
        // URL for API request to find locations
        var locationUrl = 'https://api.instagram.com/v1/locations/search?lat='+LAT+'&lng='+LNG+'&distance=5000&client_id='+client_id;
        console.log(locationUrl);

        var result = $.ajax({
            url: locationUrl,
            dataType: "jsonp",
            type: "GET",
        })
        .done(function(result){
            console.log(result);
            //grab first ID from results
            var locationId = result.data[0].id;
            console.log("locationId = " + locationId);
            return locationId
        })
    }
    var map;
    function initialize() {
        var mapCanvas = document.getElementById('map-canvas');
        var mapOptions = {
          center: new google.maps.LatLng(29.300771, -33.574219),
          zoom: 2,
        }
        var map = new google.maps.Map(mapCanvas, mapOptions);

        // Search by location clicked on the map using "getLocation" defined above
        google.maps.event.addListener(map, 'click', function(event) {
            placeMarker(event.latLng);
            var id = getLocation(LAT, LNG);            
            // This only returns "undefined" for "id"....
            
            console.log('id = ' + id);
            var client_id = '813efa314de94e618290bc8bfcbbb1ac';

            function grabImagesByLocation() {  
                $('#results').html('');
                var imagesUrl = 'https://api.instagram.com/v1/locations/'+id+'/media/recent?client_id='+client_id
                console.log(imagesUrl);

                var result = $.ajax({
                    url: imagesUrl,
                    dataType: "jsonp",
                    type: "GET",
                })
                .done(function(result){
                    console.log(result);
                    // Create variable to hold the data and append thumbnails to the DOM
                    for (var i = 0; i < result.data.length; i++) {
                        var photos = result.data[i].images.thumbnail.url;
                        $('#results').append('<img src="'+photos+'" alt="photo" style="border-radius:10%" class="hover">');
                    }

                })
            }
            grabImagesByLocation();
        
        });
    }

        
    google.maps.event.addDomListener(window, 'load', initialize);

    
    // Search by tag event handler
    $("#post-form").on("submit", function (event) {
        console.log("submit working!");
        $('#results').html('');
        $(".search").hide();
        var tag = $('input[name="tag"]').val();
        var count = 20;
        
        console.log(tag);
    
        var client_id = '813efa314de94e618290bc8bfcbbb1ac';
        var access_parameters = {client_id:client_id};
        // Grab images from Instagram API
        function grabImages(access_parameters) {  
            var instagramUrl = 'https://api.instagram.com/v1/tags/' + tag + '/media/recent?callback=?&count='+ count;

            $.getJSON(instagramUrl, access_parameters, onDataLoaded)

        }
        // Load data to the DOM 
        function onDataLoaded(instagram_data) {
            console.log(instagram_data);

            if(instagram_data.meta.code == 200) {
                console.log("Success!");
                // create a variable that holds all returned payload
                for (var i = 0; i < instagram_data.data.length; i++) {
                    var photos = instagram_data.data[i].images.thumbnail.url;
                    console.log(photos);
                    $('#results').append('<img src="'+photos+'" alt="photo" style="border-radius:10%" class="hover">');
                }

                /* Animate images on hover */
                $('.hover').mouseover(function() {
                    $(this).addClass("hover_in");
                    $(this).removeClass("hover_out");
                });

                $('.hover').mouseout(function() {
                    $(this).addClass("hover_out");
                    $(this).removeClass("hover_in");
                });
            }
            else {
                //if errors
                $('#results').append("Hmm.  I couldn’t find anything!");
            }
        }

        grabImages(access_parameters);
          
    });
    
});