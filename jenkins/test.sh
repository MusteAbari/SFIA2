  
#!/bin/bash

sudo apt update
sudo apt-get install -y python3-pip python3-venv

cd outcome
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml 
cd ..

cd player
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
cd ..

cd team
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
cd ..

cd result
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate 
cd ..