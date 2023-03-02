from virus_total_apis import PublicApi as virus_total_api

API_KEY = ""
virustotal = virus_total_api(API_KEY)

read_file = open("hashes.txt", "r")

# write_file = open("data_file.json", "w")

for line in read_file.readlines():
  response = virustotal.get_file_report(line)
  print(response)
  # json.dump(response, write_file)
  # write_file.write("\n\n")
  # write_file.write(response + "\n\n")
