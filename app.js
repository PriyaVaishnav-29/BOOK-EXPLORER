// Book data
const booksData = {
  "books": [
    {
      "id": "1",
      "title": "A Light in the Attic",
      "price": "£51.77",
      "priceValue": 51.77,
      "rating": 3,
      "stock": 22,
      "inStock": true,
      "imageUrl": "",
      "description": "A collection of whimsical poems and drawings by Shel Silverstein that has delighted readers of all ages for generations."
    },
    {
      "id": "2", 
      "title": "Tipping the Velvet",
      "price": "£53.74",
      "priceValue": 53.74,
      "rating": 1,
      "stock": 20,
      "inStock": true,
      "imageUrl": "",
      "description": "A sweeping novel of Victorian London's music halls and the passionate love story of Nancy Astley."
    },
    {
      "id": "3",
      "title": "Soumission",
      "price": "£50.10",
      "priceValue": 50.10,
      "rating": 1,
      "stock": 0,
      "inStock": false,
      "imageUrl": "",
      "description": "A controversial novel exploring themes of submission and political change in contemporary France."
    },
    {
      "id": "4",
      "title": "Sharp Objects",
      "price": "£47.82",
      "priceValue": 47.82,
      "rating": 4,
      "stock": 17,
      "inStock": true,
      "imageUrl": "",
      "description": "A dark psychological thriller about a journalist returning to her hometown to cover a series of murders."
    },
    {
      "id": "5",
      "title": "Sapiens: A Brief History of Humankind",
      "price": "£54.23",
      "priceValue": 54.23,
      "rating": 5,
      "stock": 20,
      "inStock": true,
      "imageUrl": "",
      "description": "An exploration of how Homo sapiens conquered the world, from the Stone Age to the present."
    },
    {
      "id": "6",
      "title": "The Requiem Red",
      "price": "£22.65",
      "priceValue": 22.65,
      "rating": 1,
      "stock": 0,
      "inStock": false,
      "imageUrl": "",
      "description": "A haunting tale of mystery and supernatural elements in a small town setting."
    },
    {
      "id": "7",
      "title": "The Dirty Little Secrets of Getting Your Dream Job",
      "price": "£33.34",
      "priceValue": 33.34,
      "rating": 4,
      "stock": 19,
      "inStock": true,
      "imageUrl": "",
      "description": "Career advice and strategies for landing the job you've always wanted in today's competitive market."
    },
    {
      "id": "8",
      "title": "The Coming Woman: A Novel Based on the Life of the Infamous Feminist Victoria Woodhull",
      "price": "£17.93",
      "priceValue": 17.93,
      "rating": 3,
      "stock": 17,
      "inStock": true,
      "imageUrl": "",
      "description": "A biographical novel about Victoria Woodhull, the first woman to run for President of the United States."
    },
    {
      "id": "9",
      "title": "The Boys in the Boat",
      "price": "£22.60",
      "priceValue": 22.60,
      "rating": 4,
      "stock": 22,
      "inStock": true,
      "imageUrl": "",
      "description": "The inspiring true story of the American rowing team that triumphed at the 1936 Berlin Olympics."
    },
    {
      "id": "10",
      "title": "The Black Maria",
      "price": "£52.15",
      "priceValue": 52.15,
      "rating": 1,
      "stock": 0,
      "inStock": false,
      "imageUrl": "",
      "description": "A noir thriller set in the gritty underworld of 1950s America, following a detective's dangerous investigation."
    },
    {
      "id": "11",
      "title": "Starving Hearts (Triangular Trade Trilogy, #1)",
      "price": "£13.99",
      "priceValue": 13.99,
      "rating": 2,
      "stock": 2,
      "inStock": true,
      "imageUrl": "",
      "description": "The first book in a historical fiction trilogy exploring the impact of the triangular trade on three families."
    },
    {
      "id": "12",
      "title": "Shakespeare's Sonnets",
      "price": "£20.66",
      "priceValue": 20.66,
      "rating": 4,
      "stock": 19,
      "inStock": true,
      "imageUrl": "",
      "description": "The complete collection of 154 sonnets by William Shakespeare, exploring themes of love, beauty, and mortality."
    },
    {
      "id": "13",
      "title": "Set Me Free",
      "price": "£17.46",
      "priceValue": 17.46,
      "rating": 5,
      "stock": 1,
      "inStock": true,
      "imageUrl": "",
      "description": "A powerful memoir about breaking free from an abusive relationship and finding strength and independence."
    },
    {
      "id": "14",
      "title": "Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)",
      "price": "£52.29",
      "priceValue": 52.29,
      "rating": 5,
      "stock": 0,
      "inStock": false,
      "imageUrl": "",
      "description": "The first volume in the beloved graphic novel series about Scott Pilgrim's quest to win Ramona's heart."
    },
    {
      "id": "15",
      "title": "Rip it Up and Start Again",
      "price": "£35.02",
      "priceValue": 35.02,
      "rating": 5,
      "stock": 1,
      "inStock": true,
      "imageUrl": "",
      "description": "A comprehensive look at the post-punk music scene and its revolutionary impact on culture and society."
    },
    {
      "id": "16",
      "title": "Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991",
      "price": "£57.25",
      "priceValue": 57.25,
      "rating": 3,
      "stock": 17,
      "inStock": true,
      "imageUrl": "",
      "description": "An oral history of the American indie rock scene in the 1980s, featuring bands like Sonic Youth and The Replacements."
    },
    {
      "id": "17",
      "title": "Olio",
      "price": "£23.88",
      "priceValue": 23.88,
      "rating": 1,
      "stock": 1,
      "inStock": true,
      "imageUrl": "",
      "description": "A collection of poetry exploring themes of identity, memory, and the African American experience."
    },
    {
      "id": "18",
      "title": "Mesaerion: The Best Science Fiction Stories 1800-1849",
      "price": "£37.59",
      "priceValue": 37.59,
      "rating": 1,
      "stock": 1,
      "inStock": true,
      "imageUrl": "",
      "description": "A curated collection of the finest science fiction stories from the first half of the 19th century."
    },
    {
      "id": "19",
      "title": "Libertarianism for Beginners",
      "price": "£51.33",
      "priceValue": 51.33,
      "rating": 2,
      "stock": 2,
      "inStock": true,
      "imageUrl": "",
      "description": "An accessible introduction to libertarian philosophy and its applications to modern political issues."
    },
    {
      "id": "20",
      "title": "It's Only the Himalayas",
      "price": "£45.17",
      "priceValue": 45.17,
      "rating": 2,
      "stock": 19,
      "inStock": true,
      "imageUrl": "",
      "description": "A humorous travel memoir about an unprepared adventurer's journey through the Himalayas."
    }
  ]
};

