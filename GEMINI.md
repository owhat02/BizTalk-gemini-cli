# Gemini CLI: BizTone Converter 프로젝트 개요

이 `GEMINI.md` 파일은 "BizTone Converter - 업무 말투 자동 변환 솔루션" 프로젝트에 대한 필수적인 문맥을 제공하며, Gemini CLI와의 향후 상호 작용을 위한 지침으로 사용됩니다.

## 프로젝트 개요

BizTone Converter는 AI 기반 웹 애플리케이션으로, 사용자가 일상적인 언어를 상사, 동료, 고객 등 다양한 대상에 맞춰 전문적인 비즈니스 커뮤니케이션으로 변환할 수 있도록 돕습니다. 이 프로젝트의 주요 목적은 비즈니스 환경 내에서 커뮤니케이션 품질을 향상하고, 생산성을 높이며, 교육 비용을 절감하는 것입니다.

## 주요 기술 스택

*   **프론트엔드 (Frontend):**
    *   HTML5, CSS3 (스타일링을 위한 Tailwind CSS 포함)
    *   클라이언트 측 로직을 위한 JavaScript (ES6+)
    *   백엔드와의 비동기 통신을 위한 Fetch API
*   **백엔드 (Backend):**
    *   Python 3.11 및 RESTful API 구축을 위한 Flask 프레임워크
    *   Cross-Origin Resource Sharing (CORS) 처리를 위한 Flask-CORS
    *   환경 변수 관리를 위한 `python-dotenv`
*   **AI/ML 통합 (AI/ML Integration):**
    *   자연어 변환을 위해 Groq AI API를 활용하며, `moonshotai/kimi-k2-instruct-0905` 모델을 사용합니다.
    *   AI 응답을 유도하기 위해 각 대상 고객에 최적화된 프롬프트 엔지니어링이 적용됩니다.
*   **배포 (Deployment):** PRD에 따라 정적 호스팅 및 서버리스 함수를 위한 Vercel을 사용할 예정입니다.
*   **버전 관리 (Version Control):** Git 및 GitHub.

## 아키텍처

애플리케이션은 클라이언트-서버 아키텍처를 따르며, 프론트엔드와 백엔드 구성 요소를 명확하게 분리합니다. 프론트엔드는 Flask 기반 백엔드 API와 상호 작용하며, 백엔드는 핵심 텍스트 변환 기능을 위해 Groq AI API와 통신합니다.

```
사용자 브라우저
↓
[HTML/CSS/JS 프론트엔드]
↓ (HTTP POST/GET)
[Flask 백엔드 API 서버]
↓ (API 호출)
[Groq AI API 서비스]
↓
[응답 처리 및 반환]
```

## 주요 기능

*   **핵심 말투 변환 (FR-01):** 사용자가 입력한 텍스트를 AI 기반 프롬프트를 사용하여 '상사', '동료', '고객'에게 적합한 비즈니스 톤으로 변환합니다. 최대 500자까지 지원합니다.
*   **결과 비교 (FR-02):** 원본 텍스트와 변환된 텍스트를 나란히 표시하여 쉽게 비교하고 학습할 수 있도록 합니다.
*   **결과 복사 (FR-03):** 변환된 텍스트를 클립보드에 한 번의 클릭으로 복사하는 기능을 제공합니다.
*   **입력 편의성 (FR-04):** 텍스트 입력 영역 하단에 실시간으로 글자 수를 표시합니다.
*   **오류 처리 (FR-05):** API 응답 지연 또는 실패 시 사용자에게 친화적인 메시지와 재시도 옵션을 제공합니다.

## 빌드 및 실행 방법

BizTone Converter를 실행하려면 백엔드 Flask 서버를 설정하고 프론트엔드에 접속해야 합니다.

### 백엔드 설정 (Python/Flask)

1.  **`backend` 디렉토리로 이동:**
    ```bash
    cd backend
    ```
2.  **Python 가상 환경 생성 및 활성화:**
    ```bash
    python -m venv .venv
    # Windows:
    .\.venv\Scripts\activate
    # macOS/Linux:
    source ./.venv/bin/activate
    ```
