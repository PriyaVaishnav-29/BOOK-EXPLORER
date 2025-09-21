# Create React components

# 1. API service
api_service = """import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor
api.interceptors.request.use(
  (config) => {
    // Add auth token if available
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor
api.interceptors.response.use(
  (response) => {
    return response.data;
  },
  (error) => {
    const errorMessage = error.response?.data?.error?.message || 
                        error.response?.data?.message || 
                        error.message || 
                        'An unexpected error occurred';
    
    console.error('API Error:', errorMessage);
    return Promise.reject(new Error(errorMessage));
  }
);

// API methods
export const getBooks = async (params = {}) => {
  try {
    const response = await api.get('/books', { params });
    return response;
  } catch (error) {
    throw error;
  }
};

export const getBookById = async (id) => {
  try {
    const response = await api.get(`/books/${id}`);
    return response;
  } catch (error) {
    throw error;
  }
};

export const getBookStats = async () => {
  try {
    const response = await api.get('/books/stats/summary');
    return response;
  } catch (error) {
    throw error;
  }
};

export const refreshBooks = async () => {
  try {
    const response = await api.post('/books/refresh');
    return response;
  } catch (error) {
    throw error;
  }
};

export default api;"""

# 2. BookCard component
book_card = """import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/BookCard.css';

const BookCard = ({ book }) => {
  const navigate = useNavigate();

  const handleCardClick = () => {
    navigate(`/book/${book._id}`);
  };

  const renderStars = (rating) => {
    const stars = [];
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 !== 0;

    for (let i = 0; i < fullStars; i++) {
      stars.push(<i key={`full-${i}`} className="fas fa-star"></i>);
    }

    if (hasHalfStar) {
      stars.push(<i key="half" className="fas fa-star-half-alt"></i>);
    }

    const emptyStars = 5 - fullStars - (hasHalfStar ? 1 : 0);
    for (let i = 0; i < emptyStars; i++) {
      stars.push(<i key={`empty-${i}`} className="far fa-star"></i>);
    }

    return stars;
  };

  const formatPrice = (price) => {
    if (book.priceValue) {
      return `£${book.priceValue.toFixed(2)}`;
    }
    return price || 'N/A';
  };

  return (
    <div className="book-card" onClick={handleCardClick}>
      <div className="book-image-container">
        {book.imageUrl ? (
          <img 
            src={book.imageUrl} 
            alt={book.title}
            className="book-image"
            onError={(e) => {
              e.target.src = '/placeholder-book.png';
            }}
          />
        ) : (
          <div className="book-placeholder">
            <i className="fas fa-book"></i>
          </div>
        )}
        
        {/* Stock status badge */}
        <div className={`stock-badge ${book.inStock ? 'in-stock' : 'out-of-stock'}`}>
          {book.inStock ? 'In Stock' : 'Out of Stock'}
        </div>
      </div>

      <div className="book-content">
        <h3 className="book-title" title={book.title}>
          {book.title}
        </h3>

        <div className="book-rating">
          <div className="stars">
            {renderStars(book.rating)}
          </div>
          <span className="rating-text">({book.rating}/5)</span>
        </div>

        <div className="book-price">
          <span className="price-label">Price:</span>
          <span className="price-value">{formatPrice(book.price)}</span>
        </div>

        {book.stock > 0 && (
          <div className="book-stock">
            <span className="stock-count">{book.stock} available</span>
          </div>
        )}

        <div className="book-footer">
          <button className="view-details-btn">
            View Details
            <i className="fas fa-arrow-right"></i>
          </button>
        </div>
      </div>
    </div>
  );
};

export default BookCard;"""

