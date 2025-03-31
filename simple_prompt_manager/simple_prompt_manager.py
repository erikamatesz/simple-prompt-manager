import os
import re

class PromptManager:
    """
    Manage prompts based on templates stored in text files or created at runtime.
    """

    def __init__(self, templates_dir="prompts"):
        """
        Initializes the PromptManager and loads the templates.

        Args:
            templates_dir (str): Directory where template files are stored. 
                                  Defaults to 'prompts' if not specified.
        """
        self.templates_dir = templates_dir  # Set the templates directory
        self._ensure_templates_dir_exists()
        self.templates = self._load_templates()

    def _ensure_templates_dir_exists(self):
        """
        Ensures that the templates directory exists and creates a test template if it doesn't.
        """
        if not os.path.exists(self.templates_dir):
            os.makedirs(self.templates_dir)
            self._create_test_template()

    def _create_test_template(self):
        """
        Creates a test template file in the templates directory.
        """
        test_template_content = "Hello, <<name>>! This is a test template."
        test_template_path = os.path.join(self.templates_dir, "test_template.txt")
        with open(test_template_path, "w", encoding="utf-8") as file:
            file.write(test_template_content)

    def _load_templates(self):
        """
        Loads all templates from .txt files in the specified directory.

        Returns:
            dict: A dictionary with template names as keys and their contents as values.
        """
        templates = {}
        for filename in os.listdir(self.templates_dir):
            if filename.endswith(".txt"):
                template_name = os.path.splitext(filename)[0]
                with open(os.path.join(self.templates_dir, filename), "r", encoding="utf-8") as file:
                    templates[template_name] = file.read()
        return templates

    def add_template(self, template_name, template_content):
        """
        Adds a new template to the manager at runtime.

        Args:
            template_name (str): The name of the template to add.
            template_content (str): The content of the template.
        """
        if template_name in self.templates:
            raise ValueError(f"Template '{template_name}' already exists.")
        self.templates[template_name] = template_content

    def generate_prompt(self, template_name, **kwargs):
        """
        Generates a prompt based on a template and replaces variables.

        Args:
            template_name (str): The name of the template to use.
            **kwargs: Variables to replace in the template.

        Returns:
            str: The generated prompt.
        """
        template = self.templates.get(template_name, None)
        if not template:
            raise ValueError(f"Template '{template_name}' not found.")
        
        def replace_placeholder(match):
            variable_name = match.group(1)
            if variable_name not in kwargs:
                raise ValueError(f"Missing variable in the template: {variable_name}")
            return str(kwargs[variable_name])

        pattern = re.compile(r'<<(\w+)>>')
        return pattern.sub(replace_placeholder, template)

    def list_templates(self):
        """
        Lists all available templates.

        Returns:
            list: A list of template names.
        """
        return list(self.templates.keys())