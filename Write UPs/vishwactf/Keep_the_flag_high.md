### Name: Keep the flag high
### Category: Forensics

#### Description:

![image](https://user-images.githubusercontent.com/95076839/159422699-7dabd2a2-ecd6-40d7-9c36-f664563ded96.png)

In this challenge there is image .bmb but if I try to open it there is error.
try to show the header using xxd to determine the file type I noticed that there is IHDR and this refer to the png image.

Fixed the header and I got QR code

![image](https://user-images.githubusercontent.com/95076839/159423299-376a7453-035f-44f3-8af4-6e30923cf185.png)

scan it and got google drive link open it and download the image... try every thing on it but got nothing lol!
but when I go back to the challenge description it says that we have to rotate somthing.. after some searching I got it, do strings on image and got the string in the bottom

![image](https://user-images.githubusercontent.com/95076839/159423965-bc914857-b5f9-441f-a869-0b83b5e563a2.png)

now I should to rotate it, search about it in <a href="https://www.dcode.fr/cipher-identifier">this cipher identifier</a>
and got it, its rot47 

![image](https://user-images.githubusercontent.com/95076839/159424938-c7e88c8e-eeaf-4f3e-a29d-efcca16eb058.png)

![image](https://user-images.githubusercontent.com/95076839/159425020-df521851-66e5-491b-85b3-71b0959cf94d.png)

## flag:VishwaCTF{f0r3nsic5_is_t3di0us}
