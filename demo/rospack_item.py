
class RosPackageItem:
    def init(self,package_name,package_path):
        self.package_name=package_name
        self.package_path=package_path

    def __init__(self,package_str):
        (name,path)=package_str.split(' ')
        self.init(name,path)

    def isHome(self):
        return self.package_path.startswith('/home')