import json

json_file = 'ListaDeVulnsSonar_full.csv'
with open(json_file) as f:
    file_data = f.read()

file_data = file_data.replace(';', '')


with open(json_file, 'w') as f:
    f.write(file_data)

#json_data = json.loads(file_data)

#"message":"Consider using 'throw;' to preserve the stack trace." 