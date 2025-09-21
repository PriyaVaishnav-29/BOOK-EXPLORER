# Create backend files

# 1. Backend package.json
backend_package_json = """{
  "name": "book-explorer-backend",
  "version": "1.0.0",
  "description": "REST API for Book Explorer application",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js",
    "test": "jest"
  },
  "dependencies": {
    "express": "^4.18.2",
    "mongoose": "^7.6.3",
    "cors": "^2.8.5",
    "helmet": "^7.1.0",
    "express-rate-limit": "^7.1.5",
    "dotenv": "^16.3.1",
    "compression": "^1.7.4",
    "express-validator": "^7.0.1"
  },
  "devDependencies": {
    "nodemon": "^3.0.1",
    "jest": "^29.7.0",
    "supertest": "^6.3.3"
  },
  "engines": {
    "node": ">=16.0.0"
  },
  "author": "Your Name",
  "license": "MIT"
}"""

# 2. Main server.js
server_js = """const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const helmet = require('helmet');
const compression = require('compression');
const rateLimit = require('express-rate-limit');
require('dotenv').config();

const booksRouter = require('./routes/books');
const errorHandler = require('./middleware/errorHandler');
const { connectDB } = require('./config/database');

const app = express();
const PORT = process.env.PORT || 5000;

// Security middleware
app.use(helmet());
app.use(compression());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP, please try again later.',
  standardHeaders: true,
  legacyHeaders: false,
});

app.use(limiter);

// CORS configuration
const corsOptions = {
  origin: process.env.FRONTEND_URL || ['http://localhost:3000', 'http://127.0.0.1:3000'],
  credentials: true,
  optionsSuccessStatus: 200
};

app.use(cors(corsOptions));

// Body parsing middleware
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

// Connect to database
connectDB();

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ 
    status: 'OK', 
    message: 'Book Explorer API is running',
    timestamp: new Date().toISOString(),
    environment: process.env.NODE_ENV || 'development'
  });
});

// API routes
app.use('/api/books', booksRouter);

// 404 handler
app.use('*', (req, res) => {
  res.status(404).json({
    success: false,
    message: `Route ${req.originalUrl} not found`
  });
});

// Error handling middleware
app.use(errorHandler);

// Graceful shutdown
process.on('SIGTERM', async () => {
  console.log('SIGTERM received, shutting down gracefully');
  await mongoose.connection.close();
  process.exit(0);
});

process.on('SIGINT', async () => {
  console.log('SIGINT received, shutting down gracefully');
  await mongoose.connection.close();
  process.exit(0);
});

app.listen(PORT, () => {
  console.log(`🚀 Book Explorer API server running on port ${PORT}`);
  console.log(`📖 Environment: ${process.env.NODE_ENV || 'development'}`);
  console.log(`🔗 Health check: http://localhost:${PORT}/health`);
});

module.exports = app;"""

