FROM python3.9

WORKDIR /src

COPY requirements.txt /src/

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /src/