# 3. BookList component
book_list = """import React from 'react';
import BookCard from './BookCard';
import Pagination from './Pagination';
import { Oval } from 'react-loader-spinner';

const BookList = ({ books, loading, pagination, currentPage, onPageChange }) => {
  if (loading) {
    return (
      <div className="loading-container">
        <Oval
          height={60}
          width={60}
          color="#007bff"
          wrapperStyle={{}}
          wrapperClass=""
          visible={true}
          ariaLabel='oval-loading'
          secondaryColor="#f3f3f3"
          strokeWidth={2}
          strokeWidthSecondary={2}
        />
        <p>Loading books...</p>
      </div>
    );
  }

  if (!books || books.length === 0) {
    return (
      <div className="empty-state">
        <div className="empty-icon">
          <i className="fas fa-search"></i>
        </div>
        <h3>No books found</h3>
        <p>Try adjusting your search criteria or filters to find more books.</p>
      </div>
    );
  }

  return (
    <div className="book-list-container">
      {/* Results info */}
      <div className="results-info">
        <span className="results-count">
          Showing {books.length} of {pagination.totalCount} books
          {pagination.totalPages > 1 && (
            <span> (Page {currentPage} of {pagination.totalPages})</span>
          )}
        </span>
      </div>

      {/* Books grid */}
      <div className="books-grid">
        {books.map((book) => (
          <BookCard key={book._id} book={book} />
        ))}
      </div>

      {/* Pagination */}
      {pagination.totalPages > 1 && (
        <Pagination
          currentPage={currentPage}
          totalPages={pagination.totalPages}
          onPageChange={onPageChange}
          hasNextPage={pagination.hasNextPage}
          hasPrevPage={pagination.hasPrevPage}
        />
      )}
    </div>
  );
};

export default BookList;"""