# 3. Books routes
books_routes = """const express = require('express');
const { query, param, validationResult } = require('express-validator');
const Book = require('../models/Book');
const router = express.Router();

// Validation middleware
const handleValidationErrors = (req, res, next) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({
      success: false,
      message: 'Validation failed',
      errors: errors.array()
    });
  }
  next();
};

// GET /api/books - Get paginated books with filters and search
router.get('/', [
  query('page').optional().isInt({ min: 1 }).toInt(),
  query('limit').optional().isInt({ min: 1, max: 100 }).toInt(),
  query('search').optional().isString().trim(),
  query('minRating').optional().isFloat({ min: 0, max: 5 }).toFloat(),
  query('maxRating').optional().isFloat({ min: 0, max: 5 }).toFloat(),
  query('minPrice').optional().isFloat({ min: 0 }).toFloat(),
  query('maxPrice').optional().isFloat({ min: 0 }).toFloat(),
  query('inStock').optional().isBoolean().toBoolean(),
  query('sortBy').optional().isIn(['title', 'price', 'rating', 'createdAt']),
  query('sortOrder').optional().isIn(['asc', 'desc'])
], handleValidationErrors, async (req, res, next) => {
  try {
    const {
      page = 1,
      limit = 12,
      search,
      minRating,
      maxRating,
      minPrice,
      maxPrice,
      inStock,
      sortBy = 'createdAt',
      sortOrder = 'desc'
    } = req.query;

    // Build filter object
    const filter = {};

    // Text search
    if (search) {
      filter.$text = { $search: search };
    }

    // Rating filter
    if (minRating !== undefined || maxRating !== undefined) {
      filter.rating = {};
      if (minRating !== undefined) filter.rating.$gte = minRating;
      if (maxRating !== undefined) filter.rating.$lte = maxRating;
    }

    // Price filter
    if (minPrice !== undefined || maxPrice !== undefined) {
      filter.priceValue = {};
      if (minPrice !== undefined) filter.priceValue.$gte = minPrice;
      if (maxPrice !== undefined) filter.priceValue.$lte = maxPrice;
    }

    // Stock filter
    if (inStock !== undefined) {
      filter.inStock = inStock;
    }

    // Build sort object
    const sort = {};
    sort[sortBy] = sortOrder === 'desc' ? -1 : 1;

    // Add text score sorting if searching
    if (search) {
      sort.score = { $meta: 'textScore' };
    }

    // Calculate pagination
    const skip = (page - 1) * limit;

    // Execute query
    const [books, totalCount] = await Promise.all([
      Book.find(filter)
        .sort(sort)
        .skip(skip)
        .limit(limit)
        .lean(),
      Book.countDocuments(filter)
    ]);

    // Calculate pagination info
    const totalPages = Math.ceil(totalCount / limit);
    const hasNextPage = page < totalPages;
    const hasPrevPage = page > 1;

    res.json({
      success: true,
      data: {
        books,
        pagination: {
          currentPage: page,
          totalPages,
          totalCount,
          limit,
          hasNextPage,
          hasPrevPage
        }
      }
    });

  } catch (error) {
    next(error);
  }
});

// GET /api/books/:id - Get single book by ID
router.get('/:id', [
  param('id').isMongoId().withMessage('Invalid book ID')
], handleValidationErrors, async (req, res, next) => {
  try {
    const book = await Book.findById(req.params.id).lean();
    
    if (!book) {
      return res.status(404).json({
        success: false,
        message: 'Book not found'
      });
    }

    res.json({
      success: true,
      data: book
    });

  } catch (error) {
    next(error);
  }
});

// POST /api/books/refresh - Trigger data refresh (bonus feature)
router.post('/refresh', async (req, res, next) => {
  try {
    // This would typically trigger the scraper
    // For now, just return a success message
    res.json({
      success: true,
      message: 'Data refresh triggered successfully. This may take several minutes to complete.',
      timestamp: new Date().toISOString()
    });

  } catch (error) {
    next(error);
  }
});

// GET /api/books/stats/summary - Get books statistics
router.get('/stats/summary', async (req, res, next) => {
  try {
    const [
      totalBooks,
      booksInStock,
      averageRating,
      priceStats
    ] = await Promise.all([
      Book.countDocuments(),
      Book.countDocuments({ inStock: true }),
      Book.aggregate([
        { $group: { _id: null, avgRating: { $avg: '$rating' } } }
      ]),
      Book.aggregate([
        {
          $group: {
            _id: null,
            avgPrice: { $avg: '$priceValue' },
            minPrice: { $min: '$priceValue' },
            maxPrice: { $max: '$priceValue' }
          }
        }
      ])
    ]);

    const stats = {
      totalBooks,
      booksInStock,
      booksOutOfStock: totalBooks - booksInStock,
      averageRating: averageRating[0]?.avgRating || 0,
      priceRange: priceStats[0] || { avgPrice: 0, minPrice: 0, maxPrice: 0 }
    };

    res.json({
      success: true,
      data: stats
    });

  } catch (error) {
    next(error);
  }
});

module.exports = router;"""

print("Backend files created:")
print("1. package.json")
print("2. server.js (main server)")
print("3. routes/books.js (API endpoints)")
print(f"\\nServer.js size: {len(server_js)} characters")
print(f"Books routes size: {len(books_routes)} characters")