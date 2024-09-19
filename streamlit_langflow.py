import logging
import sys
import time
from typing import Optional
import requests
import streamlit as st
import json

log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=log_format, stream=sys.stdout, level=logging.INFO)


BASxE_API_URL = "http://127.0.0.1:7860/api/v1/run"
FLOW_ID = "f5867180-2757-4ade-83ef-6c174fb2ca96"
TWEAKS = {
  "OpenAIEmbeddings-7xXoS": {},
  "ChatInput-77awA": {},
  "ChatOutput-42RjS": {},
  "ChatOpenAISpecs-D9jed": {},
  "Prompt-2fhtj": {},
  "AstraDBSearch-Or4m5": {},
  "RecordsToText-AHz8u": {},
  "ConversationChain-cgfCI": {}
}


def main():
    st.set_page_config(page_title="DataStax AI Assistant")

    st.markdown("##### Welcome to DataStax AI Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=message["avatar"]):
            st.write(message["content"])

    if prompt := st.chat_input("I'm your assistant, how may I help you?"):
        # Add user message to chat history
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )
        # Display user message in chat message container
        with st.chat_message(
            "user",
        ):
            st.write(prompt)

        # Display assistant response in chat message container
        with st.chat_message(
            "assistant",
            ):
            message_placeholder = st.empty()
            with st.spinner(text="Thinking..."):
                assistant_response = generate_response(prompt)
                message_placeholder.write(assistant_response)
        # Add assistant response to chat history
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": assistant_response,
            }
        )


def run_flow(message: str,
  flow_id: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  api_key: Optional[str] = None) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param flow_id: The ID of the flow to run
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/{flow_id}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if api_key:
        headers = {"x-api-key": api_key}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()


def generate_response(prompt):
    logging.info(f"question: {prompt}")
    #inputs = {"question": prompt}

    response = run_flow(prompt, flow_id=FLOW_ID, tweaks=TWEAKS)
    try:
        return response['outputs'][0]['outputs'][0]['results']['result']
    except Exception as exc:
        logging.error(f"error: {response}")
        return "Sorry, there was a problem finding an answer for you."


if __name__ == "__main__":
    main()   