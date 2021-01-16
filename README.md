Install pip
```
pip3 install virtualenv
```
Create and activate virtualenv
```
cd quickVax
python3 -m venv env
source env/bin/activate
```
Dependencies
```
pip3 install -r requirements.txt
cd main_project/frontend
npm install
```
Run the server
```
./launch.sh
```
Or run just the Django app
```
python3 manage.py runserver
```
