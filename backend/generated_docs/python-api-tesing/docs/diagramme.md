# Diagrammes du projet

## Architecture

```mermaid
graph TD
presentation["Presentation / Routes"]
database[("Database")]
presentation --> database
```

## Flux de données

```mermaid
graph TD
user(["User"])
request["Request"]
routes["Routes / API"]
database[("Database")]
response["Response"]
user --> request
request --> routes
routes --> database
database --> response
```

## Dépendances des modules

```mermaid
graph TD
info["Module dependency diagram unavailable"]
```

## Arborescence du projet

```mermaid
graph TD
ROOT["python-api-tesing"]
ROOT_2020_100_examples["2020_100_examples/"]
ROOT --> ROOT_2020_100_examples
ROOT_bazi["bazi/"]
ROOT --> ROOT_bazi
ROOT_book_scraper["book_scraper/"]
ROOT --> ROOT_book_scraper
ROOT_buildbot["buildbot/"]
ROOT --> ROOT_buildbot
ROOT_buildbot_hello_world["hello-world/"]
ROOT_buildbot --> ROOT_buildbot_hello_world
ROOT_flask["flask/"]
ROOT --> ROOT_flask
ROOT_flask_api_demo["api_demo/"]
ROOT_flask --> ROOT_flask_api_demo
ROOT_flask_filemanager["filemanager/"]
ROOT_flask --> ROOT_flask_filemanager
ROOT_flask_flask_web_service["flask_web_service/"]
ROOT_flask --> ROOT_flask_flask_web_service
ROOT_flask_waiter_caller_mongo["waiter_caller_mongo/"]
ROOT_flask --> ROOT_flask_waiter_caller_mongo
ROOT_flask_waiter_caller_postg["waiter_caller_postgresql/"]
ROOT_flask --> ROOT_flask_waiter_caller_postg
ROOT_install["install/"]
ROOT --> ROOT_install
ROOT_opencv_crash_deep_learnin["opencv_crash_deep_learning/"]
ROOT --> ROOT_opencv_crash_deep_learnin
ROOT_opencv_crash_deep_learnin["ch01/"]
ROOT_opencv_crash_deep_learnin --> ROOT_opencv_crash_deep_learnin
ROOT_opencv_crash_deep_learnin["ch02/"]
ROOT_opencv_crash_deep_learnin --> ROOT_opencv_crash_deep_learnin
ROOT_other["other/"]
ROOT --> ROOT_other
ROOT_pandas["pandas/"]
ROOT --> ROOT_pandas
ROOT_pandas_excel_demo["excel_demo/"]
ROOT_pandas --> ROOT_pandas_excel_demo
ROOT_pandas_python_data_analys["python_data_analyse_crash_course/"]
ROOT_pandas --> ROOT_pandas_python_data_analys
ROOT_practices["practices/"]
ROOT --> ROOT_practices
ROOT_practices_cv["cv/"]
ROOT_practices --> ROOT_practices_cv
ROOT_practices_keras["keras/"]
ROOT_practices --> ROOT_practices_keras
ROOT_practices_pandas["pandas/"]
ROOT_practices --> ROOT_practices_pandas
ROOT_practices_pillow["pillow/"]
ROOT_practices --> ROOT_practices_pillow
ROOT_practices_tk["tk/"]
ROOT_practices --> ROOT_practices_tk
ROOT_practices_ts["ts/"]
ROOT_practices --> ROOT_practices_ts
ROOT_python_automation_cook["python-automation-cook/"]
ROOT --> ROOT_python_automation_cook
ROOT_python_automation_cook_ch["ch3/"]
ROOT_python_automation_cook --> ROOT_python_automation_cook_ch
ROOT_python3_7quick["python3.7quick/"]
ROOT --> ROOT_python3_7quick
ROOT_python3_libraries["python3_libraries/"]
ROOT --> ROOT_python3_libraries
ROOT_python3_libraries_asyncio["asyncio/"]
ROOT_python3_libraries --> ROOT_python3_libraries_asyncio
ROOT_python3_libraries_collect["collections/"]
ROOT_python3_libraries --> ROOT_python3_libraries_collect
ROOT_python3_libraries_daemon["daemon/"]
ROOT_python3_libraries --> ROOT_python3_libraries_daemon
ROOT_python3_libraries_face_re["face_recognition/"]
ROOT_python3_libraries --> ROOT_python3_libraries_face_re
ROOT_python3_libraries_matplot["matplotlib/"]
ROOT_python3_libraries --> ROOT_python3_libraries_matplot
ROOT_python3_libraries_numpy["numpy/"]
ROOT_python3_libraries --> ROOT_python3_libraries_numpy
ROOT_python3_libraries_opencv["opencv/"]
ROOT_python3_libraries --> ROOT_python3_libraries_opencv
ROOT_python3_libraries_os_path["os.path/"]
ROOT_python3_libraries --> ROOT_python3_libraries_os_path
ROOT_python3_libraries_pathlib["pathlib/"]
ROOT_python3_libraries --> ROOT_python3_libraries_pathlib
ROOT_python3_libraries_pexpect["pexpect/"]
ROOT_python3_libraries --> ROOT_python3_libraries_pexpect
ROOT_python3_libraries_pillow["pillow/"]
ROOT_python3_libraries --> ROOT_python3_libraries_pillow
ROOT_python3_libraries_pytesse["pytesseract/"]
ROOT_python3_libraries --> ROOT_python3_libraries_pytesse
ROOT_python3_libraries_pytest_["pytest_testing/"]
ROOT_python3_libraries --> ROOT_python3_libraries_pytest_
ROOT_python3_libraries_string["string/"]
ROOT_python3_libraries --> ROOT_python3_libraries_string
ROOT_python3_libraries_time["time/"]
ROOT_python3_libraries --> ROOT_python3_libraries_time
ROOT_python3_libraries__dubbo["_dubbo/"]
ROOT_python3_libraries --> ROOT_python3_libraries__dubbo
ROOT_python_crash_tutorial["python_crash_tutorial/"]
ROOT --> ROOT_python_crash_tutorial
ROOT_python_crash_tutorial_Ch1["Ch1/"]
ROOT_python_crash_tutorial --> ROOT_python_crash_tutorial_Ch1
ROOT_python_crash_tutorial_Ch2["Ch2/"]
ROOT_python_crash_tutorial --> ROOT_python_crash_tutorial_Ch2
ROOT_python_crash_tutorial_Ch3["Ch3/"]
ROOT_python_crash_tutorial --> ROOT_python_crash_tutorial_Ch3
ROOT_python_crash_tutorial_Ch4["Ch4/"]
ROOT_python_crash_tutorial --> ROOT_python_crash_tutorial_Ch4
ROOT_python_crash_tutorial_Ch5["Ch5/"]
ROOT_python_crash_tutorial --> ROOT_python_crash_tutorial_Ch5
ROOT_python_crash_tutorial_exa["examples/"]
ROOT_python_crash_tutorial --> ROOT_python_crash_tutorial_exa
ROOT_selenium_examples["selenium_examples/"]
ROOT --> ROOT_selenium_examples
ROOT_selenium_examples_ch5["ch5/"]
ROOT_selenium_examples --> ROOT_selenium_examples_ch5
ROOT_selenium_examples_ch6["ch6/"]
ROOT_selenium_examples --> ROOT_selenium_examples_ch6
ROOT_shouxiang["shouxiang/"]
ROOT --> ROOT_shouxiang
ROOT_tools["tools/"]
ROOT --> ROOT_tools
ROOT_weeks["weeks/"]
ROOT --> ROOT_weeks
ROOT_weeks_2018_06_01["2018_06_01/"]
ROOT_weeks --> ROOT_weeks_2018_06_01
ROOT_weeks_2018_06_06["2018_06_06/"]
ROOT_weeks --> ROOT_weeks_2018_06_06
ROOT_weeks_2018_06_07["2018_06_07/"]
ROOT_weeks --> ROOT_weeks_2018_06_07
ROOT_weeks_2018_06_12["2018_06_12/"]
ROOT_weeks --> ROOT_weeks_2018_06_12
ROOT_weeks_2018_06_15["2018_06_15/"]
ROOT_weeks --> ROOT_weeks_2018_06_15
```
