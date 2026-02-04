document.addEventListener('DOMContentLoaded', () => {
    const originalTextInput = document.getElementById('original-text');
    const charCountDisplay = document.querySelector('.char-count');
    const targetAudienceSelect = document.getElementById('target-audience');
    const convertButton = document.getElementById('convert-button');
    const convertedTextInput = document.getElementById('converted-text');
    const copyButton = document.getElementById('copy-button');

    // 1. Character Counting
    originalTextInput.addEventListener('input', () => {
        const currentLength = originalTextInput.value.length;
        charCountDisplay.textContent = `${currentLength}/500`;
    });

    // 2. Convert Text Functionality
    convertButton.addEventListener('click', async () => {
        const originalText = originalTextInput.value.trim();
        const targetAudience = targetAudienceSelect.value;

        if (!originalText) {
            alert('변환할 텍스트를 입력해주세요.');
            return;
        }

        convertButton.disabled = true;
        convertButton.textContent = '변환 중...';
        convertedTextInput.value = '변환 중입니다. 잠시만 기다려 주세요...';

        try {
            const response = await fetch('http://localhost:5000/api/convert', { // Ensure this matches your Flask API URL
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    original_text: originalText,
                    target_audience: targetAudience,
                }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || '텍스트 변환에 실패했습니다.');
            }

            const data = await response.json();
            convertedTextInput.value = data.converted_text;
        } catch (error) {
            console.error('Error converting text:', error);
            convertedTextInput.value = `오류 발생: ${error.message}. 잠시 후 다시 시도해주세요.`;
            alert(`오류: ${error.message}`);
        } finally {
            convertButton.disabled = false;
            convertButton.textContent = '변환하기';
        }
    });

    // 3. Copy to Clipboard Functionality
    copyButton.addEventListener('click', () => {
        if (convertedTextInput.value) {
            convertedTextInput.select();
            convertedTextInput.setSelectionRange(0, 99999); // For mobile devices
            try {
                document.execCommand('copy');
                copyButton.textContent = '복사 완료!';
                setTimeout(() => {
                    copyButton.textContent = '복사하기';
                }, 2000);
            } catch (err) {
                console.error('Failed to copy: ', err);
                alert('텍스트 복사에 실패했습니다.');
            }
        }
    });
});
