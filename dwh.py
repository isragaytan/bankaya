from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(r'C:\Users\esteb\OneDrive\Documentos\isra\code\bankaya\bankaya-b3f515dfcb33.json')

project_id = "bankaya"

client = bigquery.Client(credentials=credentials,project=project_id)

query_job = client.query("""SELECT * FROM bankaya.data_migrated.test_mysql LIMIT 1000;""")

results = query_job.result()
for j in results:
    print(j)