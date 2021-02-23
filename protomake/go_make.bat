set client_in_path=../../share/clientproto
set server_in_path=../../share/serverproto
set rank_server_in_path=../../share/rankproto
set out_path="../../go/server/projects/pb"

rd /s /Q %out_path%
md %out_path%

rem go has import protobuf error must manual write
protoc.exe --plugin=protoc-gen-go=.\protoc-gen-go.exe  --proto_path %client_in_path%  --proto_path %server_in_path%  --proto_path %rank_server_in_path%  --go_out  %out_path%  cs_msg_id.proto  cs_common.proto  cs_login_sys.proto  cs_sundry_sys.proto  ss_base.proto  ss_logic.proto  db.proto  rank_client.proto

pause