

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var km_driven = document.getElementById("uiKm");
  var owner = document.getElementById("uiOwner");
  var car_age = document.getElementById("uiCarAge");
  var model = document.getElementById("uiModels");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_car_price"; //Use this if you are NOT using nginx 
  // var url = "/api/predict_home_price"; // Use this if  you are using nginx. 

  $.post(url, {
    km_driven: parseFloat(km_driven.value),
    car_age: parseFloat(car_age.value),
    owner: owner.value,
    model: model.value
  }, function (data, status) {
    console.log(data.estimated_price);
    estPrice.innerHTML = "<h2>Rs. " + Math.round(data.estimated_price.toString()) + "</h2><p>(Approx.)</p>";
    console.log(status);
  });
}

function onPageLoad() {
  console.log("document loaded");
  var url = "http://127.0.0.1:5000/get_model_names"; // Use this if you are NOT using nginx 
  // var url = "/api/get_location_names"; // Use this if  you are using nginx
  $.get(url, function (data, status) {
    console.log("got response for get_location_names request");
    if (data) {
      var models = data.models;
      var uimodels = document.getElementById("uiModels");
      $('#uiModels').empty();
      for (var i in models) {
        var opt = new Option(models[i]);
        $('#uiModels').append(opt);
      }
    }
  });
}

window.onload = onPageLoad;
