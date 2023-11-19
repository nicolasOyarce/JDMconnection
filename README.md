# JDMconnection
Project of an ecommerce realized for the backend course on jdm cars


## Prerequisites
  - Python
  - Git
  - PostgreSQL


## PostgreSQL Installation
  - Linux: 
    - Update the package index
      ```bash
      sudo apt update
      ```
    
    - Install PostgreSQL
      ```bash
      sudo apt install postgresql postgresql-contrib
      ```
      
  - Windows:
    
    - Download and install PostgreSQL from https://www.postgresql.org/download/windows/


## Basic Instalation
  - Copy repository:
  ```
  git clone https://github.com/nicolasOyarce/JDMconnection.git
  ```
  - Create virtual enviroment:
  ```
  pip install virtualenv
  virtualenv venv
  ```

  - Start the virtual environment:
    
      - Linux:
        ```
        source venv/bin/activate
        ```

      - Windows:
        ```
        venv/Scripts/activate
        ```
        
  - Once inside the virtual environment use the following command:
    ```
    pip install -r requirements.txt
    ```
