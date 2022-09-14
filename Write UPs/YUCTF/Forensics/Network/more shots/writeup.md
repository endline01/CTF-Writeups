![image](https://user-images.githubusercontent.com/95076839/190202395-8028b6d4-0e71-489c-aefc-abbf9b0707fe.png)

This challenge was a little bit tricky but still easy :)

open the file with wire shark and because the first challenge solved with ICMP I decided to start with it, While seeing the packet there is an ECHO requests to three websites but with different character every time

![image](https://user-images.githubusercontent.com/95076839/190203692-b5dd4ed7-937b-4100-b66a-c5ae052a4a7d.png)

![image](https://user-images.githubusercontent.com/95076839/190203660-cdb0e94e-f81c-4bd4-b647-54be54ade18a.png)

So because the first one was bas64 this may be the same, I take every last character in every url then decode it and I got the flag.

so lets use the easier way to solve it

![image](https://user-images.githubusercontent.com/95076839/190206810-50d5240f-2b65-4064-907d-3d862a3b7aa3.png)

I put it in output.txt file to make script takes every last char
```python3
#!/usr/bin/python3
f=open('output.txt').readlines()
for i in f:
    # this loop used to take just characters and ignore the `
    if i.strip('\n')[-1]!="`": 
        print(i.strip('\n')[-1],end='')
    else:
        print(i.strip('\n')[-2],end='')
```

![image](https://user-images.githubusercontent.com/95076839/190208486-c2a3e548-43df-4ade-ac5c-656d99c13a72.png)

#### flag: yuctf{M0r3_0ne_Sh0T5}
