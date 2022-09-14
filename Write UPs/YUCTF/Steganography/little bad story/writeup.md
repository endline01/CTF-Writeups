![image](https://user-images.githubusercontent.com/95076839/190215188-f7820012-cdc9-40e9-93ab-0714564648c9.png)

In this challenge there is an OSINT part

when you try any stego techniques to hide data in text files there is nothing appeared then I tried to do some osint and searching about the writer ```By Mark Twainy, 1875``` first thing I noticeed it that the writer name is wrong its ```Twain``` not ```Twainy```
then I searched about any story with name little bad story for the ```Mark Twain``` I found <a href="https://www.washburn.edu/sobu/broach/badboy.html">this</a>
then I made some compare between them with my eyes, I found that the ```little bad story``` #challenge file
have some underscores, then I decided to use tool to highlight the different between to files so I used this <a href='https://codebeautify.org/file-diff'>Online tool</a>

I used it then the letters and the words highlighted in the challenge file.

![image](https://user-images.githubusercontent.com/95076839/190216943-e756467d-e6de-4475-8786-0fd1e3e001fd.png)

Collect the letters and words and its the flag.

#### flag: yuctf{this_story_is_sad_right?} 
