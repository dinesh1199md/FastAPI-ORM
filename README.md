#FastAPI-ORM

This project consists of several Python API, each implementing a specific functionality(crud). The goal of the project is to demonstrate modular code. The following instructions guide you through setting upa and  running code.

## Table of Contents
1. [Requirements](#requirements)
2. [Running programs](#running-programs)
3. [Running Unit Tests](#running-unit-tests)
4. [Project Structure](#project-structure)


---
## Requirements

### Installation
Follow the steps below to install the required dependencies.

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Required Dependencies

```
pip install -r requirements.txt
```

## Running programs 
- Run the Main Program: This will execute API host

```
cd FastAPI-ORM 
```
```
uvicorn main:app --reload
```

## Project Structure

```plaintext
FastAPI-ORM/
|
├── crud.py         # entry point to call all CRUD functions            
├── database.py     # create db connection using SQLalchemy engine
├── main.py         # Main entry point to call all API            
├── models.py       # models for creating table in DB
├── schema.py       # shecma for data validation
|__ README.md       # Instructions on how to use the code                            

---



