from jinja2 import Template

template = Template(r'''#!/bin/bash
cmdexist=`whereis nmap | awk -F":" '{print $2}'`
if [ "$cmdexist" == "" ];then
        /usr/bin/yum install nmap -y
fi

[ $? -ne 0 ] && exit 1

ipmacfile="ipscan.txt"
[ -e "$ipmacfile" ] && > $ipmacfile
for networkaddr in {{iplist}};do
nmap -sP -PS22,60886 -n $networkaddr --append-output -oN $ipmacfile > /dev/null 2>&1
done
wait

for vmname in `virsh list | awk '{print $2}' | grep -v 'Name'`;do
kvmmac=`virsh domiflist $vmname | grep ".*:.*" | awk '{print $5}'`
kvmmac=`echo $kvmmac | tr "[:lower:]" "[:upper:]"`
ip=$(awk -v mac="$kvmmac" '/report for/{newip=$5}$0~mac{print newip}' $ipmacfile)
printf "%-5s %-10s \n" $vmname $ip
done''')


with open("getdominip.sh",'w') as f:
        f.write(template.render(iplist='"172.16.25.0/24 172.16.26.0/24 172.16.27.0/24"'))

