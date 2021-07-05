def check_num_of_container(Num_of_conts):
    while True:
        try:
            int(Num_of_conts)
        except Exception as e:
            Num_of_conts = input("Please enter an integer: ")
            break
        if Num_of_conts>0:
            break
        else:
            Num_of_conts = input("Cannot be zero, please re-enter: ")
    return int(Num_of_conts)


step1: ubuntu install docker
def ubuntu_install_docker():
    while True:
        update_status = os.system("sudo apt-get update")
        if not update_status:
            break

    while True:    
        install_docker_status = os.system("sudo apt-get install -y docker")
        if not install_docker_status:
            break

    while True:
        install_dockerio_status = os.system("sudo apt-get install docker.io -y")
        if not install_dockerio_status:
            break


def touch_eth_addr_file(Your_ETH_Addr):
    os.system(f"echo {Your_ETH_Addr} > ~/.revenue_address")     #0xC8xxxx  --is youself eth wallet address


step3: start - create zktube miner
def creat_miners(Num_of_conts):
    docker_run_status = os.system(f"docker run -d -v ~/.revenue_address:/revenue_address --name zktube_{Num_of_conts} zktubelabs/zktube-prover:latest")

    step4: check log
    os.system(f"docker logs --tail 100 -f zktube_{Num_of_conts}")
    
def show_me():
    print("--"*30)
    print("--"*10, " "*2, "批量部署VX: ameng198808" ," "*2,"--"*10)
    print("--"*30, '\n\n')

if __name__=="__main__":
  
    show_me()
    import os
    Your_ETH_Addr = input("Type Your ETH Wallet Address: ")
    Num_of_conts = input("Number of containers: ")
    
    Ok_Num_of_conts = check_num_of_container(Num_of_conts = Num_of_conts)
    ubuntu_install_docker()
    touch_eth_addr_file(Your_ETH_Addr)
    for i in range(1, Ok_Num_of_conts+1):
        creat_miner(i)
    
    
