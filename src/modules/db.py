from datetime import datetime
import mysql.connector

class DB:

    def __init__(self, cursor, conn) -> None:
        self.cursor = cursor
        self.conn = conn
        print(cursor)

    def insertNewDoctor(self, doctor):

        now = datetime.now()
        current_date = now.date()

        sql = "INSERT INTO Doctors(clinic_id, field_name, name, education, experience, phone_number, email, image_src, date_added) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (doctor["clinic"], doctor["speciality"], doctor["name"], doctor["education"], doctor["experience"], doctor["phone_number"], doctor["email"], doctor["image_src"], current_date)
        try:

            self.cursor.execute(sql, val)
            self.conn.commit()

            print(f"{doctor['name']} stored in DB.")

        except mysql.connector.errors.IntegrityError as err:
            print(f"ALREADY EXISTS: {doctor['name']}")
        except Exception as err:
            print(f"DATABASE ERROR: {err}")

        return True
    
        

