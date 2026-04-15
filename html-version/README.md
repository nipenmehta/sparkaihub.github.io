# SPARK AI Hub - Static HTML/CSS Website

This is a standalone HTML/CSS/JavaScript version of the SPARK AI Hub website. No build tools or dependencies required!

## Features

- ✨ Animated sparkle particles in hero section
- 📊 Animated statistics counters
- 🎨 Modern, responsive design with white and blue theme
- 📱 Mobile-friendly
- 🚀 Smooth scrolling navigation
- 📧 Contact form with API integration
- 🔗 External redirect for onboarding applications

## How to Use

### Option 1: Direct File Opening
Simply open `index.html` in your web browser. That's it!

### Option 2: Local Web Server (Recommended for API functionality)
If you want the contact form to work with the backend API:

```bash
# Using Python 3
python3 -m http.server 8080

# Using PHP
php -S localhost:8080

# Using Node.js (http-server)
npx http-server -p 8080
```

Then open http://localhost:8080 in your browser.

### Option 3: Deploy to Any Static Host
Upload the `index.html` file to any static hosting service:
- GitHub Pages
- Netlify
- Vercel
- AWS S3
- Any web hosting with static file support

## Backend API (Optional)

The contact form requires a backend API at `/api/contact`. If you're using the FastAPI backend:

1. Make sure the backend is running on port 8001
2. Update the API endpoint in the HTML file if needed
3. The form will automatically send submissions to the backend

To use without backend: Simply remove or comment out the contact form submission logic in the `<script>` section.

## Customization

### Change Colors
Look for color values in the `<style>` section:
- Primary blue: `#2563eb`
- Secondary blue: `#60a5fa`
- Dark gray: `#111827`

### Change Images
Replace image URLs in the HTML:
- Hero background: Line ~1435
- About section image: Line ~1560
- Service card images: Lines ~1620+

### Change Content
All content is directly in the HTML:
- Hero section: Lines ~1400-1450
- About section: Lines ~1550-1650
- Services: Lines ~1700-1950
- Onboarding: Lines ~1980-2080
- Contact: Lines ~2100-2250

## Browser Support

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers

## File Size

- Single HTML file: ~85KB
- No external dependencies (except Lucide icons CDN)
- Loads in < 2 seconds on average connection

## Credits

- Icons: [Lucide Icons](https://lucide.dev/)
- Fonts: [Google Fonts - Inter](https://fonts.google.com/specimen/Inter)
- Images: Professional stock photos from Unsplash and Pexels

---

**SPARK AI Hub** - Sharjah's Innovation Center for Artificial Intelligence
