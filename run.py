# run.py
import sys
import os

# 将项目根目录添加到Python路径
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# 在导入任何应用模块之前，首先加载环境变量
from dotenv import load_dotenv
load_dotenv()

from app.web.web_server import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8888))
    app.run(host='0.0.0.0', port=port, debug=False)
