var map;

function initMap() {
  var location = {lat: 49, lng: 1}
  map = new google.maps.Map(document.getElementById('map'), {
    center: location,
    zoom: 12
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
    })

    .done(function(data) {
      var no_text=document.getElementById("text").value;
      if (no_text==""){
        alert("Tu dois écrire quelque chose mon petit :)")
        return false;
      }
      console.log(data);
      $('#wiki').text(data.extract).show(); // show the extract in wiki id
      $('#adress').text(data.adress).show();
      map.setCenter({lat: data.lat, lng: data.long})
    });

    e.preventDefault(); // browser don't send input - /fake in my html for test


  });

});
