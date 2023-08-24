from datetime import datetime
import uuid

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

from utils import env

index_name = "text-memory"
# Get the service endpoint and API key from the environment
endpoint = env["SEARCH_ENDPOINT"]
key = env["SEARCH_API_KEY"]


class AzureCognitiveSearch:
    def __init__(self):
        self.endpoint = endpoint
        self.key = key
        self.index_name = index_name

        # Create a client
        self.credential = AzureKeyCredential(key)
        self.client = SearchClient(
            endpoint=endpoint, index_name=index_name, credential=self.credential
        )

    def upload_doc(self, DOCUMENT):
        assert DOCUMENT is not None
        assert DOCUMENT["role"] is not None
        assert DOCUMENT["content"] is not None

        DOCUMENT["id"] = str(uuid.uuid4())
        DOCUMENT["created"] = int(round(datetime.now().timestamp()))

        result = self.client.upload_documents(documents=[DOCUMENT])
        return result

    def search(self, query):
        assert query is not None

        results = self.client.search(search_text=query, include_total_count=True)
        return results
