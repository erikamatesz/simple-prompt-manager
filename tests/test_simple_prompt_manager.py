import os
import shutil
import pytest
from simple_prompt_manager import PromptManager

@pytest.fixture
def setup_and_teardown():
    test_dir = "test_prompts"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    yield test_dir
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)

def test_templates_dir_creation(setup_and_teardown):
    test_dir = setup_and_teardown
    pm = PromptManager(templates_dir=test_dir)
    assert os.path.exists(test_dir), "The templates directory was not created."

def test_add_template_runtime(setup_and_teardown):
    test_dir = setup_and_teardown
    pm = PromptManager(templates_dir=test_dir)
    queen_template_content = "Is this the real life? Is this just <<illusion>>?"
    pm.add_template("bohemian_rhapsody", queen_template_content)
    assert "bohemian_rhapsody" in pm.templates, "The Queen template was not added correctly."

def test_generate_queen_prompt_runtime(setup_and_teardown):
    test_dir = setup_and_teardown
    pm = PromptManager(templates_dir=test_dir)
    queen_template_content = "Is this the real life? Is this just <<illusion>>?"
    pm.add_template("bohemian_rhapsody", queen_template_content)
    prompt = pm.generate_prompt("bohemian_rhapsody", illusion="fantasy")
    assert prompt == "Is this the real life? Is this just fantasy?", "The generated prompt is incorrect."

def test_add_existing_template_raises_error(setup_and_teardown):
    test_dir = setup_and_teardown
    pm = PromptManager(templates_dir=test_dir)
    queen_template_content = "Is this the real life? Is this just <<illusion>>?"
    pm.add_template("bohemian_rhapsody", queen_template_content)
    with pytest.raises(ValueError, match="Template 'bohemian_rhapsody' already exists."):
        pm.add_template("bohemian_rhapsody", queen_template_content)

def test_generate_prompt_missing_template(setup_and_teardown):
    test_dir = setup_and_teardown
    pm = PromptManager(templates_dir=test_dir)
    with pytest.raises(ValueError, match="Template 'non_existent' not found."):
        pm.generate_prompt("non_existent", illusion="fantasy")

def test_generate_prompt_missing_variable(setup_and_teardown):
    test_dir = setup_and_teardown
    pm = PromptManager(templates_dir=test_dir)
    queen_template_content = "Is this the real life? Is this just <<illusion>>?"
    pm.add_template("bohemian_rhapsody", queen_template_content)
    with pytest.raises(ValueError, match="Missing variable in the template: illusion"):
        pm.generate_prompt("bohemian_rhapsody")