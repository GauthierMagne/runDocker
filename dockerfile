FROM python:3.7

ARG PORT
ENV PORT=$PORT

WORKDIR /app
COPY app /app
RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE $PORT

CMD ["python","main.py"] 