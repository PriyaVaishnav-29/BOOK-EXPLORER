# Create remaining backend files

# 1. Backend Book model (same as scraper but can be separate)
backend_book_model = """const mongoose = require('mongoose');

const bookSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
    trim: true,
    index: true
  },
  price: {
    type: String,
    required: true
  },
  priceValue: {
    type: Number,
    index: true
  },
  stock: {
    type: Number,
    default: 0,
    index: true
  },
  inStock: {
    type: Boolean,
    default: false,
    index: true
  },
  rating: {
    type: Number,
    min: 0,
    max: 5,
    default: 0,
    index: true
  },
  imageUrl: {
    type: String
  },
  detailUrl: {
    type: String,
    required: true,
    unique: true
  },
  description: {
    type: String
  },
  availability: {
    type: String
  }
}, {
  timestamps: true
});

// Extract numeric price value before saving
bookSchema.pre('save', function(next) {
  if (this.price && this.isModified('price')) {
    const match = this.price.match(/([0-9.]+)/);
    this.priceValue = match ? parseFloat(match[0]) : 0;
  }
  next();
});

// Indexes for efficient querying
bookSchema.index({ title: 'text', description: 'text' });
bookSchema.index({ priceValue: 1, rating: -1, inStock: -1 });
bookSchema.index({ createdAt: -1 });

// Virtual for formatted price
bookSchema.virtual('formattedPrice').get(function() {
  return this.priceValue ? `£${this.priceValue.toFixed(2)}` : this.price;
});

// Ensure virtual fields are serialized
bookSchema.set('toJSON', {
  virtuals: true,
  transform: function(doc, ret) {
    delete ret.__v;
    return ret;
  }
});

module.exports = mongoose.model('Book', bookSchema);"""

# 2. Backend database config
backend_database_config = """const mongoose = require('mongoose');
require('dotenv').config();

const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://localhost:27017/bookexplorer';

const connectDB = async () => {
  try {
    mongoose.set('strictQuery', true);
    
    const conn = await mongoose.connect(MONGODB_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });

    console.log(`🔗 MongoDB Connected: ${conn.connection.host}`);
    console.log(`📊 Database: ${conn.connection.name}`);
    
    // Handle connection events
    mongoose.connection.on('error', (err) => {
      console.error('MongoDB connection error:', err);
    });

    mongoose.connection.on('disconnected', () => {
      console.log('MongoDB disconnected');
    });

    return conn;
  } catch (error) {
    console.error('❌ Database connection failed:', error.message);
    process.exit(1);
  }
};

const closeDB = async () => {
  try {
    await mongoose.connection.close();
    console.log('✅ MongoDB connection closed');
  } catch (error) {
    console.error('❌ Error closing database connection:', error);
  }
};

module.exports = {
  connectDB,
  closeDB,
  MONGODB_URI
};"""

# 3. Error handler middleware
error_handler = """const errorHandler = (error, req, res, next) => {
  console.error('Error Stack:', error.stack);

  // Default error
  let statusCode = 500;
  let message = 'Internal Server Error';
  let details = null;

  // Mongoose validation error
  if (error.name === 'ValidationError') {
    statusCode = 400;
    message = 'Validation Error';
    details = Object.values(error.errors).map(err => ({
      field: err.path,
      message: err.message,
      value: err.value
    }));
  }

  // Mongoose cast error (invalid ObjectId)
  if (error.name === 'CastError') {
    statusCode = 400;
    message = 'Invalid ID format';
    details = { field: error.path, value: error.value };
  }

  // MongoDB duplicate key error
  if (error.code === 11000) {
    statusCode = 409;
    message = 'Duplicate entry';
    const field = Object.keys(error.keyValue)[0];
    details = { field, message: `${field} already exists` };
  }

  // JWT errors (if using authentication)
  if (error.name === 'JsonWebTokenError') {
    statusCode = 401;
    message = 'Invalid token';
  }

  if (error.name === 'TokenExpiredError') {
    statusCode = 401;
    message = 'Token expired';
  }

  // Custom API errors
  if (error.isOperational) {
    statusCode = error.statusCode;
    message = error.message;
    details = error.details;
  }

  const errorResponse = {
    success: false,
    error: {
      message,
      ...(process.env.NODE_ENV === 'development' && { 
        stack: error.stack,
        details 
      }),
      ...(details && process.env.NODE_ENV === 'production' && { details })
    },
    timestamp: new Date().toISOString(),
    path: req.originalUrl,
    method: req.method
  };

  res.status(statusCode).json(errorResponse);
};

// Custom API Error class
class APIError extends Error {
  constructor(message, statusCode = 500, details = null) {
    super(message);
    this.statusCode = statusCode;
    this.details = details;
    this.isOperational = true;

    Error.captureStackTrace(this, this.constructor);
  }
}

module.exports = {
  errorHandler,
  APIError
};"""

# 4. CORS middleware (optional separate file)
cors_middleware = """const cors = require('cors');

const corsOptions = {
  origin: function (origin, callback) {
    // Define allowed origins
    const allowedOrigins = [
      'http://localhost:3000',
      'http://127.0.0.1:3000',
      'https://your-frontend-domain.vercel.app',
      'https://your-frontend-domain.netlify.app'
    ];

    // Allow requests with no origin (mobile apps, postman, etc.)
    if (!origin) return callback(null, true);

    if (process.env.NODE_ENV === 'development') {
      return callback(null, true);
    }

    if (allowedOrigins.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Not allowed by CORS'));
    }
  },
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'],
  allowedHeaders: [
    'Origin',
    'X-Requested-With', 
    'Content-Type',
    'Accept',
    'Authorization'
  ],
  preflightContinue: false,
  optionsSuccessStatus: 200
};

module.exports = cors(corsOptions);"""

# 5. Backend environment example
backend_env_example = """# Server Configuration
PORT=5000
NODE_ENV=development

# Database
MONGODB_URI=mongodb://localhost:27017/bookexplorer
# For MongoDB Atlas:
# MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/bookexplorer

# CORS Origins (comma-separated)
FRONTEND_URL=http://localhost:3000

# Rate Limiting
RATE_LIMIT_WINDOW_MS=900000
RATE_LIMIT_MAX_REQUESTS=100

# Security
JWT_SECRET=your-super-secret-jwt-key-here
JWT_EXPIRE=7d

# API Settings
API_VERSION=v1
API_PREFIX=/api

# Logging
LOG_LEVEL=info"""

print("Additional backend files created:")
print("1. models/Book.js (MongoDB schema)")
print("2. config/database.js (DB connection)")
print("3. middleware/errorHandler.js (error handling)")
print("4. middleware/cors.js (CORS configuration)")
print("5. .env.example (environment variables)")
print(f"\\nTotal backend file sizes:")
print(f"- Book model: {len(backend_book_model)} characters")
print(f"- Error handler: {len(error_handler)} characters")