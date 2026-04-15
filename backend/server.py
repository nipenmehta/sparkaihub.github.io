from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from typing import List

from models import (
    ContactSubmission,
    ContactSubmissionCreate,
    OnboardingApplication,
    OnboardingApplicationCreate
)
from email_service import send_contact_notification, send_onboarding_notification


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Add your routes to the router instead of directly to app
@api_router.get("/")
async def root():
    return {"message": "SPARK AI Hub API"}


@api_router.post("/contact")
async def submit_contact_form(contact_data: ContactSubmissionCreate):
    """Handle contact form submission"""
    try:
        # Create contact submission object
        contact_submission = ContactSubmission(**contact_data.model_dump())
        
        # Store in MongoDB
        await db.contact_submissions.insert_one(contact_submission.model_dump())
        
        # Send email notification (non-blocking, don't fail if email fails)
        email_result = await send_contact_notification(contact_data.model_dump())
        
        return {
            "success": True,
            "message": "Thank you for your interest! We'll contact you soon.",
            "submission_id": contact_submission.id
        }
    except Exception as e:
        logger.error(f"Error processing contact form: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process contact form")


@api_router.post("/onboarding")
async def submit_onboarding_application(application_data: OnboardingApplicationCreate):
    """Handle onboarding application submission"""
    try:
        # Create onboarding application object
        application = OnboardingApplication(**application_data.model_dump())
        
        # Store in MongoDB
        await db.onboarding_applications.insert_one(application.model_dump())
        
        # Send email notification (non-blocking, don't fail if email fails)
        email_result = await send_onboarding_notification(application_data.model_dump())
        
        return {
            "success": True,
            "message": "Your application has been submitted successfully! We'll be in touch shortly.",
            "application_id": application.id
        }
    except Exception as e:
        logger.error(f"Error processing onboarding application: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process onboarding application")

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()