

##############################################################################
# Factory created module. Edit
# as you like 
# @author Nadir Hamid
# @package Package Name
# @vendor ABC Inc.
# @does Testing a module with Oneline
##############################################################################

from oneline import ol

class OnelineModule(ol.module)
    def start(self):
        self.pipeline = ol.stream()
    
    def receiver(self, message):
        self.pipeline.run(message)
