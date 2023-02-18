import boto3
import os
import requests
import zipfile
from xml.etree import ElementTree

def download_file(url, key):
    response = requests.get(url)
    if response.status_code == 200:
        content_type = response.headers['Content-Type']
        if 'image' not in content_type:
            # Skip any non-image files
            return None
        last_modified = response.headers['Last-Modified']
        content_length = response.headers['Content-Length']
        data = response.content
        return (data, last_modified, content_length)
    else:
        return None

def main():
    bucket_name = input("Enter the name of the S3 bucket: ")
    prefix = input("Enter the prefix of the objects to download: ")
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    objects = bucket.objects.filter(Prefix=prefix)
    file_list = []
    for obj in objects:
        key = obj.key
        if key.endswith('.rbxl') or key.endswith('.rbxm') or key.endswith('.rbxlx'):
            size = obj.size
            file_list.append((key, size))
    file_list = sorted(file_list, key=lambda x: x[1], reverse=True)
    zip_filename = f"{prefix}.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zip_file:
        for key, size in file_list:
            url = f"https://{bucket_name}.s3.amazonaws.com/{key}"
            file_data = download_file(url, key)
            if file_data:
                data, last_modified, content_length = file_data
                zip_file.writestr(key, data)
                print(f"{key} ({content_length} bytes, last modified {last_modified}) downloaded and added to the zip file.")
    zip_file_size = os.path.getsize(zip_filename)
    print(f"\n{len(file_list)} objects downloaded and added to {zip_filename} ({zip_file_size} bytes).")
    print(f"Zip file located at: {os.path.abspath(zip_filename)}")

if __name__ == '__main__':
    main()
