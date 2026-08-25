# Experimental Algorithm Analysis
Experimental analysis of algorithmic time complexity developed for the Algorithms and Data Structures coursework.
This project analyzes the empirical performance of algorithms through execution time measurement and graph plotting.

Algorithms evaluated:

Fibonacci (Iterative and Recursive)

Factorial (Iterative and Recursive)

O(N²) Sorting (Iterative and Recursive)

O(N log N) Sorting (Iterative and Recursive)

### Environment Requirements
To run the experiments, ensure you have:

Python >= 3.9 (https://www.python.org/downloads/)

Matplotlib (https://matplotlib.org/stable/install/index.html)

Install dependencies via terminal:
pip install matplotlib

The experiment execution is managed by ExecExperimento.py

### Running in the Terminal
Open the terminal, navigate to the project directory, and execute:
python3 ExecExperimento.py

### Running in VSCode
Open the project folder in VSCode and execute ExecExperimento.py

### Execution Example
The experiment runs sequential tests with inputs ranging from 0 to [n] for the selected algorithm. For example, running Fatorial-Iterativo:

python ExecExperimento.py
[1] -> Fatorial-Iterativo
[2] -> Fatorial-Recursivo
[3] -> Fibonacci-Iterativo
[4] -> Fibonacci-Recursivo
[5] -> OrdenacaoN2-Iterativo
[6] -> OrdenacaoN2-Recursivo
[7] -> OrdenacaoNLog-Iterativo
[8] -> OrdenacaoNLog-Recursivo
Choose an algorithm to execute or [0] to exit: 1
Enter the maximum value for input n: 10
Running Fatorial-Iterativo for input: 0
Running Fatorial-Iterativo for input: 5
Experiment completed for Fatorial-Iterativo with input: 10

When running Fatorial-Iterativo with n=10, the algorithm executes 11 times (from 0 to 10). Execution times for each input are saved as .res text files in the "resultados" folder and are used for plotting charts.

ALERT: For n=10000, the algorithm will execute 10001 times, which may take significant time depending on your machine.

### How to Run Experiments
Determine the maximum input value supported by your hardware:

Fibonacci-Recursivo: test values [10, 20, 30, 40].

OrdenacaoN2-Recursivo: test [5000, 7000, 9000, 10000].
If a maximum recursion depth error occurs, use the previous value as the limit.

### Factorial and Fibonacci Experiments
Run ExecExperimento.py for the maximum input of:

Fatorial-Iterativo

Fatorial-Recursivo

Fibonacci-Iterativo

Fibonacci-Recursivo

### Sorting Experiments
Run ExecExperimento.py for the sorting algorithms:

OrdenacaoN2-Iterativo

OrdenacaoN2-Recursivo

OrdenacaoNLog-Iterativo

OrdenacaoNLog-Recursivo

Test: Run all list variations (sorted, unsorted, reverse sorted); each generates an output file in the "resultados" folder.

### Plotting Charts
Run PlotaGrafico.py in the terminal passing [chart title] [file01] [file02] ... as arguments:

python3 PlotaGrafico.py "Fibonacci vs Factorial" resultados/Fibonacci-Iterativo.res resultados/Fibonacci-Recursivo.res resultados/Fatorial-Iterativo.res resultados/Fatorial-Recursivo.res

### Author
Thiago Gomes de Oliveira
thiago.oliveira.712@ufrn.edu.br
