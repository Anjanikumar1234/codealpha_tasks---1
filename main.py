import time
import functools
import matplotlib.pyplot as plt

# Iterative Fibonacci
def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Recursive Fibonacci with Memoization
@functools.lru_cache(maxsize=None)
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Generator-based Fibonacci
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Visualizing Fibonacci Sequence
def visualize_fibonacci(sequence):
    plt.figure(figsize=(10, 5))
    plt.bar(range(min(len(sequence), 50)), sequence[:50], color='skyblue')

    plt.xlabel("Index")
    plt.ylabel("Fibonacci Number")
    plt.title("Fibonacci Sequence Visualization")
    plt.show()

# CLI User Interface
def main():
    try:
        n = int(input("Enter number of terms: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return

        method = input("Choose method - Iterative (i), Recursive (r), Generator (g): ").strip().lower()

        start_time = time.time()

        if method == 'i':
            result = fibonacci_iterative(n)
        elif method == 'r':
            result = [fibonacci_recursive(i) for i in range(n)]
        elif method == 'g':
            result = list(fibonacci_generator(n))
        else:
            print("Invalid choice!")
            return
        
        print("Fibonacci Sequence:", result)

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


    except ValueError:
        print("Invalid input! Please enter a valid integer.")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

    
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds")

    visualize_fibonacci(result)

if __name__ == "__main__":
    main()
    # Performance comparison
    def compare_methods(n):
        methods = {
            'Iterative': lambda: fibonacci_iterative(n),
            'Recursive': lambda: [fibonacci_recursive(i) for i in range(n)],
            'Generator': lambda: list(fibonacci_generator(n))
        }
        
        results = {}
        for name, func in methods.items():
            start = time.time()
            func()
            end = time.time()
            results[name] = end - start
            
        # Plot performance comparison
        plt.figure(figsize=(10, 5))
        plt.bar(results.keys(), results.values(), color=['lightblue', 'lightgreen', 'coral'])
        plt.xlabel("Method")
        plt.ylabel("Time (seconds)")
        plt.title("Performance Comparison of Fibonacci Methods")
        plt.show()
        
        # Print detailed results
        print("\nPerformance Results:")
        for method, duration in results.items():
            print(f"{method}: {duration:.6f} seconds")
