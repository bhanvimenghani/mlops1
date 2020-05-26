FROM python
COPY . /MLOps
WORKDIR /MLOps
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python", "/bhanvi/MNIST_CNN.py" ]
