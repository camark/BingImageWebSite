import commands

class RosNode:
    def list(self):
        (status, output) = commands.getstatusoutput('rosnode list')
        if status==0:
            nodelist=output.split('\n')
            return (0,nodelist)
        else:
            return (1,output)