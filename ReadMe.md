## HOW TO RUN
* Install Python 2.7 or More
* Please install the required python modules using the requirements.txt in this folder
> python install -r requirements.txt
* Run the tests
> python RunTests.py
* Check the Report by opening "report.html"



## CODE STRUCTURE

```
4CAssignment/
+-- .gitignore
+-- requirements.txt
+-- Bug-Report.docx
+-- ReadMe.md
    +-- Tests
    ¦   +-- TestAddFetchCar.py                  # Tests for AddCar API & FetchCarDetails API
    ¦   +-- TestDeleteCar.py                    # Tests for Delete Car API
    ¦   +-- TestFetchToken.py                   # Tests for Fetch Token API
    +-- Utils
    ¦   +-- Api.py                             # BaseApi class & ApiWrapper class with default values for API endpoints
    ¦   +-- ErrorMsg.py                        # Utility for Managing all error message of API endpoints)
    ¦   +-- StatusCode.py                      # Reference of HTTP Status Codes)