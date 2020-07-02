# 3-tier-Architecture-using-Docker


One common architecture for information systems that includes a user interface and persistent storage of data is known as the three-tier architecture. A classic description of the vertical tiers is:  
Presentation - windows, reports, and so on.  
Application Logic - tasks and rules which govern the process.  
Storage - persistent storage mechanism.  
The singular quality of a three-tier architecture is the separation of the application logic into a distinct logical middle tier of software. The presentation tier is relatively free of application processing; windows forward task requests to the middle tier. The middle tier communicates with the back-end storage layer.  
Commands used. 
<ul>
<li>Sudo docker build –t <image name> <path> </li>
&nbsp;&nbsp;&nbsp;&nbsp;Sudo docker build –t frontend .  
<li> Sudo docker [commands] run </li>
&nbsp;&nbsp;&nbsp;&nbsp;-p <port to run on localhost> : <post on which it is exposed> :- port mapping   
&nbsp;&nbsp;&nbsp;&nbsp;--name <name>:- Name of the Container    
&nbsp;&nbsp;&nbsp;&nbsp;--network <network name> :- name of network  
&nbsp;&nbsp;&nbsp;&nbsp;-it :- interactive mode  
&nbsp;&nbsp;&nbsp;&nbsp;-d :- deattached mode  
<li> Sudo docker rmi <image name> </li>
&nbsp;&nbsp;&nbsp;&nbsp; -f :- forcefully delete the image 
<li>Sudo docker compose up </li>  
<li>Sudo docker compose down </li>
<li>Sudo docker rm <container name> </li>  
&nbsp;&nbsp;&nbsp;&nbsp; -f :- forcefully delete the container  
<li>sudo systemctl restart docker </li>
 &nbsp;&nbsp;&nbsp;&nbsp;Used to restart the docker
<li>sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}} <container name/id> </li>  
&nbsp;&nbsp;&nbsp;&nbsp;to know the ip address of container  
</li>sudo docker network create [options] network  </li>
<li>docker network create -d bride my-bridge-network  </li>
<li>sudo docker network connect <network name> <container name> </li>  
<li>sudo docker network inspect <network name>  </li>
<li>mysql –h <ip address> -u <user name> -p <password(if any)> </li> 
</ul>
 
