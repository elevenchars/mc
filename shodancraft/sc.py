import json
import shodan
import pyperclip
from mcstatus import MinecraftServer


with open("config.json") as config_file:
    config = json.load(config_file)
# 1.14.4 = 498
# 1.14.3 = 490
# 1.13.2 = 404
protocol = "498"
extra = " country:US"

sho = shodan.Shodan(config["key"])

print("Will's Minecraft server finder")
print("Enter for next server, 'e' to exit")
print()
option = ""

search_string = "port:25565 protocol {} NOT '0 online'{}".format(protocol, extra)

print("Using search string:\n{}\n".format(search_string))
print('searching...')
for banner in sho.search_cursor(search_string):
    try:
        server = MinecraftServer.lookup(banner["ip_str"]).status()
        if server.players.online == 0:
            continue
        print("="*24)
        print(banner["ip_str"])
        pyperclip.copy(banner['ip_str'])
        locdata = [banner["location"]["city"], banner["location"]["region_code"], banner["location"]["country_name"]]
        locdata = [d for d in locdata if d]
        print(", ".join(locdata))
        print("{} ({})".format(server.description["text"], server.version.name))
        print("{}/{} Online ({} ms)".format(server.players.online, server.players.max, server.latency))
        if server.players.sample:
            print("Players sample: ")
            print(", ".join([p.name for p in server.players.sample]))
        print("="*24)
        option = input()
        while option != '':
            if option == 'e':
                exit()
            if option == 'p':
                host_info = sho.host(banner["ip_str"])
                ports = host_info['ports']
                ports.sort()
                print("Open ports:")
                print(", ".join([str(port) for port in ports]))
            option = input()
        print('searching...')
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        continue
