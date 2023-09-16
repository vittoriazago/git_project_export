# API Exporting git projects information


# Installing packages
pip install -r requirements/development.txt
pip install -r requirements.txt

# Executing project
python -m uvicorn main:app --reload

# Safety check
safety check --stdin