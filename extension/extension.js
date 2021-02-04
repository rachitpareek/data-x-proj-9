document.addEventListener('DOMContentLoaded', function() {

  var checkPageButton = document.getElementById('checkPage');

  document.getElementById("addlDetails").style.visibility = "hidden";

  checkPageButton.addEventListener('click', function() {

    chrome.tabs.getSelected(null, function(tab) {

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
