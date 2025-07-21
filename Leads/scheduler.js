// const cron = require('node-cron');
// const { exec } = require('child_process');
// const fs = require('fs');
// const path = require('path');

// // Create a logs folder if it doesn't exist
// const logDir = path.join(__dirname, 'logs');
// if (!fs.existsSync(logDir)) {
//   fs.mkdirSync(logDir);
// }
// const logFile = path.join(logDir, 'scheduler.log');

// // Helper to write to log file
// function logToFile(message) {
//   const timestamp = new Date().toISOString();
//   fs.appendFileSync(logFile, `[${timestamp}] ${message}\n`);
// }

// // Schedule task
// cron.schedule('46 22 * * *', () => {
//   logToFile('⏰ Cron job started: Running Python script...');
  
//   exec('python3 main.py', (error, stdout, stderr) => {
//     if (error) {
//       logToFile(`❌ Error: ${error.message}`);
//       return;
//     }
//     if (stderr) {
//       logToFile(`⚠️ stderr: ${stderr}`);
//     }
//     logToFile(`✅ stdout: ${stdout}`);
//   });
// });



const { exec } = require("child_process");
const path = require("path");
const os = require("os");
const cron = require("node-cron");

const pythonCmd = os.platform() === "win32" ? "python" : "python3";
const scriptPath = path.join(__dirname, "main.py");

function runPythonScript() {
  console.log("📦 Running script:", scriptPath);
  exec(`${pythonCmd} "${scriptPath}"`, (error, stdout, stderr) => {
    if (error) {
      console.error("❌ ERROR:", error.message);
      return;
    }
    if (stderr) {
      console.error("⚠️ STDERR:", stderr);
    }
    console.log("✅ OUTPUT:\n", stdout);
  });
}

// Schedule to run every day at 8:00 AM
cron.schedule("0 8 * * *", () => {
  console.log("⏰ Running daily at 8:00 AM...");
  runPythonScript();
});
