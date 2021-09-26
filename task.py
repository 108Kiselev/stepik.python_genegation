ips = [input() for i in range(int(input()))]


def totens(ip):
    ip = list(map(int, ip.split('.')))
    return ip[0] * 256**3 + ip[1] * 256**2 + ip[2] * 256 + ip[3]


print(*sorted(ips, key=totens), sep='\n')