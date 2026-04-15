from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional
import uuid


class ContactSubmission(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: EmailStr
    phone: Optional[str] = None
    subject: str
    message: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ContactSubmissionCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    subject: str
    message: str


class OnboardingApplication(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    fullName: str
    email: EmailStr
    phone: str
    organization: Optional[str] = None
    interest: str
    message: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OnboardingApplicationCreate(BaseModel):
    fullName: str
    email: EmailStr
    phone: str
    organization: Optional[str] = None
    interest: str
    message: Optional[str] = None
