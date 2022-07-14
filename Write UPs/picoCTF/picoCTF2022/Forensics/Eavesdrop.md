### Challenge:
![image](https://user-images.githubusercontent.com/95076839/176062986-0419771f-20b6-4383-885d-e28583ac74b0.png)

Open the file with wireshark and search for any thing intersting I found chat conversation once I follow TCP frame for the first TCP packet 
there is command to decrypt triple des (des3) in the packet.
I searched alot about any file to decrypt but I found nothing, I tried binwalk to extract it and it works 

![image](https://user-images.githubusercontent.com/95076839/176063694-e24e1d57-de3c-4bc7-aa98-7885b22a924c.png)

decrypt it using the same command in the pcap file and I found the flag
![image](https://user-images.githubusercontent.com/95076839/176063920-608a3904-b5b1-47d4-bbc5-cb1c0500b7ee.png)
