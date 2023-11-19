## Running the project
1. Install requirements: `pip install requirements.txt`
2. Run server: `python manage.py runserver`

### Stuff not working as intended
**Issue**: Interacting with web sockets is a bit confusiong in Python. While Go is able to connect, the data it sent is never received, the data sent by JS is received. It also broke some dependancies, like static imports.
**To replicate**: run `uvicorn simfin.asgi:application`
**Idea(s)**: Maybe it has something to do with how data is shared and how `uvicorn` server works.
**Resolution**: For now, reverting to Django-only version of app.