import pymysql
con = pymysql.connect(db="absen", user="root", passwd="",host="localhost",port=3306,autocommit=True)

cur = con.cursor()
cur.execute("SELECT card FROM siswa")
card = [cur.fetchall()]
# try:
#    cur.execute("SELECT card FROM siswa")

#    rcount = int(cur.rowcount)
   
#    for row in rcount:
#       row = cur.fetchone()

#       card.append(row[0])
#       nama.append(row[1])

# except:
#    print ("Error: unable to fecth data")

# cur.close()


print(card)