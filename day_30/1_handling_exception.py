try:
    file=open("day_30/a_file.txt")
    # we know that there is no such file in this folder

except FileExistsError:
    # FileExistsError garyo vaney k hunxa vaney: yo error xa vaney matra new_file create hunxa
  #  print("There was an error") 
# yo vaneko k ho vaney: tyo file exist gardaina ko matlab try ma vako kura wrong xa, if so print this
    file=open("day_30/a_file.txt","w")
    # yesle chai tyo file xaina vaney pani new file create gardinxa but it will be empty

except KeyError as error_message:
    print(f" the key {error_message} does not exist.")

# else  chai try ma vako kura sucess vayo vaney run hunxa
else:
    content=file.read()
    print(content)

finally:
    file.close()
    # with use nagarda file open nei rahanxa so close it
    print("file was closed.")
    #try ma vako kura suceed vaye pani navaye pani yo print hunxa