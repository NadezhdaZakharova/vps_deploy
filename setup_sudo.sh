#!/bin/bash
# Выполните эту команду на сервере от root или через sudo
echo "zaharova ALL=(ALL) NOPASSWD: /bin/systemctl restart zaharova-api" | sudo tee /etc/sudoers.d/zaharova
sudo chmod 0440 /etc/sudoers.d/zaharova
