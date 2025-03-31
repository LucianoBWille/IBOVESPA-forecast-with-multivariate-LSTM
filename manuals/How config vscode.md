# How to Configure VS Code for Conda and Jupyter Notebooks

## Steps

### 1. Install Required Extensions
Make sure you have the following VS Code extensions installed:
- **Python** (by Microsoft)
- **Jupyter** (by Microsoft)

You can install these extensions from the Extensions Marketplace in VS Code.

---

### 2. Install IPython Kernel and Add Conda Environment as a Jupyter Kernel
First, ensure your Conda environment is activated. Then, run the following commands:

#### Install IPython Kernel
```bash
conda install ipykernel
```

#### Add Conda Environment as a Jupyter Kernel
Replace `ibovespa-env` with the name of your Conda environment if it's different:
```bash
python -m ipykernel install --user --name ibovespa-env --display-name "Python (ibovespa-env)"
```

This will make your Conda environment available as a kernel in Jupyter.

---

### 3. Set the Python Interpreter in VS Code
To configure VS Code to use your Conda environment:
1. Open the **Command Palette** (`Ctrl+Shift+P` or `F1`).
2. Search for `Python: Select Interpreter`.
3. Select the interpreter corresponding to your Conda environment (e.g., `Python (ibovespa-env)`).

For more details, refer to [How Install and config conda](How Install and config conda.md).

---

### 4. Open and Configure Jupyter Notebooks in VS Code
1. Open your Jupyter Notebook file in VS Code.
2. In the top-right corner of the notebook interface, click the **select kernel** button.
3. Select the kernel corresponding to your Conda environment (e.g., `Python (ibovespa-env)`).

---

### Additional Notes
- If you encounter issues with the kernel not appearing, ensure that the `ipykernel` package is installed in your Conda environment.
- You can verify the available kernels by running:
  ```bash
  jupyter kernelspec list
  ```
- If the kernel is still not listed, repeat step 2 to add the Conda environment as a Jupyter kernel.