/// Get Devices
function pyFindBluetoothDevices() {
  snifferActivityActive();

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
  // Get table
  let table = document.getElementById("bl_table").getElementsByTagName("tbody")[0];
  // Clear table
  table.innerHTML = "";
  // Add devices to table
  for (i = 0; i < response.length; ++i) {
    let tr = table.insertRow();
    let id = i + 1;
    let name = response[i].name;
    let address = response[i].address;
    if (name == null || name == "") {
      name = "Unknown";
    }
    if (address == null || address == "") {
      address = "Unknown";
    }
    cell1 = tr.insertCell(0);
    cell2 = tr.insertCell(1);
    cell3 = tr.insertCell(2);
    cell4 = tr.insertCell(3);

    tr.classList.add("table-primary", "tableBluetooth");

    cell1.innerHTML = id;
    cell1.classList.add("columnWidthID");
    cell2.innerHTML = name;
    cell3.innerHTML = address;
  }
}

/// Set Notification Active - BL Sniffer
function snifferActivityInactive() {
  var btn = document.getElementById("searchDevicesBtn");
  btn.textContent = "Search Devices";
  btn.disabled = false;
}

/// Set Notification Inactive - BL Sniffer
function snifferActivityActive() {
  var btn = document.getElementById("searchDevicesBtn");
  btn.textContent = "Searching...";
  btn.disabled = true;
}

/// Set Notification Active - Spoofer
function spooferActivityActive() {
  var spooferActivityNotifier = document.getElementById("spoofer-activity-notifier");
  var spooferActivityBtn = document.getElementById("spoofer-activity-btn");

  spooferActivityNotifier.classList.add("text-success");
  spooferActivityNotifier.classList.remove("text-danger");
  spooferActivityNotifier.textContent = "Active";
  spooferActivityBtn.textContent = "Deactivate Spoofer Button";
}

/// Set Notification Inactive - Spoofer
function spooferActivityInactive() {
  var spooferActivityNotifier = document.getElementById("spoofer-activity-notifier");
  var spooferActivityBtn = document.getElementById("spoofer-activity-btn");

  spooferActivityNotifier.classList.add("text-danger");
  spooferActivityNotifier.classList.remove("text-success");
  spooferActivityNotifier.textContent = "Inactive";
  spooferActivityBtn.textContent = "Activate Spoofer Button";
}

////////////////////////////////////////////////////////////////////////////////////////

/// Decrypt Message
function decrypt(msg) {
  
}