# Installation Guide

## Requirements

- Python 3.10 or above
- Internet connection
- VS Code

## Step 1

Open the EduGenie project in VS Code.

## Step 2

Open the terminal and navigate to:

Phase-5-Project-Development

## Step 3

Create a virtual environment:

python -m venv .venv

## Step 4

Activate the environment in Windows PowerShell:

.\.venv\Scripts\Activate.ps1

## Step 5

Install dependencies:

python -m pip install -r requirements.txt

## Step 6

Configure the Gemini API key using the project's environment configuration.

## Step 7

Run the application:

python -m uvicorn main:app --host 127.0.0.1 --port 8000

## Step 8

Open the application in a browser.
