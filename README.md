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
