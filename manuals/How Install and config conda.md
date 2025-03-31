# Install Anaconda (conda)
Follow the steps on [Anaconda Documentation](https://www.anaconda.com/docs/getting-started/anaconda/install) to ensure a correct installation. Select your operating system in the "Basic install instructions" section and follow their instructions.

# Create environment (with dependencies) for the project in Conda
1. Open a terminal.
2. Navigate to the project directory where the `environment.yml` file is located.
   ```bash
   cd /path/to/project
   ```
3. Run the following command to create the environment:
   ```bash
   conda env create -f environment.yml
   ```
   This will also install the dependencies listed in the `environment.yml` file.
4. Activate the environment:
   ```bash
   conda activate ibovespa-env
   ```

# Additional Conda Commands
- **Install additional packages**: If you need to install more packages, use:
  ```bash
  conda install <package-name>
  ```
  For example, to install `scikit-learn`:
  ```bash
  conda install scikit-learn
  ```

- **Update the environment**: If the `environment.yml` file is updated, apply the changes with:
  ```bash
  conda env update -f environment.yml --prune
  ```

- **Export the environment**: To share the environment, export it to a new `environment.yml` file:
  ```bash
  conda env export --no-builds > environment.yml
  ```

- **Remove the environment**: If you no longer need the environment, remove it with:
  ```bash
  conda env remove -n ibovespa-env
  ```

# Verify Installation
To ensure everything is set up correctly, check the installed packages:
```bash
conda list
```