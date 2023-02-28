from virus_total_apis import PublicApi as virus_total_api

API_KEY = ""
virustotal = virus_total_api(API_KEY)


# response = virustotal.get_file_report(line)