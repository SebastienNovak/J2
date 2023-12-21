from airtable import Airtable

def upload_to_airtable(api_key, base_id, table_name, data):
    airtable = Airtable(base_id, table_name, api_key)

    for record in data.to_dict('records'):
        airtable.insert(record)
