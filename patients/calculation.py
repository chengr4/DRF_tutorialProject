# 可以整個檔刪除
'''import sqlite3


conn = sqlite3.connect('../db.sqlite3')
print("Open DB successfully")

c = conn.cursor()

cursor = conn.execute("SELECT id, sbp_raw, dbp_raw, hr_raw from patients_patient")

for row in cursor:
  # 這行寫計算
  c.execute("UPDATE patients_patient set sbp = %d where ID = %d" % (row[1],row[0]))
  c.execute("UPDATE patients_patient set dbp = %d where ID = %d" % (row[2],row[0]))
  c.execute("UPDATE patients_patient set hr = %d where ID = %d" % (row[3],row[0]))

conn.commit()
conn.close()'''