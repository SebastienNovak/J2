from crawler.crawler import download_excel
from processor.processor import process_excel
from airtable.airtable import upload_to_airtable
from aws.s3 import upload_file_to_s3

def main():
    download_path = "/path/to/download"
    excel_file = download_excel(download_path)

    processed_data = process_excel(excel_file)

    airtable_api_key = "your_airtable_api_key"
    airtable_base_id = "your_airtable_base_id"
    airtable_table_name = "your_airtable_table_name"
    upload_to_airtable(airtable_api_key, airtable_base_id, airtable_table_name, processed_data)

    s3_bucket = "your_s3_bucket_name"
    upload_file_to_s3(excel_file, s3_bucket)

if __name__ == "__main__":
    main()
