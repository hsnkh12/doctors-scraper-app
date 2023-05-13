import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.modules.scraper import DocScraper


def main():

    scraper = DocScraper(speciality="*", clinic_id="*", store_in_db=False, database=None)
    scraper.start()


if __name__ == '__main__':
    main()