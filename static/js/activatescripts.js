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
  let tbody = document.getElementById("bl_table").getElementsByTagName("tbody")[0];
  let new_body = document.createElement("tbody");
  tbody.parentNode.replaceChild(new_body, tbody);
  // Add devices to table
  for (i = 0; i < response.length; ++i) {
    let tr = new_body.insertRow();
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
    cell2.classList.add("columnWidthName");
    cell3.innerHTML = address;
    cell3.classList.add("columnWidthAddress");

    detailsbtn = setDetailsFormButton(name, address);
    cell4.appendChild(detailsbtn);
  }
}

function setDetailsFormButton(name, address) {
  let form = document.createElement("form");
  form.action = "/details";
  form.method = "POST";

  let inputName = document.createElement("input");
  inputName.type = "hidden";
  inputName.name = "name";
  inputName.value = name;
  form.appendChild(inputName);

  let inputAddress = document.createElement("input");
  inputAddress.type = "hidden";
  inputAddress.name = "address";
  inputAddress.value = address;
  form.appendChild(inputAddress);

  let confirmbtn = document.createElement("button");
  confirmbtn.type = "submit";
  confirmbtn.className = "btn btn-secondary btn-generic-width refreshDevices";
  confirmbtn.textContent = "Details";
  form.appendChild(confirmbtn);
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

////////////////////////////////////////////////////////////////////////////////////////

/// DELETE
function deletionofdevices() {
  var xhr = new XMLHttpRequest();
  xhr.open("DELETE", "/activatescripts$delbl", true);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.send();
  location.reload();
}