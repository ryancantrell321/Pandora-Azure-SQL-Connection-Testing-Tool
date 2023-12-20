# PANDORA MICROSOFT AZURE SQL CONNECTION TESTING TOOL 
## Version 1.0

\
Welcome to PANDORA MICROSOFT AZURE SQL CONNECTION TESTING TOOL—a purpose-built tool tailored for Azure SQL developers. This streamlined application is designed to simplify the verification process of Azure SQL database credentials, ensuring correctness and reliability in your development workflow.

## Key Features:

- **Portability**: Our tool is completely portable, eliminating the need for installation. Enjoy hassle-free testing without the burden of additional setup steps.


- **Security First**: We prioritize your data security. PANDORA MICROSOFT AZURE SQL CONNECTION TESTING TOOL abstains from logging or storing any received or inputted information, providing you with peace of mind during testing.

## Minimum Requirements:
To ensure the smooth execution of PANDORA MICROSOFT AZURE SQL CONNECTION TESTING TOOL, please ensure that your system meets the following minimum requirements:

The program has been developed using a Windows 11 (x64) running Python 3.12.0. Ensure that you have Python installed on your system.

Recommended Python version: 3.11.0 and above. You can run this tool in a system running Linux OS and Windows 10/11.

This tool assumes that you, the end-user, have a stable internet connection so that you can verify that you can externally connect to your Microsoft Azure SQL Database.

### Python3 Installation:
For Windows OS, you can install Python 3.11.0 and above from here:
https://www.python.org/downloads/windows/

#### REMEMBER TO RUN THE INSTALLER AS AN ADMINISTRATOR AND ADD PYTHON TO PATH DURING THE INSTALLATION PROCESS!

For Linux OS, you can install Python 3.11.0 or above by checking the below guide:
https://www.howtogeek.com/install-latest-python-version-on-ubuntu/

To check the release versions of python, check the link below:
https://www.python.org/downloads/


#### DUE TO A LIMITATION IN AVAILABLE RESOURCES, THIS TOOL HAS NOT BEEN TESTED ON A SYSTEM RUNNING APPLE's macOS OR ON SYSTEMS WITH AN ARM64 PROCESSOR.

### ODBC Driver:

ODBC (Open Database Connectivity) is a standard interface for connecting to databases. An ODBC driver serves as a bridge between an application and a database (AZURE SQL DATABASE, in this case), allowing the application to communicate with the database using the ODBC API. 

Make sure you have the appropriate ODBC driver installed on your system. This tool supports the x64 version of ODBC Driver version 17 and 18. New versions will be added if they are released in the future.
If not installed, you can download the driver either from the link provided below or by clicking on the "INSTALL DRIVER" button within the program once you have gotten it running.

#### LINKS:

MICROSOFT ODBC DRIVER VERSION 18 (x64): https://go.microsoft.com/fwlink/?linkid=2249006
\
MICROSOFT ODBC DRIVER VERSION 17 (x64): https://go.microsoft.com/fwlink/?linkid=2249004


# Virtual Environment (venv):
The application includes a virtual environment (venv) to manage dependencies.
It is recommended to activate the virtual environment before running the program to isolate dependencies and avoid conflicts.

## Activating the Virtual Environment:
Before running the program, activate the virtual environment by using the following commands in the terminal or command prompt:

#### Navigate to the program directory using a terminal or Powershell:
`cd /path/"Pandora Azure SQL Connection Testing Tool"`

#### On Linux, type or copypaste: 
`source venv/bin/activate`

#### On Windows,
`venv\Scripts\activate`

### Launching the program or Installing Dependencies:
The program is pre-configured to check whether dependencies are installed within the virtual environment. If not, they will be installed before the program begins to work.

#### Navigate to the program directory using a terminal or Powershell:
`cd /path/"Pandora Azure SQL Connection Testing Tool"`

#### Write or copypaste the below code in the terminal based on your OS:
#### On Windows Powershell:
`python main.py`

#### On Linux Terminal:
`python3 main.py`


## How It Works:

Developers can seamlessly employ this tool to assess the external accessibility of their intended Azure SQL database. Whether you're in the early stages of system development or fine-tuning your existing project, our tester is here to streamline the database connection verification process.

### USAGE GUIDELINES:
To use this program, fill in all the blank fields and select an appropriate ODBC driver installed in your system.

1. Server: The URL or IP of your Azure SQL Database server. 
[yourservername.database.windows.net]


2. Database: The name of the target database.


3. Username: Your database username.


4. Password: Your database password.


5. Driver: Select the appropriate ODBC Driver installed in your system.


6. After this, click on 'Test Connection' to test whether your connection credentials are correct.


7. To clear the fields, click the 'RESET' button.


8. To see the License, click the 'LICENSE' button 


9. To quit the program, click the 'EXIT' button.


## LICENSE:
Pandora Azure SQL Connection Testing Tool © 2023 by Pandora Dynamics LLP is licensed under Attribution-NoDerivs 4.0 International (CC BY-ND 4.0).

To view a copy of this license, visit http://creativecommons.org/licenses/by-nd/4.0/

## Contact Us:

For any issues, bugs, or queries, feel free to reach out to us at:

**Email: pandoradynamics@gmail.com**
\
**Facebook: https://facebook.com/pandoradynamics22**
\
**Instagram: https://instagram.com/pandoradynamics22**

## Copyright:

© 2023 PANDORA DYNAMICS LLP. All Rights Reserved.

Thank you for choosing Pandora Azure SQL Connection Testing Tool—a reliable companion for your Azure SQL development journey.
