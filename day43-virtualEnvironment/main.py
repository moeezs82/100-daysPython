# first go to virtual environment in this case (myenv\Scripts\activate.bat/ps1 if in powershell) to check the different version of pandas
import pandas as pd

# global 2.0.0 in env 1.5.2
print(pd.__version__)