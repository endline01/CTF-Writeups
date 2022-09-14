for discord challenge:
 -After joining YU discord server and opening a ticket,you have to ask for a flag "nicely" As mentioned in the challenge hint.
 -dicord bot will reply with a link for an online notes contains unreadable graphics.
 -I searched about that ,then I found in 'dcode Symbols Cipher List' a cipher called 'Dancing Men Cipher'.
 -Matching each graphic in given online note with sympols in Dancing Men Cipher and decrypt them  will result with "flagz"
 -passing "flagz" to discord bot will make the bot replies with the following:
      
        -GOOD JOB Here is your half flag : yuctf{FLAGZ_
         i dont think u played fair that's why i gave u an half flag 
         if you want the second half decode that for me HAHAH
         u might use "yuctf" as your magical key 
         URNQVOQYVZ
 -It gave us half of the flag and encrypted second half(URNQVOQYVZ) with a keyword(yuctf)
 -I tried many possible ciphers,but none of them was useful
 -I came back to the bot and read the message again ,this Caught my attention : 'played fair'
    -played fair -->play fair -->playfair 
 -It is playfair cipher 
 -decrypt the second half using playfair cipher and pass it to the bot , it will reply with the final flag
 
    yuctf{FLAGZ_FOR_POINTSX}