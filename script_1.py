# Now let's create the actual project files starting with the scraper

# 1. Main README.md
readme_content = """# Book Explorer App

A full-stack web application that scrapes book data from Books to Scrape and provides a modern interface for browsing and searching books.

## Project Structure

```
book-explorer/
├── scraper/          # Data scraping script
├── backend/          # Express.js API server
├── frontend/         # React.js application
└── README.md         # This file
```

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd book-explorer
   ```

2. **Set up the scraper**
   ```bash
   cd scraper
   npm install
   cp .env.example .env
   # Edit .env with your MongoDB connection string
   node scraper.js
   ```

3. **Start the backend**
   ```bash
   cd ../backend
   npm install
   cp .env.example .env
   # Edit .env with your MongoDB connection string and port
   npm start
   ```

4. **Start the frontend**
   ```bash
   cd ../frontend
   npm install
   npm start
   ```

## Features

- **Data Scraping**: Automated extraction of book data from Books to Scrape
- **REST API**: Clean API endpoints for book data
- **Search & Filter**: Search by title, filter by rating, price, and stock status
- **Responsive UI**: Modern, mobile-friendly interface
- **Pagination**: Efficient data loading with pagination

## Tech Stack

- **Scraper**: Node.js, Puppeteer, MongoDB
- **Backend**: Node.js, Express.js, MongoDB, Mongoose
- **Frontend**: React.js, Axios, CSS3
- **Database**: MongoDB

## API Endpoints

- `GET /api/books` - Get paginated books with optional filters
- `GET /api/books/:id` - Get single book details
- `POST /api/refresh` - Trigger data refresh (bonus feature)

## Deployment

The application is deployed on:
- **Backend**: Render/Railway
- **Frontend**: Vercel/Netlify
- **Database**: MongoDB Atlas

## Environment Variables

Refer to `.env.example` files in each directory for required environment variables.

## License

MIT License
"""

# 2. Root package.json
root_package_json = """{
  "name": "book-explorer",
  "version": "1.0.0",
  "description": "Full-stack book explorer application",
  "private": true,
  "workspaces": [
    "scraper",
    "backend", 
    "frontend"
  ],
  "scripts": {
    "install-all": "npm install && npm run install-scraper && npm run install-backend && npm run install-frontend",
    "install-scraper": "cd scraper && npm install",
    "install-backend": "cd backend && npm install", 
    "install-frontend": "cd frontend && npm install",
    "scrape": "cd scraper && node scraper.js",
    "start-backend": "cd backend && npm start",
    "start-frontend": "cd frontend && npm start",
    "dev": "concurrently \\"npm run start-backend\\" \\"npm run start-frontend\\"",
    "build": "cd frontend && npm run build"
  },
  "devDependencies": {
    "concurrently": "^8.2.2"
  },
  "author": "Your Name",
  "license": "MIT"
}"""

# 3. .gitignore
gitignore_content = """# Dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Build directories
/frontend/build
/frontend/dist

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
logs
*.log

# Database
*.db
*.sqlite3

# Coverage directory used by tools like istanbul
coverage/
"""

print("Main project files created:")
print("1. README.md")
print("2. package.json") 
print("3. .gitignore")
print("\nContent preview for README.md:")
print(readme_content[:500] + "...")