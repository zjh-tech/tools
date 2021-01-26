set client_in_path=../../share/clientproto
set server_in_path=../../share/serverproto
set out_path="../../cplusplus/code/projects/pb"

del /a /f /s  %out_path%\*pb.h
del /a /f /s  %out_path%\*pb.cc

rem go has import protobuf error must manual write
protoc.exe  --proto_path %client_in_path% --proto_path %server_in_path%  --cpp_out  %out_path%  cs_msg_id.proto  cs_common.proto   ss_base.proto

pause