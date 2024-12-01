FROM python:3.9-slim
WORKDIR /app
COPY requirements_dashboard.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8050
CMD python main.py