Hey guys in this challenge we have png file.
And according to the name I think it's hex corrupted file.
#### <a href='https://github.com/endline01/CTF-Writeups/blob/main/Write%20UPs/JUST-CTF/Warmup/FIX/flag'>challenge file
</a>

So first let's check hexdata 


![image](https://user-images.githubusercontent.com/95076839/221692920-117980dc-9574-439a-bdc5-1d2c02afe64a.png)

Now we realize that the file is png, let's try to fix it. First thing I did was remove all 37 from hexdump(7 in data) but this was so wrong because there is some 37s
that belongs to the image real data.

I put the file on <a href='https://hexed.it/'>hexed.it</a> and I saw that there is columns of 37 in hexdump, So we must remove just these columns.

```bash
xxd -p -c 1 flag > data.txt
```
this command used to extract the hexdump in plain then use this code to remove 37 columns and write the output to 'out.txt' file

```python3
file  = open("data.txt")
f2  = open('out.txt','w')
a = file.readlines()
for i in a[::2]:
	f2.write(i.strip('\n')+' ')
file.close()
f2.close()
```

Now take the out data then convert from hex to png file using cyberchef

![image](https://user-images.githubusercontent.com/95076839/221697573-c0ac7225-6081-4f68-846e-841c999fa76a.png)

### flag: JUST{pyth0n_u53fu!_t0ol!!}
