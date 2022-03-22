### Name: SoForgetful
### Category: Forensics
### Level: easy  

![image](https://user-images.githubusercontent.com/95076839/159420703-60e8be1b-1b44-439b-94e3-68d7f92adb3d.png)

In this challenge there is a pcap file and I want to find the password in it.

When I opened the file I try protocol hirarchy (statistics -->protocol hirarchy) and I noticed that there are HTML form URL encoded

![image](https://user-images.githubusercontent.com/95076839/159413917-a1b9586b-1886-4c91-b498-51572cca6497.png)

checked it and got the password base64 encoded decode it and got the flag

![image](https://user-images.githubusercontent.com/95076839/159413990-29425dff-b382-4e3b-80a1-7a0086c726fc.png)

## flag: vishwactf{KN1Z6PXVy9}
