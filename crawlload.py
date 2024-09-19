from langchain.docstore.document import Document
from langchain_community.utilities import ApifyWrapper
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ApifyDatasetLoader
import os

token=os.environ['ASTRA_DB_APPLICATION_TOKEN']
api_endpoint=os.environ['ASTRA_DB_API_ENDPOINT']
openai_api_key=os.environ["OPENAI_API_KEY"]
apify_api_key=os.environ["APIFY_API_TOKEN"]

vstore = AstraDBVectorStore(
    embedding=OpenAIEmbeddings(model="text-embedding-3-large"),
    collection_name="hornsby_docs",
    api_endpoint=api_endpoint,
    token=token,
)
apify = ApifyWrapper()

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 4096,
    chunk_overlap  = 64,
    length_function = len,
    is_separator_regex = False,
)

#loader = apify.call_actor(
#   actor_id="apify/website-content-crawler",
#    run_input={"startUrls": [{"url": "https://www.hornsby.nsw.gov.au/"}]},
#    dataset_mapping_function=lambda item: Document(
#        page_content=item["text"] or "", metadata={"source": item["url"]}
#    ),
#)

loader = ApifyDatasetLoader(
    dataset_id="fhVpQ0UQU8C91dkXV",
    dataset_mapping_function=lambda dataset_item: Document(
        page_content=dataset_item["text"], metadata={"source": dataset_item["url"]}
    ),
)

docs = loader.load()

texts = text_splitter.split_documents(docs)

#texts = text_splitter.create_documents([docs])
print(texts[0])
print(texts[1])

inserted_ids = vstore.add_documents(texts)
print(f"\nInserted {len(inserted_ids)} documents.")
