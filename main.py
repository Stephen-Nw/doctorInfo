import requests

DOCTOR_NAME = input("Enter the doctor name: \n")
DOCTOR_QUALIFIER = input("Enter city, state, or zip code: \n")


DOCTOR_ENDPOINT = "https://clinicaltables.nlm.nih.gov/api/npi_idv/v3/search"


doctor_parameters = {
    "terms": DOCTOR_NAME,
    "maxList": 5,
    "q": DOCTOR_QUALIFIER
}

doctor_info = requests.get(DOCTOR_ENDPOINT, params=doctor_parameters)
doctor_info.raise_for_status()
doctors = doctor_info.json()

print(doctors)
print(doctor_info.status_code)
