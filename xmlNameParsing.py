"""
This code snippet parses xml files in a folder and does the operation you want.
Here we are excluding xml tags by name and saving the newly generated file with it's name extented by '_output'
"""


import os
import xml.etree.ElementTree as ET

class xmlConverter():
    @staticmethod
    def header_rows():
        # This should be your input directory
        rootdir = "C:/testing"
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                input1 = os.path.join(subdir, file)
                try:
                    tree = ET.parse(input1)
                    root = tree.getroot()
                    # looping over the tags in the xml file in a hierarchical manner 
                    for child1 in root.findall("<parenttag>"):
                        for child2 in child1.findall("<tag1>"):
                            for child3 in child2.findall("<tag2>"):
                                for child4 in child3.findall("<tag3>"):
                                    for child5 in child4.findall("<tag4>"):
                                        for child6 in child5.findall("<tag5>"):
                                            for child7 in child6.findall("<tagwewanttoexclude>"):
                                                child6.remove(child7)
                    file_name = file+"_output"
                    output = os.path.join(subdir, file_name)
                    tree.write(output)
                except Exception as e:
                    print("This file has no data that we need so this is skipped ---> "+e)




if __name__ == '__main__':
    xmlConverter.header_rows()
