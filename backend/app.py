import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv
import logging

# .env 파일에서 환경 변수 로드
load_dotenv()

app = Flask(__name__, static_folder='../frontend/public', static_url_path='/')
# Configure logging
logging.basicConfig(level=logging.INFO)
# 프론트엔드からの 모든 출처에서의 요청을 허용
CORS(app) 

# Groq 클라이언트 초기화
# API 키는 환경 변수 'GROQ_API_KEY'에서 자동으로 로드됩니다.
try:
    groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    print("Groq client initialized successfully.")
except Exception as e:
    groq_client = None
    print(f"Error initializing Groq client: {e}")

@app.route('/api/convert', methods=['POST'])
def convert_text():
    """
    텍스트 변환을 위한 API 엔드포인트.
    Sprint 1에서는 실제 변환 로직 대신 더미 데이터를 반환합니다.
    """
    data = request.json
    original_text = data.get('text')
    target = data.get('target')

    if not original_text or not target:
        return jsonify({"error": "텍스트와 변환 대상은 필수입니다."}), 400

    # Define prompts for each target audience
    prompts = {
        "상사": "당신은 상사에게 보고하는 어투로 문장을 변환해주는 비서입니다. 핵심을 명확하게 전달하고 존댓말을 사용하여 정중하게 변환해주세요.",
        "동료": "당신은 타팀 동료에게 협업을 요청하는 어투로 문장을 변환해주는 비서입니다. 친절하고 명확하게 요청사항을 전달하고 상호 존중하는 어투를 사용해주세요.",
        "고객": "당신은 고객에게 응대하는 어투로 문장을 변환해주는 비서입니다. 극존칭을 사용하고 전문성과 서비스 마인드를 강조하여 변환해주세요.",
    }

    selected_prompt = prompts.get(target, "당신은 전문적인 비즈니스 어투로 문장을 변환해주는 비서입니다. 상황에 맞게 적절하게 변환해주세요.")

    try:
        if groq_client is None:
            raise Exception("Groq client is not initialized. Check GROQ_API_KEY.")

        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": selected_prompt,
                },
                {
                    "role": "user",
                    "content": original_text,
                }
            ],
            model="moonshotai/kimi-k2-instruct-0905",
            temperature=0.7,
            max_tokens=200,
        )
        converted_text = chat_completion.choices[0].message.content
        
    except Exception as e:
        app.logger.error(f"Error calling Groq API: {e}")
        return jsonify({"error": f"텍스트 변환 중 오류가 발생했습니다: {e}"}), 500

    response_data = {
        "original_text": original_text,
        "converted_text": converted_text,
        "target": target
    }
    
    return jsonify(response_data)

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)