![image](https://user-images.githubusercontent.com/95076839/190148027-26beca88-fa62-4163-bd25-3412b4d0d4bc.png)

Xor challenge, first I tried yuctf{ because this what I know from the flag.
The output:

![image](https://user-images.githubusercontent.com/95076839/190148619-06592551-d854-44f5-8a70-5d2b93e2679f.png)

its perfect word I used it as a key and got this

![image](https://user-images.githubusercontent.com/95076839/190148754-9af20a15-042c-4994-bfe7-20d86f72e4e2.png)

now because the key has 8 stars that indicates to length of the key

![image](https://user-images.githubusercontent.com/95076839/190148901-18fee33a-6a24-405b-92a9-53590456558b.png) 

the length of the perfect word = 7 so we must brute force the last char of the key.

![image](https://user-images.githubusercontent.com/95076839/190149323-98fbe66f-5f20-4285-ae86-0f6bf1ae8655.png)

<a href='https://www.geeksforgeeks.org/python-string-printable/'>printable</a>

<a href='https://dtabarie.com/posts/2020-08-16-python3-xor-bytes.html'>from pwn import xor</a>

![image](https://user-images.githubusercontent.com/95076839/190149950-5d8a6c7e-c0b5-41ff-aa90-28bcdcd772a1.png)


#### flag: yuctf{X0r_15_r3v3rsible}
