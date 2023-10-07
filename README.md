# API Exporting git projects information


# Installing packages

Local enviroment:

```pip install -r requirements/development.txt```

Production enviroment:

```pip install -r requirements.txt```

# Executing project

```python -m uvicorn app.main:app --reload```

# Safety check
```safety check --stdin```

# Lint check
```flake8```

# Docker image
Building:

```docker build . -t git_export```

Running:

```docker run -d --name git_export -p 80:80 --env-file .env git_export```