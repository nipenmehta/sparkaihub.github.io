# SPARK AI Hub Website - Product Requirements Document

## Original Problem Statement
Create website for SPARK AI Hub, Sharjah - an innovation center focused on artificial intelligence. Website should include sections for About Us, AI Services, How to onboard with us, and Contact us. Theme: white and blue with sparkling AI effects. Must look amazing with agency-quality design.

## User Personas
1. **Entrepreneurs/Startups**: Looking for AI innovation support and incubation
2. **Researchers/Academics**: Seeking collaboration opportunities and research facilities
3. **Businesses**: Interested in AI consulting and digital transformation
4. **Students/Professionals**: Looking for AI training and skill development
5. **Government Partners**: Exploring partnership opportunities

## Core Requirements (Static)
- White and blue color scheme
- Sparkling AI effects and animations
- Professional, agency-quality design
- Responsive layout
- Sections: Hero, About Us, AI Services, Onboarding, Contact
- Interactive elements: animated counters, service cards, smooth scrolling
- Forms: Contact form and Onboarding application form

## Architecture
- **Frontend**: React, Tailwind CSS, Shadcn UI components
- **Backend**: FastAPI (Python)
- **Database**: MongoDB
- **Email Service**: Resend API (for contact form)

## What's Been Implemented (December 2025)

### Phase 1: Frontend with Mock Data ✅
**Date**: December 2025

#### Components Created:
1. **Header** - Fixed navigation with smooth scroll, glass-morphism effect on scroll
2. **Hero Section** - Animated sparkle particles, gradient overlay, CTA buttons
3. **About Section** - Animated statistics counters, feature list with checkmarks
4. **Services Section** - 6 AI services in 3x2 grid with hover effects and images
5. **Onboarding Section** - 4-step timeline + application form
6. **Contact Section** - Contact form + info cards with map placeholder
7. **Footer** - Company info, links, social media icons
8. **AnimatedCounter** - Reusable counter component with intersection observer

#### Features:
- ✅ Sparkling AI particle effects in hero section
- ✅ Smooth scroll navigation
- ✅ Animated statistics counters (triggered on scroll)
- ✅ Interactive service cards with hover effects
- ✅ Glass-morphism header effect
- ✅ Responsive design
- ✅ Toast notifications using Sonner
- ✅ Professional AI-themed stock images
- ✅ Mock data for forms (console logging)

#### Mock Data:
- Contact form submission (mockData.js)
- Onboarding form submission (mockData.js)
- All content data (hero, services, stats, etc.)

## API Contracts (To Be Implemented)

### 1. Contact Form Submission
**Endpoint**: `POST /api/contact`
**Request Body**:
```json
{
  "name": "string",
  "email": "string",
  "phone": "string (optional)",
  "subject": "string",
  "message": "string"
}
```
**Response**:
```json
{
  "success": true,
  "message": "Thank you for contacting us!"
}
```
**Action**: Send email via Resend API + Store in MongoDB

### 2. Onboarding Application Submission
**Endpoint**: `POST /api/onboarding`
**Request Body**:
```json
{
  "fullName": "string",
  "email": "string",
  "phone": "string",
  "organization": "string (optional)",
  "interest": "string (enum: ml, nlp, cv, research, training, consulting, other)",
  "message": "string (optional)"
}
```
**Response**:
```json
{
  "success": true,
  "message": "Application submitted successfully!",
  "applicationId": "string"
}
```
**Action**: Send confirmation email + Store in MongoDB

## Prioritized Backlog

### P0 - Critical (Next Phase)
1. **Backend Development**
   - [ ] Contact form API endpoint
   - [ ] Onboarding form API endpoint
   - [ ] MongoDB models for submissions
   - [ ] Resend email integration
   - [ ] Form validation

2. **Frontend-Backend Integration**
   - [ ] Remove mock data
   - [ ] Connect forms to real APIs
   - [ ] Error handling
   - [ ] Loading states
   - [ ] Success confirmations

### P1 - Important
- [ ] Get recipient email address from client
- [ ] Email templates for contact/onboarding confirmations
- [ ] Form field validation (client & server-side)
- [ ] Admin dashboard to view submissions (future enhancement)

### P2 - Nice to Have
- [ ] Google Maps integration for location
- [ ] Newsletter subscription
- [ ] Multi-language support (Arabic/English)
- [ ] Blog/News section
- [ ] Success stories/case studies
- [ ] Team member profiles

## Next Tasks
1. Get recipient email address from user for contact form
2. Implement backend API endpoints for contact and onboarding forms
3. Integrate Resend API for email sending
4. Create MongoDB models for storing submissions
5. Connect frontend forms to backend APIs
6. Test end-to-end functionality with testing agent
7. Deploy to production

## Technical Notes
- Using Resend API for email (requires API key)
- Sender email in test mode: onboarding@resend.dev
- Frontend environment variable: REACT_APP_BACKEND_URL
- Backend environment variable: MONGO_URL, RESEND_API_KEY, SENDER_EMAIL

## Updates - December 2025

### Phase 2: Backend Integration & UI Changes ✅
**Date**: December 2025

#### Backend Implementation:
- ✅ Contact form API endpoint (/api/contact)
- ✅ Onboarding form API endpoint (/api/onboarding) - REMOVED in latest update
- ✅ MongoDB models for submissions
- ✅ Resend email integration (requires API key)
- ✅ Email notifications to dt@srtip.ae
- ✅ Form validation and error handling

#### UI Changes:
- ✅ Removed onboarding application form
- ✅ Changed "Submit Application" button to external redirect
- ✅ Button now redirects to https://ai.srtip.ae/#contact
- ✅ Contact form connected to backend API
- ✅ Toast notifications working for contact form

#### Static HTML Version Created: ✅
- ✅ Converted entire React app to standalone HTML/CSS/JS
- ✅ Single file (`/app/html-version/index.html`) - ~85KB
- ✅ No build process or dependencies required
- ✅ All animations and effects preserved
- ✅ Contact form API integration included
- ✅ Mobile responsive design
- ✅ Can be deployed anywhere (GitHub Pages, Netlify, etc.)

## Current State

### React Version (Full-Stack):
- **Location**: `/app/frontend/` and `/app/backend/`
- **Features**: Full backend integration, contact form with email
- **Use Case**: When you need backend functionality and form submissions

### HTML Version (Static):
- **Location**: `/app/html-version/index.html`
- **Features**: Standalone, no dependencies, optional API integration
- **Use Case**: Quick deployment, static hosting, no backend needed

## API Endpoints Status

### Active Endpoints:
1. **POST /api/contact** - Working ✅
   - Stores submissions in MongoDB
   - Sends email to dt@srtip.ae
   - Returns success/error response

### Removed Endpoints:
2. **POST /api/onboarding** - No longer used ❌
   - Replaced with external redirect to https://ai.srtip.ae/#contact

## Next Steps
- [ ] Add real Resend API key to enable email functionality
- [ ] Test HTML version on static hosting
- [ ] Optional: Add analytics tracking
- [ ] Optional: Add more sections (blog, case studies, team)