3.  **Python 의존성 설치:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **환경 변수 설정:**
    프로젝트 루트 (`C:\vibe_coding\BIZTALK_LLM/`)에 `.env` 파일이 없다면 생성하고 `GROQ_API_KEY`를 추가합니다:
    ```
    GROQ_API_KEY=your_groq_api_key_here
    ```
    *참고: `your_groq_api_key_here`를 실제 Groq API 키로 교체하세요.*
5.  **Flask 백엔드 서버 실행:**
    ```bash
    python app.py
    ```
    서버는 일반적으로 `http://127.0.0.1:5000` 또는 `http://localhost:5000`에서 실행됩니다. 이 터미널을 열어두고 서버를 계속 실행 상태로 유지하세요.

### 프론트엔드 접속 (HTML/CSS/JS)

프론트엔드는 Flask 백엔드에 의해 직접 서비스됩니다. 이 설정에서는 Tailwind CSS가 CDN을 통해 포함되므로 프론트엔드를 위한 별도의 빌드 과정은 없습니다.

1.  **Flask 백엔드가 실행 중인지 확인** (위의 백엔드 설정 참조).
2.  **웹 브라우저에서 애플리케이션에 접속:**
    브라우저에서 `http://127.0.0.1:5000` (또는 `http://localhost:5000`)을 엽니다.

## 개발 컨벤션

*   **언어:** 프로젝트 내 UI 및 문서의 주요 언어는 한국어입니다.
*   **스타일링:** 모든 프론트엔드 스타일링에는 CDN을 통해 통합된 Tailwind CSS가 사용됩니다.
*   **API 키 및 민감 정보:** Groq AI API 키와 같은 모든 민감한 데이터는 환경 변수(`.env` 파일)를 통해 관리되며, `python-dotenv`를 통해 백엔드에서만 독점적으로 접근됩니다. 이는 클라이언트 측에 노출되거나 버전 관리에 커밋되지 않도록 보장합니다.
*   **버전 관리 워크플로우:** 프로젝트는 Git/GitHub 브랜칭 전략(`feature -> develop -> main`)을 따르며, 코드 리뷰 및 협업을 위해 Pull Request 사용을 강조합니다.
*   **코드 구조:** 프로젝트는 프론트엔드와 백엔드 구성 요소 간의 명확한 분리를 통해 깔끔하고 모듈화된 구조를 유지합니다.
*   **로깅:** Flask 백엔드에는 오류 가시성 및 디버깅을 위한 기본 로깅이 포함되어 있습니다.
*   **에이전트의 `.env` 파일 수정 금지:** `my-rules.md`에 따라 AI 에이전트는 `.env` 파일을 수정해서는 안 됩니다.

## 프로젝트 구조

-   **`./` (프로젝트 루트):**
    -   `.env`: 환경 변수 설정 파일 (Git에서 무시됨).
    -   `.gitignore`: 버전 관리에서 제외할 파일 및 디렉토리를 지정합니다.
    -   `PRD.md`: 제품 요구사항 정의 문서로, 프로젝트 범위 및 기능을 상세히 설명합니다.
    -   `프로그램개요서.md`: 초기 프로젝트 기획 문서.
    -   `my-rules.md`: Gemini CLI 에이전트를 위한 사용자 정의 지침/규칙.
-   **`backend/`:** Flask 기반의 백엔드 API 서버를 포함합니다.
    -   `app.py`: 메인 Flask 애플리케이션 진입점이며, API 라우트, Groq AI API 통합 및 비즈니스 로직을 처리합니다.
    -   `requirements.txt`: Python 패키지 의존성 목록입니다.
-   **`frontend/`:** 사용자 인터페이스(UI)를 위한 정적 웹 파일을 포함합니다.
    -   `public/`:
        -   `index.html`: 애플리케이션의 메인 HTML 파일.
        -   `js/main.js`: 클라이언트 측 JavaScript 로직 (API 호출, DOM 조작 등).
-   **`.venv/`:** Python 가상 환경 디렉토리로, 의존성을 격리합니다.