from simple_prompt_manager import PromptManager

# Initialize the PromptManager
pm = PromptManager()

# Example 1: Bohemian Rhapsody
# Add a template inspired by "Bohemian Rhapsody"
pm.add_template("bohemian_rhapsody", "Is this the real life? Is this just <<illusion>>?")

# Generate a prompt
prompt1 = pm.generate_prompt("bohemian_rhapsody", illusion="fantasy")
print(prompt1)  # Output: Is this the real life? Is this just fantasy?

# Example 2: We Will Rock You
# Add a template inspired by "We Will Rock You"
pm.add_template("we_will_rock_you", "<<name>>, you got mud on your face, you big disgrace!")

# Generate a prompt
prompt2 = pm.generate_prompt("we_will_rock_you", name="Buddy")
print(prompt2)  # Output: Buddy, you got mud on your face, you big disgrace!

# Example 3: Another One Bites the Dust
# Add a template inspired by "Another One Bites the Dust"
pm.add_template("another_one_bites_the_dust", "Are you ready? Are you ready for this? Are you hanging on the edge of your <<seat>>?")

# Generate a prompt
prompt3 = pm.generate_prompt("another_one_bites_the_dust", seat="chair")
print(prompt3)  # Output: Are you ready? Are you ready for this? Are you hanging on the edge of your chair?