# Doctors scraper app 

### How to use 

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
- Start your Mysql server locally.
- Run **init.sql** script on your Mysql server to create the tables.
- Run scraper celery process.
```
celery -A src.celery worker  --loglevel info
```
- To test the scraper, go to /tests/test_celery/ folder.
- Install node requiremnts (NOTE: npm and nodeJS should be already installed in your system) then run:
```
npm i
```
- Now test the scraper by running the testing app.
```
node app.js
```

### How to use with Docker
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
