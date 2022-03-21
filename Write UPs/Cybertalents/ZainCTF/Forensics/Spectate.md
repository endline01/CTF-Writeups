### Name: Spectate
### Category: Network Secrity
### Level: easy
## The material for Spectate <a href="https://drive.google.com/file/d/16zDubqlXtNYd6EjX9TGSzsxlgzLgtjLB/view?usp=sharing">here</a>
Hi guys this write up for Spectate in zainc CTF

In the description they told us that the conversation on TCP.

when we open the file and follow the TCP of the packet in the first three we got password for data.txt file but there is no file like that in the packet so I try to extract it using "binwalk" and I got Zip file that needs a password.

When I go back to the packet and follow the TCP of the TCP packets I got password

![image](https://user-images.githubusercontent.com/95076839/159231346-c5d733c9-af9d-49c1-8ba2-6ebd878a2ff9.png)

extracted the file and I got the flag:)
