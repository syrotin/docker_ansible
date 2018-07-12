# docker_ansibled

Fast start
-- preparation of the system
If you decide to use the script on a new system, download and run the script: preconf.py

For this:

chmod +x preconf.py
./preconf.py

This will prepare the system and install docker-ce and ansible

-- next step
download docker.yml

and run as:

ansible-playbook docker.yml

it will download git repos, create custom isolated network(isolated_vn), build dockers custom container and start four container
1. php-fpm container
2. nginx container
3. master mysql container
4. slave mysql container

Test 

for test:

open your browser and write ip address host machine, you should see a small website.
to test replication, run: docker exec -it mysql_slave mysql -uroot -pmysqlroot -e "SHOW SLAVE STATUS\G;" in your console
