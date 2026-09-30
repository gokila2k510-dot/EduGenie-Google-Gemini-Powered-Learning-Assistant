# Phase 3 – Project Design

## 1. Project Overview

EduGenie is an AI-powered educational assistant designed to support students in learning activities.

## 2. Main Modules

The system contains the following modules:

- Question and Answer
- Concept Explanation
- Quiz Generation
- Text Summarization
- Learning Path Recommendation

## 3. System Architecture

The system consists of:

1. Frontend
2. FastAPI Backend
3. AI Processing Modules
4. Gemini API

## 4. Frontend Design

The frontend provides:

- Task selection
- Student level selection
- Text input
- Submit button
- Result display

## 5. Backend Design

FastAPI is used as the backend framework.

The backend provides:

- /qa
- /explain
- /quiz
- /summarize
- /learn/recommendations

## 6. AI Module Design

Different modules handle different educational tasks.

- qna.py – Question answering
- explanation_module.py – Concept explanation
- quiz_module.py – Quiz generation
- summary_module.py – Text summarization
- learning_path.py – Learning path recommendation

## 7. Expected Workflow

Student Input
    ↓
Frontend
    ↓
FastAPI Backend
    ↓
Selected AI Module
    ↓
AI Processing
    ↓
Result
    ↓
Frontend Display
