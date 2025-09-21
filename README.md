# BOOK EXPLORER

[README.md](https://github.com/user-attachments/files/22450036/README.md)

---

# 📚 Book Explorer

Book Explorer is a web-based application that allows users to browse, filter, and explore books.
The project uses **Python scripts** for data generation and **ReactJS** for the front-end.

---

## 🚀 Features

* 🔎 **Search** books by title
* ⭐ **Filter** by minimum rating, price range, and stock availability
* 🔄 **Sort** books by title, price, rating, or stock
* 📊 **Live statistics**: total books, in-stock books, and average rating
* 📖 **Book details modal** with description, rating, and price
* 🛒 Demo **Add to Cart** functionality

---

## 🛠️ Tech Stack

* **Frontend:** ReactJS (with vanilla JS components for some logic in `app_1.js` and `app_2.js`)
* **Backend/Data Preparation:** Python scripts (`script_1.py` … `script_9.py`) to scrape, clean, or format book data
* **Styling:** CSS (`style.css`)
* **Data Source:** Generated JSON/JS objects from scripts

---

## 📂 Project Structure

```bash
.
├── scripts/               # Data preparation scripts
│   ├── script_1.py
│   ├── script_2.py
│   ├── ...
│   └── script_9.py
│
├── src/                   # Frontend React code
│   ├── app_1.js
│   ├── app_2.js
│   └── components/
│
├── public/                # Static assets (index.html, icons, etc.)
│
├── style.css              # Global styles
├── README.md              # Project documentation
└── package.json           # React dependencies
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2️⃣ Install Dependencies

```bash
npm install
```

### 3️⃣ Run Python Scripts (if needed to regenerate data)

```bash
cd scripts
python script_1.py
python script_2.py
# ... repeat up to script_9.py
```

### 4️⃣ Start the Development Server

```bash
npm start
```

The app will be available at **[http://localhost:3000/](http://localhost:3000/)**

---

## 📸 Screenshots

*(Add screenshots of your app UI here)*

---

## 🔮 Future Improvements

* [ ] Persistent cart with **localStorage**
* [ ] API integration for real book datasets
* [ ] Authentication & user favorites
* [ ] Deployment on **Vercel/Netlify**

---

## 👩‍💻 Author

* **Your Name** – [GitHub](https://github.com/<your-username>)

---

