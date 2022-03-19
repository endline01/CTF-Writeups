### Name Squirrel
### Category: Digital Forensics
### Level: easy
## The meterial for the chellange <a href="https://drive.google.com/file/d/1vnVepy7harBHCWaY2nVzjXG1pZGwQ0tx/view?usp=sharing">here</a>

Hey guys here we go with another Forensics challenges.

In this challenge We have this image:

![image](https://user-images.githubusercontent.com/95076839/159137091-1d867acb-1284-484f-b3cf-9e7459f29d48.png)

First we check metadate and strings in any thing we have

checking output of exiftool.. got nothing, when I check strings there is mediafire link there 
" https://www.mediafire.com/file/yuy6pf4pj3004em/iamnotreal.zip/file "

I downloaded the file and it turned out that it needs a password, crack it using John the ripper then I got EVIL directory that have EVIL file and the file doesn't open and corrupt, also checking string and it have media fire link inside it but this time the link doesn't work..

Ok checking the file header and then I noticed that the file hav JFIF value in the header
![image](https://user-images.githubusercontent.com/95076839/159137185-f0856894-4d3e-41e0-8774-7078e1f23817.png)

and this means that the file can be <a href="https://en.wikipedia.org/wiki/JPEG_File_Interchange_Format">JPEG</a>


Fix the header and open the image then I got the flag but base32 encoded ... decode it and submit the flag :)

![image](https://user-images.githubusercontent.com/95076839/159137235-c64119c9-c5b8-4dc2-991a-8737e4433af5.png)

# I hope this was helpful
