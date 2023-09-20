install all the lib:
    git clone --single-branch --branch helpers git@github.com:khoamajik1752/rest-cinema.git helpers
    pip install -r requirements.txt


run the program:
    uvicorn main:app --port 8001 --reload