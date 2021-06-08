from google.cloud import storage

bucket_name = 'bucket_name'
source_file_name = 'example.pdf'
destination_blob_name = source_file_name


class upload_example():
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(source_file_name)
    blob.upload_from_filename(destination_blob_name)


print(
    "File {} uploaded to {}.".format(
        source_file_name, destination_blob_name
    )
)
