from datetime import date, datetime
import uuid
from enum import Enum

from pydantic import BaseModel, EmailStr, Field, field_validator
from pydantic.types import SecretStr


class UserRole(str, Enum):
    OWNER = "owner"
    ADMIN = "admin"
    STAFF = "staff"


class UserBase(BaseModel):
    """
    Base Model: Pure Data Contract to enforce Pydantic Validation
    """

    email: EmailStr
    nickname: str = Field(max_length=15)
    firstname: str = Field(max_length=15)
    lastname: str = Field(max_length=15)
    dob: date = Field(..., description="Date of Birth in YYYY-MM-DD format")
    role: UserRole = Field(default=UserRole.STAFF)

    @field_validator("dob")
    def validate_dob(cls, dob: date) -> date:
        today = date.today()
        if dob > today:
            raise ValueError("Date of Birth cannot be in the future.")
        if (today.year - dob.year) > 120:
            raise ValueError("Please provide a valid date of birth.")
        return dob


class UserRegister(UserBase):
    """
    API Input: Expects a raw password.
    Uses SecretStr to prevent accidental logging of plain-text passwords.
    """
    password: SecretStr

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, value: SecretStr) -> SecretStr:
        # Pydantic validation runs on the SecretStr object so we must extract the string first
        raw_password = value.get_secret_value()
        if len(raw_password) < 8:
            raise ValueError("Password must be at least 8 characters long.")

        return value


class UserResponse(UserBase):
    id: uuid.UUID
    created_at: datetime
