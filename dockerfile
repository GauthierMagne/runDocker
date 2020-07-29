FROM python:3.7

ARG PORT
ENV PORT=5000

WORKDIR /app
COPY app /app
RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE $5000

CMD ["python","main.py"] 
