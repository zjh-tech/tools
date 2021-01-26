#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import sys
import xlrd
import string

PB_INPUTPATH = sys.argv[1]
CFG_MGR_OUTPATH = sys.argv[2]

#PB_INPUTPATH = u"..\\config\\out\\binary"
#CFG_MGR_OUTPATH = u"..\\config\\out\\csharp_cfg_mgr"

CODE = "utf8"

CLIENT_FLAG = 1
SERVER_FLAG = 2
COMMON_FLAG = 3

change_line = "\n"
empty_line = "                     \n"
tab_code = "   "


class CTool:
    def __init__(self):
        self.mCodeData = []

    def get_code_data(self):
        return self.mCodeData

    def generate_include(self):
        code = "using System;" + change_line
        code += "using Google.Protobuf;" + change_line
        code += "using Config;" + change_line
        code += "using System.IO;" + change_line
        code += "using Framework.ELog;" + change_line
        code += empty_line

        self.mCodeData += code

    def generate_class_start(self):
        code = "public class StaticDataMgr" + change_line
        code += "{" + change_line
        code += tab_code + "public static StaticDataMgr Instance = new StaticDataMgr();" + \
            change_line
        code += empty_line
        self.mCodeData += code

    def generate_class_end(self):
        code = "}" + change_line
        code += empty_line
        self.mCodeData += code

    def generate_load_all_cfg_start(self):
        code = tab_code + \
            "public ErrorString LoadAllCfg(string prefix_path)" + change_line
        code += tab_code + "{" + change_line
        self.mCodeData += code

    def generate_load_all_cfg(self, fileName):
        cap_file_name = fileName.capitalize()
        code = tab_code + tab_code + "string " + fileName + \
            "_path = prefix_path + " + "\"/" + fileName + ".pb\";" + change_line
        code += tab_code + tab_code + fileName + \
            "_cfg = (" + fileName + "cfg)load_cfg<" + fileName + \
            "cfg>(" + fileName + "_path);" + change_line
        code += tab_code + tab_code + \
            "if (" + fileName + "_cfg == null)" + change_line
        code += tab_code + tab_code + "{" + change_line
        code += tab_code + tab_code + tab_code + \
            "return new ErrorString(\"Load " + cap_file_name + \
            " File Error...\");" + change_line
        code += tab_code + tab_code + "}" + change_line
        code += tab_code + tab_code + \
            "Log.Infof(\"[StaticDataMgr] " + cap_file_name + \
            "={0}\", " + fileName + "_cfg.ToString());" + change_line
        code += empty_line
        self.mCodeData += code

    def generate_load_all_cfg_end(self):
        code = tab_code + tab_code + "return null;" + change_line
        code += tab_code + "}" + change_line
        code += empty_line
        self.mCodeData += code

    def generate_load_cfg(self):
        code = tab_code + \
            "private IMessage load_cfg<T>(string path) where T : IMessage<T> ,new()" + \
            change_line
        code += tab_code + "{" + change_line
        code += tab_code + tab_code + "FileStream file_stream = null;" + change_line
        code += tab_code + tab_code + "try" + change_line
        code += tab_code + tab_code + "{" + change_line
        code += tab_code + tab_code + tab_code + \
            "file_stream = File.Open(path, FileMode.Open);" + change_line
        code += tab_code + tab_code + "}" + change_line
        code += tab_code + tab_code + "catch(SystemException)" + change_line
        code += tab_code + tab_code + "{" + change_line
        code += tab_code + tab_code + tab_code + \
            "Log.Infof(\"[StaticDataMgr] Path = {0} Open File Error\", path); " + change_line
        code += tab_code + tab_code + tab_code + "return null;" + change_line
        code += tab_code + tab_code + "}" + change_line
        code += empty_line
        code += tab_code + tab_code + "if (file_stream != null)" + change_line
        code += tab_code + tab_code + "{" + change_line
        code += tab_code + tab_code + tab_code + \
            "BinaryReader reader = new BinaryReader(file_stream);" + \
            change_line
        code += tab_code + tab_code + tab_code + \
            "if(reader != null)" + change_line
        code += tab_code + tab_code + tab_code + "{" + change_line
        code += tab_code + tab_code + tab_code + tab_code + \
            "byte[] datas = reader.ReadBytes((int)file_stream.Length);" + \
            change_line
        code += tab_code + tab_code + tab_code + tab_code + \
            "MessageParser<T> parser = new MessageParser<T>(() => new T());" + \
            change_line
        code += tab_code + tab_code + tab_code + tab_code + \
            "return parser.ParseFrom(datas);" + change_line
        code += tab_code + tab_code + tab_code + "}" + change_line
        code += tab_code + tab_code + "}" + change_line
        code += empty_line
        code += tab_code + tab_code + "return null;" + change_line
        code += tab_code + "}" + change_line
        code += empty_line
        self.mCodeData += code

    def generate_define_class(self, fileName):
        code = tab_code + "private " + fileName + "cfg " + \
            fileName + "_cfg = null;" + change_line
        code += empty_line
        self.mCodeData += code

    def generate_get_cfg(self, fileName):
        cap_file_name = fileName.capitalize()
        code = tab_code + "public " + fileName + \
            "cfg  Get" + cap_file_name + "Cfg()" + change_line
        code += tab_code + "{" + change_line
        code += tab_code + tab_code + "return " + fileName + "_cfg;" + change_line
        code += tab_code + "}" + change_line
        code += empty_line
        self.mCodeData += code

    def generate_get_cfg_by_id(self, fileName):
        cap_file_name = fileName.capitalize()
        code = tab_code + "public " + fileName + "  Get" + \
            cap_file_name + "ByID(UInt32 id)" + change_line
        code += tab_code + "{" + change_line
        code += tab_code + tab_code + \
            "if (" + fileName + "_cfg.Datas.ContainsKey(id))" + change_line
        code += tab_code + tab_code + "{" + change_line
        code += tab_code + tab_code + tab_code + "return " + \
            fileName + "_cfg.Datas[id];" + change_line
        code += tab_code + tab_code + "}" + change_line
        code += empty_line
        code += tab_code + tab_code + "return null;" + change_line
        code += tab_code + "}" + change_line
        code += empty_line
        self.mCodeData += code

    def del_file(self, path):
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                self.del_file(c_path)
            else:
                os.remove(c_path)

    def write(self, path, filename, content):
        if not os.path.exists(path):
            os.makedirs(path)

        all_path_filename = path + "\\" + filename
        code_file = open(all_path_filename, 'w')
        code_file.write(''.join(content))
        code_file.close()


