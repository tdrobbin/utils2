# utils2

As separate steps
```
# Create the Conda environment and install uv
conda create -n uv310m python=3.10 -y && conda activate uv310m && pip install uv

# Use 'uv' for requirement management (assuming 'uv' has similar functionality to 'pip-tools')
uv compile requirements-uv310m.in -o requirements-uv310m-arm64.txt

# sync it up
uv sync requirements-uv310m.txt
```

As one step
```
conda create -n uv310m python=3.10 -y && conda activate uv310m && pip install uv && \
uv compile requirements-uv310m.in -o requirements-uv310m-arm64.txt && \
uv sync requirements-uv310m-arm64.txt
```