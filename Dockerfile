FROM python:3

RUN git clone https://github.com/nataliohercovich/sudoku.git

WORKDIR /sudoku

RUN pip freeze > requirements.txt

RUN pip install parametrized

RUN pip install requests

RUN pip install -r requirements.txt

CMD ["python", "./test_sudoku.py"]