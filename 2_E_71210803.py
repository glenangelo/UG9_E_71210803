#input
nama = input("Nama : ").rsplit(" ",1)
ttl = input("Tempat tanggal lahir : ").split(" ",1)

#
print ("Haloo! %s, %s " %(nama[1],nama[0]))
print ("Anda lahir di %s pada tanggal %s" % (ttl[0], ttl[1]))
