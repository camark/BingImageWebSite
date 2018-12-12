from baseop import BaseOp

class RosPackage(BaseOp):
    def list(self):
	    return self.list_op('rospack list')

