FROM python:3.12-slim

# Copy the uv binary from the official image (pin a specific version in production)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

WORKDIR /app

# Install dependencies first so Docker can cache this layer.
# --locked fails if uv.lock is out of date; --no-dev skips dev-only dependencies.
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev

# Copy the project (including triage_optimized.json if you generated it)
COPY . .

# Use the project's virtual environment directly at runtime
ENV PATH="/app/.venv/bin:$PATH"

# Run as a non-root user
RUN useradd --create-home appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]