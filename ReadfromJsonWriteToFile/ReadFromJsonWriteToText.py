import json


with open('input.json') as json_data:
    data = json.load(json_data)
    for r in data['Employee']:
        if r.has_key('manager'):
            fo = open(r['id']+"_"+r['name']+".txt","wb")
            fo.write(r['name'] + "       " + r['manager'] + "       " + r['City'])
            fo.close()
