from virus_total_apis import PublicApi as virus_total_api

API_KEY = "c7f5c8cc25558c1aeda19926ea88d4c061dac219098c2d125af88cad4b5df897"
virustotal = virus_total_api(API_KEY)

file = open("hashes.txt", "r")

for line in file.readlines():

    print(line)
    response = virustotal.get_file_report(line)
    print(response)
    print("\n\n")