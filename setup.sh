#!/bin/bash


sudo apt-get install python-rpi.gpio git

cd /opt && git clone https://github.com/planet-winter/artefact.git artefact

cd artefact
sudo artefact.service /lib/systemd/system/artefact.service
sudo chmod 644 /lib/systemd/system/artefact.service
sudo systemctl daemon-reload
sudo systemctl enable artefact.service
sudo systemctl start artefact.service