# 4. SearchFilter component
search_filter = """import React, { useState, useEffect } from 'react';
import { toast } from 'react-toastify';
import { refreshBooks } from '../services/api';

const SearchFilter = ({ filters, onFilterChange, loading }) => {
  const [localFilters, setLocalFilters] = useState(filters);
  const [showFilters, setShowFilters] = useState(false);
  const [refreshing, setRefreshing] = useState(false);

  // Update local filters when props change
  useEffect(() => {
    setLocalFilters(filters);
  }, [filters]);

  const handleInputChange = (e) => {
    const { name, value, type, checked } = e.target;
    const newValue = type === 'checkbox' ? (checked ? true : null) : 
                     type === 'number' ? (value === '' ? 0 : parseFloat(value)) : 
                     value;

    setLocalFilters(prev => ({
      ...prev,
      [name]: newValue
    }));
  };

  const handleSearch = (e) => {
    e.preventDefault();
    onFilterChange(localFilters);
  };

  const handleClearFilters = () => {
    const defaultFilters = {
      search: '',
      minRating: 0,
      maxRating: 5,
      minPrice: 0,
      maxPrice: 100,
      inStock: null,
      sortBy: 'createdAt',
      sortOrder: 'desc'
    };
    setLocalFilters(defaultFilters);
    onFilterChange(defaultFilters);
  };

  const handleRefresh = async () => {
    try {
      setRefreshing(true);
      await refreshBooks();
      toast.success('Data refresh triggered successfully!');
      // Reload the current page after a short delay
      setTimeout(() => {
        onFilterChange(localFilters);
      }, 1000);
    } catch (error) {
      toast.error('Failed to refresh data');
    } finally {
      setRefreshing(false);
    }
  };

  return (
    <div className="search-filter-container">
      {/* Search Bar */}
      <form onSubmit={handleSearch} className="search-form">
        <div className="search-input-group">
          <input
            type="text"
            name="search"
            placeholder="Search books by title..."
            value={localFilters.search}
            onChange={handleInputChange}
            className="search-input"
          />
          <button 
            type="submit" 
            className="search-button"
            disabled={loading}
          >
            <i className="fas fa-search"></i>
          </button>
        </div>
      </form>

      {/* Filter Controls */}
      <div className="filter-controls">
        <button 
          className="toggle-filters-btn"
          onClick={() => setShowFilters(!showFilters)}
          type="button"
        >
          <i className="fas fa-filter"></i>
          {showFilters ? 'Hide Filters' : 'Show Filters'}
        </button>

        <button 
          className="refresh-btn"
          onClick={handleRefresh}
          disabled={refreshing}
          type="button"
        >
          <i className={`fas fa-sync-alt ${refreshing ? 'spinning' : ''}`}></i>
          {refreshing ? 'Refreshing...' : 'Refresh Data'}
        </button>

        <button 
          className="clear-filters-btn"
          onClick={handleClearFilters}
          type="button"
        >
          <i className="fas fa-times"></i>
          Clear Filters
        </button>
      </div>

      {/* Expandable Filters */}
      {showFilters && (
        <div className="filters-panel">
          <div className="filters-grid">
            {/* Rating Filter */}
            <div className="filter-group">
              <label>Rating Range</label>
              <div className="range-inputs">
                <select
                  name="minRating"
                  value={localFilters.minRating}
                  onChange={handleInputChange}
                >
                  <option value={0}>Any</option>
                  <option value={1}>1+ Stars</option>
                  <option value={2}>2+ Stars</option>
                  <option value={3}>3+ Stars</option>
                  <option value={4}>4+ Stars</option>
                  <option value={5}>5 Stars</option>
                </select>
                <span>to</span>
                <select
                  name="maxRating"
                  value={localFilters.maxRating}
                  onChange={handleInputChange}
                >
                  <option value={1}>1 Star</option>
                  <option value={2}>2 Stars</option>
                  <option value={3}>3 Stars</option>
                  <option value={4}>4 Stars</option>
                  <option value={5}>5 Stars</option>
                </select>
              </div>
            </div>

            {/* Price Filter */}
            <div className="filter-group">
              <label>Price Range (£)</label>
              <div className="range-inputs">
                <input
                  type="number"
                  name="minPrice"
                  placeholder="Min"
                  value={localFilters.minPrice}
                  onChange={handleInputChange}
                  min="0"
                  step="0.01"
                />
                <span>to</span>
                <input
                  type="number"
                  name="maxPrice"
                  placeholder="Max"
                  value={localFilters.maxPrice}
                  onChange={handleInputChange}
                  min="0"
                  step="0.01"
                />
              </div>
            </div>

            {/* Stock Filter */}
            <div className="filter-group">
              <label>Availability</label>
              <select
                name="inStock"
                value={localFilters.inStock || ''}
                onChange={handleInputChange}
              >
                <option value="">All Books</option>
                <option value={true}>In Stock Only</option>
                <option value={false}>Out of Stock Only</option>
              </select>
            </div>

            {/* Sort Options */}
            <div className="filter-group">
              <label>Sort By</label>
              <div className="sort-controls">
                <select
                  name="sortBy"
                  value={localFilters.sortBy}
                  onChange={handleInputChange}
                >
                  <option value="createdAt">Date Added</option>
                  <option value="title">Title</option>
                  <option value="priceValue">Price</option>
                  <option value="rating">Rating</option>
                </select>
                <select
                  name="sortOrder"
                  value={localFilters.sortOrder}
                  onChange={handleInputChange}
                >
                  <option value="desc">Descending</option>
                  <option value="asc">Ascending</option>
                </select>
              </div>
            </div>
          </div>

          <div className="filter-actions">
            <button 
              type="button"
              onClick={handleSearch}
              className="apply-filters-btn"
              disabled={loading}
            >
              <i className="fas fa-check"></i>
              Apply Filters
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default SearchFilter;"""

print("React components created:")
print("1. services/api.js (API service)")
print("2. components/BookCard.js")
print("3. components/BookList.js") 
print("4. components/SearchFilter.js")
print(f"\\nComponent sizes:")
print(f"- API service: {len(api_service)} characters")
print(f"- BookCard: {len(book_card)} characters") 
print(f"- BookList: {len(book_list)} characters")
print(f"- SearchFilter: {len(search_filter)} characters")