$(document).ready(function () {
    console.log("dom is ready!");
    $('#map').hide();
    $('.retry').hide();
    $('#search').hide();


    //Initialize Google Maps canvas when "location" button is clicked
    $("#location").on("submit", function (event) {
        $('#map').show();
        initialize();
        $("#home").hide();
    });

    // Search by tag if "tag" button is clicked
    $("#tag").on("submit", function (event) {
        $('#search').show();
        $("#home").hide();
    });

    // Animate images on hover once results are displayed
    function hoverAnimations() {
        $('.hover').mouseover(function() {
            $(this).addClass("hover_in");
            $(this).removeClass("hover_out");
        });

        $('.hover').mouseout(function() {
            $(this).addClass("hover_out");
            $(this).removeClass("hover_in");
        });
    }

    // Get lat/long coordinates from location clicked on the map
    function placeMarker(location) {
            var marker = new google.maps.Marker({
            position: location,
            map: map
        });
        LAT = location.k;
        LNG = location.B;
    }

    // Get Images from Media endpoint by lat/long
    function getImages(LAT, LNG) {
        $('.retry').show();;
        console.log(LAT, LNG);
        var client_id = '813efa314de94e618290bc8bfcbbb1ac';
        // URL for API request to find recent media by location
        var imagesUrl = 'https://api.instagram.com/v1/media/search?lat='+LAT+'&lng='+LNG+'&distance=5000&client_id='+client_id;
        console.log(imagesUrl);

        var result = $.ajax({
            url: imagesUrl,
            dataType: "jsonp",
            type: "GET",
        })
        .done(function(result){
            console.log(result);
            $('#results').html('');
            if (result.data.length > 0) {
                for (var i = 0; i < result.data.length; i++) {
                var photos = result.data[i].images.thumbnail.url;
                $('#results').append('<img src="'+photos+'" alt="photo" style="border-radius:10%" class="hover">');
                hoverAnimations();
                }
            }
            else {
                $('#results').append("Hmm.  I couldn’t find anything!");
            }

        });
    }

    // Initializing Google Maps Canvas/Function
    var map;
    var markers = [];
    // Adding markers to the maps
    function setAllMap(map) {
      for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
      }
    }
    function initialize() {
        var mapCanvas = document.getElementById('map-canvas');
        var mapOptions = {
          center: new google.maps.LatLng(29.300771, -33.574219),
          zoom: 2,
        }
        var map = new google.maps.Map(mapCanvas, mapOptions);
        google.maps.event.addListener(map, 'click', function(event) {
            // Clear markers on click
            setAllMap(null);
            var LAT = event.latLng.lat();
            var LNG = event.latLng.lng();
            placeMarker(event.latLng);
            getImages(LAT, LNG);

            var point = new google.maps.LatLng(LAT, LNG);
            var marker = new google.maps.Marker({
                position: point,
                map: map,
                zoom: 4,
              });
            // Add new marker to array
            markers.push(marker);
            // Zoom into location clicked
            map.setZoom(4);
            map.setCenter(marker.getPosition());
            // Zoom in further if marker is clicked
            google.maps.event.addListener(marker, 'click', function() {
                map.setZoom(8);
                map.setCenter(marker.getPosition());
              });

        });
    }

    google.maps.event.addDomListener(window, 'load', initialize);

     // Search by tag event handler
    $("#post-form").on("submit", function (event) {
        console.log("submit working!");
          console.log($('.carousel').hasClass('slick-initialized'));
          if($('.carousel').hasClass('slick-initialized')) {
           $('.carousel').slick('unslick');
           $('.carousel').empty();
          }

        $('.retry').show();
        input = $('input[name="tag"]').val();
        var tag = input.replace(/\s+/g, '');
        console.log(tag);
        var count = 20;

        var client_id = '813efa314de94e618290bc8bfcbbb1ac';
        var access_parameters = {client_id:client_id};
        // Grab images from Instagram API
        function grabImages(access_parameters) {
            var instagramUrl = 'https://api.instagram.com/v1/tags/' + tag + '/media/recent?callback=?&count='+ count;
            $.getJSON(instagramUrl, access_parameters, onDataLoaded);

        }
        // Load data to the DOM
        function onDataLoaded(instagram_data) {
            // console.log(instagram_data);

            if (instagram_data.data.length > 0) {

                // create a variable that holds all returned payload
                for (var i = 0; i < instagram_data.data.length; i++) {
                    var photos = instagram_data.data[i].images.thumbnail.url;
                    $('.carousel').append('<div><img src="'+photos+'" alt="photo" style="border-radius:10%" class="hover"><div>');
                    hoverAnimations();
                }
                $('.carousel').slick({
                        infinite: true,
                        speed: 300,
                        slidesToShow: 5,
                        slidesToScroll: 5,
                        autoplay: true,
                        autoplaySpeed: 2000,
                        arrows: true,
                    });
            }
            else {
                //if errors
                $('#results').append("Hmm.  I couldn’t find anything!");
            }
        }

        grabImages(access_parameters);

    });

    $(".retry").on("click", function (event) {
        location.reload();
    });

});