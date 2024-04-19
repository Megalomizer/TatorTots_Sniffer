/// Get Devices
function pyFindBluetoothDevices() {
  snifferActivityInactive();

  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/activatescripts$getbl", true);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      displayBluetoothDevices(response);
    } else {
      console.log("Error: " + xhr.status);
    }
  };
  xhr.send();
}

/// Display Devices in list
function displayBluetoothDevices(response) {
  snifferActivityInactive();
  console.log(response);
}

/// Set Notification Active - BL Sniffer
function snifferActivityActive() {
  var snifferActivityNotifier = document.getElementById("sniffer-activity-notifier");
  var snifferActivityBtn = document.getElementById("sniffer-activity-btn");

  snifferActivityNotifier.classList.add("text-success");
  snifferActivityNotifier.classList.remove("text-danger");
  snifferActivityNotifier.textContent = "Active";
  snifferActivityBtn.textContent = "Deactivate Sniffer Button";
}

/// Set Notification Inactive - BL Sniffer
function snifferActivityInactive() {
  console.log("TURN BACK BITCH")
  var snifferActivityNotifier = document.getElementById("sniffer-activity-notifier");
  var snifferActivityBtn = document.getElementById("sniffer-activity-btn");

  snifferActivityNotifier.classList.add("text-success");
  snifferActivityNotifier.classList.remove("text-danger");
  snifferActivityNotifier.textContent = "Scanning...";
  snifferActivityBtn.textContent = "Please wait...";
}

////////////////////////////////////////////////////////////////////////////////
function changeSpooferActivity() {
  var spooferActivityNotifier = document.getElementById("spoofer-activity-notifier");
  var spooferActivityBtn = document.getElementById("spoofer-activity-btn");

  if (spooferActivityNotifier.textContent.trim() === "Active") {
    spooferActivityNotifier.classList.add("text-danger");
    spooferActivityNotifier.classList.remove("text-success");
    spooferActivityNotifier.textContent = "Inactive";
    spooferActivityBtn.textContent = "Activate Spoofer Button";
  }
  else if (spooferActivityNotifier.textContent.trim() === "Inactive") {
    spooferActivityNotifier.classList.add("text-success");
    spooferActivityNotifier.classList.remove("text-danger");
    spooferActivityNotifier.textContent = "Active";
    spooferActivityBtn.textContent = "Deactivate Spoofer Button";
  }
}