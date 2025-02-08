from pathlib import Path

class Common:
    @staticmethod
    def rightPath(imageName: str):
        currenDir = Path(__file__).parent.parent
        rightPath: str = str(currenDir/'VIEW/images'/imageName)
        return rightPath
