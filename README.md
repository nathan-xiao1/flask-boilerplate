# Minimal Flask Boilerplate

This is a minimal pre-setup of the popular Flask framework.

## Setup

```bash
# Clone the git repository
git clone git@github.com:nathan-xiao1/flask-boilerplate.git

# Navigate into newly cloned repository folder
cd flask-boilerplate

# [Optional but recommended]
# Setup virtual environment 
virtualenv -p python3 env

# Activate the virtual environment
source env/bin/activate

# Install the required modules
pip install -r requirements.txt

# Run Flask!
python run.py
```

## Includes
- Bootstrap via CDN
	- Latest compiled and minified CSS
	- Latest compiled JavaScript
- jQuery library via CDN
- Basic `base.html` template
- Dummy `JS` and `CSS` file
- Automatically uses next available port
