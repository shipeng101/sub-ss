# 使用 Python 作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制代码到容器中
COPY script.py .

# 安装所需的依赖
RUN pip install requests pyaes flask

# 创建 output 目录
RUN mkdir sub

# 执行脚本
CMD ["python", "script.py"]
