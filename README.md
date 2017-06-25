# BigPanda exercise - Asher Frenkel

## python implementation
I chose to implement the services with python and flask nanoservices framework.
gunicorn is running the application and invoked by supervisor for watchdoging

## Ansible deployment
I created 3 roles:
1. flask - used to make sure flask,gunicorn and supervisord is insalled
2. img-panda - deploy img-panda service and start it
3. smart-panda -  deploy smart-panda service and start it

I tried to make the deployment roles generic using vars, so that if a new similar service is created just copying the role and changing the app_name and app_port would be suffecient

## Wrapper
simple bash script that does the trick
./deploy.sh -a <app_name> - deploy app_name
./deploy.sh -a all - deploy all application
./deploy.sh (using defaullt all) deploy all applications



