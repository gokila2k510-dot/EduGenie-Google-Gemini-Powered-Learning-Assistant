from pathlib import Path
import traceback

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from explanation_module import explain_topic
from learning_path import get_learning_recommendations

from models import (
    ExplainRequest,
    LearningPathRequest,
    QARequest,
    QuizRequest,
    SummaryRequest,
)

from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text


# --------------------------------------------------
# Base directory
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent


# --------------------------------------------------
# FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0",
)


# --------------------------------------------------
# Static files
# --------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)


# --------------------------------------------------
# Templates
# --------------------------------------------------

templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


# --------------------------------------------------
# Home page
# --------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request},
    )


# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "message": "EduGenie is running",
    }


# --------------------------------------------------
# Ask EduGenie / Q&A
# --------------------------------------------------

@app.post("/api/qa")
async def ask_question(request: QARequest):

    try:
        answer = answer_question(
            question=request.question,
            level=request.level,
        )

        return {
            "answer": answer,
        }

    except Exception as e:

        print("\n========== QA ERROR ==========")
        print(f"Error: {e}")
        traceback.print_exc()
        print("================================\n")

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# --------------------------------------------------
# Explain a topic
# --------------------------------------------------

@app.post("/api/explain")
async def explain(request: ExplainRequest):

    try:
        result = explain_topic(
            topic=request.topic,
            level=request.level,
        )

        return {
            "answer": result,
        }

    except Exception as e:

        print("\n========== EXPLAIN ERROR ==========")
        print(f"Error: {e}")
        traceback.print_exc()
        print("====================================\n")

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# --------------------------------------------------
# Generate quiz
# --------------------------------------------------

@app.post("/api/quiz")
async def quiz(request: QuizRequest):

    try:
        result = generate_quiz(
            text=request.text,
            level=request.level,
        )

        return result

    except Exception as e:

        print("\n========== QUIZ ERROR ==========")
        print(f"Error: {e}")
        traceback.print_exc()
        print("=================================\n")

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# --------------------------------------------------
# Summarize content
# --------------------------------------------------

@app.post("/api/summary")
async def summary(request: SummaryRequest):

    try:
        result = summarize_text(
            text=request.text,
            level=request.level,
        )

        return {
            "summary": result,
        }

    except Exception as e:

        print("\n========== SUMMARY ERROR ==========")
        print(f"Error: {e}")
        traceback.print_exc()
        print("====================================\n")

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# --------------------------------------------------
# Learning path
# --------------------------------------------------

@app.post("/api/learning-path")
async def learning_path(request: LearningPathRequest):

    try:
        result = get_learning_recommendations(
            topic=request.topic,
            level=request.level,
            timeline=request.timeline,
        )

        return result

    except Exception as e:

        print("\n========== LEARNING PATH ERROR ==========")
        print(f"Error: {e}")
        traceback.print_exc()
        print("==========================================\n")

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# --------------------------------------------------
# Learning path - GET version
# --------------------------------------------------

@app.get("/api/recommendations")
async def recommendations(
    topic: str,
    level: str = "beginner",
):

    try:
        result = get_learning_recommendations(
            topic=topic,
            level=level,
        )

        return result

    except Exception as e:

        print("\n========== RECOMMENDATIONS ERROR ==========")
        print(f"Error: {e}")
        traceback.print_exc()
        print("============================================\n")

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )