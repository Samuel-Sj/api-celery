FROM python:3.12-slim
WORKDIR /api-celery
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY ./pyproject.toml ./uv.lock ./api-celery/

RUN uv sync --locked

COPY .app/ /api-celery/

EXPOSE 8000

CMD ["uv", "run", "uvicorn","app.main:main","--host","0.0.0.0","--port","8000"]