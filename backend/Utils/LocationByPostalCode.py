import pgeocode
from Core.Models.ResultModel import Result


def getLocationByPincode(pincodeBody, country="IN") -> Result:
    try:
        pincode = pincodeBody.Pincode
        nomi = pgeocode.Nominatim(country)
        location = nomi.query_postal_code(pincode)

        if location.empty or location.place_name is None:
            return {"error": "Invalid or unknown postal code"}
        print(location)

        result = {
            "postal_code": location.postal_code,
            "place_name": location.place_name,
            "state_name": location.state_name,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "city": location.county_name,
        }

        return Result(
            Data=result, Status=200, Message="Loocation Retrieved successfully"
        )
    except Exception as e:
        return {"error": str(e)}
