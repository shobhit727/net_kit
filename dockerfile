FROM python:3.10.6-alpine

# Install dependencies\
#RUN apt-get update && apt-get install -y && rm -rf /var/lib/apt/lists/* 
RUN python3 -m pip install --upgrade pip

#run pip install json configparser requests uuid time datetime tqdm
WORKDIR /app
COPY requirements.txt requirements.txt
#RUN python3 -m pip install 
#RUN pip install --verbose -r requirements.txt

COPY . .

CMD [ "python3 main.py"]
