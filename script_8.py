# Create CSS styles

# 1. Main App.css
app_css = """/* ===== CSS RESET & BASE STYLES ===== */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f8f9fa;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* ===== APP HEADER ===== */
.app-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 2rem 0;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.app-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

.app-title i {
  font-size: 2.2rem;
}

.app-subtitle {
  font-size: 1.1rem;
  opacity: 0.9;
  margin-bottom: 1.5rem;
}

.stats-summary {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-top: 1.5rem;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  background: rgba(255,255,255,0.1);
  backdrop-filter: blur(10px);
}

.stat-number {
  font-size: 1.5rem;
  font-weight: 600;
}

.stat-label {
  font-size: 0.9rem;
  opacity: 0.8;
}

/* ===== MAIN CONTENT ===== */
.main-content {
  padding: 2rem 0;
  min-height: calc(100vh - 200px);
}

/* ===== SEARCH & FILTERS ===== */
.search-filter-container {
  margin-bottom: 2rem;
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

.search-form {
  margin-bottom: 1rem;
}

.search-input-group {
  display: flex;
  max-width: 600px;
  margin: 0 auto;
}

.search-input {
  flex: 1;
  padding: 0.75rem 1rem;
  border: 2px solid #e1e5e9;
  border-right: none;
  border-radius: 8px 0 0 8px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.search-input:focus {
  outline: none;
  border-color: #667eea;
}

.search-button {
  padding: 0.75rem 1.5rem;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 0 8px 8px 0;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-button:hover {
  background: #5a6fd8;
}

.filter-controls {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 1rem;
}

.toggle-filters-btn,
.refresh-btn,
.clear-filters-btn {
  padding: 0.5rem 1rem;
  border: 1px solid #ddd;
  background: white;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  font-size: 0.9rem;
}

.toggle-filters-btn:hover,
.clear-filters-btn:hover {
  background: #f8f9fa;
  border-color: #adb5bd;
}

.refresh-btn {
  border-color: #28a745;
  color: #28a745;
}

.refresh-btn:hover {
  background: #28a745;
  color: white;
}

.spinning {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.filters-panel {
  border-top: 1px solid #e9ecef;
  padding-top: 1.5rem;
  margin-top: 1rem;
}

.filters-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin-bottom: 1rem;
}

.filter-group {
  display: flex;
  flex-direction: column;
}

.filter-group label {
  font-weight: 500;
  margin-bottom: 0.5rem;
  color: #555;
}

.filter-group select,
.filter-group input {
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 0.9rem;
}

.range-inputs,
.sort-controls {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.range-inputs span {
  font-size: 0.9rem;
  color: #666;
}

.filter-actions {
  text-align: center;
}

.apply-filters-btn {
  padding: 0.75rem 1.5rem;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: background-color 0.3s ease;
}

.apply-filters-btn:hover {
  background: #5a6fd8;
}

/* ===== BOOK LIST ===== */
.book-list-container {
  margin-top: 2rem;
}

.results-info {
  margin-bottom: 1.5rem;
  text-align: center;
  color: #666;
  font-size: 0.95rem;
}

.books-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

/* ===== LOADING & ERROR STATES ===== */
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  text-align: center;
}

.loading-container p {
  margin-top: 1rem;
  color: #666;
  font-size: 1.1rem;
}

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: #666;
}

.empty-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  color: #ccc;
}

.empty-state h3 {
  margin-bottom: 1rem;
  color: #333;
}

.error-message {
  background: #f8d7da;
  color: #721c24;
  padding: 1rem;
  border-radius: 8px;
  margin: 1rem 0;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.retry-button {
  background: #dc3545;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  margin-left: auto;
}

/* ===== PAGINATION ===== */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
  margin: 2rem 0;
  flex-wrap: wrap;
}

.pagination-btn {
  padding: 0.5rem 1rem;
  border: 1px solid #ddd;
  background: white;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
}

.pagination-btn:hover:not(.disabled) {
  background: #f8f9fa;
  border-color: #adb5bd;
}

.pagination-btn.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-numbers {
  display: flex;
  gap: 0.25rem;
}

.pagination-number {
  width: 40px;
  height: 40px;
  border: 1px solid #ddd;
  background: white;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.pagination-number:hover:not(.ellipsis):not(.active) {
  background: #f8f9fa;
  border-color: #adb5bd;
}

.pagination-number.active {
  background: #667eea;
  color: white;
  border-color: #667eea;
}

.pagination-number.ellipsis {
  border: none;
  background: none;
  cursor: default;
}

/* ===== FOOTER ===== */
.app-footer {
  background: #343a40;
  color: white;
  text-align: center;
  padding: 2rem 0;
  margin-top: 3rem;
}

/* ===== RESPONSIVE DESIGN ===== */
@media (max-width: 768px) {
  .app-title {
    font-size: 2rem;
  }
  
  .stats-summary {
    flex-direction: column;
    gap: 1rem;
  }
  
  .stat-item {
    flex-direction: row;
    justify-content: space-between;
  }
  
  .search-input-group {
    flex-direction: column;
  }
  
  .search-input {
    border-radius: 8px;
    border-right: 2px solid #e1e5e9;
    margin-bottom: 0.5rem;
  }
  
  .search-button {
    border-radius: 8px;
  }
  
  .filter-controls {
    flex-direction: column;
    align-items: stretch;
  }
  
  .filters-grid {
    grid-template-columns: 1fr;
  }
  
  .books-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
  }
  
  .pagination {
    gap: 0.25rem;
  }
  
  .pagination-btn {
    padding: 0.4rem 0.8rem;
    font-size: 0.9rem;
  }
}

@media (max-width: 480px) {
  .container {
    padding: 0 15px;
  }
  
  .app-title {
    font-size: 1.5rem;
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .books-grid {
    grid-template-columns: 1fr;
  }
}"""

