from utils.email_statistics import Statistics_Entry

stats = {}
word_check = ["account", "inform", "updat", "pleas", "secur", "alert",
              "request", "click", "fradul", "notif", "upgrad", "indefinit",
              "access", "password", "verif", "provid", "confidenti"]

for el in word_check:
    stats.update({el: 0})
    stats[el] += 1

entry = Statistics_Entry("hi", stats["access"], stats["account"], stats["alert"], stats["click"], stats["confidenti"],
                         stats["fradul"], stats["indefinit"], stats["inform"], stats["notif"], stats["password"],
                         stats["pleas"], stats["provid"], stats["request"], stats["updat"], stats["upgrad"], stats["verif"], 0)
print(entry)