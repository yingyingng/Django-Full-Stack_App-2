to create virtual env:

in Django-Full-Stack_App-2 directory, run:

python3 -m venv env

activate virtual env:

source env/bin/activate

download requirements:

pip install -r backend/requiremnts.txt

------------------------------------------------------------------

to test backend: 

curl -X POST http://localhost:8000/guest-login/ \
-H "Content-Type: application/json" \
-d '{"username": "Ng", "password": 8486}' 