// Application state
let filteredBooks = [...booksData.books];
let currentFilters = {
  search: '',
  rating: '',
  minPrice: '',
  maxPrice: '',
  stock: '',
  sortBy: 'title',
  sortOrder: 'asc'
};

// Utility functions
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

function createStarRating(rating) {
  const stars = [];
  for (let i = 1; i <= 5; i++) {
    stars.push(`<span class="star ${i <= rating ? 'filled' : ''}">★</span>`);
  }
  return `<div class="stars">${stars.join('')}</div><span class="rating-text">${rating}/5</span>`;
}

function getStockBadge(book) {
  if (!book.inStock) {
    return '<span class="stock-badge stock-badge--out-of-stock">Out of Stock</span>';
  } else if (book.stock <= 5) {
    return '<span class="stock-badge stock-badge--low-stock">Low Stock</span>';
  } else {
    return '<span class="stock-badge stock-badge--in-stock">In Stock</span>';
  }
}

function createBookCard(book) {
  return `
    <div class="book-card" data-book-id="${book.id}">
      <div class="book-cover"></div>
      <div class="book-card__content">
        <h3 class="book-card__title">${book.title}</h3>
        <div class="rating">
          ${createStarRating(book.rating)}
        </div>
        <div class="book-card__footer">
          <span class="price">${book.price}</span>
          ${getStockBadge(book)}
        </div>
      </div>
    </div>
  `;
}

