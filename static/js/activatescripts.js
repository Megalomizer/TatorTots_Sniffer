function changeSnifferActivity() {
  var snifferActivityNotifier = document.getElementById("sniffer-activity-notifier");
  var snifferActivityBtn = document.getElementById("sniffer-activity-btn");

  if (snifferActivityNotifier.textContent.trim() === "Active") {
    snifferActivityNotifier.classList.add("text-danger");
    snifferActivityNotifier.classList.remove("text-success");
    snifferActivityNotifier.textContent = "Inactive";
    snifferActivityBtn.textContent = "Activate Sniffer Button";
  }
  else if (snifferActivityNotifier.textContent.trim() === "Inactive") {
    snifferActivityNotifier.classList.add("text-success");
    snifferActivityNotifier.classList.remove("text-danger");
    snifferActivityNotifier.textContent = "Active";
    snifferActivityBtn.textContent = "Deactivate Sniffer Button";
  }
}

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