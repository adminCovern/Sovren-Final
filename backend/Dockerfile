FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Hide noisy pip root user warning inside containers
ENV PIP_ROOT_USER_ACTION=ignore


WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Code is bind-mounted by docker compose; default command is defined in compose as well
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

