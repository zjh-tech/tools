set  server_in_path=../../share/serverproto
set  out_path="../../csharp/code/projects/frame/pb"

del /a /f /s  %out_path%\*cs

rem go has import protobuf error must manual write
protoc.exe  --proto_path %server_in_path%  --csharp_out  %out_path%  ss_base.proto

pause