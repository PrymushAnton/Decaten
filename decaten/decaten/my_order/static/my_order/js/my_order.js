$(document).ready(function() {
    $.ajax({
      url: '/areas/',
      success: function(data) {
        var $areaSelect = $('#area-select');
        $areaSelect.empty();
        
        $areaSelect.append('<option value="0" selected disabled hidden>Оберіть область</option>');
        data.forEach(function(area) {
          $areaSelect.append(
            $('<option>', {
              value: area.Ref,
              text: area.Description
            })
          );
        });
      }
    });
  });

  // Завантаження списку міст при виборі області
  $('#area-select').on('change', function() {
    var areaRef = $(this).val();
    $('#Branch').prop('checked', false)
    $('#Postomat').prop('checked', false)

    $('#Branch').attr('disabled', true)
    $('#Postomat').attr('disabled', true)
    $.ajax({
      url: '/cities/',
      data: { 'area_ref': areaRef },
      success: function(data) {
        var $citySelect = $('#city-select');
        $citySelect.empty();
        $('#location-select').empty()

        $citySelect.append('<option value="0" selected disabled hidden>Оберіть місто</option>');
        $('#location-select').append('<option value="0" selected disabled hidden>Оберіть відділення</option>')
        data.forEach(function(city) {
            // console.log(city)
          $citySelect.append(
            $('<option>', {
              value: city.Ref,
              text: city.Description
            })
          );
        });
      }
    });
  });

  // Перевірка наявності відділень та поштоматів при виборі міста
  $('#city-select').on('change', function() {
    var cityRef = $(this).val();
    $('#Branch').prop('checked', false)
    $('#Postomat').prop('checked', false)

    $('#Branch').attr('disabled', true)
    $('#Postomat').attr('disabled', true)
    $('#location-select').empty()
    $('#location-select').append('<option value="0" selected disabled hidden>Оберіть відділення</option>')
    $.ajax({
      url: '/warehouses/',
      data: { 'city_ref': cityRef },
      success: function(data) {

        var branch = false
        var postomat = false
        data.forEach(function(location) {
          if (!branch){
            if (location.CategoryOfWarehouse == 'Branch'){
              branch = true

            }
          }
          if (!postomat){
            if (location.CategoryOfWarehouse == 'Postomat'){
              postomat = true
            }
          }
        });
        if (branch){
          $("#Branch").removeAttr('disabled')
        }
        if (postomat){
          $("#Postomat").removeAttr('disabled')
        }
      }
    });
  });

  $('#Branch').on('click', function(){
    var cityRef = $('#city-select').val()
    $.ajax({
      url: '/warehouses/',
      type: "GET",
      data: {'city_ref': cityRef},
      success: function(data){
        var $locationSelect = $('#location-select');
        $locationSelect.empty();
        $locationSelect.append('<option value="0" selected disabled hidden>Оберіть відділення</option>');
        data.forEach(function(location) {
          if (location.CategoryOfWarehouse == 'Branch'){
            $locationSelect.append(
            $('<option>', {
              value: location.Ref,
              text: location.Description
            })
          );
          }
        });
      }
    })
  })

  $('#Postomat').on('click', function(){
    var cityRef = $('#city-select').val()
    $.ajax({
      url: '/warehouses/',
      type: "GET",
      data: {'city_ref': cityRef},
      success: function(data){
        var $locationSelect = $('#location-select');
        $locationSelect.empty();
        $locationSelect.append('<option value="0" selected disabled hidden>Оберіть поштомат</option>');
        data.forEach(function(location) {
          if (location.CategoryOfWarehouse == 'Postomat'){
            $locationSelect.append(
            $('<option>', {
              value: location.Ref,
              text: location.Description
            })
          );
          }
        });
      }
    })
  })


$('.go_to_auth').click(function(){
  window.location.replace('../login/')
})