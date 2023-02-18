# S3-Roblox-File-Downloader
The code is a Python script that downloads files from an Amazon S3 bucket. Here's how it works:

First, the script prompts the user to enter the name of the S3 bucket they want to download files from, and the prefix of the objects they want to download.

Next, the script creates a connection to the S3 bucket using the boto3 library, which is a Python library that makes it easy to work with Amazon Web Services (AWS).

The script then retrieves a list of objects in the S3 bucket that match the specified prefix. It filters the objects based on whether they end with the file extensions .rbxl, .rbxm, or .rbxlx.

The objects are then sorted by size in descending order. This ensures that the largest files are downloaded first.

The script then creates a new zip file with the specified prefix as the name. It will add the downloaded files to this zip file.

The script then loops through each object in the filtered and sorted list of objects, and attempts to download it. If the object is not an image, it is skipped.

If the object is an image, the script downloads the object's data, last modified date, and content length using the requests library, which is a Python library for making HTTP requests.

The script then adds the downloaded file to the zip file with the same name as the object's key. It also prints out a message saying that the file was downloaded and added to the zip file, along with the file's size and last modified date.

After all of the objects have been downloaded and added to the zip file, the script prints out a message saying how many files were downloaded and added to the zip file, along with the name of the zip file, its size, and its location on the computer.
