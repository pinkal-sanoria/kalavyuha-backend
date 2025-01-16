from pydantic import BaseModel


class PinCodeModel(BaseModel):
    Pincode: int
