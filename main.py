import requests

DOCTOR_NAME = "Vasudevan"

DOCTOR_ENDPOINT = "https://clinicaltables.nlm.nih.gov/api/npi_idv/v3/search"


doctor_parameters = {
    "terms": DOCTOR_NAME,
    "maxList": 5,
}

doctor_info = requests.get(DOCTOR_ENDPOINT, params=doctor_parameters)
doctor_info.raise_for_status()
doctors = doctor_info.json()

print(doctors)
