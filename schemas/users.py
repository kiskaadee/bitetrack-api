from datetime import date
from enum import Enum

from pydantic import BaseModel, EmailStr, Field, field_validator


class UserRole(str, Enum):
    ADMIN = "admin"
    STAFF = "staff"
    CUSTOMER = "customer"


class UserBase(BaseModel):
    """
    Base Model: Pure Data Contract to enforce Pydantic Valdation
    """

    email: EmailStr
    nickname: str = Field(max_length=15)
    firstname: str = Field(max_length=15)
    lastname: str = Field(max_length=15)
    dob: date = Field(..., description="Date of Birth in YYYY-MM-DD format")
    role: UserRole = Field(default=UserRole.CUSTOMER)

    @field_validator("dob")
    def validate_dob(cls, dob: date) -> date:
        today = date.today()
        if dob > today:
            raise ValueError("Date of Birth cannot be in the future.")
        if (today.year - dob.year) > 120:
            raise ValueError("Please provide a valid date of birth.")
        return dob
