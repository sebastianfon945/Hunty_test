FROM python:3.10
WORKDIR /HUNTY_PJ
COPY ./requirements.txt /HUNTY_PJ/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /HUNTY_PJ/requirements.txt
COPY ./app /HUNTY_PJ/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
