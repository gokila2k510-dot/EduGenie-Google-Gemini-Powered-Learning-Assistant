from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import (
    QARequest,
    ExplainRequest,
    QuizRequest,
    SummaryRequest,
    LearningPathRequest,
)

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import generate_learning_path

app = FastAPI(
    title="EduGenie",
    description="AI-powered Educational Assistant",
    version="1.0.0",
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/qa")
async def qa(request: QARequest):
    result = answer_question(
        request.question,
        request.level
    )
    return {
        "success": True,
        "result": result
    }

@app.post("/explain")
async def explain(request: ExplainRequest):
    result = explain_topic(
        request.topic,
        request.level
    )
    return {
        "success": True,
        "result": result
    }

@app.post("/quiz")
async def quiz(request: QuizRequest):
    result = generate_quiz(
        request.topic,
        request.level
    )
    return {
        "success": True,
        "result": result
    }

@app.post("/summarize")
async def summarize(request: SummaryRequest):
    result = summarize_text(request.text)
    return {
        "success": True,
        "result": result
    }

@app.post("/learn/recommendations")
async def learning_path(request: LearningPathRequest):
    result = generate_learning_path(
        request.topic,
        request.level
    )
    return {
        "success": True,
        "result": result
    }
