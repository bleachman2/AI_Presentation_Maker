usr_prompt = """
[topic] = List of day to day AI Tools for Developers
[number] = 8
[target audience] = developers
[Key point 1] = Finish with a Q/A slide
[Key point 2] = Have the second to Last slide be manual coding LLM integration
[Key point 3] = Include search tools like perplexity, research tools like notebookLM, Transcription tools like Otter.ai
"""


sys_prompt = """
Reset conversation
You are a professional content presenter.
Create a PowerPoint presentation on [topic].
The presentation should be [number] slides long and aimed at [target audience].
Include the following key points:
    [Key point 1]
    [Key point 2]
    [Key point 3]
    
Please structure the presentation with an introduction, main content slides, and a conclusion.
"""

