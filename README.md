# Leads Email Automation

## Clone the Repository

```
git clone https://github.com/WhiteboxHub/Automation_Leads_Email.git
cd Leads
```

## Create a virtual environment and activate it:
```
python -m venv YOUR_FOLDER_NAME
```
    
### for mac/linux platforms:  
```
source YOUR_FOLDER_NAME/bin/activate
```

### for Windows platforms   
```
cd YOUR_FOLDER_NAME\Scripts
activate
```

### Install Dependencies

``` 
pip install -r requirements.txt

```


   
## Environment Variables
To run this project, you will need to add the following environment variables to your .env file

```
EMAIL_USER=
EMAIL_PASS=
SMTP_SERVER=
SMTP_PORT=

DB_HOST=
DB_USER=
DB_PASS=
DB_NAME=

UNSUBSCRIBE_URL=https://whitebox-learning.com/unsubscribe
# UNSUBSCRIBE_URL=http://localhost:8000/api/unsubscribe
```


# run main file 
```
python main.py

```
### then we will logs and print staments
