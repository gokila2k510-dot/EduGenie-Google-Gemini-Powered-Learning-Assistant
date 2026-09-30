from pydantic import BaseModel, Field

class QARequest(BaseModel):
    question: str = Field(..., min_length=1)
    level: str = "beginner"

class ExplainRequest(BaseModel):
    topic: str = Field(..., min_length=1)
    level: str = "beginner"

class QuizRequest(BaseModel):
    topic: str = Field(..., min_length=1)
    level: str = "beginner"

class SummaryRequest(BaseModel):
    text: str = Field(..., min_length=1)

class LearningPathRequest(BaseModel):
    topic: str = Field(..., min_length=1)
    level: str = "beginner"
