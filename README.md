### Quick Start

Simple fastapi template to launch microservices using cookiecutter

```
pip install -U cookiecutter
cookiecutter gh:jcc-ne/microservice-fastapi-cookiecutter

# -- enter custom project name and db urls

# -- in your venv
cd <project>/app_pkg/
pip install -r requirements.txt
python main.py  # -- launch dev server locally

```

Expected output:
```
INFO:     Will watch for changes in these directories: ['/private/tmp/microservice example/app_pkg']
INFO:     Uvicorn running on http://0.0.0.0:8081 (Press CTRL+C to quit)
INFO:     Started reloader process [92911] using statreload
...
```
open browser to the url shown http://0.0.0.0:8081/docs
