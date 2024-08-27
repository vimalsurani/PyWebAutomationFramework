- Name - Vimal Surani
- Author - Vimal Surani

### Web Automation Framework with POM in Python(Selenium)

- Python, PyTest
- Selenium
- Allure Report
- Gitignore, PyTest Report
- Page Object Model and Page Factory both
- Highlight element while run
- Parallel Run with xdist
- MY SQL data base connect to verify data.

### Folder Structure

![image](https://github.com/user-attachments/assets/b324f64f-86d3-4597-961d-ae85ab364e85)

### CI/CD Run

![image](https://github.com/user-attachments/assets/9615283a-1cdf-4c72-97e9-6bb077a59b45)

### All the dependencies used 

```
- pip install allure-pytest selenium
- pip install pytest selenium pytest-html openpyxl 
- pip install selenium-page-factory 
- pip install pyyaml faker openpyxl
- pip install pytest-xdist 
- pip install mysql-connector-python
- pip install pytest-reportportal
- pip install python-dotenv
```
### How to Install Packages

```pip install allure-pytest selenium pytest openpyxl faker pytest-xdist pytest-html```

### To Freeze your Package version
`` pip freeze > requirements.txt ``

### To Install the Freeze Version
``pip install -r requirements.txt``

### How to run your Testcase Parallel

```pip install pytest-xdist```

#### How to run the Framework?

```pytest -n auto tests/vwoLoginTests/pom/test_*```

#### How to run Testcase parallel ?

```pytest -n auto tests/vwoLoginTests/test_vwo_login.py```





