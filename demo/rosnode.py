import commands
from baseop import BaseOp

class RosNode(BaseOp):
    def list(self):
	return self.list_op('rosnode list')
    
    def getDetail(self,nodename):
        return self.list_op('rosnode info /'+nodename)
