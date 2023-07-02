import json

chemin = "D:\Assos\AltruismeEfficace\HRAI\data_brut.json"
chemin_export = "D:\Assos\AltruismeEfficace\HRAI\data_processed.json"

income_distrib = []

with open(chemin) as f:

    pre = f.read()
    data = json.loads(pre)
    data = data[0:100]
    # print(data)
    for i in range(len(data)):
        income_distrib.append({"percentile" : i+1, "threshold":data[i]['World Threshold (â‚¬)']})
# print(income_distrib)


with open(chemin_export, 'w') as j:

    json_object = json.dumps(income_distrib, indent = 4) 
    j.write(json_object)