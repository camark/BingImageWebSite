import commands
from baseop import BaseOp

class RosTopic(BaseOp):
    def list(self):
	    return self.list_op('rostopic list')

    def detail(self,topicname):
        return self.list_op('rostopic info '+topicname)

