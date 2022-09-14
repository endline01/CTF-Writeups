![image](https://user-images.githubusercontent.com/95076839/190197776-b347829a-11ac-4df0-9037-0e054d43219e.png)

This challenge can be solved in two ways. The first way: open the file in wire shark and investigate the packets to find an interesting string or any thing indicates that there is data here.

while seeing the packets I found one ICMP packet that have base64 in it so lets decode it and get the flag.

![image](https://user-images.githubusercontent.com/95076839/190198861-55eaced5-657a-47e7-8dcc-483f270f6aad.png)

The second way is to use strings and you'll find base64 decode it you'll get the flag.

![image](https://user-images.githubusercontent.com/95076839/190200799-7e987f6f-6322-43df-968c-53b2e92cc031.png)

![image](https://user-images.githubusercontent.com/95076839/190200900-d2dd8b4a-13fd-40c0-85e1-164999d3e664.png)

#### flag: yuctf{1_c4n_see3_1cMp}