def Start():
    tool = CTool()
    tool.generate_include()
    tool.generate_class_start()

    tool.generate_load_all_cfg_start()
    for _, _, files in os.walk(PB_INPUTPATH):
        for filename in files:
            file_full_path = os.path.join(PB_INPUTPATH, filename)
            if os.path.exists(file_full_path):
                pb_name = filename.replace(".pb", "")
                tool.generate_load_all_cfg(pb_name)
    tool.generate_load_all_cfg_end()

    tool.generate_load_cfg()
    for _, _, files in os.walk(PB_INPUTPATH):
        for filename in files:
            file_full_path = os.path.join(PB_INPUTPATH, filename)
            if os.path.exists(file_full_path):
                pb_name = filename.replace(".pb", "")
                tool.generate_get_cfg(pb_name)
                tool.generate_get_cfg_by_id(pb_name)

    for _, _, files in os.walk(PB_INPUTPATH):
        for filename in files:
            file_full_path = os.path.join(PB_INPUTPATH, filename)
            if os.path.exists(file_full_path):
                pb_name = filename.replace(".pb", "")
                tool.generate_define_class(pb_name)

    tool.generate_class_end()

    h_filename = "staticdatamgr.cs"
    # tool.del_file(CFG_MGR_OUTPATH)
    tool.write(CFG_MGR_OUTPATH, h_filename, tool.get_code_data())
    print "ok"


if __name__ == '__main__':
    Start()
