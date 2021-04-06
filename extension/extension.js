var articleText = "";
const API_URL = "http://127.0.0.1:5000/api";

chrome.runtime.onMessage.addListener(function (request, sender) {
  if (request.action == "getSource") {
    var parser = new DOMParser();
    var htmlDoc = parser.parseFromString(request.source, 'text/html');
    var site;
    chrome.tabs.getSelected(null, function (tab) {
      site = tab["url"];
      var selector;
      if (site.substring(0, 4) === "file") {
        selector = "articleText";
        articleText = htmlDoc.getElementById(selector).innerText;
      } else if (site.split("//")[1].substring(0, 11) === "www.nbcnews") {
        selector = "article-body__content";
        articleText = htmlDoc.getElementsByClassName(selector)[0].innerText;
      }
      console.log(articleText);
    });
  }
});

document.addEventListener('DOMContentLoaded', function () {

  var message = document.querySelector('#message');

  chrome.tabs.executeScript(null, {
    file: "getPagesSource.js"
  }, function () {
    // If you try and inject into an extensions page or the webstore/NTP you'll get an error
    if (chrome.runtime.lastError) {
      message.innerText = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
    }
  });

  document.getElementById("localservercontainer").style.visibility = "hidden";

  var localServerButton = document.getElementById('callLocalBtn');

  localServerButton.addEventListener('click', async function () {
    var text = await getData(API_URL);
    text = text.replaceAll("'", "").replaceAll("[", "").replaceAll("]", "").toUpperCase();
    document.getElementById("localserverdata").innerHTML = text;
    document.getElementById("localservercontainer").style.visibility = "visible";
  })

  async function getData(url) {
    console.log("ARITCLE TXT", articleText)
    let response = await fetch(url, {
      method: 'post',
      body: JSON.stringify({ message: articleText })
    });
    let text = await response.text()
    return text;
  }

  var checkPageButton = document.getElementById('checkPage');

  document.getElementById("addlDetails").style.visibility = "hidden";

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

    document.getElementById("addlDetails").style.visibility = "visible";

  }, false);

}, false);
