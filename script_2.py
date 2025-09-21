# Create scraper files

# 1. Scraper package.json
scraper_package_json = """{
  "name": "book-scraper",
  "version": "1.0.0",
  "description": "Book data scraper for Books to Scrape website",
  "main": "scraper.js",
  "scripts": {
    "start": "node scraper.js",
    "dev": "nodemon scraper.js"
  },
  "dependencies": {
    "puppeteer": "^21.3.8",
    "mongoose": "^7.6.3",
    "dotenv": "^16.3.1",
    "axios": "^1.5.1",
    "cheerio": "^1.0.0-rc.12",
    "node-cron": "^3.0.2"
  },
  "devDependencies": {
    "nodemon": "^3.0.1"
  },
  "author": "Your Name",
  "license": "MIT"
}"""

# 2. Scraper main script
scraper_js = """const puppeteer = require('puppeteer');
const mongoose = require('mongoose');
require('dotenv').config();
const Book = require('./models/Book');

const BASE_URL = 'https://books.toscrape.com';
const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://localhost:27017/bookexplorer';

class BookScraper {
  constructor() {
    this.browser = null;
    this.page = null;
  }

  async initialize() {
    try {
      // Connect to MongoDB
      await mongoose.connect(MONGODB_URI);
      console.log('Connected to MongoDB');

      // Launch browser
      this.browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
      });
      
      this.page = await this.browser.newPage();
      await this.page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36');
      
      console.log('Browser initialized');
    } catch (error) {
      console.error('Initialization failed:', error);
      throw error;
    }
  }

  async scrapeBookDetails(bookUrl) {
    try {
      await this.page.goto(bookUrl, { waitUntil: 'networkidle0' });

      const bookDetails = await this.page.evaluate(() => {
        const getStockNumber = (text) => {
          const match = text.match(/\\((\\d+) available\\)/);
          return match ? parseInt(match[1]) : 0;
        };

        const getRatingNumber = (className) => {
          const ratingMap = {
            'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5
          };
          const ratingClass = className.split(' ').find(cls => ratingMap[cls]);
          return ratingMap[ratingClass] || 0;
        };

        const title = document.querySelector('h1')?.textContent?.trim();
        const price = document.querySelector('p.price_color')?.textContent?.trim();
        const stockText = document.querySelector('p.availability')?.textContent?.trim();
        const stock = getStockNumber(stockText);
        const inStock = stockText?.includes('In stock') || false;
        const ratingClass = document.querySelector('p.star-rating')?.className || '';
        const rating = getRatingNumber(ratingClass);
        const imageUrl = document.querySelector('img')?.src;
        const description = document.querySelector('#product_description + p')?.textContent?.trim();

        return {
          title,
          price,
          stock,
          inStock,
          rating,
          imageUrl: imageUrl ? new URL(imageUrl, window.location.href).href : null,
          description,
          detailUrl: window.location.href
        };
      });

      return bookDetails;
    } catch (error) {
      console.error(`Error scraping book details from ${bookUrl}:`, error);
      return null;
    }
  }

  async scrapeBooksFromPage(pageUrl) {
    try {
      console.log(`Scraping page: ${pageUrl}`);
      await this.page.goto(pageUrl, { waitUntil: 'networkidle0' });

      const bookLinks = await this.page.evaluate(() => {
        const books = Array.from(document.querySelectorAll('article.product_pod'));
        return books.map(book => {
          const linkElement = book.querySelector('h3 a');
          const imageElement = book.querySelector('div.image_container img');
          const priceElement = book.querySelector('p.price_color');
          const ratingElement = book.querySelector('p.star-rating');
          const stockElement = book.querySelector('p.availability');

          return {
            title: linkElement?.getAttribute('title') || '',
            detailUrl: linkElement?.href ? new URL(linkElement.href, window.location.href).href : '',
            imageUrl: imageElement?.src ? new URL(imageElement.src, window.location.href).href : '',
            price: priceElement?.textContent?.trim() || '',
            rating: ratingElement?.className || '',
            availability: stockElement?.textContent?.trim() || ''
          };
        });
      });

      // Get detailed information for each book
      const detailedBooks = [];
      for (const book of bookLinks) {
        if (book.detailUrl) {
          const details = await this.scrapeBookDetails(book.detailUrl);
          if (details) {
            detailedBooks.push({
              ...book,
              ...details
            });
          }
        }
        // Add delay to be respectful to the server
        await new Promise(resolve => setTimeout(resolve, 1000));
      }

      return detailedBooks;
    } catch (error) {
      console.error(`Error scraping page ${pageUrl}:`, error);
      return [];
    }
  }

  async getNextPageUrl() {
    try {
      return await this.page.evaluate(() => {
        const nextButton = document.querySelector('li.next a');
        return nextButton ? new URL(nextButton.href, window.location.href).href : null;
      });
    } catch (error) {
      return null;
    }
  }

  async scrapeAllBooks() {
    try {
      let currentPageUrl = BASE_URL;
      let allBooks = [];
      let pageCount = 0;

      while (currentPageUrl && pageCount < 50) { // Limit to 50 pages as safety
        console.log(`\\nProcessing page ${pageCount + 1}...`);
        
        const booksFromPage = await this.scrapeBooksFromPage(currentPageUrl);
        allBooks = allBooks.concat(booksFromPage);
        
        console.log(`Found ${booksFromPage.length} books on this page`);
        console.log(`Total books collected: ${allBooks.length}`);

        // Get next page URL
        await this.page.goto(currentPageUrl, { waitUntil: 'networkidle0' });
        currentPageUrl = await this.getNextPageUrl();
        pageCount++;

        if (!currentPageUrl) {
          console.log('No more pages found');
          break;
        }
      }

      return allBooks;
    } catch (error) {
      console.error('Error scraping all books:', error);
      throw error;
    }
  }

  async saveToDatabase(books) {
    try {
      console.log(`\\nSaving ${books.length} books to database...`);
      
      // Clear existing data
      await Book.deleteMany({});
      console.log('Cleared existing books from database');

      // Save new data
      const savedBooks = await Book.insertMany(books, { ordered: false });
      console.log(`Successfully saved ${savedBooks.length} books to database`);

      return savedBooks;
    } catch (error) {
      console.error('Error saving to database:', error);
      throw error;
    }
  }

  async cleanup() {
    try {
      if (this.browser) {
        await this.browser.close();
        console.log('Browser closed');
      }
      await mongoose.connection.close();
      console.log('Database connection closed');
    } catch (error) {
      console.error('Error during cleanup:', error);
    }
  }

  async run() {
    try {
      console.log('Starting Book Explorer Scraper...');
      console.log('Target website:', BASE_URL);
      
      await this.initialize();
      const books = await this.scrapeAllBooks();
      
      if (books.length > 0) {
        await this.saveToDatabase(books);
        console.log(`\\n✅ Scraping completed successfully!`);
        console.log(`📚 Total books scraped: ${books.length}`);
      } else {
        console.log('❌ No books were scraped');
      }

    } catch (error) {
      console.error('❌ Scraping failed:', error);
    } finally {
      await this.cleanup();
    }
  }
}

// Run the scraper
if (require.main === module) {
  const scraper = new BookScraper();
  scraper.run().catch(console.error);
}

module.exports = BookScraper;"""

