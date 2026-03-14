# Fractional Stirling Triangle Generator

This repository contains a symbolic computation engine for generating generalized Stirling-type triangles, as presented in the research paper **"Fractional Stirling Numbers: Delta Operators and Weighted Ferrers Geometry"** by Derek Streidl and Udita Katugampola (2026).

The core of this project is the implementation of a universal recurrence relation derived from the iteration of a generalized fractional delta-derivative operator:

$$\delta_{r,1}=x^{r}\frac{d}{dx}$$

By treating the parameter $r$ as a real number rather than a fixed integer, this tool explores the "continuous deformation" of classical combinatorial structures.

---

## 🚀 Key Features

* **Symbolic Precision**: Utilizes Python’s `fractions` module to maintain exact rational values, preventing floating-point drift during deep triangle generation.
* **Universal Recurrence**: Implements the operator-induced formula:
    $S_r(n+1, k) = ((r-1)(n-1) + k)S_r(n, k) + S_r(n, k-1)$
* **OEIS Alignment**: Handles the reindexing required for higher-order cases (e.g., $r=3$) to match established sequences like **A265649**.
* **Integerization**: Automatically calculates the LCM of denominators to produce the "integer form" of fractional triangles for easier pattern recognition.

---

## 🛠 Installation

No external dependencies are required. The script runs on any standard Python 3.x environment.

```bash
# Clone the repository
git clone [https://github.com/](https://github.com/)[your-username]/fractional-stirling-generator.git
cd fractional-stirling-generator