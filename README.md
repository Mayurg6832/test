# Data Project :: Comapny Master

To convert raw open data into plots, that tell a story on the state of company registration in Maharashtra.

<br/>

> ## Prerequisites

<br/>

1. Setup Virtual environment
   ```console
   $ pip3 install virtualenv
   $ virtualenv env_name
   $ source env_name/bin/activate
   ``` 

2. Make sure to install the requirements for the project using the **_requirements.txt_** file.

    ```console
    $ pip3 install -r requirements.txt
    ```

3. Download the project as zip archive and extract it to your desired location or just clone the repository.

<br/>


4. Download the dataset using the<a href="https://data.gov.in/resources/company-master-data-maharashtra-upto-28th-february-2019"> 
   Link </a> and move to dataset in folder where all files of this project are in.


> ## To run the Project

<br/>

1. Open the Terminal and change the path to directory with all python files.

2. Run the `main.py` file by the following command
  ```console
  $ python3 main.py
  ```

On the terminal, 4 options will appear, Choose the option for the output of respective problem.

> ## Library Used
<br/>

- Matplotlib

<br/>



> ### Project Description

- The project contains 5 file:
  
    - `main.py`
    - `preprocessing.py`
    - `hist_plot.py`
    - `top_registrations.py`
    - `bar_plot_year.py`
    - `group_plot.py`


- The `main.py` file is responsible for the Data parsing and execution of plots output.

- The `preprocesing.py` file contain methods that preprocess or transform the data for the plotting.

- Each file `hist_plot.py`, `top_registrations.py`, `bar_plot_year.py`, `group_plot.py` are responsible for the plotting of graphs.


