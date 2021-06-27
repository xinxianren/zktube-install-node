step1: ubuntu install docker

sudo apt-get update
sudo apt-get install -y docker
sudo apt-get install docker.io -y


step2: create one files .revenue_address input your eth walllet address

echo "0xC8c1B630835F4cC996e5cD05441a0d7e2D9e9e68" > ~/.revenue_address     #0xC8xxxx  --is youself eth wallet address

step3: start

docker run -d -v ~/.revenue_address:/revenue_address --name zktube zktube/prover:rinkeby

step: check log

docker logs --tail 100 -f zktube


go go go!
