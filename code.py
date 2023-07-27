import random, time
def ip():
	return str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))
def ver():
	return str(random.randint(1, 30))+"."+str(random.randint(0, 9))
def rstr():
	return random.choice(["Ransomware", "TCP", "UDP", "STREAM", "DGRAM", "Byte", "Send", "Formed", "Hijack", "Hack", "Boom", "IP", "UA", "F", "OMNI", "Try", "Version", "X-Forwarded-For", "X-Except"])
def tstr():
	return random.choice(["Host", "Block", "Hosted", "X", "Chrome", "Firefox", "Bing", "Mozilla", "WIFI", "Ethernet", "Kali", "Linux", "Android", "IPhone", "Tecno", "Q", "Z", "Backdoor"])
def n():
	q = []
	for _ in range(random.randint(2, 5)):
		q.append(random.choice([ip(), ver(), rstr(), tstr()]))
	nb = random.choice([";", "/", " - ", " / ", "-", " ; ", " + ", "+", ", "])
	nc = "["+str(nb).join(q)+"]"
	return f"\033[92m[{nc}]"
while True:
	print(n())
	time.sleep(0.1)
