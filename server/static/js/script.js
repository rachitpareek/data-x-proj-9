var articleText = "";
const API_URL = "http://127.0.0.1:5000/api";

document.addEventListener('DOMContentLoaded', function () {

  var message = document.querySelector('#message');

  document.getElementById("localservercontainer").style.visibility = "hidden";

  var localServerButton = document.getElementById('callLocalBtn');

  localServerButton.addEventListener('click', async function () {
    var text = await getData(API_URL);
    text = text.replaceAll("'", "").replaceAll("[", "").replaceAll("]", "").toUpperCase();
    document.getElementById("localserverdata").innerHTML = text;
    document.getElementById("localservercontainer").style.visibility = "visible";
  })

  async function getData(url) {
    articleText = document.getElementById("textBox").value;
    console.log("ARTICLE TXT", articleText)
    document.getElementsByClassName("lds-roller")[0].style.display = "block";
    let response = await fetch(url, {
      method: 'post',
      body: JSON.stringify({ message: articleText })
    });
    let text = await response.text()
    document.getElementsByClassName("lds-roller")[0].style.visibility = "none";
    return text;
  }

  var checkPageButton = document.getElementById('checkPage');

  checkPageButton.addEventListener('click', function () {

    chrome.tabs.getSelected(null, function (tab) {

      d = document;

      document.getElementById("tabName").innerHTML = "<h3>You are visiting " + tab["url"] + "</h3>";

      var ul = d.getElementById('tabDetails');

      for (var key in tab) {
        if (!tab.hasOwnProperty(key)) continue;
        var li = document.createElement('li');
        ul.appendChild(li);
        li.innerHTML = key + ": " + tab[key];
      }

    });

  }, false);

}, false);
