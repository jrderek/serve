from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/read-parquet")
def read_parquet():
    df = pd.read_parquet("path/to/parquet/file.parquet")
    return {"data": df.to_dict()}


