"""File with LLM prompts to be used in notebook."""

from __future__ import annotations


def format_nested_list_to_string(data_list: list[list[str]]) -> str:
    temp = []
    for data in data_list:
        title = data[0]
        examples = data[1:]
        temp.append(f"- {title}:")
        temp.append(f"{' '*4}- Example points:")
        temp.extend(f"{' '*8}- {example}" for example in examples)
    return "\n".join(temp).strip()


def generalized_outline_prompt(
    slides: int, topic: str, audience_level: str, points: list[list[str]],
    additional_info: list[str]|None = None,
) -> str:
    additional_info_text = "- "+"\n".join(additional_info) if additional_info else ""
    return f"""
# Task

Create a detailed outline for a {slides} slide PowerPoint presentation titled {topic}. Focus on the topic - {topic} and expand it with relevant examples and content.
Presentation Details:

- Number of Slides: {slides}
- Target Audience: {audience_level} in {topic}

# Content Requirements

- Introduction Slide:
    - Include [Presenter Name] and the topic - {topic}.
    - The title of this slide should be {topic}

# Talking Points
{format_nested_list_to_string(points)}

- Additional Topics:
    - Research and include other relevant points beneficial for [Target Audience].

- [Summary or Compilation Slide]:
    - Compile several key takeaways from the presentation.

- Q&A Slide:
    - Conclude with a slide for questions and answers.

# Slide Format:

For each slide, provide:

    - Slide Title: A concise title.
    - Key Points: Bullet points highlighting main content.

# Additional Instructions:

- Merge Similar Topics: Combine similar subjects into the same slides to streamline content.
- Focus on Practicality: Emphasize real-world applications for [Target Audience].
- Benefits and Use Cases: Highlight efficiencies and provide specific examples.
- Logical Flow: Ensure a coherent progression from start to finish.
- Engaging Content: Craft informative content suited for an [Target Audience].
- Slides Sequence: The first slide is the Introduction with the [Presenter Name], and the last slide is the Q&A.
{additional_info_text}

# Deliverable:

    - Provide the PowerPoint outline in a structured format, listing each slide with its title and bullet points.
"""  # noqa: E501


PPT_prompt = """
# Task

Given a PowerPoint (PPT) outline, create detailed content for each slide.

For **each slide**, provide:

1. **Slide Text**: The main points or content to be included on the slide. Use clear and concise bullet points or brief paragraphs as appropriate.
2. **Image Prompt**: A descriptive prompt for Stable Diffusion to generate an image that complements the slide's content.

# Instructions

- **Content Development**:
    - Expand on the key points provided in the outline.
    - Merge slides if the content is similar.
    - Ensure the content is informative and engaging for an audience knowledgeable about the topic.
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
Presentation Date: [Current Date]
Presented by: [Your Name]

##Image Prompt:
"An abstract illustration of AI intertwining with coding symbols, representing the fusion of AI and software development."

---

Use this format to provide content for each slide in the outline.

"""  # noqa: E501


notes_prompt = """
# Task

Using the slide content and image prompts provided, create detailed presenter notes for each slide in the presentation.

# Instructions

- **Objective**:
    - For each slide, write comprehensive presenter notes that will guide the speaker during the presentation.
    - Make sure there are generated notes for every slide.
    - Include additional information regarding the slide that might be important for the presenter to know.

- **Presenter Notes Should Include**:
    - An expansion of the slide's main points with additional details, explanations, and context.
    - Engaging language to connect with an audience knowledgeable about AI and development.
    - Examples, anecdotes, or insights that enhance the understanding of the topic.
    - Concise and casual human language.
    - A logical flow that complements the slide content without simply reading the slide text verbatim.

# Formatting Guidelines

- Present the notes for each slide in the following format:

# Slide {Number}: {Slide Title}

## Presenter Notes
[Your detailed presenter notes here.]

## Additional information:
[Additional information here.]


# Example


```
# Slide 1: Introduction

## Presenter Notes

Welcome to today's presentation on [topic] My name is [Your Name], and I'm excited to share how {topic}. ....

## Additional Information

# Slide 2: {Slide 2 Title}

## Presenter Notes
Regarding x

## Additional Information
n percent of developers use tool x....

# Slide 3: {Slide 3 Title}

## Presenter Notes
Regarding y

## Additional Information
y is a ...

# Slide m:
...
```

Use this format to provide presenter notes for each slide, ensuring that the content is informative, engaging, and adds value beyond the text on the slides.

"""  # noqa: E501