# 3. Book model for scraper
book_model_scraper = """const mongoose = require('mongoose');

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
    required: true
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
  if (this.price) {
    const match = this.price.match(/([0-9.]+)/);
    this.priceValue = match ? parseFloat(match[0]) : 0;
  }
  next();
});

// Indexes for efficient querying
bookSchema.index({ title: 'text' });
bookSchema.index({ priceValue: 1, rating: 1, inStock: 1 });

module.exports = mongoose.model('Book', bookSchema);"""

# 4. Database config for scraper
database_config_scraper = """const mongoose = require('mongoose');
require('dotenv').config();

const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://localhost:27017/bookexplorer';

const connectDB = async () => {
  try {
    const conn = await mongoose.connect(MONGODB_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });

    console.log(`MongoDB Connected: ${conn.connection.host}`);
    return conn;
  } catch (error) {
    console.error('Database connection error:', error);
    process.exit(1);
  }
};

const closeDB = async () => {
  try {
    await mongoose.connection.close();
    console.log('MongoDB connection closed');
  } catch (error) {
    console.error('Error closing database connection:', error);
  }
};

module.exports = {
  connectDB,
  closeDB,
  MONGODB_URI
};"""

# 5. Environment example for scraper
scraper_env_example = """# MongoDB Connection
MONGODB_URI=mongodb://localhost:27017/bookexplorer

# Or use MongoDB Atlas
# MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/bookexplorer

# Scraper Settings
SCRAPER_DELAY=1000
MAX_PAGES=50
HEADLESS_MODE=true

# Cron Schedule (optional)
CRON_SCHEDULE=0 2 * * *"""

print("Scraper files created:")
print("1. package.json")
print("2. scraper.js (main scraping logic)")
print("3. models/Book.js (MongoDB schema)")
print("4. config/database.js (DB connection)")
print("5. .env.example (environment variables)")
print(f"\nScraper script size: {len(scraper_js)} characters")