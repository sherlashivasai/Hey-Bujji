from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai.knowledge.source.crew_docling_source import CrewDoclingSource
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

# Create a knowledge source from web
content_source = CrewDoclingSource(
    file_paths=[
        "https://www.linkedin.com/in/shivasaisherla",
        "https://github.com/sherlashivasai",
    ], 
)

# Add specific knowledge source
pdf_source = PDFKnowledgeSource(
    file_paths=[
        "Agent_data/Sherla_Shiva_Sai_Resume_Nvidia_LLM_intern.pdf",
        "Agent_data/Sherla_Shiva_Sai_Resume_Research_Fellow.pdf",
        "Agent_data/Uber_AIML_security.pdf"
    ]
)

@CrewBase
class Bujji():
    """Bujji crew"""

    @agent
    def researcher(self) -> Agent:
        return Agent(
            role="Portfolio Description Agent",
            goal="Describe the portfolio owner in a personalized and engaging way",
            backstory="""Your name is Bujji.
            You are an AI assistant designed to provide concise, professional descriptions of the portfolio owner.
            You use the information provided to generate a tailored response.
            Known for your ability to find the most relevant information and present it in a clear and concise manner.""",
            verbose=True,
            llm=LLM(
                model='ollama/mistral:7b',
                temperature=0.2,
                base_url='http://localhost:11434'  # Default Ollama URL
            ),
            knowledge_sources=[pdf_source],
            embedder={'provider': 'ollama',
                      'config':{'model':'nomic-embed-text:latest'}}
        )

    @task
    def research_task(self) -> Task:
        return Task(
            description="""Conduct a thorough research and understand the information given to you in knowledge source.
            The information given to you is about a person with their records, achievements, work and etc.""",
            expected_output="Answer with the most relevant information and present it in a clear and concise manner for the questions: {question}",
            agent=self.researcher()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Bujji crew"""
        return Crew(
            agents=[self.researcher()],
            tasks=[self.research_task()],
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[content_source]
        )
