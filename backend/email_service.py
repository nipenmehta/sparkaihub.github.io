import os
import asyncio
import logging
import resend
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Configure Resend
resend.api_key = os.environ.get('RESEND_API_KEY')
SENDER_EMAIL = os.environ.get('SENDER_EMAIL', 'onboarding@resend.dev')
RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL', 'dt@srtip.ae')

logger = logging.getLogger(__name__)


async def send_contact_notification(contact_data: dict):
    """Send email notification for contact form submission"""
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%); color: white; padding: 20px; text-align: center; }}
            .content {{ background: #f9fafb; padding: 30px; border-radius: 8px; margin-top: 20px; }}
            .field {{ margin-bottom: 15px; }}
            .label {{ font-weight: bold; color: #1e40af; }}
            .value {{ color: #4b5563; margin-top: 5px; }}
            .footer {{ text-align: center; margin-top: 30px; color: #6b7280; font-size: 14px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>✨ New Contact Form Submission</h1>
                <p>SPARK AI Hub Website</p>
            </div>
            <div class="content">
                <div class="field">
                    <div class="label">Name:</div>
                    <div class="value">{contact_data.get('name', 'N/A')}</div>
                </div>
                <div class="field">
                    <div class="label">Email:</div>
                    <div class="value">{contact_data.get('email', 'N/A')}</div>
                </div>
                <div class="field">
                    <div class="label">Phone:</div>
                    <div class="value">{contact_data.get('phone', 'Not provided')}</div>
                </div>
                <div class="field">
                    <div class="label">Subject:</div>
                    <div class="value">{contact_data.get('subject', 'N/A')}</div>
                </div>
                <div class="field">
                    <div class="label">Message:</div>
                    <div class="value">{contact_data.get('message', 'N/A')}</div>
                </div>
            </div>
            <div class="footer">
                <p>This email was sent from SPARK AI Hub contact form</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    params = {
        "from": SENDER_EMAIL,
        "to": [RECIPIENT_EMAIL],
        "subject": f"New Contact Form Submission - {contact_data.get('subject', 'No Subject')}",
        "html": html_content
    }
    
    try:
        email = await asyncio.to_thread(resend.Emails.send, params)
        logger.info(f"Contact notification email sent successfully: {email.get('id')}")
        return {"success": True, "email_id": email.get("id")}
    except Exception as e:
        logger.error(f"Failed to send contact notification email: {str(e)}")
        # Don't fail the request if email fails, just log it
        return {"success": False, "error": str(e)}


async def send_onboarding_notification(application_data: dict):
    """Send email notification for onboarding application"""
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%); color: white; padding: 20px; text-align: center; }}
            .content {{ background: #f9fafb; padding: 30px; border-radius: 8px; margin-top: 20px; }}
            .field {{ margin-bottom: 15px; }}
            .label {{ font-weight: bold; color: #1e40af; }}
            .value {{ color: #4b5563; margin-top: 5px; }}
            .footer {{ text-align: center; margin-top: 30px; color: #6b7280; font-size: 14px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🚀 New Onboarding Application</h1>
                <p>SPARK AI Hub Website</p>
            </div>
            <div class="content">
                <div class="field">
                    <div class="label">Full Name:</div>
                    <div class="value">{application_data.get('fullName', 'N/A')}</div>
                </div>
                <div class="field">
                    <div class="label">Email:</div>
                    <div class="value">{application_data.get('email', 'N/A')}</div>
                </div>
                <div class="field">
                    <div class="label">Phone:</div>
                    <div class="value">{application_data.get('phone', 'N/A')}</div>
                </div>
                <div class="field">
                    <div class="label">Organization:</div>
                    <div class="value">{application_data.get('organization', 'Not provided')}</div>
                </div>
                <div class="field">
                    <div class="label">Area of Interest:</div>
                    <div class="value">{application_data.get('interest', 'N/A')}</div>
                </div>
                <div class="field">
                    <div class="label">Project Details:</div>
                    <div class="value">{application_data.get('message', 'Not provided')}</div>
                </div>
            </div>
            <div class="footer">
                <p>This email was sent from SPARK AI Hub onboarding form</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    params = {
        "from": SENDER_EMAIL,
        "to": [RECIPIENT_EMAIL],
        "subject": f"New Onboarding Application - {application_data.get('fullName', 'Unknown')}",
        "html": html_content
    }
    
    try:
        email = await asyncio.to_thread(resend.Emails.send, params)
        logger.info(f"Onboarding notification email sent successfully: {email.get('id')}")
        return {"success": True, "email_id": email.get("id")}
    except Exception as e:
        logger.error(f"Failed to send onboarding notification email: {str(e)}")
        # Don't fail the request if email fails, just log it
        return {"success": False, "error": str(e)}
