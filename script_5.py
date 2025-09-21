# Create frontend React application files

# 1. Frontend package.json
frontend_package_json = """{
  "name": "book-explorer-frontend",
  "version": "1.0.0",
  "description": "React frontend for Book Explorer application",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "axios": "^1.5.1",
    "react-router-dom": "^6.18.0",
    "@fortawesome/fontawesome-free": "^6.4.2",
    "react-loader-spinner": "^5.4.5",
    "react-toastify": "^9.1.3"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "proxy": "http://localhost:5000"
}"""

# 2. Frontend index.html
index_html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Book Explorer - Discover and browse books from Books to Scrape"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    
    <!-- Font Awesome for icons -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
      integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    />
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <title>Book Explorer</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>"""

# 3. Frontend index.js (entry point)
index_js = """import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import App from './App';
import './styles/App.css';
import 'react-toastify/dist/ReactToastify.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
      <ToastContainer
        position="top-right"
        autoClose={3000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme="light"
      />
    </BrowserRouter>
  </React.StrictMode>
);"""

# 4. Main App.js
app_js = """import React, { useState, useEffect } from 'react';
import { Routes, Route } from 'react-router-dom';
import { toast } from 'react-toastify';
import BookList from './components/BookList';
import SearchFilter from './components/SearchFilter';
import BookDetails from './components/BookDetails';
import { getBooks, getBookStats } from './services/api';
import './styles/App.css';

function App() {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [pagination, setPagination] = useState({});
  const [filters, setFilters] = useState({
    search: '',
    minRating: 0,
    maxRating: 5,
    minPrice: 0,
    maxPrice: 100,
    inStock: null,
    sortBy: 'createdAt',
    sortOrder: 'desc'
  });
  const [currentPage, setCurrentPage] = useState(1);
  const [stats, setStats] = useState(null);

  // Load books data
  const loadBooks = async (page = 1, newFilters = filters) => {
    try {
      setLoading(true);
      setError(null);

      const params = {
        page,
        limit: 12,
        ...newFilters
      };

      // Remove empty or default values
      Object.keys(params).forEach(key => {
        if (params[key] === '' || params[key] === null || params[key] === undefined) {
          delete params[key];
        }
      });

      const response = await getBooks(params);
      
      if (response.success) {
        setBooks(response.data.books);
        setPagination(response.data.pagination);
        setCurrentPage(page);
      } else {
        throw new Error(response.message || 'Failed to load books');
      }
    } catch (err) {
      console.error('Error loading books:', err);
      setError(err.message);
      toast.error('Failed to load books. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  // Load statistics
  const loadStats = async () => {
    try {
      const response = await getBookStats();
      if (response.success) {
        setStats(response.data);
      }
    } catch (err) {
      console.error('Error loading stats:', err);
    }
  };

  // Handle filter changes
  const handleFilterChange = (newFilters) => {
    setFilters(newFilters);
    setCurrentPage(1);
    loadBooks(1, newFilters);
  };

  // Handle page change
  const handlePageChange = (page) => {
    loadBooks(page, filters);
  };

  // Initial load
  useEffect(() => {
    loadBooks();
    loadStats();
  }, []);

  return (
    <div className="App">
      <Routes>
        <Route path="/" element={
          <>
            {/* Header */}
            <header className="app-header">
              <div className="container">
                <h1 className="app-title">
                  <i className="fas fa-book-open"></i>
                  Book Explorer
                </h1>
                <p className="app-subtitle">
                  Discover amazing books from our curated collection
                </p>
                
                {/* Stats Display */}
                {stats && (
                  <div className="stats-summary">
                    <div className="stat-item">
                      <span className="stat-number">{stats.totalBooks}</span>
                      <span className="stat-label">Total Books</span>
                    </div>
                    <div className="stat-item">
                      <span className="stat-number">{stats.booksInStock}</span>
                      <span className="stat-label">In Stock</span>
                    </div>
                    <div className="stat-item">
                      <span className="stat-number">
                        {stats.averageRating.toFixed(1)}★
                      </span>
                      <span className="stat-label">Avg Rating</span>
                    </div>
                  </div>
                )}
              </div>
            </header>

            {/* Main Content */}
            <main className="main-content">
              <div className="container">
                {/* Search and Filters */}
                <SearchFilter 
                  filters={filters}
                  onFilterChange={handleFilterChange}
                  loading={loading}
                />

                {/* Error Display */}
                {error && (
                  <div className="error-message">
                    <i className="fas fa-exclamation-triangle"></i>
                    {error}
                    <button 
                      onClick={() => loadBooks(currentPage, filters)}
                      className="retry-button"
                    >
                      Try Again
                    </button>
                  </div>
                )}

                {/* Books List */}
                <BookList 
                  books={books}
                  loading={loading}
                  pagination={pagination}
                  currentPage={currentPage}
                  onPageChange={handlePageChange}
                />
              </div>
            </main>

            {/* Footer */}
            <footer className="app-footer">
              <div className="container">
                <p>&copy; 2024 Book Explorer. Data sourced from Books to Scrape.</p>
              </div>
            </footer>
          </>
        } />
        
        <Route path="/book/:id" element={<BookDetails />} />
      </Routes>
    </div>
  );
}

export default App;"""

print("Frontend core files created:")
print("1. package.json")
print("2. public/index.html")
print("3. src/index.js")
print("4. src/App.js (main component)")
print(f"\\nApp.js size: {len(app_js)} characters")
print(f"Index.html includes Font Awesome and Google Fonts")