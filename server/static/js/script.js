var articleText = "";
const API_URL = "http://127.0.0.1:5000/api";

document.addEventListener('DOMContentLoaded', function () {

  var message = document.querySelector('#message');

  document.getElementById("localservercontainer").style.visibility = "hidden";

    // Set up localServerButton
  var localServerButton = document.getElementById('callLocalBtn');

  localServerButton.addEventListener('click', async function () {
    document.getElementById("localservercontainer").style.visibility = "hidden";
    document.getElementById("localserverdata").innerHTML = "";
    var text = await getData(API_URL);
    var listItems = parseListItems(text);
    document.getElementById("localserverdata").innerHTML = "<ul class=\"list-group\">" + listItems + "</ul>";
    document.getElementById("localservercontainer").style.visibility = "visible";
  })

  // Function to capitalize a string
const capitalize = (s) => {
  if (typeof s !== 'string') return ''
  return s.charAt(0).toUpperCase() + s.slice(1)
}

// Return Bootstrap 4 list item color based on label
const getListItemType = (item) => {
  const ORANGE_CLASSES = ['satire', 'unreliable', 'junksci',
    'rumor', 'clickbait', 'political', 'bias'];
  const RED_CLASSES = ['fake', 'hate', 'conspiracy'];
  const GREEN_CLASSES = ['reliable',];
  const BLUE_CLASSES = ['unknown'];

  if (ORANGE_CLASSES.includes(item)) {
    return "list-group-item-warning";
  } else if (RED_CLASSES.includes(item)) {
    return "list-group-item-danger";
  } else if (GREEN_CLASSES.includes(item)) {
    return "list-group-item-success";
  } else if (BLUE_CLASSES.includes(item)) {
    return "list-group-item-primary";
  }

  return "";
}

const parseListItems = (text) => {
  var items = "";
  for (let val in text.split(";")) {
    valText = text.split(";")[val];
    valText = valText.replace(/\s+/g, ' ').trim();
    if (valText !== "") {
      items += "<li class=\"list-group-item " + getListItemType(valText) + "\">";
      items += (Number(val) + 1) + ": " + capitalize(valText) + "</li>";
    }
  }
  return items;
}

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
