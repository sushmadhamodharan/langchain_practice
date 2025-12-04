import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    info = """Key Skills to Focus On
1. Data Strategy & Business Understanding
○
Ability to design a structured data strategy framework for business use cases.
○
Skilled in identifying, prioritizing, and validating data sources.
○
Strong at aligning technical solutions with business needs.
2. End-to-End Data Pipeline & Architecture
○
Experience designing scalable ingestion, staging, and preprocessing workflows.
○
Knowledge of trade-offs in architecture and ability to make strategic decisions.
○
Comfort with both structured and unstructured data handling.
3. Knowledge Base & RAG Systems
○
Solid understanding of chunking strategies and their impact on retrieval.
○
Hands-on experience with embeddings, similarity search, and vector databases.
○
Ability to benchmark and optimize RAG implementations in production.
4. Database Systems & Storage Decisions
○
Strong understanding of relational vs NoSQL vs vector databases.
○
Ability to recommend the right database for different workloads.
○
Knowledge of scalability, performance, and cost considerations.
5. Programming & Implementation
○
Proficiency in Python (already a strength in Dinesh but still critical).
○
Hands-on coding for preprocessing, data pipelines, and integration with
databases.
○
Production-grade coding practices (logging, exception handling, optimization).
6. Communication & Collaboration
○
Ability to explain technical concepts in simple, business-friendly language.
○
Clear communication for cross-functional collaboration.
○
Skills in stakeholder alignment and requirement gathering.
Ideal Candidate Profile to Target
●
Background:
○
Data Engineer, AI/ML Engineer, or Knowledge Engineer with 3–7 years of
experience in designing and implementing data-driven systems.
○
Someone who has worked on end-to-end data pipelines, not just coding pieces
of it.
●
Domain Knowledge:
○
Hands-on exposure to RAG (Retrieval-Augmented Generation) or knowledge
base projects.
○
Strong grasp of data strategy and architecture decisions, not just
implementation.
○
Experience with vector databases (Pinecone, FAISS, Weaviate, Milvus) along
with relational and NoSQL databases.
●
Technical Strengths:
○
Advanced Python skills for data processing and integration.
○
Practical knowledge of embeddings, similarity search, and chunking
strategies.
○
Ability to benchmark and optimize knowledge systems in production.
●
Soft Skills:
○
Strong communication skills to explain data concepts to business stakeholders.
○
Proven ability to bridge the gap between business and technical teams.
○
Structured problem-solving and decision-making abilities.
👉 In short: You need a candidate who is not just a coder but also a strategic thinker with
end-to-end data architecture and knowledge base (RAG) experience, along with th"""

    prompt = """these are some interview notes {info} sent by hiring manager for ai engineer role.
Help me to 
1.summarize the key skills required for this role in bullet points.
2.How i can focus my learning given i have 2 days until interview
"""

    summary_prompt_template = PromptTemplate(input_variables=["info"], template=prompt)
    llm = ChatOpenAI(temperature=0, model_name="gpt-5")
    #llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"info": info})
    print(response.content)


if __name__ == "__main__":
    main()
