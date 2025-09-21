# Create remaining React components and styles

# 1. Pagination component
pagination = """import React from 'react';

const Pagination = ({ currentPage, totalPages, onPageChange, hasNextPage, hasPrevPage }) => {
  const getPageNumbers = () => {
    const pages = [];
    const maxVisiblePages = 5;
    
    if (totalPages <= maxVisiblePages) {
      // Show all pages if total is small
      for (let i = 1; i <= totalPages; i++) {
        pages.push(i);
      }
    } else {
      // Show pages around current page
      const startPage = Math.max(1, currentPage - 2);
      const endPage = Math.min(totalPages, currentPage + 2);
      
      if (startPage > 1) {
        pages.push(1);
        if (startPage > 2) pages.push('...');
      }
      
      for (let i = startPage; i <= endPage; i++) {
        pages.push(i);
      }
      
      if (endPage < totalPages) {
        if (endPage < totalPages - 1) pages.push('...');
        pages.push(totalPages);
      }
    }
    
    return pages;
  };

  const handlePageClick = (page) => {
    if (page !== currentPage && page !== '...') {
      onPageChange(page);
    }
  };

  const pageNumbers = getPageNumbers();

  return (
    <div className="pagination">
      <button
        className={`pagination-btn ${!hasPrevPage ? 'disabled' : ''}`}
        onClick={() => handlePageClick(currentPage - 1)}
        disabled={!hasPrevPage}
        aria-label="Previous page"
      >
        <i className="fas fa-chevron-left"></i>
        Previous
      </button>

      <div className="pagination-numbers">
        {pageNumbers.map((page, index) => (
          <button
            key={index}
            className={`pagination-number ${
              page === currentPage ? 'active' : ''
            } ${page === '...' ? 'ellipsis' : ''}`}
            onClick={() => handlePageClick(page)}
            disabled={page === '...'}
          >
            {page}
          </button>
        ))}
      </div>

      <button
        className={`pagination-btn ${!hasNextPage ? 'disabled' : ''}`}
        onClick={() => handlePageClick(currentPage + 1)}
        disabled={!hasNextPage}
        aria-label="Next page"
      >
        Next
        <i className="fas fa-chevron-right"></i>
      </button>
    </div>
  );
};

export default Pagination;"""

# 2. BookDetails component
book_details = """import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import { Oval } from 'react-loader-spinner';
import { getBookById } from '../services/api';

const BookDetails = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [book, setBook] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadBookDetails = async () => {
      try {
        setLoading(true);
        setError(null);
        
        const response = await getBookById(id);
        
        if (response.success) {
          setBook(response.data);
        } else {
          throw new Error(response.message || 'Failed to load book details');
        }
      } catch (err) {
        console.error('Error loading book details:', err);
        setError(err.message);
        toast.error('Failed to load book details');
      } finally {
        setLoading(false);
      }
    };

    if (id) {
      loadBookDetails();
    }
  }, [id]);

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

  const formatPrice = (book) => {
    if (book.priceValue) {
      return `£${book.priceValue.toFixed(2)}`;
    }
    return book.price || 'N/A';
  };

  if (loading) {
    return (
      <div className="book-details-loading">
        <div className="loading-container">
          <Oval
            height={60}
            width={60}
            color="#007bff"
            visible={true}
            ariaLabel="oval-loading"
            secondaryColor="#f3f3f3"
            strokeWidth={2}
            strokeWidthSecondary={2}
          />
          <p>Loading book details...</p>
        </div>
      </div>
    );
  }

  if (error || !book) {
    return (
      <div className="book-details-error">
        <div className="container">
          <div className="error-content">
            <i className="fas fa-exclamation-triangle"></i>
            <h2>Book Not Found</h2>
            <p>{error || 'The requested book could not be found.'}</p>
            <button onClick={() => navigate('/')} className="back-home-btn">
              <i className="fas fa-home"></i>
              Back to Books
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="book-details">
      <div className="container">
        {/* Navigation */}
        <nav className="breadcrumb">
          <button onClick={() => navigate('/')} className="breadcrumb-link">
            <i className="fas fa-chevron-left"></i>
            Back to Books
          </button>
        </nav>

        {/* Book Details Content */}
        <div className="book-details-content">
          <div className="book-details-image">
            {book.imageUrl ? (
              <img 
                src={book.imageUrl} 
                alt={book.title}
                onError={(e) => {
                  e.target.src = '/placeholder-book.png';
                }}
              />
            ) : (
              <div className="book-placeholder-large">
                <i className="fas fa-book"></i>
              </div>
            )}
          </div>

          <div className="book-details-info">
            <h1 className="book-title">{book.title}</h1>

            <div className="book-rating-large">
              <div className="stars">
                {renderStars(book.rating)}
              </div>
              <span className="rating-text">({book.rating}/5 stars)</span>
            </div>

            <div className="book-price-large">
              <span className="price-label">Price:</span>
              <span className="price-value">{formatPrice(book)}</span>
            </div>

            <div className="book-availability">
              <div className={`availability-badge ${book.inStock ? 'available' : 'unavailable'}`}>
                <i className={`fas ${book.inStock ? 'fa-check-circle' : 'fa-times-circle'}`}></i>
                {book.inStock ? 'In Stock' : 'Out of Stock'}
              </div>
              {book.stock > 0 && (
                <span className="stock-count">{book.stock} copies available</span>
              )}
            </div>

            {book.description && (
              <div className="book-description">
                <h3>Description</h3>
                <p>{book.description}</p>
              </div>
            )}

            <div className="book-meta">
              <div className="meta-item">
                <strong>Availability Status:</strong>
                <span>{book.availability || 'Unknown'}</span>
              </div>
              {book.detailUrl && (
                <div className="meta-item">
                  <strong>Original Source:</strong>
                  <a 
                    href={book.detailUrl} 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="source-link"
                  >
                    View on Books to Scrape
                    <i className="fas fa-external-link-alt"></i>
                  </a>
                </div>
              )}
            </div>

            <div className="book-actions">
              {book.inStock ? (
                <button className="add-to-cart-btn" disabled>
                  <i className="fas fa-shopping-cart"></i>
                  Add to Cart (Demo)
                </button>
              ) : (
                <button className="notify-btn" disabled>
                  <i className="fas fa-bell"></i>
                  Notify When Available (Demo)
                </button>
              )}
              
              <button 
                onClick={() => navigate('/')}
                className="continue-browsing-btn"
              >
                <i className="fas fa-arrow-left"></i>
                Continue Browsing
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BookDetails;"""

print("Additional React components created:")
print("1. components/Pagination.js")
print("2. components/BookDetails.js") 
print(f"\\nComponent sizes:")
print(f"- Pagination: {len(pagination)} characters")
print(f"- BookDetails: {len(book_details)} characters")