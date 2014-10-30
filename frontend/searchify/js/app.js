$(document).ready(function() {

  // random background image
  (function($) {
      $.rand = function(arg) {
          if ($.isArray(arg)) {
              return arg[$.rand(arg.length)];
          } else if (typeof arg == "number") {
              return Math.floor(Math.random() * arg);
          } else {
              return 4;
          }
      };
  })(jQuery);

  var image = ['party0', 'party1', 'party2', 'party3', 'party4', 'party5', 'party6'];

  $('body').css('background-image', 'url(images/' + $.rand(image) + '.jpg)');

  // identifying the buttons, searchboxes, and other elements
  var askUser = $('#ask-user');
  var buttonsContainer = $('#buttons-container');
  var artistButton = $('#artist-button');
  var albumButton = $('#album-button');
  var trackButton = $('#track-button');
  var searchContainer = $('#search-container');
  var artistSearch = $('#artist-search');
  var albumSearch = $('#album-search');
  var trackSearch = $('#track-search');
  var artistMic = $('#artist-mic');
  var albumMic = $('#album-mic');
  var trackMic = $('#track-mic');
  var allMics = $('.all-mics');
  var micImage = $('.all-mics img');
  var closeButton = $('#close');
  var resultBackground = $('.result-background');
  var resultContent = $('.result-content');
  var keys = {
    enter: 13
  };

  //ajax request for searching artist
  function searchArtist() {
    var usersArtist = $(artistSearch).val();

    $.ajax({
      url: 'https://api.spotify.com/v1/search',
      data: {
        q: usersArtist,
        type: 'artist'
      },
      success: function(data) {
        console.log('success', data);
        for(secondCounter in data.artists.items) {
          var artist = data.artists.items[secondCounter]
            $('.results').append('<div class="result-background"><div class="result-content">' +
              '<img src="' + artist.images[0].url + '" onload="this.width/=2;this.onload=null;"><span>' +
              artist.name + '</span></div></div>');

            //clicking on an artist returns albums from that artist
            var artistAlbums = function() {
              var artistId = artist.id;
              console.log(artistId)
              $.ajax({
                url: 'https://api.spotify.com/v1/artists/' + artistId + '/albums',
                success: function(data) {
                  console.log('success', data);
                  for(thirdCounter in data.items) {
                    var album = data.items[thirdCounter];
                    $('.results').append('<div class="result-background"><div class="result-content">' +
                      '<img src="' + album.images[0].url + '" onload="this.width/=2;this.onload=null;"><span>' +
                      album.name + '</span></div></div>');
                  }
                },
                error: function(data) {
                  console.log('error', data);
                }
              });
            };

            $('.result-content span').click(function() {
              $('.result-background, result-content').remove();
              artistAlbums();
            });
        };
      },
      error: function(data) {
        console.log('error', data)
      }
    });
  };

  //ajax request for searching album
  function searchAlbum() {
    var usersAlbum = $(albumSearch).val();

    $.ajax({
      url: 'https://api.spotify.com/v1/search',
      data: {
        q: usersAlbum,
        type: 'album'
      },
      success: function(data) {
        console.log('success', data);
        for(fourthCounter in data.albums.items) {
          var album = data.albums.items[fourthCounter]
          $('.results').append('<div class="result-background"><div class="result-content">' +
            '<img src="' + album.images[0].url + '" onload="this.width/=2;this.onload=null;"><span>' +
            album.name + '</span></div></div>');
        }
      },
      error: function(data) {
        console.log('error', data)
      }
    });
  };

  //ajax request for searching track
  function searchTrack() {
    var usersTrack = $(trackSearch).val();

    $.ajax({
      url: 'https://api.spotify.com/v1/search',
      data: {
        q: usersTrack,
        type: 'track'
      },
      success: function(data) {
        console.log('success', data);
        for(firstCounter in data.tracks.items) {
          var track = data.tracks.items[firstCounter];
          $('.results').append('<div class="result-background">' +
            '<div class="result-content">' +
            '<img src="' + track.album.images[0].url + '" onload="this.width/=2;this.onload=null;">' +
            '<ul>' +
            '<li>' + track.name + '</li>' +
            '<li class="subheading">Album: ' + track.album.name + '</li>' +
            '<li class="subheading">By: ' + track.artists[0].name + '</li>' +
            '</ul>' +
            '<ul class="play-stop">' +
            '<li class="play">play preview</li>' +
            '<li class="pause">pause preview</li>' +
            '<li class="stop">stop preview</li>' +
            '</ul>' +
            '</div>' +
            '</div>');
          var audio = new Audio(track.preview_url);
          $('.play').click(function() {
            console.log('number of times clicked');
            audio.play();
          });

          $('.pause').click(function() {
            console.log('number of times clicked');
            audio.pause();
          });

          $('.stop').click(function() {
            console.log('number of times clicked');
            audio.pause();
            audio.currentTime = 0;
          });
        }
      },
      error: function(data) {
        console.log('error', data)
      }
    });
  };

  $(artistButton).click(function() {
    $('#artist-button, #album-button, #track-button').slideUp();
    $(askUser).slideUp();
    $(searchContainer).slideDown();
    $(artistSearch).slideDown();
    $(micImage).slideDown();
    $(closeButton).slideDown();
    $(artistSearch).keydown(function(e) {
      if(e.keyCode === keys.enter) {
        $('.result-background, result-content').remove();
        searchArtist();
        artistSearch = $(artistSearch).val('');
      }
    });
  });

  $(albumButton).click(function() {
    $('#artist-button, #album-button, #track-button').slideUp();
    $(askUser).slideUp();
    $(searchContainer).slideDown();
    $(albumSearch).slideDown();
    $(micImage).slideDown();
    $(closeButton).slideDown();
    $(albumSearch).keydown(function(e) {
      if(e.keyCode === keys.enter) {
        $('.result-background, result-content').remove();
        searchAlbum();
        albumSearch = $(albumSearch).val('');
      }
    });
  });

  $(trackButton).click(function() {
    $('#artist-button, #album-button, #track-button').slideUp();
    $(askUser).slideUp();
    $(searchContainer).slideDown();
    $(trackSearch).slideDown();
    $(micImage).slideDown();
    $(closeButton).slideDown();
    $(trackSearch).keydown(function(e) {
      if(e.keyCode === keys.enter) {
        $('.result-background, result-content').remove();
        searchTrack();
        trackSearch = $(trackSearch).val('');
      }
    });
  });

  $(closeButton).click(function() {
    $(artistSearch).slideUp();
    $(albumSearch).slideUp();
    $(trackSearch).slideUp();
    $(micImage).slideUp();
    $(closeButton).slideUp();
    $(askUser).slideDown();
    $('#artist-button, #album-button, #track-button').slideDown();
  });
});
