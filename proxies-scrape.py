import re
import requests
import threading


print('''
                        ━━━┳╮╱╱╭┳━╮╱╭┳━╮╭━╮
                        ┃╭━╮┃╰╮╭╯┃┃╰╮┃┣╮╰╯╭╯
                        ┃┃╱╰┻╮╰╯╭┫╭╮╰╯┃╰╮╭╯
                        ┃┃╱╭╮╰╮╭╯┃┃╰╮┃┃╭╯╰╮
                        ┃╰━╯┃╱┃┃╱┃┃╱┃┃┣╯╭╮╰╮
                        ╰━━━╯╱╰╯╱╰╯╱╰━┻━╯╰━╯ - Proxy Scrape Code By Cynx
            
''')


urls = '''
https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=ipport&format=text&protocol=socks4%2Csocks5%2Chttp&anonymity=elite%2Canonymous&country=af%2Cal%2Cdz%2Cad%2Cao%2Car%2Cam%2Cau%2Cat%2Caz%2Cbd%2Cby%2Cbe%2Cbj%2Cbm%2Cbt%2Cbo%2Cbw%2Cbg%2Cbf%2Cbi%2Ckh%2Ccm%2Cca%2Ctd%2Ccl%2Ccn%2Cco%2Ccg%2Ccr%2Chr%2Ccy%2Ccz%2Cdk%2Cdo%2Cec%2Ceg%2Csv%2Cgq%2Cee%2Csz%2Cet%2Cfj%2Cfi%2Cfr%2Cgm%2Cge%2Cde%2Cgh%2Cgi%2Cgr%2Cgu%2Cgt%2Cgn%2Cht%2Chn%2Chk%2Chu%2Cin%2Cid%2Cir%2Ciq%2Cie%2Cil%2Cit%2Cjm%2Cjp%2Cjo%2Ckz%2Cke%2Ckr%2Ckg%2Clv%2Clb%2Cls%2Clt%2Cmg%2Cmw%2Cmy%2Cmv%2Cml%2Cmt%2Cmu%2Cmx%2Cmd%2Cmn%2Cme%2Cma%2Cmz%2Cmm%2Cna%2Cnp%2Cnl%2Cnz%2Cni%2Cng%2Cmk%2Cno%2Cpk%2Cps%2Cpa%2Cpy%2Cpe%2Cph%2Cpl%2Cpt%2Cpr%2Cqa%2Cro%2Crw%2Ckn%2Csa%2Csn%2Crs%2Csc%2Csl%2Csg%2Csk%2Csi%2Cso%2Cza%2Ces%2Clk%2Csd%2Cse%2Cch%2Csy%2Ctw%2Ctj%2Ctz%2Cth%2Ctl%2Ctg%2Ctn%2Ctr%2Cug%2Cua%2Cae%2Cgb%2Cus%2Cuy%2Cuz%2Cve%2Cvn%2Cvi%2Cye%2Czw
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt
https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt
https://www.proxy-list.download/api/v1/get?type=socks4
https://www.proxyscan.io/api/proxy?uptime=50&ping=1000&limit=100&type=socks4&format=txt
https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt
https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=2000&country=all
https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt
https://raw.githubusercontent.com/RX4096/proxy-list/main/online/socks4.txt
https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt
https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt
https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt
'''


file = open('proxies.txt', 'w')
file = open('proxies.txt', 'a')
good_proxies = list()


def pattern_one(url):
    ip_port = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}:\d{2,5})', url)
    if not ip_port: pattern_two(url)
    else:
        for i in ip_port:
            file.write(str(i) + '\n')
            good_proxies.append(i)


def pattern_two(url):
    ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)
    port = re.findall('td>(\d{2,5})<', url)
    if not ip or not port: pattern_three(url)
    else:
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def pattern_three(url):
    ip = re.findall('>\n[\s]+(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)
    port = re.findall('>\n[\s]+(\d{2,5})\n', url)
    if not ip or not port: pattern_four(url)
    else:
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def pattern_four(url):
    ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)
    port = re.findall('>(\d{2,5})<', url)
    if not ip or not port: pattern_five(url)
    else:
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def pattern_five(url):
    ip = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)
    port = re.findall('(\d{2,5})', url)
    for i in range(len(ip)):
        file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
        good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def start(url):
    try:
        req = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}).text
        pattern_one(req)
        print(f' [+] Scrapping from: {url}')
    except requests.exceptions.SSLError: print(str(url) + ' [x] SSL Error')
    except: print(str(url) + ' [x] Random Error')


threads = list()
for url in urls.splitlines():
    if url:
        x = threading.Thread(target=start, args=(url, ))
        x.start()
        threads.append(x)


for th in threads:
    th.join()

print(f' \n\n[/] Total scraped proxies: ({len(good_proxies)})')
