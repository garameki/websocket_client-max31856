#!/bin/bash

_stem=websocket-client-max31856-9801
_description="Send sockets of temperature from max31856"
_forward=/etc/systemd/system/

_here=$(pwd)

_STEM=$_here/$_stem

sed s/$^//<< EOS > $_STEM.service 
[Unit]
Description=$_description

[Service]
ExecStart=$_STEM.sh
Restart=always

[Install]
WantedBy=multi-user.target
EOS

sudo chmod 640 $_STEM.service
sudo ln -fs $_STEM.service $_forward
sudo systemctl enable $_STEM.service
