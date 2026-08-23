import uuid
from datetime import UTC, date, datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, Field, field_validator
from pydantic.types import SecretStr

# --- Validation Helpers ---

def validate_password_strength(value: SecretStr)-> SecretStr:
    """Helper to enforce password length requirements"""
    raw_password = value.get_secret_value()
    if len(raw_password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    # additional checks comming soon
    return value

def validate_dob_value(dob: date) -> date:
    """Helper to valudate date of birth constraints"""
    today = datetime.now(tz=UTC).date()
    if dob > today:
        raise ValueError("Date of Birth cannot be in the future.")
    if (today.year - dob.year) > 120:
        raise ValueError("Please provide a valid date of birth.")
    return dob

# --- Schemas ---

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
    role: UserRole

    @field_validator("dob")
    @classmethod
    def validate_dob(cls, dob: date) -> date:
        return validate_dob_value(dob)

class UserRegister(UserBase):
    """
    API Input: Expects a raw password.
    Uses SecretStr to prevent accidental logging of plain-text passwords.
    """
    password: SecretStr

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, value: SecretStr) -> SecretStr:
        return validate_password_strength(value)

class UserUpdate(BaseModel):
    """
    TO-DO
    """
    nickname: str | None = Field(None, max_length=15)
    firstname: str | None = Field(None, max_length=15)
    lastname: str | None = Field(None, max_length=15)
    dob: date | None = Field(None, description="Date of Birth in YYYY-MM-DD format")

    @field_validator("dob")
    @classmethod
    def validate_dob(cls, dob: date | None) -> date | None:
        if dob is None:
            return dob
        return validate_dob_value(dob)

class UserPasswordUpdate(BaseModel):
    """
    TO-DO
    """
    email: EmailStr
    dob: date = Field(..., description="Date of Birth in YYYY-MM-DD format")
    current_password: SecretStr
    new_password: SecretStr

    @field_validator("new_password")
    @classmethod
    def validate_password(cls, value: SecretStr) -> SecretStr:
        return validate_password_strength(value)

    @field_validator("dob")
    @classmethod
    def validate_dob(cls, dob: date) -> date:
        return validate_dob_value(dob)

class UserResponse(UserBase):
    id: uuid.UUID
    modified_at: datetime
