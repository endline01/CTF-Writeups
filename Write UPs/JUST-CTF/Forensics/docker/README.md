In this challenge we must solve something realtable to docker.

```docker name: hk17/justctf```

<a href='https://docs.docker.com/get-started/overview/'>Docker overview</a>

<a href='https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/docker-forensics'>Docker Forensics</a>

Firs thing I did was try to run the docker so I can reach it to do another things, so I used this command

```bash
sudo docker dun hk17/justctf
```
Then trying to find what it does so I run docker history.

![image](https://user-images.githubusercontent.com/95076839/221848834-75beaf42-d2d8-475b-9d22-62b2f649ff6f.png)

there is something interesting ```/bin/sh -c rm -rf "/root/secret.txt"```

So let's save the modification new file by running 
```bash
sudo docker save hk17/justctf > docker.tar
```
extract file from it 

![image](https://user-images.githubusercontent.com/95076839/221849661-54b209e2-42ca-48ea-94f8-322ad2d37f8f.png)

then trying to extract each layer and see if the secret there.

![image](https://user-images.githubusercontent.com/95076839/221849910-2e7a15c6-a15f-4f7a-847d-0850779a2e41.png)

![image](https://user-images.githubusercontent.com/95076839/221849991-be87c577-6ceb-4ad3-8262-566fa8280ac6.png)

![image](https://user-images.githubusercontent.com/95076839/221850099-deb2278b-2d5a-4d3f-b281-44ec43cfb206.png)

![image](https://user-images.githubusercontent.com/95076839/221850227-59bc9978-c580-4c07-a7d2-8a5152f2d906.png)

And here I got the flag but I think it's roted using rot13 so just decode it and I got the final flag

![image](https://user-images.githubusercontent.com/95076839/221850583-2a56279b-3b8a-4117-ab38-7022edb22a49.png)

#### flag: JUST{D0CK3R_1M4G3_S0LV3D}
