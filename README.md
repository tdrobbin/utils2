# utils2

As separate steps
```
# Step 1: Create the Conda environment
conda create -n uv310l pip -y

# After creation, activate the environment in the terminal
# Step 2: Activate the Conda environment (this might need to be done in a new command line prompt)
conda activate uv310l

# Step 3: Install 'uv' using pip (assumes 'pip' was installed in the environment)
pip install uv

# Step 4: Use 'uv' for requirement management (assuming 'uv' has similar functionality to 'pip-tools')
uv compile requirements-uv310l.in -o requirements-uv310l.txt
uv sync requirements-uv310l.txt
```

As one step
```
conda create -n uv310l pip -y && \
bash -c "source activate uv310l && pip install uv && uv compile requirements-uv310l.in -o requirements-uv310l.txt && uv sync requirements-uv310l.txt"

```