![image](https://user-images.githubusercontent.com/95076839/190122510-c83cd98c-fe7b-46ec-898a-dcd5248988ce.png)

According to the description we must use rockyou.txt to solve this challenge so lets try to under stand the script

![image](https://user-images.githubusercontent.com/95076839/190123375-7a8d5373-3e4b-4bde-ba24-eea34cb639e2.png)

There is nothing interest in it except the function and how the data passed to it.
In the function it hashed every character in md5 then in sha256 so we know that every character becomes 64 bit(we'll get back to this soon).
Ok know we first must brute force the first 3 characters and because we don't know where they come I used <a href="https://www.geeksforgeeks.org/python-string-printable/" target="_blank">string.printable </a>```is a pre-initialized string used as string constant. In Python, string.printable will give the all sets of punctuation, digits, ascii_letters and whitespace.```

![image](https://user-images.githubusercontent.com/95076839/190125645-79d2cb75-e212-48bb-bbac-0c3d9ea04e5f.png)

The highlighted part is for brute force on the first 3 chars.

![image](https://user-images.githubusercontent.com/95076839/190125913-841b858e-4bc8-46bf-a236-f55cd1fc05b0.png)

Now we found the 3 chars lets find the word from rockyou and let's pay attention that the script remove first 3 chars from the returned hash of the word.

![image](https://user-images.githubusercontent.com/95076839/190127558-a4aed206-170d-4472-b014-5482b09769ba.png)

The highlighted part used to brute force on the word and ```word[:-1] used to remove \n, c[192:] used to remove the hash of the three chars we found them above```

![image](https://user-images.githubusercontent.com/95076839/190128403-45db9e18-90e9-44fe-b8f0-625d758e41c8.png)

#### flag: yuctf{%G0janetrzig}
