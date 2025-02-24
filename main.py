import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数を取得する
api_key = os.getenv('GEMINI_API_KEY')
print(f"API Key: {api_key}")
