PYTHON_CMD="python3"
which $PYTHON_CMD >/dev/null 2>&1
if [[ "$?" -ne 0 ]]; then
    PYTHON_CMD="python"
fi

SCRIPT_DIR=`dirname ${BASH_SOURCE[0]}`
cd $SCRIPT_DIR

# $PYTHON_CMD manage.py makemigrations
# $PYTHON_CMD manage.py migrate

cd frontend
npm run dev

cd ..
$PYTHON_CMD manage.py runserver 0.0.0.0:8000
