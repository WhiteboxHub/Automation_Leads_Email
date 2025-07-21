const schedule = require('node-schedule');
const { exec } = require('child_process');

// Schedule the job to run at 8 AM every day
schedule.scheduleJob('38 12 * * *', function() {
  console.log('Running main.py at 8 AM...');

  // Execute the Python script
  exec('python main.py', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing Python script: ${error}`);
      return;
    }
    console.log(`Python script output: ${stdout}`);
    if (stderr) {
      console.error(`Python script stderr: ${stderr}`);
    }
  });
});

console.log('Scheduler started. Waiting to run main.py at 8 AM daily...');
