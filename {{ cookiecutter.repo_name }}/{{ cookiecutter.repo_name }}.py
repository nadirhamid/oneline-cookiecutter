

##############################################################################
# Factory created module. Edit
# as you like 
# @author {{ cookiecutter.author_name }}
# @package {{ cookiecutter.oneline_package_name }}
# @vendor {{ cookiecutter.oneline_vendor_name }}
# @does {{ cookiecutter.description }}
##############################################################################

from oneline import ol

class {{ cookiecutter.repo_name }}(ol.module)
    def start(self):
        self.pipeline = ol.stream()
    
    def receiver(self, message):
        self.pipeline.run(message)
