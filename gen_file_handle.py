import xml.sax
import os


fileNameList_g = []
fileDataList_g = []


class GenFileHandler(xml.sax.ContentHandler):
    def __init__(self):
        # 标签内容，注意清理空格
        self.content = ""

    def startElement(self, tag, arrtibutes):
        """
        开始处理标签，存储标签名称

        Args:
            tag: 标签名
            attributes: 标签属性列表
        """
        pass

    def endElement(self, tag):
        """
        结束处理标签

        Args:
            tag: 标签名
        """
        if tag == "TSeq_accver":
            if not self.content.isspace():
                genFilePath = "target/gen_file/" + self.content + ".seq"
                fileNameList_g.append(genFilePath)
        elif tag == "TSeq_sequence":
            if not self.content.isspace():
                fileDataList_g.append(self.content)
        self.content = ""

    def characters(self, content):
        """
        处理标签的内容

        Args:
            content: 标签内容
        """
        self.content += content.strip()


def writeFile():
    """
    创建文件并写入内容
    fileNameList_g 文件名列表
    fileDataList_g 数据列表
    """
    for i in range(len(fileNameList_g)):
        with open(fileNameList_g[i], "w") as f:
            print(fileDataList_g[i].strip(), file=f)


def getFiles(dataFilePath):
    """
    打开文件夹，并遍历下面的文件

    Return:
        filePathList: 文件名数组
    """
    files = os.listdir(dataFilePath)
    filePathList = []

    for file in files:
        filePathList.append(dataFilePath + "/" + file)

    return filePathList


if __name__ == "__main__":
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # 关闭 namespaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    handler = GenFileHandler()
    parser.setContentHandler(handler)

    gen_files = r"resource/data/gen_data"

    for file in getFiles(gen_files):
        parser.parse(file)

    writeFile()
