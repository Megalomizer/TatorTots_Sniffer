function scanServices() {
  scannerActive();
  let deviceAddress = document.getElementById("device-address").innerHTML

  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/details$scanservices?address=" + deviceAddress, true);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      fillTable(response);
      scannerInactive();
    } else {
      console.log("Error: " + xhr.status);
    }
  };
  xhr.send();
}

function fillTable(msg) {
  let tablebody = document.getElementById("services-table").getElementsByTagName("tbody")[0];
  let new_body = document.createElement("tbody");
  tablebody.parentNode.replaceChild(new_body, tablebody);

  for (i=0; i < msg.length; ++i) {
    let tr = new_body.insertRow();
    let id = i + 1;
    let name = msg[i].name;
    let description = msg[i].description;
    let host = msg[i].host;
    let provider = msg[i].provider;
    let port = msg[i].port;
    let protocol = msg[i].protocol;

    if (name == null || name == "") {
      name = "Unknown";
    }
    if (description == null || description == "") {
      description = "Unknown";
    }
    if (host == null || host == "") {
      host = "Unknown";
    }
    if (provider == null || provider == "") {
      provider = "Unknown";
    }
    if (port == null || port == "") {
      port = "Unknown";
    }
    if (protocol == null || protocol == "") {
      protocol = "Unknown";
    }
    
    cell1 = tr.insertCell(0);
    cell2 = tr.insertCell(1);
    cell3 = tr.insertCell(2);
    cell4 = tr.insertCell(3);
    cell5 = tr.insertCell(4);
    cell6 = tr.insertCell(5);
    cell7 = tr.insertCell(6);
    cell8 = tr.insertCell(7);

    tr.classList.add("table-primary", "table-services");
    cell1.innerHTML = id;
    cell1.classList.add("services-col-id");
    cell2.innerHTML = name;
    cell2.classList.add("services-col-name");
    cell3.innerHTML = description;
    cell3.classList.add("services-col-description");
    cell4.innerHTML = host;
    cell4.classList.add("services-col-host");
    cell5.innerHTML = provider;
    cell5.classList.add("services-col-provider");
    cell6.innerHTML = port;
    cell6.classList.add("services-col-port");
    cell7.innerHTML = protocol;
    cell7.classList.add("services-col-protocol");

    address = document.getElementById("device-address").innerHTML;
    formConfirm = forceConnect(address, port, protocol);
    cell8.appendChild(formConfirm);
  }
}

function scannerActive() {
  var btn = document.getElementById("activateScannerBtn");
  btn.textContent = "Scanning...";
  btn.disabled = true;
}

function scannerInactive() {
  var btn = document.getElementById("activateScannerBtn");
  btn.textContent = "Scan Services";
  btn.disabled = false;
}

function forceConnect(address, port, protocol) {
  let form = document.createElement("form");
  form.action = "/details$forcedconnect"
  form.method = "POST"

  let inputAddress = document.createElement("input");
  inputAddress.type = "hidden";
  inputAddress.name = "address";
  inputAddress.value = address;
  form.appendChild(inputAddress);

  let inputPort = document.createElement("input");
  inputPort.type = "hidden";
  inputPort.name = "port";
  inputPort.value = port;
  form.appendChild(inputPort);

  let inputProtocol = document.createElement("input");
  inputProtocol.type = "hidden";
  inputProtocol.name = "protocol";
  inputProtocol.value = protocol;
  form.appendChild(inputProtocol);

  let confirmbtn = document.createElement("button");
  confirmbtn.type = "submit";
  confirmbtn.className = "btn btn-secondary btn-generic-width refreshDevices";
  confirmbtn.textContent = "Connect";
  form.appendChild(confirmbtn);
  return form
}

function dosAttackStart() {
  var btn = document.getElementById("activateDosBtn");
  btn.setAttribute("class", "btn btn-danger btn-generic-width button-style");
  btn.setAttribute("onclick", "dosAttackStop()");
  btn.textContent = "Stop DoS Attack";

  let address = document.getElementById("device-address").innerHTML
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/details$dos-start?address=" + address, true);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.send();
}

function dosAttackStop() {
  var btn = document.getElementById("activateDosBtn");
  btn.setAttribute("class", "btn btn-primary btn-generic-width button-style");
  btn.setAttribute("onclick", "dosAttackStart()");
  btn.textContent = "Start DoS Attack";

  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/details$dos-stop", true);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.send();
}

function spoofMacAddress() {
  var xhr = new XMLHttpRequest();
  address = document.getElementById("device-address").innerHTML;
  xhr.open("GET", "/details$spoofmac?address=" + address, true);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.send();
}