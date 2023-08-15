# Computers_Network_Project
Written by:
* Roy ofer
* Kfir Zilbernagel

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

* src Directory: Here, you'll find the heart of our code.
* resources Directory: The following directory houses all the files we exported as CSVs from WireShark, along with the packet recordings stored as PCAP files.
* res Directory: This directory contains images showcasing all the graphs generated as a result of the filters we applied.
* Dry part: Encompassing the essence of the article "Practical Traffic Analysis Attacks on Secure Messaging Applications," it encapsulates key insights. Additionally, it provides responses to the assigned questions.

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

![image](https://github.com/Kfirul/Computers_Network_Final_Project/assets/99495429/a78aad1b-7774-43e2-a586-ffc434130cef)


 2.Example Two - Categorizing Packets for Message Types:**
   In this case, we sorted the packets based on the type of content they carried: text, image, video, or file. By examining packet lengths, timing, and content, we could accurately categorize messages according to their formats. This approach provided a granular view of how different message types were transmitted and received within the encrypted traffic.

![image](https://github.com/Kfirul/Computers_Network_Final_Project/assets/99495429/0619f099-adbd-4803-b9c9-3aa1f6202863)

## Getting Started with the Project
To make use of this project, follow these simple steps:

### Clone the Repository:
Open your terminal and navigate to the directory where you want to store the project. Use the following command to clone the repository:

Copy code:git clone https://github.com/Kfirul/Computers_Network_Final_Project.git

Explore and Run: inside the project directory, explore the contents and follow the README instructions to set up and run the project as needed.

Now you're all set to dive into the project and explore its functionalities.

Enjoy!

  
