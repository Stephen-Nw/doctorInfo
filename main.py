import requests

DOCTOR_LAST_NAME = input("Enter the doctor's last name: \n")
DOCTOR_QUALIFIER = input("Enter city, state, or zip code: \n")
MAX_LIST = 5


DOCTOR_ENDPOINT = "https://clinicaltables.nlm.nih.gov/api/npi_idv/v3/search"


doctor_parameters = {
    "terms": DOCTOR_LAST_NAME,
    "maxList": MAX_LIST,
    "q": DOCTOR_QUALIFIER
}

try:
    raw_data = requests.get(DOCTOR_ENDPOINT, params=doctor_parameters)
    raw_data.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    clean_doctor_list = []
    doctors_data = raw_data.json()

    # number_of_doctors = doctors_data[0]
    original_list_of_doctors = doctors_data[3]

    print("================================================")
    # print(f"Returning the first {number_of_doctors} doctors")
    print(original_list_of_doctors)

    for doctor in original_list_of_doctors:
        if DOCTOR_LAST_NAME in doctor[0]:
            clean_doctor_list.append(doctor)
    print("***************************************************")
    print(clean_doctor_list)
    print(len(clean_doctor_list))


# for item in doctors_data:
#     print(f"{doctors_data.index(item)} - {item}")
