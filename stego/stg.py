from stegano import lsb


secret = lsb.hide("./Cat.jpeg", "No one should know this")
secret.save("./Secret Cat.png")
