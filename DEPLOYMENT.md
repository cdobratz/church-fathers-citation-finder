# Deployment Guide

## Backend Deployment (Render)

1. Create account at https://render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - Name: `church-fathers-api`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `cd backend && gunicorn run:app`
5. Add Environment Variables:
   - `FLASK_ENV=production`
   - `ALLOWED_ORIGINS=https://your-frontend-url.vercel.app`
6. Click "Create Web Service"
7. Note your backend URL (e.g., `https://church-fathers-api.onrender.com`)

## Frontend Deployment (Vercel)

1. Create account at https://vercel.com
2. Click "Add New Project"
3. Import your GitHub repository
4. Configure:
   - Framework Preset: `Vite`
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`
5. Add Environment Variable:
   - `VITE_API_URL=https://your-backend-url.onrender.com/api`
6. Click "Deploy"

## Alternative: Railway (Backend)

1. Create account at https://railway.app
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway auto-detects Python
5. Add environment variables in Variables tab
6. Deploy!

## Alternative: Netlify (Frontend)

1. Create account at https://netlify.com
2. Click "Add new site" → "Import existing project"
3. Connect GitHub
4. Configure:
   - Base directory: `frontend`
   - Build command: `npm run build`
   - Publish directory: `frontend/dist`
5. Add environment variables
6. Deploy!

## Testing Deployment

1. Visit your frontend URL
2. Upload the sample PDF (Clement)
3. Verify processing works
4. Check downloads
5. Monitor backend logs

## Cost Estimate

- **Render Free Tier**: $0/month
  - Sleeps after 15 min inactivity
  - 750 hours/month
  
- **Vercel Free Tier**: $0/month
  - 100 GB bandwidth
  - Unlimited projects

- **Railway Free Trial**: $5 credit
  - Then ~$5-10/month

Total: **FREE** for MVP with low traffic!

## Monitoring

- Render Dashboard: Check logs and metrics
- Vercel Analytics: Monitor frontend performance
- Both platforms email you on errors

## Troubleshooting

**Backend not responding:**
- Check Render logs
- Verify environment variables
- Ensure build succeeded

**Frontend can't reach backend:**
- Check CORS settings
- Verify API URL in frontend env
- Check browser console for errors

**PDF processing fails:**
- Check backend logs
- Verify PyPDF2/pdfplumber installed
- Test with different PDF

**API rate limiting:**
- Bible API may rate limit
- Add delays between requests
- Consider caching responses
