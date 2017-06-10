python helper.py
appcfg.py update ./app.yaml ./module-worker.yaml
appcfg.py update .





































#!/bin/bash                                                                                                    
                                                                                                               
# ------------------------------------------                                                                   
# 名称：KindleEar安装脚本                                                                                      
# 作者：richars，kindlefere基础上修改
# 更新：2017.02.09                                                                                             
# ------------------------------------------                                                                   
                                                                                                               
cd ~                                                                                                           
                                                                                                               
                                                                                                    
rm -rf ./KindleEar                                                                                   
git clone https://github.com/richars/KindleEar.git                                                    
cd ./KindleEar                                                                                         
                                                 
cemail=$(sed -n "s/^SRC_EMAIL = \"\(.*\)\".*#.*/\1/p" ./config.py)                                             
cappid=$(sed -n "s/^DOMAIN = \"https:\/\/\(.*\)\.appspot.com\".*#.*/\1/p" ./config.py)                         
response='y'                                                                                                   
                                                                                                               
echo '当前的 Gmail 为：'$cemail                                                                                
echo '当前的 APPID 为：'$cappid                                                                                
                                                                                                               
if [ ! $cemail = "akindleear@gmail.com" -o ! $cappid = "kindleear" ]                                           
then                                                                                                           
    read -r -p "是否修改 APP 信息? [y/N] " response                                                            
fi                                                                                                             
                                                                                                               
if [[ $response =~ ^([yY][eE][sS]|[yY])$ ]]                                                                    
then                                                                                                           
    echo -n "请输入你的 Gmail 地址："                                                                          
    read email                                                                                                 
    echo "您输入的 Gmail 地址是：'$email'"                                                                     
    sed -i "s/^SRC_EMAIL = \".*\"/SRC_EMAIL = \"$email\"/g" ./config.py                                        
    echo -n "请输入你的 APP ID："                                                                              
    read appid                                                                                                 
    echo "您输入的 APP ID 是：'$appid'"                                                                        
    sed -i "s/^application: .*/application: $appid/g" ./app.yaml ./module-worker.yaml                          
    sed -i "s/^DOMAIN = \"https:\/\/.*\.appspot.com\"/DOMAIN = \"https:\/\/$appid\.appspot.com\"/g" ./config.py
fi                                                                                                             
                                                                                                               
appcfg.py update app.yaml module-worker.yaml --no_cookie --noauth_local_webserver                              
appcfg.py update . --no_cookie --noauth_local_webserver        