![image](https://user-images.githubusercontent.com/95076839/190195891-05d281a4-b9e8-4c47-bc0f-450b28cf4335.png)

This challenge was so easy this how you can solve it

```bash
└─$ strings Angry.pcapng|grep -i {
```
then you'll find the flag reversed
```bash
└─$ python3 -c "flag='}y3sae_os_53os_s3tneMm0C{ftcuy';print(flag[::-1])"
```

![image](https://user-images.githubusercontent.com/95076839/190196336-7bce5d14-f296-4435-90c2-ab3f34d9c116.png)

#### flag: yuctf{C0mMent3s_so35_so_eas3y}
