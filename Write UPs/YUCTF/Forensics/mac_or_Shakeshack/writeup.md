![image](https://user-images.githubusercontent.com/95076839/190164694-40fffdb3-d293-4530-a345-6d9c3806eec9.png)

For this challenge I used binwalk to extract the files in the word document
```bash
└─$ binwalk --extract <filename>
```
Then I tried to find the flag in the extracted files

![image](https://user-images.githubusercontent.com/95076839/190165400-9fda73eb-c95c-4d09-a1a7-084e7f4c761b.png)

#### flag: yuctf{M@acros_1s_N0t_My3_fr1ends}
