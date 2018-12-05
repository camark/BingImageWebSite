from baseop import BaseOp


class RosParam(BaseOp):

    def list(self):
        return self.list_op('rosparam list')

    def detail(self,param_name):
        return self.list_op('rosparam info '+param_name)