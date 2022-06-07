import requests


def doctor_list():
    """Retrieve a list of providers who match the criteria specified by the user"""

    DOCTOR_LAST_NAME = input("Enter the doctor's last name: \n").upper()
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
        print(err)  # placeholder - redirect to a 404 page
    else:

        doctors_data = raw_data.json()

        original_list_of_doctors = doctors_data[3]

        if len(original_list_of_doctors) == 0:
            # placeholder - redirect to a No results found page
            return ("No results found")
        else:

            clean_doctor_list = [
                doctor for doctor in original_list_of_doctors if DOCTOR_LAST_NAME in doctor[0]]

            print(f"Returning the first {len(clean_doctor_list)} doctors")

            return clean_doctor_list


a = doctor_list()
print(a)
