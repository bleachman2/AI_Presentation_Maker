"""File with LLM prompts to be used in notebook."""


outline_prompt = """
# Task:

Create a detailed outline for an 8-slide PowerPoint presentation titled "Practical Uses of AI on a Daily Basis for Developers".

# Presentation Details:

    Number of Slides: 8
    Target Audience: Developers familiar with AI concepts

# Content Requirements:

    - Introduction Slide:
        - Include [Presenter Name] and [Presentation Topic].

    - AI Tools for Searching:
        - Tools like Perplexity and ChatGPT Search

    - AI Tools for Research:
        - Tools like NotebookLM

    - AI Tools for Transcriptions and Meetings:
        - Tools like OtterAI

    - AI Tools for Note-Taking:
        - Tools like Notion AI and Obsidian with AI plugins

    - Additional AI Tools:
        - Research and include other relevant tools beneficial for developers
        - Merge similar tools into the same slides to streamline content

    - API and Automation Tools:
        - Tools like OpenAI API
        - Position this as the second-to-last slide

    - Q/A Slide:
        - Conclude with a slide for questions and answers

# Slide Format

For each slide, provide:

    - Slide Title: A concise title
    - Key Points: Bullet points highlighting main content

# Additional Instructions

    - Focus on Practicality: Emphasize real-world applications for developers
    - Benefits and Use Cases: Highlight efficiencies and specific examples
    - Logical Flow: Ensure a coherent progression from start to finish
    - Engaging Content: Craft informative content suited for an AI-savvy audience

# Deliverable:

Provide the PowerPoint outline in a structured format, listing each slide with its title and bullet points.""" # noqa: E501

PPT_prompt = """
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
    - Format the text to not use bullet point markers and instead use line breaks.

- **Image Creation**:
    - Craft an image prompt that will produce a visual supporting the slide's theme.
    - The prompt should be detailed enough for Stable Diffusion to generate a relevant and high-quality image.
    - The prompt should make sure that no text is contained in the image.
    - The prompt should create abstract images.
    - The prompt will be used with the Flux image model.

# Formatting Guidelines

Present the content for each slide in the following format:

---

## {Slide Title}

Slide Text:
Point 1
Point 2
Point 3

##Image Prompt:
*"Your Stable Diffusion image prompt here."*

---

# Example

---

## Title Slide

Slide Text:
Practical Uses of AI on a Daily Basis for Developers
Presentation Date: [Insert Date]
Presented by: [Your Name]

##Image Prompt:
"An abstract illustration of AI intertwining with coding symbols, representing the fusion of AI and software development."

---

Use this format to provide content for each slide in the outline.

""" # noqa: E501


notes_prompt = """
# Task

Using the slide content and image prompts provided, create detailed presenter notes for each slide in the presentation.

# Instructions

- **Objective**: For each slide, write comprehensive presenter notes that will guide the speaker during the presentation.

- **Presenter Notes Should Include**:
    - An expansion of the slide's main points with additional details, explanations, and context.
    - Engaging language to connect with an audience knowledgeable about AI and development.
    - Examples, anecdotes, or insights that enhance the understanding of the topic.
    - A logical flow that complements the slide content without simply reading the slide text verbatim.

# Formatting Guidelines

- Present the notes for each slide in the following format:

# Slide {Number}: {Slide Title}

## Presenter Notes
[Your detailed presenter notes here.]


# Example



# Slide 1: Introduction

## Presenter Notes

Welcome to today's presentation on 'Practical Uses of AI on a Daily Basis for Developers.' My name is [Your Name], and I'm excited to share how AI is transforming our daily workflows as developers. We'll explore various AI tools that enhance productivity, streamline processes, and open up new possibilities in software development. By the end of this session, I hope you'll have a deeper understanding of how to leverage these tools in your own projects.


Use this format to provide presenter notes for each slide, ensuring that the content is informative, engaging, and adds value beyond the text on the slides.

""" # noqa: E501
