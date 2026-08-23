# E-Commerce Web Application QA & Automation Framework

An end-to-end Quality Assurance testing suite and Page Object Model (POM) test automation framework built using **Python, Selenium WebDriver, Pytest, and Postman**.

## Project Scope
- **Functional & Regression Testing:** Automated end-to-end user journeys (Auth, Catalog, Cart, Checkout).
- **Negative Validation:** Validated edge cases (locked-out user, invalid credentials).
- **API Testing:** Postman collections for core REST endpoints.
- **CI/CD:** GitHub Actions workflow for automated regression on push/PR.

## Tech Stack
- Python 3.10+, Selenium WebDriver, Pytest, Postman, Git, GitHub Actions

## Setup & Run
```bash
python -m venv venv
source venv/Scripts/activate   # or venv\Scripts\activate on Windows CMD
pip install -r requirements.txt
pytest --html=reports/execution_report.html --self-contained-html