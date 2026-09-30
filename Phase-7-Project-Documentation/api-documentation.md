# API Documentation

## Base URL

http://127.0.0.1:8000

## 1. Question and Answer

### Endpoint

POST /qa

### Input

{
  "question": "What is photosynthesis?",
  "level": "beginner"
}

### Output

The API returns an educational answer.

## 2. Concept Explanation

### Endpoint

POST /explain

### Input

{
  "topic": "Photosynthesis",
  "level": "beginner"
}

## 3. Quiz Generation

### Endpoint

POST /quiz

### Input

{
  "topic": "Photosynthesis",
  "level": "beginner"
}

## 4. Text Summarization

### Endpoint

POST /summarize

### Input

{
  "text": "Educational text..."
}

## 5. Learning Path

### Endpoint

POST /learn/recommendations

### Input

{
  "topic": "Python Programming",
  "level": "beginner"
}
