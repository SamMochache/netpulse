# backend/monitor/utils.py
import nmap
import logging

logger = logging.getLogger(__name__)

def advanced_scan(subnet="192.168.1.0/24"):
    """
    Perform network scan using nmap
    """
    try:
        logger.info(f"Starting nmap scan for subnet: {subnet}")
        scanner = nmap.PortScanner()
        
        # Perform ping scan (-sn) to discover hosts
        scanner.scan(hosts=subnet, arguments='-sn')
        hosts = []

        for host in scanner.all_hosts():
            host_info = {
                "ip": host,
                "hostname": scanner[host].hostname() or "Unknown",
                "state": scanner[host].state()
            }
            hosts.append(host_info)
            logger.debug(f"Found host: {host_info}")

        logger.info(f"Scan completed. Found {len(hosts)} hosts")
        return hosts
        
    except Exception as e:
        logger.error(f"Scan failed for subnet {subnet}: {str(e)}")
        return []

# ============================================