### Challenge:
![image](https://user-images.githubusercontent.com/95076839/179048172-004935ee-ba03-4650-94c7-14c8327cb6e8.png)

This challenge wants us to learn about <a href="https://en.wikipedia.org/wiki/BitTorrent">BitTorrent</a> protocol

First I enabled the protocol > BT-DHT

![image](https://user-images.githubusercontent.com/95076839/179050493-e9000afd-09f0-42fb-a307-c0218af86ca3.png)

After enable this protocol I excluded other protocols by searching about bt-dht 

![image](https://user-images.githubusercontent.com/95076839/179051560-5ae9e76f-271a-43e6-b2de-abaa46a871ec.png)

Because I solve similar challenge in some onsite CTFs I noticed what I should search on.
It was the hash of the file and in the challenge description asked for file name.
I searched in the packets for the hash of the file 
open BitTorrent DHT protocol in the packets
![image](https://user-images.githubusercontent.com/95076839/179052651-e196da84-ec69-4b96-b88b-e2682d6ed5fa.png)

And I search for the valid value of ```info_hash``` then I try to install the file using hash with <a href='https://www.utorrent.com/'> uTorrent</a>  
```Installing files using there hash in uTorrent``` <a href='https://www.techjunkie.com/utorrent-add-info-hash/'> link </a>
I found it in packet with 139 length try to install it using uTorrent then get the file name:
