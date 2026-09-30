from pydantic import BaseModel, Field


class ExplainRequest(BaseModel):
    topic: str
    level: str = "beginner"


class LearningPathRequest(BaseModel):
    topic: str
    level: str = "beginner"
    timeline: str = "4 weeks"


class QARequest(BaseModel):
    question: str
    level: str = "beginner"


class QuizRequest(BaseModel):
    text: str
    level: str = "beginner"


class SummaryRequest(BaseModel):
    text: str
    level: str = "beginner"