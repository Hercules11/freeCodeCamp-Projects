let api = "https://fcc-weather-api.glitch.me/api/current?";
let tempUnit = "C";
let currentTempCelsius;

$(document).ready(function () {
    if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition((position) => {
        let lat = position.coords.latitude;
        let lon = position.coords.longitude;
        getWeather(lat, lon);
    });
    } else {
    console.log("Geolocation is not supported by this browser.");
    }

    $('#tempunit').click(function () {
        let currentTempUnit = $('#tempunit').text();
        let newTempUnit = currentTempUnit == 'C' ? 'F' : 'C';
        $("#tempunit").text(newTempUnit);
        if (newTempUnit == 'F') {
            let fahTemp = Math.round(
              (parseInt($("#temp").text()) * 9) / 5 + 32
            );
            $('#temp').text(fahTemp + " " + String.fromCharCode(176));
        } else {
            $("#temp").text(
              currentTempCelsius + " " + String.fromCharCode(176)
            );
        }
    })
})


function getWeather(lat, lon) {
    let urlString = api + "lat=" + lat + "&" + "lon=" + lon;
    $.ajax({
        url: urlString, success: function (result) {
            $("#city").text(result.name + ", ");
            $("#country").text(result.sys.country);
            currentTempCelsius = Math.round(result.main.temp * 10) / 10;
            $("#temp").text(currentTempCelsius + " " + String.fromCharCode(176));
            $("#tempunit").text(tempUnit);
            $("#desc").text(result.weather[0].main);
            IconGen(result.weather[0].main);
        }
    })
}

function IconGen(desc) {
    let weather = desc.toLowerCase();
    switch (weather) {
      case "drizzle":
        addIcon(weather);
        break;
      case "clouds":
        addIcon(weather);
        break;
      case "rain":
        addIcon(weather);
        break;
      case "snow":
        addIcon(weather);
        break;
      case "clear":
        addIcon(weather);
        break;
      case "thunderstorm":
        addIcon(weather);
        break;
      default:
        $("div.clouds").removeClass("hide");
    }
}

function addIcon(desc) {
    $('div.' + desc).removeClass('hide');
}