var map;

function initMap(lat, lng) {
  var location = {lat: lat, lng: lng}
  map = new google.maps.Map(document.getElementById('map'), {
    center: location,
    zoom: 8
  });
}
$(document).ready(function() {

  $('form').on('submit', function(e) {

    $.ajax({
      data : {
        query : $('text').val(),
      },
      type : 'POST',
      url : '/ajax'
    })
    .done(function(data) {
    $('#wiki').text(data.extract).show(); // show the extract in wiki id

    });
    e.preventDefault(); // browser don't send input


  });

});
