const { app, BrowserWindow } = require('electron')

function createWindow () {
  // Create the browser window.
  let win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  })

  // here we need to know if someone is logged in (backend/acc_status.py) (-> else load a different file)
  win.loadFile('html/index.html')
}

app.whenReady().then(createWindow)
