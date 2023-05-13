from . import app
from .modules.scraper import DocScraper
# celery -A src.celery worker  --loglevel info
from .db_config import get_cursor_connection
from .modules.db import DB

@app.task(serializer='json')
def scrapNewDoctors(speciality, clinic_id):

    cursor, conn = get_cursor_connection()
    database = DB(cursor, conn)

    print(f"Task recieved for scraping '{speciality}, {clinic_id}'")
    scraper = DocScraper(store_in_db=True, speciality=speciality, clinic_id=clinic_id, database=database)
    scraper.start()

    cursor.close()
    conn.close()

    return True