// Filter and sort functions
function applyFilters() {
  console.log('Applying filters:', currentFilters);
  let filtered = [...booksData.books];

  // Search filter
  if (currentFilters.search) {
    const searchTerm = currentFilters.search.toLowerCase();
    filtered = filtered.filter(book =>
      book.title.toLowerCase().includes(searchTerm)
    );
    console.log('After search filter:', filtered.length, 'books');
  }

  // Rating filter
  if (currentFilters.rating) {
    const minRating = parseInt(currentFilters.rating);
    filtered = filtered.filter(book => book.rating >= minRating);
    console.log('After rating filter:', filtered.length, 'books');
  }

  // Price filter
  if (currentFilters.minPrice) {
    const minPrice = parseFloat(currentFilters.minPrice);
    filtered = filtered.filter(book => book.priceValue >= minPrice);
  }

  if (currentFilters.maxPrice) {
    const maxPrice = parseFloat(currentFilters.maxPrice);
    filtered = filtered.filter(book => book.priceValue <= maxPrice);
  }

  // Stock filter
  if (currentFilters.stock === 'in-stock') {
    filtered = filtered.filter(book => book.inStock);
  } else if (currentFilters.stock === 'out-of-stock') {
    filtered = filtered.filter(book => !book.inStock);
  }

  // Apply sorting
  filtered.sort((a, b) => {
    let aValue, bValue;

    switch (currentFilters.sortBy) {
      case 'title':
        aValue = a.title.toLowerCase();
        bValue = b.title.toLowerCase();
        break;
      case 'price':
        aValue = a.priceValue;
        bValue = b.priceValue;
        break;
      case 'rating':
        aValue = a.rating;
        bValue = b.rating;
        break;
      case 'stock':
        aValue = a.stock;
        bValue = b.stock;
        break;
      default:
        return 0;
    }

    if (currentFilters.sortOrder === 'desc') {
      return aValue < bValue ? 1 : aValue > bValue ? -1 : 0;
    } else {
      return aValue > bValue ? 1 : aValue < bValue ? -1 : 0;
    }
  });

  filteredBooks = filtered;
  updateStats();
  renderBooks();
}

function updateStats() {
  const totalBooks = filteredBooks.length;
  const inStockBooks = filteredBooks.filter(book => book.inStock).length;
  const avgRating = totalBooks > 0 
    ? (filteredBooks.reduce((sum, book) => sum + book.rating, 0) / totalBooks).toFixed(1)
    : '0.0';

  const totalBooksSpan = document.getElementById('total-books');
  const inStockSpan = document.getElementById('in-stock');
  const avgRatingSpan = document.getElementById('avg-rating');

  if (totalBooksSpan) totalBooksSpan.textContent = totalBooks;
  if (inStockSpan) inStockSpan.textContent = inStockBooks;
  if (avgRatingSpan) avgRatingSpan.textContent = avgRating;
}

function renderBooks() {
  const loading = document.getElementById('loading');
  const booksGrid = document.getElementById('books-grid');
  const emptyState = document.getElementById('empty-state');

  if (!loading || !booksGrid || !emptyState) return;

  // Show loading state
  loading.classList.remove('hidden');
  booksGrid.innerHTML = '';
  emptyState.classList.add('hidden');

  // Simulate loading delay
  setTimeout(() => {
    loading.classList.add('hidden');

    if (filteredBooks.length === 0) {
      emptyState.classList.remove('hidden');
      return;
    }

    booksGrid.innerHTML = filteredBooks.map(createBookCard).join('');
    attachBookCardListeners();
  }, 100);
}

function attachBookCardListeners() {
  const bookCards = document.querySelectorAll('.book-card');
  bookCards.forEach(card => {
    card.addEventListener('click', (e) => {
      e.preventDefault();
      const bookId = card.dataset.bookId;
      const book = booksData.books.find(b => b.id === bookId);
      if (book) {
        console.log('Opening book details for:', book.title);
        showBookDetails(book);
      }
    });

    // Add keyboard navigation
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        card.click();
      }
    });

    // Make cards focusable
    card.setAttribute('tabindex', '0');
  });
}

function showBookDetails(book) {
  const modal = document.getElementById('book-modal');
  if (!modal) return;

  console.log('Showing modal for book:', book.title);

  // Populate modal with book details
  const modalTitle = document.getElementById('modal-book-title');
  const modalRating = document.getElementById('modal-book-rating');
  const modalPrice = document.getElementById('modal-book-price');
  const modalStock = document.getElementById('modal-book-stock');
  const modalDescription = document.getElementById('modal-book-description');

  if (modalTitle) modalTitle.textContent = book.title;
  if (modalRating) modalRating.innerHTML = createStarRating(book.rating);
  if (modalPrice) modalPrice.textContent = book.price;
  if (modalStock) modalStock.innerHTML = getStockBadge(book);
  if (modalDescription) modalDescription.textContent = book.description;

  // Show modal
  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';

  // Focus management
  const closeModalBtn = document.getElementById('close-modal');
  if (closeModalBtn) {
    setTimeout(() => closeModalBtn.focus(), 100);
  }
}

function hideBookDetails() {
  const modal = document.getElementById('book-modal');
  if (!modal) return;
  
  console.log('Hiding modal');
  modal.classList.add('hidden');
  document.body.style.overflow = '';
}

