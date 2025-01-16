import phonenumbers
from phonenumbers import geocoder


def get_phone_location(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)

        # Get location (region or country)
        location = geocoder.description_for_number(parsed_number, "en")
        return {"Location": location}
    except phonenumbers.NumberParseException as e:
        return {"Error": str(e)}


# Example usage
phone_number = input("Enter the phone number with country code (e.g., +14155552671): ")
location_info = get_phone_location(phone_number)

print("Phone Number Location Information:")
for key, value in location_info.items():
    print(f"{key}: {value}")
