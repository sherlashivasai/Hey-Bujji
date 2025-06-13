#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from bujji.crew import Bujji

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

question  = "Introduce Yourself "

def run():
    """
    Run the crew.
    """
    inputs = {
        "question": question
    }
    
    try:
        Bujji().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "question": question
    }
    try:
        Bujji().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Bujji().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "question": question
    }
    
    try:
        Bujji().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
