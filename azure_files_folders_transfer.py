from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def transfer_blobs(source_conn_str, source_container_name, target_conn_str, target_container_name):
    # Create a BlobServiceClient object for the source and target
    source_blob_service_client = BlobServiceClient.from_connection_string(source_conn_str)
    target_blob_service_client = BlobServiceClient.from_connection_string(target_conn_str)
    
    # Access the source container and list all blobs
    source_container_client = source_blob_service_client.get_container_client(source_container_name)
    blobs_list = source_container_client.list_blobs()

    for blob in blobs_list:
        # Create a BlobClient for the source blob
        source_blob = source_container_client.get_blob_client(blob)
        
        # Create a BlobClient for the target blob
        target_blob = target_blob_service_client.get_blob_client(target_container_name, blob.name)

        # Copy source blob to target blob
        target_blob.start_copy_from_url(source_blob.url)

        # Optional: You can delete the source blob after copying
        # source_blob.delete_blob()

if __name__ == "__main__":
    source_connection_string = 'DefaultEndpointsProtocol=https;AccountName=SOURCE_ACCOUNT_NAME;AccountKey=SOURCE_ACCOUNT_KEY;EndpointSuffix=core.windows.net'
    target_connection_string = 'DefaultEndpointsProtocol=https;AccountName=TARGET_ACCOUNT_NAME;AccountKey=TARGET_ACCOUNT_KEY;EndpointSuffix=core.windows.net'
    source_container = 'source-container-name'
    target_container = 'target-container-name'
    
    transfer_blobs(source_connection_string, source_container, target_connection_string, target_container)
