FROM python:3.11.5 as build
WORKDIR /app
COPY poetry.lock .
COPY pyproject.toml .
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry export -f requirements.txt --output requirements.txt        


FROM python:3.11.5
WORKDIR /ua
COPY --from=build /app/requirements.txt .
COPY main.py .
COPY app/ app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    playwright install && \
    playwright install-deps
CMD [ "python", "main.py" ]