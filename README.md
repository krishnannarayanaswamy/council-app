You are here because you are curious about simplifying your Gen AI journey. DataStax has the answer. DataStax is a real-time data company for building production Gen AI applications. Our vector search capability is the key to harnessing the potential of generative AI and Retrieval-Augmented Generation (RAG) for your Gen AI applications. Think of it as a mix of Astra DB, our fully managed data service with vector search capabilities, seamlessly integrated into the LangChain and Cassio app developer framework. This unique cocktail is loved by developers because it provides the means to rapidly master Gen AI and RAG, enabling the creation of powerful, contextually rich systems.

You don’t need to be a Deep Learning Machine Learning Expert / Data Scientist to understand how to use LLM’s like OpenAI and Vector Database like AstraDB to make intelligent Experts, Assistants, and Platforms

This Dev Jam will help your enterprise architects, developers and practitioners to quickly become familiar with RAGStack, LLMs and Vector Database. These sessions with a DataStax technical coach, self-paced and hands-on learning assignments. Bring in a Gen AI use case, your data and build a Gen AI agent using DataStax Astra platform.

# RAGBot Astra

Welcome to DataStax Gen AI Dev Jam. This Dev Jam will help you quickly become familiar with DataStax RAGStack, LLMs and Astra Vector Database. These hands-on jam normally runs with a DataStax technical coach, self-paced and hands-on learning assignments. Bring in a Gen AI use case, your data and build a Gen AI chatbot using DataStax Astra platform.
This project is a starter for creating your production ready chatbot using Astra DB, Vercel, Next.js and OpenAI. It's designed to be easy to deploy and use, with a focus on performance and usability. Let's Go!

## What you'll learn:

- 🚀 How to use Astra DB Vector Store for Semantic Similarity search
- 🤖 How to use OpenAI's Large Language Models for Q&A style chatbots
- Vercel:  How to use Vercel to deploy the ChatBot

## Features

- **Astra DB Integration**: Store and retrieve data from your Astra DB database with ease.
- **OpenAI Integration**: Leverage the power of OpenAI to generate intelligent responses.
- **Easy Deployment**: Deploy your chatbot to Vercel with just a few clicks.
- **Customizable**: Modify and extend the chatbot to suit your needs.

## Getting Started

### Prerequisites

This workshop assumes you have access to:
1. [A Github account](https://github.com)
2. [Google Colab](https://colab.research.google.com/)

Follow the below steps and provide the **Astra DB API Endpoint**, **Astra DB ApplicationToken** and **OpenAI API Key** when required.

### Sign up for Astra DB

Make sure you have a vector-capable Astra database (get one for free at [astra.datastax.com](https://astra.datastax.com/register))


- Create a Astra Vector database as below


![codespace](./ai-assistant/assets/images/createdb2.png)


- Wait for the DB to initialized and be ready


![codespace](./ai-assistant/assets/images/dbinitial.png)


- Explore connectivity options using Java, Python and Typescript


![codespace](./ai-assistant/assets/images/dbconnections.png)



- Key information you will need shortly, explore them.
- You will be asked to provide the **API Endpoint** which can be found in the right pane underneath *Database details*.
- Ensure you have an **Application Token** for your database which can be created in the right pane underneath *Database details*.

![codespace](./ai-assistant/assets/images/dbdetails.png)


- You will need DB ID.


![codespace](./ai-assistant/assets/images/dbdbid.png)


### Sign up for OpenAI

- Create an [OpenAI account](https://platform.openai.com/signup) or [sign in](https://platform.openai.com/login).
- Navigate to the [API key page](https://platform.openai.com/account/api-keys) and create a new **Secret Key**, optionally naming the key.

# Google Colab Data Load with LangChain

We will use a Google Colab to do a simple RAG chatbot first to become familiar with the toolsets. We will create embeddings of the data from files (PDF, txt) and store them in Astra DB collections to enable Vector search.

Open this [Colab notebook](https://colab.research.google.com/drive/1PXfEVMobBVPAs_5vqAw-USZK1b1opHSF) in a browser

Make a copy of this in your own Google Drive (Otherwise you will be editing my copy of the notebook)

Run each cell individually in sequence and observe the outputs

Feel free to change the Astra collection name and also change Bring your own Data (BYOD)

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
## For Windows Users (For macos and linus users, please skip)

Assumption: you have/use powershell

Install Python using this [guide](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

Install nodejs using this [guide](https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows)

Install Git and VSCode, if required

For exporting environment variables, you will need to add the environment variables in the system settings as documented [here](https://www.computerhope.com/issues/ch000549.htm). 

Alternatively, if you have admin privileges, you can do so using powershell using commands [here](https://lazyadmin.nl/powershell/set-environment-variable/)

## Ready for launch

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

There are two components: 
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
