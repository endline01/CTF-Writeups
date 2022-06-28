# Sleuthkit Apprentice
### Challenge: 
![image](https://user-images.githubusercontent.com/95076839/175832864-137deaff-1fd8-446b-aa4c-91415ffa5a36.png)

This challenge can be solved using <a href='https://www.kali.org/tools/sleuthkit'> Sleuthkit </a> 
but I solve it using FTK imager 

first I try to mount the disk image in FTK imager
then I searched for the flag in partition 1 and 2 but I found nothing.
in partition 3 I serched in home directory for any user but there is nothing to search for. 
But there is another root directory in first root dir open it and found my_folder when open it I found the flag.
![image](https://user-images.githubusercontent.com/95076839/176062226-70b93748-2a9b-4c28-a926-d6aeb0d73d61.png)


#### Just searching in the disk image using FTK imager.

# ---------------------------------------------------- 
# Operation Oni
### Challenge:
![image](https://user-images.githubusercontent.com/95076839/176065403-6d9c25a1-36a8-4b95-9cc8-edeaf956bd3f.png)

In this challenge I also used FTK imager to solve it,

In partition2 in root directory in the first root directory I found ssh key 
![image](https://user-images.githubusercontent.com/95076839/176065636-e54d5b25-4ee5-48dd-9b5d-bdbbef88ada5.png)

copy the key in file and make the permissions just for the user, I make it just read
and this step because you can't connect with private rsa key if it readable for anyone

![image](https://user-images.githubusercontent.com/95076839/176066677-8fbcc280-0904-43ab-a66c-d1fe56ecc623.png)
