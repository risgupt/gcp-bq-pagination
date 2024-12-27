# gcp-bq-pagination

**How It Works
    Client Initialization: Creates a BigQuery client instance.
    Pagination Loop:
        Uses client.list_rows() to fetch a page of results.
        Prints the rows by converting each to a dictionary.
        Retrieves the next_page_token to fetch subsequent pages.
        Stops when next_page_token is None.
    Page Size: You can control the number of rows fetched per page using the max_results parameter.
    
**Testing with curl
curl -k --header "Authorization: Bearer $(gcloud auth print-identity-token)" --header "Content-Type: application/json" -X POST "https://<<cloud_run_url>>?page_size=<<pagesize>>&pageToken=<<pageToken>>"
