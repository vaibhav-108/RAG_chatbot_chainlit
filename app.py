import os
from typing import List
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI
from langchain_community.docstore.document import Document
from langchain.memory import ConversationBufferMemory,ChatMessageHistory

import chainlit as cl

from dotenv import load_dotenv



load_dotenv()


