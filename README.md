<div style="text-align: center;">
    <img src="assets/readme_image.png" />
</div>

# Welcome to the Simple Prompt Manager! ✨

This is a very simple and lightweight library designed for managing and generating text prompts based on templates, particularly useful in generative AI projects. It supports loading templates from text files and creating them at runtime, allowing for dynamic text generation by replacing placeholders with specified values. This makes it an ideal tool for applications that require flexible and dynamic prompt generation, such as chatbots, content creation tools, and other AI-driven applications.

## Installation

Install it using pip:

```bash
pip install simple-prompt-manager
```

## Usage

### Basic Usage

Initialize the `PromptManager` and generate a prompt using a runtime template:

```python
from promptmanager import PromptManager

# Initialize the PromptManager
pm = PromptManager()

# Add a new template at runtime
pm.add_template("greeting", "Hello, <<name>>! Welcome to the PromptManager.")

# Generate a prompt
prompt = pm.generate_prompt("greeting", name="Alice")
print(prompt)  # Output: Hello, Alice! Welcome to the PromptManager.
```

### Using a Custom Templates Directory

Create a custom directory for your templates and load them:

```python
import os
from promptmanager import PromptManager

# Create a custom directory for templates
custom_dir = "my_templates"
os.makedirs(custom_dir, exist_ok=True)

# Initialize the PromptManager with the custom directory
pm = PromptManager(templates_dir=custom_dir)

# Add a template file manually in the custom directory
with open(os.path.join(custom_dir, "farewell.txt"), "w") as file:
    file.write("Goodbye, <<name>>! See you soon.")

# Load templates from the custom directory
pm.templates = pm._load_templates()

# Generate a prompt from the file-based template
prompt = pm.generate_prompt("farewell", name="Bob")
print(prompt)  # Output: Goodbye, Bob! See you soon.
```

## Examples

You can find an example script demonstrating how to use this package with Queen song lyrics in the `examples` directory. The `basic_usage.py` script covers adding templates at runtime and generating prompts inspired by songs like "Bohemian Rhapsody", "We Will Rock You", and "Another One Bites the Dust".

## Changelog

For a detailed list of changes and updates, please refer to the [CHANGELOG](CHANGELOG.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.