# 3-tier-Architecture-using-Docker


One common architecture for information systems that includes a user interface and persistent storage of data is known as the three-tier architecture. A classic description of the vertical tiers is:  
Presentation - windows, reports, and so on.  
Application Logic - tasks and rules which govern the process.  
Storage - persistent storage mechanism.  
The singular quality of a three-tier architecture is the separation of the application logic into a distinct logical middle tier of software. The presentation tier is relatively free of application processing; windows forward task requests to the middle tier. The middle tier communicates with the back-end storage layer.
Commands used.  
•   Sudo docker build –t <image name> <path>  
&nbsp;&nbsp;&nbsp;&nbsp;Sudo docker build –t frontend .  
•   Sudo docker [commands] run  
&nbsp;&nbsp;&nbsp;&nbsp;-p <port to run on localhost> : <post on which it is exposed> :- port mapping   
&nbsp;&nbsp;&nbsp;&nbsp;--name <name>:- Name of the Container    
&nbsp;&nbsp;&nbsp;&nbsp;--network <network name> :- name of network  
&nbsp;&nbsp;&nbsp;&nbsp;-it :- interactive mode  
&nbsp;&nbsp;&nbsp;&nbsp;-d :- deattached mode  
•	Sudo docker rmi <image name>  
&nbsp;&nbsp;&nbsp;&nbsp;-f :- forcefully delete the image  
•	Sudo docker compose up  
•	Sudo docker compose down  
•	Sudo docker rm <container name>  
&nbsp;&nbsp;&nbsp;&nbsp;-f :- forcefully delete the container  
•	sudo systemctl restart docker: restart docker  
•	sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}} <container name/id>  
&nbsp;&nbsp;&nbsp;&nbsp;to know the ip address of container  
•	sudo docker network create [options] network  
&nbsp;&nbsp;&nbsp;&nbsp;docker network create -d bridge my-bridge-network  
•	sudo docker network connect <network name> <container name>  
•	sudo docker network inspect <network name>  
•	mysql –h <ip address> -u <user name> -p <password(if any)>  

 
