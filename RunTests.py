import os

import pytest

tst_files = ['TestAddFetchCar.py', 'TestDeleteCar.py', 'TestFetchToken.py']

base_path=os.path.join(os.getcwd(), "Tests")

params=['--html=report.html']

for testclass in tst_files:
    params.append(os.path.join(base_path,testclass))

pytest.main(params)
