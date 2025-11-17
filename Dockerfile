FROM python:3.9-slim

RUN useradd -m user

WORKDIR /home/user/app

COPY --chown=user . /home/user/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

USER user

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
