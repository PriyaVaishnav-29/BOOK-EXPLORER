# First, let's create the project structure and scraper component
import os
import json
from pathlib import Path

# Create the main project directory structure
project_structure = {
    'book-explorer/': {
        'README.md': '',
        'package.json': '',
        '.gitignore': '',
        'scraper/': {
            'package.json': '',
            'scraper.js': '',
            'config/': {
                'database.js': ''
            },
            'models/': {
                'Book.js': ''
            },
            '.env.example': ''
        },
        'backend/': {
            'package.json': '',
            'server.js': '',
            'routes/': {
                'books.js': ''
            },
            'models/': {
                'Book.js': ''
            },
            'config/': {
                'database.js': ''
            },
            'middleware/': {
                'cors.js': '',
                'errorHandler.js': ''
            },
            '.env.example': ''
        },
        'frontend/': {
            'package.json': '',
            'public/': {
                'index.html': ''
            },
            'src/': {
                'App.js': '',
                'index.js': '',
                'components/': {
                    'BookCard.js': '',
                    'BookList.js': '',
                    'SearchFilter.js': '',
                    'BookDetails.js': '',
                    'Pagination.js': ''
                },
                'services/': {
                    'api.js': ''
                },
                'styles/': {
                    'App.css': '',
                    'BookCard.css': ''
                }
            },
            '.env.example': ''
        }
    }
}

print("Project structure created:")
print(json.dumps(project_structure, indent=2))