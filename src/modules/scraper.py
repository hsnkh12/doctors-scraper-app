from bs4 import BeautifulSoup
import requests
from .utils import medical_specialties, decodeTurkishText
import json
import time


class CCH_Clinic:

    ID = "CCH"
    CLINIC_NAME = "Cyprus Central Hospital"
    URL = "https://cypruscentralhospital.com"
    ADDRESS = "Esref Bitlis Cad. Narlik Street, Famagusta"
    EMAIL = "info@cypruscentralhospital.com"
    PHONE_NUMBER = "+90 (392) 366 50 85"

    def __init__(self, speciality="*", store_in_db=False, database=None) -> None:
        self.store_in_db = store_in_db
        self.speciality = speciality
        self.database = database

    def __getDoctorPersonalInfo(self, details_div) -> dict:

        info = {}
        personal_div = details_div.find("div", attrs= {"class":"mkdf-ts-image-holder mkdf-grid-col-3"})
        contact_divs = personal_div.find_all("div", attrs={"class", "mkdf-contact-info"})
        info["image_src"] = personal_div.find("img")["data-src"]
        info["phone_number"] = contact_divs[0].find("span", attrs={"class":"mkdf-ts-bio-info"}).text.strip()
        info["email"] = contact_divs[1].find("a").text.strip()

        return info

    def __findDoctorDetail(self, row) -> str:

        text =  row.find("span",attrs={"class":"mkdf-ts-bio-info"}).text.strip()
        return decodeTurkishText(text)
        return articles
        
    def __getDoctorBio(self, url) -> dict:

        bio = {}

        res = requests.get(url)
        soup = BeautifulSoup(res.content,"lxml")

        details_div = soup.find("div", attrs={"class" : "mkdf-grid-row"})
        rows = details_div.find_all("div",attrs={"class":"mkdf-ts-info-row"})
        bio["education"] = self.__findDoctorDetail(rows[0])
        bio["experience"] = self.__findDoctorDetail(rows[1])
        bio["personal_info"] = self.__getDoctorPersonalInfo(details_div)

        return bio


    def __getDoctor(self, div) -> dict: 

        doctor = {}

        title_div = div.find("div", attrs={"class":"mkdf-team-title-holder"})
        a = title_div.find("a")

        name = decodeTurkishText(a.text.strip())
        doctor['name'] = name
        speciality = medical_specialties[title_div.find("h6").text.strip()]
        if self.speciality != "*" and self.speciality != speciality: return

        doctor['clinic'] = self.ID
        doctor['address'] = self.ADDRESS 
        doctor['speciality'] = speciality
        bio = self.__getDoctorBio(a["href"])
        doctor['education'] = bio['education']
        doctor['experience'] = bio['experience']
        doctor['phone_number'] = bio['personal_info']['phone_number']
        doctor['email'] = bio['personal_info']['email']
        doctor['image_src'] = bio['personal_info']['image_src']


        return doctor

    
    def __getAllDoctors(self) -> None:
        
        res = requests.get(self.URL)
        soup = BeautifulSoup(res.content,"lxml")
        
        divs = soup.find_all("div", attrs={"class":"mkdf-team info-bellow"})

        for div in divs:

            doctor = self.__getDoctor(div)
            if doctor == None: continue

            if self.store_in_db:
                self.__storeInDB(doctor)
            else:
                print(json.dumps(doctor, indent=4, ensure_ascii=False))
        return
    

    def scrap(self) -> None:

        startTime = time.time()
        self.__getAllDoctors()
        endTime = time.time() - startTime

        print(f"Elapsed time for {self.speciality}, {self.ID}: {endTime}")

    def __storeInDB(self, doctor) -> None:

        self.database.insertNewDoctor(doctor)
        



class DocScraper:

    URL = "https://cypruscentralhospital.com/doktorlarimiz/"


    def __init__(self, clinic_id="*", speciality="*" ,store_in_db=False, database=None) -> None:
        self.clinic_id = clinic_id
        self.speciality = speciality
        self.store_in_db = store_in_db
        self.database = database

    def start(self) -> None:

        clinic = CCH_Clinic(speciality=self.speciality, store_in_db=self.store_in_db, database= self.database)
        clinic.scrap()





