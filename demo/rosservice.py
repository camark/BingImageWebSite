import commands
from baseop import BaseOp

class RosService(BaseOp):
    def list(self):
	return self.list_op('rosservice list')

    def detail(self,servicename):
        #servicename=servicename.replace('%2F','/')
        return self.list_op('rosservice info '+servicename)
