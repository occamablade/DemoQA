# Project for UI auto-tests in [demoqa.com](https://demoqa.com/)

<!-- Stek -->

## Used stek 
<p  align="center">
  <code><img width="10%" title="Python" src="conf/img/python.png"></code>
  <code><img width="10%" title="Pytest" src="conf/img/pytest.png"></code>
  <code><img width="10%" title="Selenium" src="conf/img/selenium.png"></code>
  <code><img width="10%" title="GitHub" src="conf/img/github.png"></code>
  <code><img width="10%" title="Allure TestOps" src="conf/img/allure_testops.png"></code>
  <code><img width="10%" title="Git" src="conf/img/git.png"></code>
</p>

## To run a project and get an Allure report:
1. Clone repo.
   ```
   git@github.com:occamablade/DemoQA.git
   ```
2. Create and activate a virtual environment:
    ```
      $ cd occamablade/DemoQA
      $ python -m venv venv
    ```
    Windows:
    ```
      $ source venv/Scripts/activate
    ```
    MacOs/Linux:
    ```
      $ source venv/bin/activate
    ```
3. Install dependencies from file requirements.txt:
    ```
    (venv) $ python -m pip install --upgrade pip
    (venv) $ pip install -r requirements.txt
    ```
4. Run tests with command
    ```
    (venv) $ pytest -v --alluredir=test_result/
    ```
5. After completing all tests, generate a report
   ```
   (venv) $ allure serve test_result
   ```

### In the [Elements](https://demoqa.com/elements) section automated next pages: 
-  Text Box
-  Check Box
-  Radio Button
-  Web Tables
-  Buttons
-  Links
-  Upload and Download
-  Dynamic Properties

### In the [Forms](https://demoqa.com/forms) section automated next pages:


- ### Registration Form:
  - The data is generated using **Faker**
  - All data choiced and generated randomly
  - Picture is loaded from the folder `conf\img\me.pmg`


### In the [Alerts, Frame & Windows](https://demoqa.com/alertsWindows) section automated next pages:

- Browser Windows
- Alerts
- Frames
- Nested Frames
- Modal Dialogs


### In the [Widgets](https://demoqa.com/widgets) section automated next pages:

[//]: # (- Accordian)

[//]: # ()
[//]: # (- Auto Complete)

[//]: # ()
[//]: # (- Date Picker)

[//]: # ()
[//]: # (- Slider)

[//]: # ()
[//]: # (- Progress Bar)

[//]: # ()
[//]: # (- Tabs)

[//]: # ()
[//]: # (- Tool Tips)

[//]: # ()
[//]: # (- Menu)


### In the [Interactions](https://demoqa.com/interaction) section automated next pages:

[//]: # (- Sortable)

[//]: # ()
[//]: # (- Selectable)

[//]: # ()
[//]: # (- Resizable)

[//]: # ()
[//]: # (- Droppable)

[//]: # ()
[//]: # (- Dragabble)

## Owner
**Ivan Bezborodnikov** 

[![Telegram Badge](https://img.shields.io/badge/-vanyshqa-blue?style=social&logo=telegram&link=https://t.me/vanyshqa)](https://t.me/vanyshqa)