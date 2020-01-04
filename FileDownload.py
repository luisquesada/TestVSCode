import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")

try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: {0}".format(exc))

result_File = open("info.txt","wb")

for chunck in res.iter_content(100000): #100000 bytes
    result_File.write(chunck)

result_File.close()


