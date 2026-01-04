document.getElementById("test").onclick = async () => {
  const payload = `<svg/onload=alert('LΞX XSS')>`;

  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    func: (payload) => {
      document.body.innerHTML += payload;
    },
    args: [payload]
  });
};
