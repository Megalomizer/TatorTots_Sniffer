function sendMessage() {
  inputfield = document.getElementById("msg-input");
  socket = document.getElementById("device-socket").innerHTML;
  message = inputfield.value;
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/details$forcedconnect-msgsend?socket=" + socket + "&msg=" + message, true);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.send();
  document.getElementById("msg-input").value = "";
}

function receiveMessage() {
  socket = document.getElementById("device-socket").innerHTML;
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/details$forcedconnect-msgreceive?socket=" + socket, true);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.onreadystatechange = function() {
    if(xhr.readyState === 4 && xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      document.getElementById("message-received").innerHTML = response;
    }
  }
  xhr.send();
  document.getElementById("msg-input").innerHTML = "";
}