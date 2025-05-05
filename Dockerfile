FROM python:3.12-slim

WORKDIR /app
COPY . .

# Install livereload (and watchdog as a dep)
RUN pip install livereload

EXPOSE 8888

CMD ["python", "devserver.py"]