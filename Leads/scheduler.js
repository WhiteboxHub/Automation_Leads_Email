const cron = require('node-cron');
const { exec } = require('child_process');

// Schedule to run every day at 8:00 AM
cron.schedule('22 21 * * *', () => {
  console.log('Running Python email script at 8:00 AM...');
  exec('python3 main.py', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`stderr: ${stderr}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
  });
});
