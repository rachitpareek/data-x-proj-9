document.addEventListener('DOMContentLoaded', function () {

  document.getElementById("localservercontainer").style.visibility = "hidden";

  var localServerButton = document.getElementById('callLocalBtn');

  localServerButton.addEventListener('click', async function () {
    var text = await getData("http://127.0.0.1:5000/");
    console.log('text', text);
    document.getElementById("localserverdata").innerHTML = text;
    document.getElementById("localservercontainer").style.visibility = "visible";
  })

  async function getData(url) {
    let response = await fetch(url, {
      method: 'post',
      body: JSON.stringify({ test: "3" })
    });
    let text = await response.text()
    return text;
  }

  var checkPageButton = document.getElementById('checkPage');

  document.getElementById("addlDetails").style.visibility = "hidden";

  checkPageButton.addEventListener('click', function () {

    chrome.tabs.getSelected(null, function (tab) {

      d = document;

      document.getElementById("tabName").innerHTML = "You are visiting " + tab["url"];

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
