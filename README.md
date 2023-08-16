# Computers_Network_Project
Written by:
* Roy ofer
* Kfir Zilbernagel

## Getting Started with the Project
To make use of this project, follow these simple steps:

### Clone the Repository:
Open your terminal and navigate to the directory where you want to store the project. Use the following command to clone the repository:

Copy code:git clone https://github.com/Kfirul/Computers_Network_Final_Project.git

In case the folder doesn't appear in your Jupter do the following steps:

1.Open Jupter Notebook via Anaconda Navigator.

2.Upload to Jupter the Folder as *ZIP* file then open a new Notebook type python3, and write there the following code:
* import zipfile as zf
* files = zf.ZipFile("Computers_Network_Final_Project.zip", 'r')
* files.extractall('Computers_Network_Final_Project')
* files.close()

3.After using the code, you will now have a folder name Computers_Network_Final_Project, where the code is inside src folder and the file named Computers Network.ipynb.

4.Now you're all set to dive into the project and explore its functionalities.


## Project Overview
Welcome to this project, where we delve into the realm of secure messaging application vulnerabilities through an exploration inspired by the research paper titled "Practical Traffic Analysis Attacks on Secure Messaging Applications".

This intriguing study exposes the illusion of complete secrecy in instant messaging apps. 
By harnessing simple statistical techniques and employing filters, we unearth valuable insights from the data transportation process.

Link to the paper: https://www.ndss-symposium.org/wp-content/uploads/2020/02/24347-paper.pdf

## Our Approach
Our journey begins by dissecting the inter-message delays and message sizes within various groups in Whatsapp, meticulously documented in the aforementioned paper.

With a keen eye, we identify distinctive attributes within each group, encompassing messages, images, videos and files.
We meticulously consider two scenarios:

* Singular Group Activity: In this scenario, we examine instances where the targeted user engages in a single IM group at a time.
* Concurrent Group Activity: This scenario explores situations where the targeted user participates in multiple IM groups simultaneously.

# The Project Structure
Let's navigate through the project structure to orient ourselves:

* src Directory: Here, you'll find the heart of our code in the Jupyter Notebook, In the functions file, we documented the key functions we utilized solely for the purpose of facilitating easy access to their code, should anyone prefer to locate them there instead of navigating through the entire notebook.
  (It is organized neatly in the notebook as well).
* resources Directory: The following directory houses all the files we exported as CSVs from WireShark, along with the packet recordings stored as PCAP files.
* res Directory: This directory contains images showcasing all the graphs generated as a result of the filters we applied.
* Dry part:The name will be Our IDs combine. Encompassing the essence of the article "Practical Traffic Analysis Attacks on Secure Messaging Applications," it encapsulates key insights. Additionally, it provides responses to the assigned questions.

# Dataset and Insights
Our methodology relies on transforming Wireshark records into CSV files for streamlined analysis. Each CSV file is a repository of vital information:

1. No. - Packet number
2. Time - Timestamp in milliseconds of packet/message capture
3. Source - Source IP address
4. Destination - Destination IP address
5. Protocol - Network protocol governing communication
6. Length - Packet length in bytes, including headers and payload data

# Examples of Filtered Results
1. Example One - Categorizing Packets for WhatsApp and Spotify:
   In this scenario, we organized the packets into distinct categories for WhatsApp and Spotify. By analyzing network protocols, we identified specific patterns unique to each application. This allowed us to differentiate the traffic associated with WhatsApp from that of Spotify, enabling a comprehensive analysis of their behaviors.

![image](https://github.com/Kfirul/Computers_Network_Final_Project/assets/99495429/ec138688-8fe6-45e8-aca5-5f081a392957)



 2.Example Two - Categorizing Packets for Message Types:**
   In this case, we sorted the packets based on the type of content they carried: text, image, video, or file. By examining packet lengths, timing, and content, we could accurately categorize messages according to their formats. This approach provided a granular view of how different message types were transmitted and received within the encrypted traffic.

![image](https://github.com/Kfirul/Computers_Network_Final_Project/assets/99495429/0619f099-adbd-4803-b9c9-3aa1f6202863)




  