# 2. BookCard.css
book_card_css = """/* ===== BOOK CARD STYLES ===== */
.book-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
  transition: all 0.3s ease;
  cursor: pointer;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.book-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.book-image-container {
  position: relative;
  height: 200px;
  overflow: hidden;
  background: #f8f9fa;
}

.book-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.book-card:hover .book-image {
  transform: scale(1.05);
}

.book-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #e9ecef 0%, #f8f9fa 100%);
  color: #adb5bd;
  font-size: 3rem;
}

.stock-badge {
  position: absolute;
  top: 12px;
  right: 12px;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.stock-badge.in-stock {
  background: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.stock-badge.out-of-stock {
  background: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

.book-content {
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.book-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
  color: #2c3e50;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  min-height: 2.8rem;
}

.book-rating {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
}

.stars {
  display: flex;
  gap: 0.15rem;
  color: #ffc107;
}

.stars i {
  font-size: 0.9rem;
}

.rating-text {
  font-size: 0.85rem;
  color: #6c757d;
  font-weight: 500;
}

.book-price {
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.price-label {
  font-size: 0.9rem;
  color: #6c757d;
}

.price-value {
  font-size: 1.1rem;
  font-weight: 600;
  color: #28a745;
}

.book-stock {
  margin-bottom: 1rem;
}

.stock-count {
  font-size: 0.85rem;
  color: #6c757d;
  background: #f8f9fa;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  display: inline-block;
}

.book-footer {
  margin-top: auto;
  padding-top: 1rem;
}

.view-details-btn {
  width: 100%;
  padding: 0.75rem 1rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-size: 0.9rem;
}

.view-details-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.view-details-btn i {
  font-size: 0.8rem;
  transition: transform 0.3s ease;
}

.book-card:hover .view-details-btn i {
  transform: translateX(3px);
}

/* ===== BOOK DETAILS PAGE ===== */
.book-details {
  min-height: 100vh;
  background: #f8f9fa;
  padding: 2rem 0;
}

.book-details-loading {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f8f9fa;
}

.book-details-error {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f8f9fa;
}

.error-content {
  text-align: center;
  padding: 2rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.error-content i {
  font-size: 3rem;
  color: #dc3545;
  margin-bottom: 1rem;
}

.error-content h2 {
  margin-bottom: 1rem;
  color: #333;
}

.back-home-btn {
  padding: 0.75rem 1.5rem;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: background-color 0.3s ease;
  margin-top: 1rem;
}

.back-home-btn:hover {
  background: #5a6fd8;
}

.breadcrumb {
  margin-bottom: 2rem;
}

.breadcrumb-link {
  background: none;
  border: none;
  color: #667eea;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.95rem;
  padding: 0.5rem 0;
  transition: color 0.3s ease;
}

.breadcrumb-link:hover {
  color: #5a6fd8;
  text-decoration: underline;
}

.book-details-content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 3rem;
  background: white;
  border-radius: 16px;
  padding: 2.5rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.07);
}

.book-details-image {
  display: flex;
  justify-content: center;
}

.book-details-image img {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

.book-placeholder-large {
  width: 300px;
  height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #e9ecef 0%, #f8f9fa 100%);
  color: #adb5bd;
  font-size: 4rem;
  border-radius: 12px;
}

.book-details-info h1 {
  font-size: 2rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 1.5rem;
  line-height: 1.3;
}

.book-rating-large {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.book-rating-large .stars {
  font-size: 1.2rem;
  gap: 0.2rem;
}

.book-rating-large .rating-text {
  font-size: 1rem;
  font-weight: 500;
}

.book-price-large {
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.book-price-large .price-label {
  font-size: 1.1rem;
  color: #6c757d;
  font-weight: 500;
}

.book-price-large .price-value {
  font-size: 2rem;
  font-weight: 700;
  color: #28a745;
}

.book-availability {
  margin-bottom: 2rem;
}

.availability-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

.availability-badge.available {
  background: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.availability-badge.unavailable {
  background: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

.book-description {
  margin-bottom: 2rem;
}

.book-description h3 {
  font-size: 1.3rem;
  margin-bottom: 1rem;
  color: #2c3e50;
}

.book-description p {
  line-height: 1.7;
  color: #555;
  font-size: 1rem;
}

.book-meta {
  margin-bottom: 2rem;
  border-top: 1px solid #e9ecef;
  padding-top: 2rem;
}

.meta-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 0;
  border-bottom: 1px solid #f8f9fa;
}

.meta-item:last-child {
  border-bottom: none;
}

.source-link {
  color: #667eea;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.95rem;
}

.source-link:hover {
  text-decoration: underline;
}

.book-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.add-to-cart-btn,
.notify-btn,
.continue-browsing-btn {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  text-decoration: none;
}

.add-to-cart-btn {
  background: #28a745;
  color: white;
}

.add-to-cart-btn:disabled {
  background: #6c757d;
  cursor: not-allowed;
}

.notify-btn {
  background: #ffc107;
  color: #212529;
}

.notify-btn:disabled {
  background: #6c757d;
  color: white;
  cursor: not-allowed;
}

.continue-browsing-btn {
  background: #6c757d;
  color: white;
}

.continue-browsing-btn:hover {
  background: #5a6268;
}

/* ===== RESPONSIVE DESIGN ===== */
@media (max-width: 768px) {
  .book-details-content {
    grid-template-columns: 1fr;
    gap: 2rem;
    padding: 1.5rem;
  }
  
  .book-details-image {
    order: 1;
  }
  
  .book-details-info {
    order: 2;
  }
  
  .book-details-info h1 {
    font-size: 1.5rem;
  }
  
  .book-price-large .price-value {
    font-size: 1.5rem;
  }
  
  .book-actions {
    flex-direction: column;
  }
  
  .add-to-cart-btn,
  .notify-btn,
  .continue-browsing-btn {
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .book-details {
    padding: 1rem 0;
  }
  
  .book-placeholder-large {
    width: 200px;
    height: 300px;
    font-size: 3rem;
  }
  
  .meta-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
}"""

print("CSS styles created:")
print("1. styles/App.css (main application styles)")
print("2. styles/BookCard.css (book card and details styles)")
print(f"\\nCSS file sizes:")
print(f"- App.css: {len(app_css)} characters")
print(f"- BookCard.css: {len(book_card_css)} characters")