from stegano import lsb

clear_message = lsb.reveal("./Secret Cat.png")

print(clear_message)