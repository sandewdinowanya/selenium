# selenium

A small repository for Selenium WebDriver tests and utilities.

## Contents

- tests/ - Selenium test scripts
- drivers/ - Browser driver helpers and configuration
- examples/ - Example scripts showing how to use the helpers

## Requirements

- Python 3.8+
- pip
- Google Chrome or Mozilla Firefox (or another supported browser)
- Corresponding WebDriver (chromedriver/geckodriver)

## Installation

1. Create and activate a virtual environment:

   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate    # Windows

2. Install dependencies (if a requirements.txt exists):

   pip install -r requirements.txt

## Usage

- Update the drivers in drivers/ or ensure the webdriver is in your PATH.
- Run tests with pytest (if tests use pytest):

  pytest

- To run an example script:

  python examples/example_test.py

## Contributing

Contributions are welcome. Please open issues or pull requests with clear descriptions of changes.

## License

This project does not include a license file. Add one if you intend to make the project open source.