function clearFilters() {
  console.log('Clearing filters');
  currentFilters = {
    search: '',
    rating: '',
    minPrice: '',
    maxPrice: '',
    stock: '',
    sortBy: 'title',
    sortOrder: 'asc'
  };

  // Reset form elements
  const searchInput = document.getElementById('search-input');
  const ratingFilter = document.getElementById('rating-filter');
  const minPriceInput = document.getElementById('min-price');
  const maxPriceInput = document.getElementById('max-price');
  const stockFilter = document.getElementById('stock-filter');
  const sortBySelect = document.getElementById('sort-by');
  const sortOrderSelect = document.getElementById('sort-order');

  if (searchInput) searchInput.value = '';
  if (ratingFilter) ratingFilter.value = '';
  if (minPriceInput) minPriceInput.value = '';
  if (maxPriceInput) maxPriceInput.value = '';
  if (stockFilter) stockFilter.value = '';
  if (sortBySelect) sortBySelect.value = 'title';
  if (sortOrderSelect) sortOrderSelect.value = 'asc';

  applyFilters();
}

// Event listeners
function attachEventListeners() {
  console.log('Attaching event listeners');

  // Search input
  const searchInput = document.getElementById('search-input');
  if (searchInput) {
    const debouncedSearch = debounce((value) => {
      console.log('Search input changed:', value);
      currentFilters.search = value.trim();
      applyFilters();
    }, 300);

    searchInput.addEventListener('input', (e) => {
      debouncedSearch(e.target.value);
    });
    console.log('Search input listener attached');
  }

  // Rating filter
  const ratingFilter = document.getElementById('rating-filter');
  if (ratingFilter) {
    ratingFilter.addEventListener('change', (e) => {
      console.log('Rating filter changed:', e.target.value);
      currentFilters.rating = e.target.value;
      applyFilters();
    });
    console.log('Rating filter listener attached');
  }

  // Price filters
  const minPriceInput = document.getElementById('min-price');
  const maxPriceInput = document.getElementById('max-price');
  
  if (minPriceInput) {
    minPriceInput.addEventListener('input', debounce((e) => {
      currentFilters.minPrice = e.target.value;
      applyFilters();
    }, 500));
  }

  if (maxPriceInput) {
    maxPriceInput.addEventListener('input', debounce((e) => {
      currentFilters.maxPrice = e.target.value;
      applyFilters();
    }, 500));
  }

  // Stock filter
  const stockFilter = document.getElementById('stock-filter');
  if (stockFilter) {
    stockFilter.addEventListener('change', (e) => {
      currentFilters.stock = e.target.value;
      applyFilters();
    });
  }

  // Sort controls
  const sortBySelect = document.getElementById('sort-by');
  const sortOrderSelect = document.getElementById('sort-order');
  
  if (sortBySelect) {
    sortBySelect.addEventListener('change', (e) => {
      currentFilters.sortBy = e.target.value;
      applyFilters();
    });
  }

  if (sortOrderSelect) {
    sortOrderSelect.addEventListener('change', (e) => {
      currentFilters.sortOrder = e.target.value;
      applyFilters();
    });
  }

  // Clear filters buttons
  const clearFiltersBtn = document.getElementById('clear-filters');
  const resetSearchBtn = document.getElementById('reset-search');
  
  if (clearFiltersBtn) {
    clearFiltersBtn.addEventListener('click', (e) => {
      e.preventDefault();
      clearFilters();
    });
  }
  
  if (resetSearchBtn) {
    resetSearchBtn.addEventListener('click', (e) => {
      e.preventDefault();
      clearFilters();
    });
  }

  // Modal controls
  const closeModalBtn = document.getElementById('close-modal');
  const backToBrowseBtn = document.getElementById('back-to-browse');
  const addToCartBtn = document.getElementById('add-to-cart');
  const modal = document.getElementById('book-modal');

  if (closeModalBtn) {
    closeModalBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      hideBookDetails();
    });
  }

  if (backToBrowseBtn) {
    backToBrowseBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      hideBookDetails();
    });
  }

  if (addToCartBtn) {
    addToCartBtn.addEventListener('click', (e) => {
      e.preventDefault();
      alert('Book added to cart! (This is a demo feature)');
    });
  }

  // Modal backdrop click
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal || e.target.classList.contains('modal__backdrop')) {
        e.preventDefault();
        e.stopPropagation();
        hideBookDetails();
      }
    });
  }

  // Keyboard navigation for modal
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal && !modal.classList.contains('hidden')) {
      e.preventDefault();
      hideBookDetails();
    }
  });
}

// Initialize application
function init() {
  console.log('Initializing Book Explorer');
  attachEventListeners();
  updateStats();
  renderBooks();
}

// Start the application when DOM is loaded
document.addEventListener('DOMContentLoaded', init);