import socket
import threading
import json
from htmlParser import parse

IP = socket.gethostbyname(socket.gethostname())
PORT = 65432
ADDR = (IP, PORT)
SIZE = 2048
FORMAT = "utf-8"

location = 'C:/CS361/loltoolkit/ddragonData/dragontail-12.6.1/12.6.1/data/en_US/item.json'

# opens data
jsonfile = open(location,'r', encoding = "utf8")
data = jsonfile.read()

# parse json data into data object
object = json.loads(data)



#   -> if found, use below, else return "Error, item not found, please try again"
# loop once and make a new dictionary with # and item name, keys and values respectively and use key to access json information
# build to check if valid item
itemDict = {}
for k,v in object['data'].items():
    for key in v.keys():
        if key == 'name':
            lowerKey = v[key].lower()
            # sanitized key, no "'"
            sanKey = ''
            for char in range(0,len(lowerKey)):
                if lowerKey[char] != "'":
                    sanKey += lowerKey[char]

            itemDict[sanKey] = k 



# building again to keep integrity of casing while returning to screen item info
itemRevDict = {}
for k,v in object['data'].items():
    for key in v.keys():
        if key == 'name':
            itemRevDict[v[key]] = k 

itemDictID = {}
# for loop to find reverse dictionary items for 'builds into' and 'builds from'
for k,v in itemRevDict.items():
   itemDictID[v] = k




# server code:
def dictionary_response(conn, addr):
    print(f"{addr} connected.")

    connected = True
    while connected:
        item = conn.recv(SIZE).decode(FORMAT)
        # prepping user input for
        item = item.lower()

        # not print, but send*
        if item in itemDict.keys():
            # find item number
            id = itemDict[item]

            # to screen aspects of items
            # parsing func for description text
            name = object['data'][id]['name']
            description = parse(object['data'][id]['description'])
            gold = object['data'][id]['gold']['base']
            sell = object['data'][id]['gold']['sell']

            # builds into & from are arrays
            itemComponent = False
            itemBuilt = False
            if 'into' in object['data'][id].keys():
                buildsInto = object['data'][id]['into']
                itemComponent = True

            if 'from' in object['data'][id].keys():
                buildsFrom = object['data'][id]['from']
                itemBuilt = True

            stringReturn = 'Name: '
            stringReturn += name + '\n'
            stringReturn += description + '\n'
            stringReturn += 'Gold: ' + str(gold) + '\n'
            stringReturn += 'Sell: ' + str(sell) + '\n' + '\n'


            if itemComponent == True:
                stringReturn += 'Builds into: ' + '\n'
                for x in buildsInto:
                    stringReturn += itemDictID[x] + '\n'

            if itemBuilt == True:
                stringReturn += 'Builds from: ' + '\n'
                for x in buildsFrom:
                    stringReturn += itemDictID[x] + '\n'


            stringReturn = f'{stringReturn}'
            print(f"Item: {name}")
            msg = stringReturn
            conn.send(msg.encode(FORMAT))

        else:
            print("Item not found")
            stringReturn = f'Error: Item not found'
            msg = stringReturn
            conn.send(msg.encode(FORMAT))

    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"Server is listening on port {PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=dictionary_response, args=(conn, addr))
        thread.start()
if __name__ == "__main__":
    main()