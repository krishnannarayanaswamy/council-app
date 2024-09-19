# DataStax Astra Chat with LangChain

This repo is an implementation of a locally hosted chatbot specifically focused on question answering 
Built with [LangChain](https://github.com/langchain-ai/langchain/), [FastAPI](https://fastapi.tiangolo.com/), and [Next.js](https://nextjs.org) and [DataStax Astra as Vector Store](https://astra.datastax.com).

The app leverages LangChain's streaming support and async API to update the page in real time for multiple users.

The app leverages DataStax [RAGStack](https://github.com/datastax/ragstack-ai) to ensure you always have a stable production ready version to deploy. The RagStack makes sure that all the libraries that are needed are tested for compatability and you can find the test results [here](https://ragstack-ai.testspace.com/)

## ✅ Running locally
1. Install python 3.10 
2. Install node.js 
2. Change directory `cd ai-assistant`
3. Install backend dependencies: `pip install -r requirements.txt`.
4. Make sure to enter your environment variables to configure the application:
```
export ASTRA_DB_API_ENDPOINT=""
export OPENAI_API_KEY=""
export ASTRA_DB_KEYSPACE="default_keyspace"
export ASTRA_DB_APPLICATION_TOKEN=""

# for tracing
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
export LANGCHAIN_API_KEY=
export LANGCHAIN_PROJECT=

# for other models
export ANTHROPIC_API_KEY=""
export GOOGLE_API_KEY= ""
export FIREWORKS_API_KEY=""
export COHERE_API_KEY=""

```
1. Run the Colab notebook to load data into DataStax Astra.
2. Navigate to the folder `cd backend`
3. Navigate to `constants.py` and change `ASTRA_COLLECTION_NAME =` value to your collection
4. Start the Python backend with `python main.py`.
5. Open another terminal window
6. Install frontend dependencies by running `cd ./frontend`, then `npm install`.
7. Run the frontend build with `npm run build` for frontend.
8. Run the frontend code with `npm run dev` 
9. Open [localhost:3000](http://localhost:3000) in your browser.

## 📚 Technical description

There are two components: ingestion and question-answering.

Ingestion has the following steps:

1. Pull html from documentation site as well as the Github Codebase
2. Load html with LangChain's [RecursiveURLLoader](https://python.langchain.com/docs/integrations/document_loaders/recursive_url_loader) and [SitemapLoader](https://python.langchain.com/docs/integrations/document_loaders/sitemap)
3. Split documents with LangChain's [RecursiveCharacterTextSplitter](https://api.python.langchain.com/en/latest/text_splitter/langchain.text_splitter.RecursiveCharacterTextSplitter.html)
4. Create a vectorstore of embeddings, using LangChain's [Astra vectorstore wrapper] (with OpenAI's embeddings).

Question-Answering has the following steps:

1. Given the chat history and new user input, determine what a standalone question would be using GPT-3.5.
2. Given that standalone question, look up relevant documents from the vectorstore.
3. Pass the standalone question and relevant documents to the model to generate and stream the final answer.
4. Generate a trace URL for the current chat session, as well as the endpoint to collect feedback.

## Documentation

Looking to use or modify this Use Case Accelerant for your own needs? We've added a few docs to aid with this:

- **[Concepts](./CONCEPTS.md)**: A conceptual overview of the different components of Chat LangChain. Goes over features like ingestion, vector stores, query analysis, etc.
- **[LangSmith](./LANGSMITH.md)**: A guide on adding robustness to your application using LangSmith. Covers observability, evaluations, and feedback.
- **[Production](./PRODUCTION.md)**: Documentation on preparing your application for production usage. Explains different security considerations, and more.
- **[Deployment](./DEPLOYMENT.md)**: How to deploy your application to production. Covers setting up production databases, deploying the frontend, and more.


## Deploy backend in Cloud Run in GCP 



gcloud components update

gcloud auth login

gcloud config set run/region asia-southeast1

gcloud auth configure-docker

poetry export -f requirements.txt --output requirements.txt --without-hashes

gcloud run deploy astra-langchain-ai-assistant --port 8080 --source .

Assuming you will deploy the frontent in Vercel, get the URL from the backend deployment in Cloud Run and export as ENV variable with vercel during the frontend deployment

## Deploy backend and frontend in AWS EC2 Ubuntu instance

python --version
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
sudo apt-get install python3-venv
python3 --version
python3 -m venv astra-langchain-aichat-api
source astra-langchain-aichat-api/bin/activate

git clone https://github.com/krishnannarayanaswamy/astra-langchain-chatbot.git
cd astra-langchain-chatbot/

cd ai-assistant/

pip install -r requirements.txt
export ASTRA_DB_API_ENDPOINT=""
export OPENAI_API_KEY=""
export ASTRA_DB_KEYSPACE="default_keyspace"
export ASTRA_DB_APPLICATION_TOKEN=""
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
export LANGCHAIN_API_KEY=""
export LANGCHAIN_PROJECT="default"
export ANTHROPIC_API_KEY=""
export GOOGLE_API_KEY=""
export FIREWORKS_API_KEY=""
export COHERE_API_KEY=""
cd backend/
nohup python main.py &
tail -f nohup.out

cd frontend/
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

nvm install --lts
npm --version
cd astra-langchain-chatbot/ai-assistant/frontend/
npm install
npm install -g pm2
npm run build
export NEXT_PUBLIC_API_BASE_URL="http://13.229.107.21:8080"
pm2 start npm --name "astra-langchain-mili-assistant" -- start
pm2 status
pm2 monitor
pm2 logs astra-langchain-mbbank-assistant