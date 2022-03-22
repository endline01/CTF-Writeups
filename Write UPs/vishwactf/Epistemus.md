### Name: Epistemus
### Category: Forensics

#### Description:

 ![image](https://user-images.githubusercontent.com/95076839/159429262-65b72c7d-89d9-4abb-b27d-800a97a9daf4.png)
 
 This challenge was medium because its new idea for me.
 Ok lets start the challenge

 ![image](https://user-images.githubusercontent.com/95076839/159429747-7d2b051c-19c4-4dac-9a38-62c31f889005.png)

 in this challenge I have this image.. tried steghide..strings..binwalk nothing work, when I go back to the image I noticed there is link in the bottom of the image.
 Open it and got rar and txt files.. tried to open the rar but there is password required tried to crack it but nothing worked.

 After some searching about the text file I found <a href="https://arstechnica.com/information-technology/2014/05/how-to-stash-secret-messages-in-tweets-using-point-and-click-steganography/">this</a>
and using twitter secret message <a href="https://holloway.nz/steg/">online decoder</a>
I got the password and extract the files from it, and there is alot of files.

![image](https://user-images.githubusercontent.com/95076839/159432085-e38a93c9-0e70-4445-bd63-b86c1b67078f.png)

```bash
$ cat *|grep -i flag
```
![image](https://user-images.githubusercontent.com/95076839/159432296-e0553a3f-0ea4-4212-89e2-5f9ae82d6c31.png)

#### flag: `vishwactf{th1ng$_a43_n0t_wh4t_th3y_4lw4y$_$33m}`
