$(function() {


  $("#search-form").submit(function(event) {
    event.preventDefault();
    $("#search-results").empty();
    var searchTerm = $('#query').val();
    search(searchTerm)
  });


  function search(term) {

    var query = {
      key: "AIzaSyCdfadHd-MS-pAihYaStxo9-g6k9EMeYb0",
      part: "snippet",
      type:'video',
      q: term
    }

    $.getJSON("https://www.googleapis.com/youtube/v3/search", query, function(data) {
      var resultsArray = data.items;
      var arrayLength = resultsArray.length;
      for (var i = 0; i < arrayLength; i++) {
        console.log(resultsArray[i].id.videoId)
        $("#search-results").append("<a href=https://www.youtube.com/watch?v="+
          resultsArray[i].id.videoId+"><img src="+resultsArray[i].snippet.thumbnails.high.url+"></a>");

      };
    });

  };

});