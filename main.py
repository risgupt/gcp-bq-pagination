import json
from google.cloud import bigquery

def fetch_data(request):
    """
    HTTP Cloud Function to fetch data from a BigQuery table with pagination.
    """
    # Initialize BigQuery client
    client = bigquery.Client()

    # Define your dataset and table
    dataset_id = "<<dataset_id>>"
    table_id = "<<table_id>>"
    target_project_id = "<<project_id>>"

    # Parse query parameters
    page_size = int(request.args.get("page_size", 10))  # Default 10 rows
    pageToken = request.args.get("pageToken", None)
    
    # Construct the table reference
    table_ref = client.dataset(dataset_id, project=target_project_id).table(table_id)

    # Fetch rows from the table with pagination
    rows = client.list_rows(
        table_ref,
        max_results=page_size,
        page_token=pageToken,
    )

    # Serialize rows and pagination info
    rows_data = [dict(row) for row in rows]
    next_page_token = rows.next_page_token

    response = {
        "rows": rows_data,
        "pageToken": next_page_token,
    }

    return json.dumps(response), 200, {"Content-Type": "application/json"}
