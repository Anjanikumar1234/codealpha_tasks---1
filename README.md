# codealpha_tasks---1

# Fibonacci Sequence Generator

## 📌 Description
This Python program generates Fibonacci numbers using three different methods:  
✅ **Iterative** (Efficient for large numbers)  
✅ **Recursive with Memoization** (Uses caching to improve performance)  
✅ **Generator-based** (Memory-efficient approach)  

Additionally, it provides a **visual representation** of the Fibonacci sequence using a **bar chart**.

---

## 🛠 Installation
To run this project, ensure you have Python installed. You can download it from:  
🔗 [Python Official Website](https://www.python.org/downloads/)

### Required Dependencies
This project requires the following Python libraries:  
- **functools** (built-in, no installation needed)  
- **time** (built-in, no installation needed)  
- **matplotlib** (for visualization)

To install `matplotlib`, run:  
```bash
pip install matplotlib
```

---

## 🚀 How to Run
Run the program using:  
```bash
python main.py
```

It will prompt you for:  
1️⃣ The number of Fibonacci terms to generate  
2️⃣ The method you want to use:  
   - **Iterative (i)**
   - **Recursive (r)**
   - **Generator (g)**

---

## 📊 Example Runs
### Example 1 - Iterative
```
Enter number of terms: 10
Choose method - Iterative (i), Recursive (r), Generator (g): i
Fibonacci Sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Time taken: 0.000002 seconds
```
*(A bar chart of the sequence is displayed.)*

### Example 2 - Recursive
```
Enter number of terms: 7
Choose method - Iterative (i), Recursive (r), Generator (g): r
Fibonacci Sequence: [0, 1, 1, 2, 3, 5, 8]
Time taken: 0.000010 seconds
```
*(A bar chart of the sequence is displayed.)*

### Example 3 - Generator
```
Enter number of terms: 5
Choose method - Iterative (i), Recursive (r), Generator (g): g
Fibonacci Sequence: [0, 1, 1, 2, 3]
Time taken: 0.000004 seconds
```
*(A bar chart of the sequence is displayed.)*

---

## ⏳ Performance Comparison
To compare the execution time of all three methods, run:
```python
compare_methods(n)
```

### Example Output
```
Performance Results:
Iterative: 0.000003 seconds
Recursive: 0.000010 seconds
Generator: 0.000004 seconds
```
*A bar chart comparing execution times will be displayed.*

---

## 💡 Key Features
✅ Three Fibonacci generation methods  
✅ Execution time comparison for performance analysis  
✅ Graphical visualization of Fibonacci sequences  
✅ Efficient use of caching with `functools.lru_cache`  
✅ Memory-efficient generator implementation  

---

## 🤝 Contributing
Want to improve this project? Feel free to:  
🔹 Fork the repository  
🔹 Create a new branch  
🔹 Submit a pull request  

Your contributions are always welcome! 😊

---

## 📜 License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

### 🚀 Happy Coding! 🎯

