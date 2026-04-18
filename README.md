
# Statistical Mechanics: Algorithms and Computations (Coursera)

This repository contains my implementations of the programming exercises and algorithms from the Coursera course **Statistical Mechanics: Algorithms and Computations**.

All code has been adapted to **Python 3**, with performance improvements using **NumPy** and **Numba** wherever appropriate.

---

## 📌 Overview

The goal of this repository is to:

* Reproduce key algorithms from statistical mechanics
* Provide clean, readable implementations in modern Python
* Explore computational techniques such as Monte Carlo sampling and Markov chains
* Improve performance using vectorization and JIT compilation

---

## ⚙️ Tech Stack

* Python 3
* NumPy
* Numba
* Jupyter Notebook

---

## 🚀 Features

* Python 3-compatible implementations (original course uses Python 2)
* Optimized numerical computations using NumPy
* Accelerated loops with Numba (`@njit` where beneficial)
* Organized as Jupyter notebooks for clarity and experimentation

---

## 📂 Repository Structure

```
.
├── notebooks/
│   ├── week1_*.ipynb
│   ├── week2_*.ipynb
│   └── ...
├── utils/
│   └── helper_functions.py
├── requirements.txt
└── README.md
```

---

## 📊 Topics Covered

* Markov Chain Monte Carlo (MCMC)
* Metropolis Algorithm
* Sampling techniques
* Random walks
* Ising model simulations
* Statistical estimators

---

## 🧪 Running the Notebooks

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Launch Jupyter:

   ```bash
   jupyter notebook
   ```

---

## ⚡ Notes on Performance

Some algorithms in the course can be computationally intensive. To address this:

* **NumPy** is used for vectorized operations
* **Numba** is applied to critical sections to speed up loops
* In some cases, performance improvements can be **orders of magnitude faster** compared to naive implementations

---

## 🧠 Motivation

This repository serves as:

* A personal reference for statistical mechanics algorithms
* A Python 3 modernized version of the course material
* A foundation for further experimentation and optimization

---

## ⚠️ Disclaimer

This repository is intended for educational purposes. It follows the structure of the Coursera course but is independently implemented.

---

## 📎 References

* Coursera: *Statistical Mechanics: Algorithms and Computations*

---

## 📬 Contributing

Feel free to open issues or submit pull requests if you’d like to improve implementations or add optimizations.

---
