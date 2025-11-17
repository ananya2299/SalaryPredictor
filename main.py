# main.py (copy this file)
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import joblib
import pandas as pd
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

MODEL_PATH = os.path.join(os.path.dirname(__file__), "lin_regress.sav")
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Upload it to the Space repo.")

model = joblib.load(MODEL_PATH)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prediction": None})

@app.post("/predict")
async def predict(request: Request):
    """
    Accepts either JSON (application/json) or form-data (multipart/form-data).
    Returns JSON for API clients, and HTML template for browser form submits.
    """
    content_type = request.headers.get("content-type", "")
    data = {}

    # parse incoming payload
    if "application/json" in content_type:
        try:
            data = await request.json()
        except Exception:
            return JSONResponse({"error": "Invalid JSON body"}, status_code=400)
    else:
        form = await request.form()
        data = {k: form.get(k) for k in form.keys()}

    # helpers
    def to_float(x, default=0.0):
        try:
            return float(x)
        except Exception:
            return default

    def to_int(x, default=0):
        try:
            return int(float(x))
        except Exception:
            return default

    # build the row that matches training columns
    row = {
        "experience_level_encoded": to_float(data.get("experience_level_encoded", 0.0)),
        "company_size_encoded": to_float(data.get("company_size_encoded", 0.0)),
        "employment_type_PT": to_int(data.get("employment_type_PT", 0)),
        "job_title_Data_Engineer": to_int(data.get("job_title_Data_Engineer", 0)),
        "job_title_Data_Scientist": to_int(data.get("job_title_Data_Scientist", 0)),
        "job_title_Machine_Learning_Engineer": to_int(data.get("job_title_Machine_Learning_Engineer", 0))
    }

    # predict
    try:
        df = pd.DataFrame([row])
        pred = model.predict(df)[0]
    except Exception as e:
        if "application/json" in content_type:
            return JSONResponse({"error": str(e)}, status_code=500)
        else:
            return templates.TemplateResponse("index.html", {"request": request, "prediction": None, "error": str(e)})

    # return the right type
    if "application/json" in content_type:
        return JSONResponse({"Salary (USD)": float(pred)})
    else:
        return templates.TemplateResponse("index.html", {"request": request, "prediction": round(float(pred), 2)})
