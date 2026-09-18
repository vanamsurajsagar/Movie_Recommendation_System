# 🎬 Movie Recommendation System

A simple **content-based Movie Recommendation System** built with **Python and NumPy**. The system recommends a movie based on the similarity between a user's preferences and predefined movie preference vectors.

The project demonstrates how **vector representation and Euclidean distance** can be used to build a basic recommendation system.

---

## 📌 Project Overview

This project takes the user's preferences for three movie characteristics:

* 🎬 Action
* 😂 Comedy
* 🔍 Suspense

The user provides a preference score from **-5 to +5** for each category.

These preferences are converted into a numerical vector and compared with predefined movie vectors using **Euclidean distance**.

The movie with the **smallest distance** from the user's preference vector is recommended.

---

## ⚙️ How It Works

The recommendation process is:

```text
User Preferences
       ↓
Action, Comedy, Suspense
       ↓
Convert Preferences into NumPy Vector
       ↓
Compare with Movie Vectors
       ↓
Calculate Euclidean Distance
       ↓
Find Minimum Distance
       ↓
🎬 Recommended Movie
```

### Example

If the user enters:

```text
Action: 3
Comedy: 1
Suspense: 4
```

The user's preference vector becomes:

```python
[3, 1, 4]
```

The system compares this vector with every movie in the database.

For example:

```python
Movie 1 = [2, 1, 3]
Movie 2 = [5, 1, 4]
Movie 3 = [1, 2, 1]
```

The Euclidean distance is calculated for each movie.

The movie with the **lowest distance** is selected as the recommendation.

---

## 🧮 Algorithm

The system uses **Euclidean Distance** to measure how close a movie is to the user's preferences.

The formula is:

$$
d = \sqrt{(x_1-y_1)^2 + (x_2-y_2)^2 + (x_3-y_3)^2}
$$

Where:

* `x` = user's preference vector
* `y` = movie preference vector
* `d` = Euclidean distance

A **smaller distance means greater similarity** between the user's preferences and the movie.

---

## 🛠️ Technologies Used

| Technology         | Usage                                           |
| ------------------ | ----------------------------------------------- |
| Python             | Core programming language                       |
| NumPy              | Numerical operations and vector calculations    |
| Euclidean Distance | Measuring similarity between preference vectors |

---

## 📂 Project Structure

```text
Movie_Recommendation_System/
│
├── Movie recomendation model.py
│
├── README.md
│
└── .gitignore
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vanamsurajsagar/Movie_Recommendation_System.git
```

### 2. Navigate to the Project

```bash
cd Movie_Recommendation_System
```

### 3. Install NumPy

```bash
pip install numpy
```

### 4. Run the Program

```bash
python "Movie recomendation model.py"
```

---

## 💻 Example

### Input

```text
Enter your preferences (scale -5 to +5)

Action: 2
Comedy: 1
Suspense: 3
```

### Output

```text
Movie 1 distance: 0.00
Movie 2 distance: 3.00
Movie 3 distance: 2.45
Movie 4 distance: 5.48
Movie 5 distance: 3.16

Recommended Movie: Movie 1
```

*The exact distances and recommendation depend on the user's input.*

---

## 🧠 Key Concepts Demonstrated

This project demonstrates the fundamentals of:

* Python dictionaries
* User input handling
* NumPy arrays
* Vector representation
* Euclidean distance
* Iterating through a movie database
* Finding the minimum distance
* Basic recommendation system logic

---

## 🎯 Learning Objective

The main objective of this project is to understand the fundamental idea behind **similarity-based recommendation systems**.

Instead of using a complex machine learning model, the system represents both the user and movies as vectors and calculates their distance.

This provides a simple introduction to concepts that are commonly used in more advanced recommendation systems.

---

## 🔮 Future Improvements

The current implementation uses a small manually defined movie database. It can be extended with:

* 📚 A larger movie dataset
* 🎞️ Real movie names and genres
* ⭐ User ratings
* 🔢 Top-N movie recommendations
* 📊 Movie datasets using Pandas
* 🎯 Cosine similarity
* 👥 Collaborative filtering
* 🤖 Machine-learning-based recommendation techniques
* 🌐 Streamlit web interface
* 🚀 Online deployment
* 🖼️ Movie posters and additional movie information

---

## 👨‍💻 Author

**Vanam Surajsagar**

B.Tech Computer Science & Engineering
AI & Machine Learning

### GitHub

https://github.com/vanamsurajsagar

### Project Repository

https://github.com/vanamsurajsagar/Movie_Recommendation_System

---

## ⭐ Project Status

**Status:** Basic Recommendation System

This project is currently an educational implementation focused on understanding **vector-based similarity and recommendation logic**.

---

## 📄 License

This project is created for **educational and learning purposes**.
