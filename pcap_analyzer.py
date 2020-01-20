import os
import subprocess


def visited_sites(pcap_file):
    var = os.popen(
        'tshark -T fields -e http.host -r '+pcap_file+' | sort | uniq -c | sort -nr | head').read()
    outputlist = var.split('\n')
    for i in outputlist:
        print(i)


def useragents(pcap_file):
    var = os.popen(
        'tshark -Y \'http contains "User-Agent:"\' -T fields -e http.user_agent -r '+pcap_file+' | sort | uniq -c | sort -nr | less').read()
    outputlist = var.split('\n')
    for i in outputlist:
        print(i)


def conn_details(pcap_file):
    var = os.popen(
        'tshark -r ' + pcap_file).read()
    outputlist = var.split('\n')
    for i in outputlist:
        print(i)


def grepmode(pcap_file):
    string = input("Enter the string to search : ")
    cmd = 'grep '+string+' -a '+pcap_file
    cmd = bytes(cmd, 'utf-8')
    pro = subprocess.Popen('bash',
                           stderr=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stdin=subprocess.PIPE)
    out, err = pro.communicate(cmd)
    out = out.decode("utf-8", errors="replace")
    print(out)


def ips(pcap_file):
    var = os.popen(
        'tshark -r '+pcap_file+' -T fields -e ip.dst ip.src | sort | uniq').read()
    outputlist = var.split('\n')
    for i in outputlist:
        print(i)


def ports(pcap_file):
    var = os.popen(
        'tshark -r '+pcap_file+' -Y "tcp" -T fields -e tcp.srcport -e tcp.dstport').read()
    outputlist = var.split('\n')
    for i in outputlist:
        print(i)

def main():
    pcap_file = input("enter location of pcap file : ")
    option_list = ['', 'visited_sites(pcap_file)', 'useragents(pcap_file)', 'conn_details(pcap_file)', 'grepmode(pcap_file)', 'ips(pcap_file)', 'ports(pcap_file)', 'quit()']
    while True:

        option = input("""
1) Visited sites
2) User-Agents
3) Connection details
4) String grep mode
5) list all IPs
6) list source and destination ports 
7) quit       
""")
        option = int(option)
        eval(option_list[option])



main()

