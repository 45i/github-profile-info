from urllib.request import urlopen
import requests
import os
import json

print('Enter GitHub username:')
name = input()

url = f'https://api.github.com/users/{name}'

response = urlopen(url)

string = response.read().decode('utf-8')
json_obj = json.loads(string)


path = os.getcwd()

avatar = json_obj["avatar_url"]

r = requests.get(avatar)

class getData():
    print('\nUsername:', json_obj["login"])
    print('Name:', json_obj["name"])
    print('ID:', json_obj["id"])
    print('Node ID:', json_obj["node_id"])
    print('Public repositories:', json_obj["public_repos"])
    print('Public gists:', json_obj["public_gists"])
    print('Followers:', json_obj["followers"])
    print('Following:', json_obj["following"])
    print('BIO:', json_obj["bio"])
    print('Account created:', json_obj["created_at"])
    print('Account type:', json_obj["type"])
    
    if json_obj["email"] == None:
        print('No email attached.')
    else:
        print('Email attached:', json_obj["email"])

    if json_obj["twitter_username"] == None:
        print('No Twitter attached.')
    else:
        print('Twitter:', json_obj["twitter_username"])

    if json_obj["location"] == None:
        print('No public location.')
    else:
        print('Location:', json_obj["location"])

    if json_obj["site_admin"] == False:
        print('Site admin: False')
    else:
        print('Site admin: True')

    if json_obj["hireable"] == None:
        print('Nonhireable')
    else:
        print('Hireable')

class createFile():
    stringn = json_obj["login"]
    os.mkdir(path + '\\' + json_obj["login"])

    file = os.path.join(path + '\\' + json_obj["login"], stringn.lower() + ".png")
    filedata = open(file, "wb")
    filedata.write(r.content)
    filedata.close()
    print('\nProfile image saved in', path + '\\' + stringn.lower())
    done = input()
