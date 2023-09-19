FROM python:3.11.5 as build
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry export -f requirements.txt --output requirements.txt        

FROM python:3.11.5
WORKDIR /ua
COPY --from=build /app/app app/
COPY --from=build /app/main.py .
COPY --from=build /app/requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    playwright install && \
    playwright install-deps
ENV UNDER_ARMOUR_OFFERS_URL="https://www.underarmour.com.br/calcados/outlet?initialMap=productclusterids&initialQuery=386&map=category-2,productclusternames"
ENV MAX_CONCURRENCY=8
CMD [ "sleep", "3000" ]