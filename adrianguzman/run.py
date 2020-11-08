import subprocess


subprocess.run(['python', 'manage.py', 'runserver', '0.0.0.0:8000'],
               shell=True)
