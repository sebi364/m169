FROM python:3.12.2

# create and set working directory
WORKDIR /app
COPY ./app.py ./app.py
COPY ./requirements.txt ./requirements.txt

# install dependencies
RUN pip install -r /app/requirements.txt

# expose port and start app
EXPOSE 5000
CMD ["python", "-u", "/app/app.py"]