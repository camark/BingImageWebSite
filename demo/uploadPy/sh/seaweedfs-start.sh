set -ex

#ps  -ef | grep weed | grep -v grep| kill -9 `awk '{print $2}'`

mkdir mdir t_v1 t_v2 t_v3 v_mdir
nohup ./weed master -mdir=./mdir -port=9333 -defaultReplication="001"  >>./mdir/server_sfs.log &

nohup ./weed volume -dir=./t_v1 -max=1000 -mserver=localhost:9333 -port=8091 -ip=localhost >>./v_mdir/v1_sfs.log &
nohup ./weed volume -dir=./t_v2 -max=1000 -mserver=localhost:9333 -port=8092 -ip=localhost >>./v_mdir/v2_sfs.log &
nohup ./weed volume -dir=./t_v3 -max=1000 -mserver=localhost:9333 -port=8093 -ip=localhost >>./v_mdir/v3_sfs.log &

