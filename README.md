This is a demo code to show how to transfer folders, sub-folders and files underneath from one azure tenant to another. 
The process involves using Azure Blob Storage services, where files are stored in containers that are analogous to directories.

The process in general involves:

1- Set up Azure Blob Service Clients: We have to set up Azure Blob service clients for both the source and target storage accounts. This involves authenticating to each Azure tenant using credentials like the Azure Storage Account name and key (any other ways?)
2- List and Copy Files: Then we'll use the Azure Blob Storage SDK for Python to list all blobs (files) and directories (if hierarchical namespace is enabled) in the source container, and then copy them to the destination container in the other tenant.
3- Verify and Delete: If needed, we can (after copying), verify that the files have been copied correctly before deleting them from the source container.
