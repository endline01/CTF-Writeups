![image](https://user-images.githubusercontent.com/95076839/190170187-efd21755-1cee-4281-aaf5-bfd668d0fdc4.png)

In this challenge I learned a new idea, when I see its extension I tried to find .dat file viewer but when open the file I found nothing, so after alot of seaching the writers release a hint about it 

hint: Xory

so now we know that its xor, I tried tools to xor the file like xcat,xortool,xor-decrypt, and xor_tools but none of them help me to solve the challenge so I tried cyberchef
upload the file on the cyberchef and lets try the key in the description with all formulas(hex, latin,...etc) first I try hex but nothing and after some attempts I tried decimal key

![image](https://user-images.githubusercontent.com/95076839/190172383-345e844f-e6ea-43b7-bca6-8d1fc3ad22c3.png)


Here the JPEG file structure appeared.
And save the output as a jpg file and when I opened the image I found the flag.

![image](https://user-images.githubusercontent.com/95076839/190172585-efdfdc5d-4e94-45a0-89ca-95ae0f6a934f.png)

#### flag: yuctf{X0r_1s_y0ur_friend}
