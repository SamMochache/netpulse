import nmap

def advanced_scan(subnet="192.168.1.0/24"):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=subnet, arguments='-sn')
    hosts = []

    for host in scanner.all_hosts():
        hosts.append({
            "ip": host,
            "hostname": scanner[host].hostname(),
            "state": scanner[host].state()
        })

    return hosts
