FROM jupyter/scipy-notebook

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install voila

ADD . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8888"]