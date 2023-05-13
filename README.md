# Doctors scraper app 

### How to test the scraper 
- Clone the repo.
```
git clone https://github.com/hsnkh12/doctors-scraper-app
```
- Create **py** virtual environment 
```
python3 -m venv venv
```
- Activate your **py** environment
```
source venv/bin/activate
```
- Install **py** requiremntes.
```
pip3 install -r requirements.txt
```
- Go to tests folder, and run:
```
python3 test_scraper.py
```


### How to use it (without Docker)
- Start your Mysql server locally.
- Create a new database 'doctors_scraper', and then run **init.sql** script on your Mysql server to create the tables.
- create .env file and add the your database information
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=doctors_scraper
```
- Run scraper celery process.
```
celery -A src.celery worker  --loglevel info
```
- To test the process, go to /tests/test_celery/ folder.
- Install node requiremnts (NOTE: npm and nodeJS should be already installed in your system) then run:
```
npm i
```
- Now test it by running the testing app.
```
node app.js
```
-------

### How to use it **with Docker**
- Start your Mysql server locally.
- Create a new database 'doctors_scraper', and then run **init.sql** script on your Mysql server to create the tables.
- Build docker image using Dockerfile by running.
```
docker build -t doctors-scraper-app .
```
- Before running the container, u should add a new host to your mysql server, to do that, you have first to login to mysql server, and add the following:
```
CREATE USER 'root'@'your_local_ip_address' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'local_ip_address';
```
- Then run the docker container:
```
docker run --env DB_HOST=your_local_ip_address --env DB_USER=root --env DB_PASSWORD=your_password--env DB_NAME=doctors_scraper doctors-scraper-app
```
