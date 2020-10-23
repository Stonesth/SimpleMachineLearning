from Tools import tools_v000 as tools
import os
from os.path import dirname


# -21 for the name of this project SimpleMachineLearning
save_path = dirname(__file__)[ : -21]
propertiesFolder_path = save_path + "Properties"

# Example of used
# user_text = tools.readProperty(propertiesFolder_path, 'SimpleMachineLearning', 'user_text=')
