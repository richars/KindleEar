#!/bin/bash                                                                                                    
                                                                                                               
# ------------------------------------------                                                                   
# ���ƣ�KindleEar��װ�ű�                                                                                      
# ���ߣ�richars��kindlefere�������޸�
# ���£�2017.02.09                                                                                             
# ------------------------------------------                                                                   
                                                                                                               
cd ~                                                                                                           
                                                                                                               
                                                                                                    
rm -rf ./KindleEar                                                                                   
git clone https://github.com/richars/KindleEar.git                                                    
cd ./KindleEar                                                                                         
                                                 
cemail=$(sed -n "s/^SRC_EMAIL = \"\(.*\)\".*#.*/\1/p" ./config.py)                                             
cappid=$(sed -n "s/^DOMAIN = \"https:\/\/\(.*\)\.appspot.com\".*#.*/\1/p" ./config.py)                         
response='y'                                                                                                   
                                                                                                               
echo '��ǰ�� Gmail Ϊ��'$cemail                                                                                
echo '��ǰ�� APPID Ϊ��'$cappid                                                                                
                                                                                                               
if [ ! $cemail = "akindleear@gmail.com" -o ! $cappid = "kindleear" ]                                           
then                                                                                                           
    read -r -p "�Ƿ��޸� APP ��Ϣ? [y/N] " response                                                            
fi                                                                                                             
                                                                                                               
if [[ $response =~ ^([yY][eE][sS]|[yY])$ ]]                                                                    
then                                                                                                           
    echo -n "��������� Gmail ��ַ��"                                                                          
    read email                                                                                                 
    echo "������� Gmail ��ַ�ǣ�'$email'"                                                                     
    sed -i "s/^SRC_EMAIL = \".*\"/SRC_EMAIL = \"$email\"/g" ./config.py                                        
    echo -n "��������� APP ID��"                                                                              
    read appid                                                                                                 
    echo "������� APP ID �ǣ�'$appid'"                                                                        
    sed -i "s/^application: .*/application: $appid/g" ./app.yaml ./module-worker.yaml                          
    sed -i "s/^DOMAIN = \"https:\/\/.*\.appspot.com\"/DOMAIN = \"https:\/\/$appid\.appspot.com\"/g" ./config.py
fi                                                                                                             
                                                                                                               
appcfg.py update app.yaml module-worker.yaml --no_cookie --noauth_local_webserver                              
appcfg.py update . --no_cookie --noauth_local_webserver                                                        