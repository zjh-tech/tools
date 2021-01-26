set   excel_in="../../share/excel"

set   temp_proto_out="./config/out/proto"
set   temp_python_out="./config/out/python"
set   temp_binary_out="./config/out/binary"
set   temp_csharp_out="./config/out/csharp"
set   temp_csharp_mgr_out="./config/out/csharp_cfg_mgr"

set   csharp_cfg_out="../../csharp/code/projects/frame/staticdata"

rmdir /s /q  %temp_proto_out%
mkdir %temp_proto_out%
python python\excel2proto.pyc   %excel_in%    %temp_proto_out%
pause 

rmdir /s /q  %temp_python_out%
mkdir %temp_python_out%
rmdir /s /q  %temp_csharp_out%
mkdir %temp_csharp_out%
rmdir /s /q  %temp_binary_out%
mkdir %temp_binary_out%

protoc.exe  --proto_path %temp_proto_out% --python_out=%temp_python_out%  %temp_proto_out%\*.proto
protoc.exe  --proto_path %temp_proto_out% --csharp_out %temp_csharp_out%  %temp_proto_out%\*.proto
python  python\binary.pyc   %excel_in%\    %temp_python_out%\  %temp_binary_out%\
pause

rmdir /s /q  %temp_csharp_mgr_out%
mkdir %temp_csharp_mgr_out%
python  python\csharp_code.pyc  %temp_binary_out%    %temp_csharp_mgr_out%
xcopy  %temp_csharp_out%  %csharp_cfg_out%  /y
xcopy  %temp_csharp_mgr_out%  %csharp_cfg_out%  /y
pause 
