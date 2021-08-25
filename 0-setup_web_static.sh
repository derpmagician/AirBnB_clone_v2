#!/usr/bin/env bash
# Install nginX, configure http header to your hostname and create directories
sudo apt-get -y update
sudo apt-get -y install nginx
sudo sed -i "15i add_header X-Served-By \$hostname;" /etc/nginx/nginx.conf
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
# Create a fake HTML file
printf "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>\n" | 
sudo tee /data/web_static/releases/test/index.html
# Create the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/
# Set-up the content of /data/web_static/current/ to redirect to magictech.tech/hbnb_static
sudo sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
# Restart nginx service
sudo service nginx restart
sudo service nginx reload
