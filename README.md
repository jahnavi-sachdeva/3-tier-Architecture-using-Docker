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
<li>Sudo docker [commands] run</li>
&nbsp;&nbsp;&nbsp;&nbsp;-p <port to run on localhost> : <post on which it is exposed> :- port mapping   
&nbsp;&nbsp;&nbsp;&nbsp;--name <name>:- Name of the Container    
&nbsp;&nbsp;&nbsp;&nbsp;--network <network name> :- name of network  
&nbsp;&nbsp;&nbsp;&nbsp;-it :- interactive mode  
&nbsp;&nbsp;&nbsp;&nbsp;-d :- deattached mode  
<li>Sudo docker rmi <image name></li>
&nbsp;&nbsp;&nbsp;&nbsp;-f :- forcefully del<li>e the image / 
<li>Sudo docker compose up </li>  
<li>Sudo docker compose down </li>
<li>Sudo docker <li> rm <container name> </li>  
&nbsp;&nbsp;&nbs/p;&nbsp;-f :- forcefully delete the container  
<li>sudo systemctl restart</li>ocker: restart docker</li>  
<li>sudo docker i</li>nspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}} <container name/id> </li>  
&nbsp;&nbsp;&nbsp;&nbsp;to<li>now the ip address of container  
</li>sudo docker network  </li>create [options] network  <li>li>
&nbsp;&nbsp;&nbsp;&nbsp;dock</li>er network create -d bri<li>e my-bridge-network  
<li>sudo docker network connect <network na</li>me> <container name> </li>  
<li>sudo docker network inspect <network name>  </li>
<li>mysql –h <ip address> -u <user name> -p <password(if any)> </li> 
</ul>
 
