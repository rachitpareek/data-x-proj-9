// Establish constants and functions
var articleText = "";
const API_URL = "http://127.0.0.1:5000/api";

async function getData(url) {
  document.getElementsByClassName("lds-roller")[0].style.display = "block";
  let response = await fetch(url, {
    method: 'post',
    body: JSON.stringify({ message: articleText })
  });
  let text = await response.text()
  document.getElementsByClassName("lds-roller")[0].style.display = "none";
  return text;
}

// Get page HTML on extension load and extract article text
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

// On page load, add event listeners to buttons
document.addEventListener('DOMContentLoaded', function () {

  document.getElementById("localservercontainer").style.visibility = "hidden";

  // Extract article text from page HTML
  var message = document.querySelector('#message');

  chrome.tabs.executeScript(null, {
    file: "getPagesSource.js"
  }, function () {
    if (chrome.runtime.lastError) {
      message.innerText = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
    }
  });

  // Set up infoPageButton
  var infoPageButton = document.getElementById('infoPageBtn');

  infoPageButton.addEventListener('click', async function () {
    var newURL = "http://127.0.0.1:5000/info";
    chrome.tabs.create({ url: newURL });
  })

  // Set up localServerButton
  var localServerButton = document.getElementById('callLocalBtn');

  localServerButton.addEventListener('click', async function () {
    document.getElementById("localservercontainer").style.visibility = "hidden";
    document.getElementById("localserverdata").innerHTML = "";
    var text = await getData(API_URL);
    text = text.replaceAll("'", "").replaceAll("[", "").replaceAll("]", "").toUpperCase();
    document.getElementById("localserverdata").innerHTML = text;
    document.getElementById("localservercontainer").style.visibility = "visible";
  })

}, false);
