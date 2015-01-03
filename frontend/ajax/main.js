$(document).ready(function(){});

$(function(){
  $('#search-form').submit(function(event){
    event.preventDefault();
    var searchTerm = $('#query').val();
    getRequest(searchTerm);
    });
  });

function getRequest(searchTerm){
    var params = {
        s: searchTerm,
        r: 'json'
    };
    url = 'http://www.omdbapi.com/'

    $.getJSON(url, params, function(data){
    showResults(data.Search);
    });
}

function showResults(results){
    var html = "";
    $.each(results, function(idx, obj){
        html += '<p>' + obj.Title + '</p>'
    });
    $("#results").html(html);
}