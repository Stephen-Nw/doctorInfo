import requests

DOCTOR_NAME = input("Enter the doctor name: \n")
DOCTOR_QUALIFIER = input("Enter city, state, or zip code: \n")
MAX_LIST = 5


DOCTOR_ENDPOINT = "https://clinicaltables.nlm.nih.gov/api/npi_idv/v3/search"


doctor_parameters = {
    "terms": DOCTOR_NAME,
    "maxList": MAX_LIST,
    "q": DOCTOR_QUALIFIER
}

doctor_info = requests.get(DOCTOR_ENDPOINT, params=doctor_parameters)
doctor_info.raise_for_status()
doctors_data = doctor_info.json()

number_of_doctors = doctors_data[0]


print(f"Returning the first {number_of_doctors} doctors")
print(doctors_data)
