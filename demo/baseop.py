import commands

class BaseOp:
    def list_op(self,str):
        (status, output) = commands.getstatusoutput(str)
        if status==0:
            nodelist=output.split('\n')
            return (0,nodelist)
        else:
            return (1,output)
