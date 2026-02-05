# Gemini CLI: BizTone Converter Project Overview

This `GEMINI.md` file provides essential context for the "BizTone Converter - 업무 말투 자동 변환 솔루션" (Business Tone Converter - Automatic Business Tone Conversion Solution) project, to be used as instructional context for future interactions with the Gemini CLI.

## Project Overview

The BizTone Converter is an AI-powered web application designed to help users convert everyday language into professional business communication tailored for different audiences (supervisors, colleagues, and clients). Its primary purpose is to enhance communication quality, improve productivity, and reduce training costs within a business context.

## Main Technologies

*   **Frontend:**
    *   HTML5, CSS3 (with Tailwind CSS for styling)
    *   JavaScript (ES6+) for client-side logic
    *   Fetch API for asynchronous communication with the backend
*   **Backend:**
    *   Python 3.11 with Flask framework for building RESTful APIs
    *   Flask-CORS for handling Cross-Origin Resource Sharing
    *   `python-dotenv` for managing environment variables
*   **AI/ML Integration:**
    *   Groq AI API is utilized for natural language conversion, employing the `moonshotai/kimi-k2-instruct-0905` model.
    *   Optimized prompt engineering is applied for each target audience to guide the AI's response.
*   **Deployment:** Vercel (intended for static hosting and serverless functions, as per PRD).
*   **Version Control:** Git and GitHub.

## Architecture

The application follows a client-server architecture, clearly separating frontend and backend components. The frontend interacts with a Flask-based backend API, which in turn communicates with the Groq AI API for the core text conversion functionality.

```
User Browser
↓
[HTML/CSS/JS Frontend]
↓ (HTTP POST/GET)
[Flask Backend API Server]
↓ (API Call)
[Groq AI API Service]
↓
[Response Processing & Return]
```

## Key Features

*   **Core Tone Conversion (FR-01):** Transforms user-inputted text into appropriate business tones for '상사' (supervisors), '동료' (colleagues), and '고객' (clients) using AI-driven prompts. Supports up to 500 characters.
*   **Result Comparison (FR-02):** Presents the original and converted text side-by-side for easy comparison and learning.
*   **Copy Result (FR-03):** Provides a one-click functionality to copy the converted text to the clipboard.
*   **Input Convenience (FR-04):** Displays a real-time character count below the text input area.
*   **Error Handling (FR-05):** Offers user-friendly messages and retry options in case of API response delays or failures.

## Building and Running

To get the BizTone Converter running, you need to set up both the backend Flask server and access the frontend.

### Backend Setup (Python/Flask)

1.  **Navigate to the `backend` directory:**
    ```bash
    cd backend
    ```
2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv .venv
    # On Windows:
    .\.venv\Scripts\activate
    # On macOS/Linux:
    source ./.venv/bin/activate
    ```
3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up Environment Variables:**
    Create a `.env` file in the project root (`C:\vibe_coding\BIZTALK_LLM/`) if it doesn't exist, and add your `GROQ_API_KEY`:
    ```
    GROQ_API_KEY=your_groq_api_key_here
    ```
    *Note: Replace `your_groq_api_key_here` with your actual Groq API Key.*
5.  **Run the Flask backend server:**
    ```bash
    python app.py
    ```
    The server will typically run on `http://127.0.0.1:5000` or `http://localhost:5000`. Keep this terminal open and the server running.

### Frontend Access (HTML/CSS/JS)

The frontend is served directly by the Flask backend. There is no separate build process for the frontend in this setup as Tailwind CSS is included via CDN.

1.  **Ensure the Flask backend is running** (as described in the Backend Setup).
2.  **Access the application in your web browser:**
    Open `http://127.0.0.1:5000` (or `http://localhost:5000`) in your browser.

## Development Conventions

*   **Language:** The primary language for the user interface and documentation within the project is Korean.
*   **Styling:** Tailwind CSS is used for all frontend styling, integrated via CDN.
*   **API Keys & Sensitive Information:** All sensitive data, such as Groq AI API keys, are managed through environment variables (`.env` files) and accessed exclusively on the backend via `python-dotenv`, ensuring they are not exposed on the client-side or committed to version control.
*   **Version Control Workflow:** The project adheres to a Git/GitHub branching strategy (`feature -> develop -> main`), emphasizing the use of Pull Requests for code review and collaboration.
*   **Code Structure:** The project maintains a clean, modular structure with a clear separation between frontend and backend components.
*   **Logging:** The Flask backend includes basic logging for error visibility and debugging.
*   **No `.env` Modification by Agent:** As per `my-rules.md`, the AI agent should not modify the `.env` file.

## Project Structure

-   **`./` (Project Root)**:
    -   `.env`: Environment variable configuration file (ignored by Git).
    -   `.gitignore`: Specifies files and directories to be excluded from version control.
    -   `PRD.md`: Product Requirements Document, detailing project scope and features.
    -   `프로그램개요서.md`: Initial project planning document.
    -   `my-rules.md`: Custom instructions/rules for the Gemini CLI agent.
-   **`backend/`**: Contains the Flask-based backend API server.
    -   `app.py`: The main Flask application entry point, handling API routes, Groq AI API integration, and business logic.
    -   `requirements.txt`: Lists Python package dependencies.
-   **`frontend/`**: Contains the static web files for the user interface.
    -   `public/`:
        -   `index.html`: The main HTML file of the application.
        -   `js/main.js`: Client-side JavaScript logic (API calls, DOM manipulation, etc.).
-   **`.venv/`**: Python virtual environment directory for isolating dependencies.
