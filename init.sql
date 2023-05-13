create table Clinic ( 
clinic_id VARCHAR(5) PRIMARY KEY NOT NULL,
clinic_name VARCHAR(100) NOT NULL,
website VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL,
phone_number VARCHAR(20) NOT NULL
);

create table Speciality (
spec_name VARCHAR(100) NOT NULL,
PRIMARY KEY(spec_name)
);


create table Doctor(
name VARCHAR(100) PRIMARY KEY NOT NULL,
clinic_id VARCHAR(5) NOT NULL,
spec_name VARCHAR(100) NOT NULL,
education VARCHAR(1000) NOT NULL,
experience VARCHAR(1000) NOT NULL,
phone_number VARCHAR(20) NOT NULL,
email VARCHAR(100) NOT NULL,
image_src VARCHAR(100) NOT NULL,
date_added DATE NOT NULL,

FOREIGN KEY (clinic_id) REFERENCES Clinic(clinic_id),
FOREIGN KEY (spec_name) REFERENCES Speciality(spec_name)

);

INSERT INTO Clinic(clinic_id, clinic_name, website, email, phone_number, address) VALUES("CCH","Cyprus Central Hospital","https://cypruscentralhospital.com", "info@cypruscentralhospital.com", "+90 (392) 366 50 85", "Esref Bitlis Cad. Narlik Street, Famagusta");



INSERT INTO Speciality (spec_name) VALUES ('IN VITRO FERTILIZATION');
INSERT INTO Speciality (spec_name) VALUES ('General Surgery');
INSERT INTO Speciality (spec_name) VALUES ('Physical Treatment and Rehabilitation');
INSERT INTO Speciality (spec_name) VALUES ('Pediatrics');
INSERT INTO Speciality (spec_name) VALUES ('Gastroenterology');
INSERT INTO Speciality (spec_name) VALUES ('X Orthesis and Prosthesis');
INSERT INTO Speciality (spec_name) VALUES ('Pathology');
INSERT INTO Speciality (spec_name) VALUES ('Internal Medicine');
INSERT INTO Speciality (spec_name) VALUES ('Ophthalmology');
INSERT INTO Speciality (spec_name) VALUES ('Cardiology');
INSERT INTO Speciality (spec_name) VALUES ('Gynecology and Obstetrics');
INSERT INTO Speciality (spec_name) VALUES ('Orthopedics and Traumatology');
INSERT INTO Speciality (spec_name) VALUES ('Urology');
INSERT INTO Speciality (spec_name) VALUES ('Aesthetics and Plastic Reconstructive Surgery');
INSERT INTO Speciality (spec_name) VALUES ('Radiology');
INSERT INTO Speciality (spec_name) VALUES ('Anesthesia and Reanimation');
INSERT INTO Speciality (spec_name) VALUES ('Otorhinolaryngology');
INSERT INTO Speciality (spec_name) VALUES ('Neurology');
INSERT INTO Speciality (spec_name) VALUES ('Cardiovascular Surgery');
INSERT INTO Speciality (spec_name) VALUES ('Eye Health and Diseases');
INSERT INTO Speciality (spec_name) VALUES ('Skin Diseases');
INSERT INTO Speciality (spec_name) VALUES ('Pulmonology');
INSERT INTO Speciality (spec_name) VALUES ('Psychiatry');
INSERT INTO Speciality (spec_name) VALUES ('Oral, Dental and Maxillofacial Surgery');
INSERT INTO Speciality (spec_name) VALUES ('Orthodontics');
INSERT INTO Speciality (spec_name) VALUES ('Periodontology (Gingival Diseases)');
INSERT INTO Speciality (spec_name) VALUES ('Dentist');
INSERT INTO Speciality (spec_name) VALUES ('Pedodontics (Pediatric Dentistry)');
INSERT INTO Speciality (spec_name) VALUES ('Laboratory');
INSERT INTO Speciality (spec_name) VALUES ('Language and Speech Disorders');
INSERT INTO Speciality (spec_name) VALUES ('Nutrition and Diet');
INSERT INTO Speciality (spec_name) VALUES ('Techniques Podology');
INSERT INTO Speciality (spec_name) VALUES ('Psychology');


