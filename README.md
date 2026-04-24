# SDN-Traffic-Classification-System
## Description
This project implements a Software Defined Networking (SDN) based traffic classification system using the POX controller and Mininet.

The controller captures packets and classifies traffic based on protocol type such as ARP, IPv4, and IPv6. The classification logic is implemented in a separate module.

---

## Tools Used
- Python  
- Mininet  
- POX Controller  

---

## Network Topology
- 1 Switch (s1)  
- 2 Hosts (h1, h2)  

---

## Project Structure

code/
- topology.py → Defines Mininet topology  
- controller_pox.py → Handles packets in controller  
- classifier.py → Classifies traffic  

---

## How to Run

Step 1: Start Controller  
cd ~/pox  
./pox.py log.level --DEBUG openflow.of_01 forwarding.l2_learning controller_pox  

Step 2: Run Topology  
cd ~/SDN_Project  
sudo mn --custom code/topology.py --topo mytopo --controller=remote,ip=127.0.0.1,port=6633  

Step 3: Test  
h1 ping h2  

---

## Output
The controller displays packet details and classification in real-time.

---

## Key Concept
This project demonstrates SDN architecture where the control plane is separated from the data plane.

---

## Author
LAKSHITHA 
