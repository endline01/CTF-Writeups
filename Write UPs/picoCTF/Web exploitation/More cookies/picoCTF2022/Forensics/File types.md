## Challenge:
![image](https://user-images.githubusercontent.com/95076839/175823737-cbbaed5f-0c41-442d-896a-60436adfb817.png)

This challenge have file and the file end with .pdf but try to read its content 
its bash script.

first install uudecode 
```bash
sudo apt-get install sharutils
```
then run the file its output will be flag file 
fun file command on flag to know what its type and its ar archive
![image](https://user-images.githubusercontent.com/95076839/175824382-638d9be0-ceb3-4eb7-9b00-ac6468389890.png)

run 
```bash
ar x fil_name
```
then repeat the steps run file command on the file output to know what type of archive and decompress it 

#### Note: some archives you must to rename the files to their extension

use this commands after the above steps to solve the challenge:

```bash
$ mv flag flag.cpio

$ cpio -i <flag.cpio

$ bzip2 -d flag

$ mv flag.out flag.gz

$ gzip -d flag.gz

$ sudo apt install lunzip

$ lunzip -d flag

$ sudo apt install lz4

$ mv flag.out flag.lz4

$ lz4 -d flag.lz4

$ sudo apt install lzma

$ mv flag flag.lzma

$ lzma -d flag.lzma

$ sudo apt install lzop

$ mv flag flag.lzop

$ lzop -d flag.lzop

$ lzip -d flag

$ mv flag.out flag.xz

$ xz -d flag.xz

$ cat flag
```
the output from cat flag will be hex convert it to ascii and you'll get the flag.
