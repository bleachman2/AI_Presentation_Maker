"""File with LLM prompts to be used in notebook."""

usr_prompt = """
[topic] = List of day to day AI Tools for Developers
[number] = 8
[target audience] = developers
[Key point 1] = Finish with a Q/A slide
[Key point 2] = Have the second to Last slide be manual coding LLM integration
[Key point 3] = Include search tools like perplexity, research tools like notebookLM, Transcription tools like Otter.ai
""" # noqa: E501


sys_prompt = """
You are a professional content presenter.
Create a PowerPoint presentation on [topic].
The presentation should be [number] slides long and aimed at [target audience].
Include the following key points:
    [Key point 1]
    [Key point 2]
    [Key point 3]

Please structure the presentation with an introduction, main content slides, and a conclusion.
""" # noqa: E501

first_prompt = """
#Task
As an Expert AI developer, your task is to create a detailed outline for a PowerPoint presentation on the topic: "Practical Uses of AI on a Daily Basis for Developers".

#Presentation Details

- Number of Slides: 10 slides.
- Target Audience: Developers who are fairly knowledgeable about AI.

# Content Requirements

- Include AI Tools: Incorporate tools like NotebookLM, OtterAI, Perplexity, and other relevant AI tools that developers can use in their daily work.
- Additional Tools: Research and include other AI tools that fit the topic and are beneficial for developers.
- Merge Similar Tools: Combine similar tools or topics into the same slides to streamline the presentation.

# Structure and Formatting

## Slide Format:
- Slide Number: Indicate the slide number.
- Slide Title: Provide a concise title for each slide.
- Key Points: List bullet points highlighting the main content of each slide.
- Description: Optionally, include a brief description or notes for clarification if necessary.

# Additional Instructions

- Focus on Practicality: Emphasize how AI tools can be practically applied by developers in their daily routines.
- Benefits and Use Cases: Highlight the benefits, efficiencies, and specific use cases of each tool or category of tools.
- Logical Flow: Ensure the presentation flows logically from introduction to conclusion.
- Engaging Content: Aim for content that is engaging and informative for an audience already familiar with AI concepts.
- Q/A Section: Finish the presentation with a Q/A slide

# Deliverable

Provide the PPT outline in a structured format, clearly listing each slide with its number, title, and bullet points.""" # noqa: E501

second_prompt = """
# Task

Given a PowerPoint (PPT) outline, create detailed content for each slide.

For **each slide**, provide:

1. **Slide Text**: The main points or content to be included on the slide. Use clear and concise bullet points or brief paragraphs as appropriate.
2. **Image Prompt**: A descriptive prompt for Stable Diffusion to generate an image that complements the slide's content.

# Instructions

- **Content Development**:
    - Expand on the key points provided in the outline.
    - Ensure the content is informative and engaging for an audience knowledgeable about AI.
    - Keep slide text concise to fit typical PPT slide formats.

- **Image Creation**:
    - Craft an image prompt that will produce a visual supporting the slide's theme.
    - The prompt should be detailed enough for Stable Diffusion to generate a relevant and high-quality image.

# Formatting Guidelines

Present the content for each slide in the following format:

---

## Slide {Number}: {Slide Title}

**Slide Text**:
- Point 1
- Point 2
- Point 3

**Image Prompt**:
*"Your Stable Diffusion image prompt here."*

---

# Example

---

## Slide 1: Title Slide

**Slide Text**:
- **Practical Uses of AI on a Daily Basis for Developers**
- Presentation Date: [Insert Date]
- Presented by: [Your Name]

**Image Prompt**:
*"An abstract illustration of AI intertwining with coding symbols, representing the fusion of AI and software development."*

---

Use this format to provide content for each slide in the outline.

""" # noqa: E501
