var map;

function initMap(lat, lng) {
  var location = {lat: lat, lng: lng}
  map = new google.maps.Map(document.getElementById('map'), {
    center: location,
    zoom: 8
  });
};

$(document).ready(function() {

  $('form').submit(function(e) {

    $.ajax({
      data : {
        query : $('#text').val(),
      },
      type : 'GET',
      url : '/ajax'
    }).done(function(data) {
    console.log($('input#text').val());
    $('#wiki').text(data.extract).show(); // show the extract in wiki id

    });

    e.preventDefault(); // browser don't send input
    console.log($('input#text').val());

  });

});
