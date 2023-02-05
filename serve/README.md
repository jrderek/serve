# FastApi Docker - Application

Here are the steps to build an app in FastAPI to load CSV file and Dockerize the application:

1. Set up a Python environment and install the necessary packages such as FastAPI, Pandas, and Uvicorn.

2. Create a new directory for your project and navigate to it in the terminal.

3. Create a new file named app.py in the project directory and paste the following code:


docker build -t myapp .


docker run -p 8000:8000 myapp


 http://localhost:8000/docs 


docker build -t myapp .


docker run -p 8000:8000 myapp


http://localhost:8000/read-parquet
