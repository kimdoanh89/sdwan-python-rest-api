echo "1. Generating VE-System template"
sdwancli template feature create system -t '["vedge-cloud"]' -n VE-System-cli -time "Europe/London"
echo "--------------------------------------------------------"
echo "2. Generating VE-Banner template"
sdwancli template feature create banner -t '["vedge-cloud"]' -n VE-Banner-cli
echo "--------------------------------------------------------"
echo "3. Generating VE-BR123-VPN0 template"
sdwancli template feature create vpn -t '["vedge-cloud"]' -n VE-BR123-VPN0-cli -id 0 -d "Transport VPN" -p "0.0.0.0/0" \
-nh '["vpn0_g0_next_hop_ip_address_0", "vpn0_g1_next_hop_ip_address_1", "vpn0_g2_next_hop_ip_address_2"]'
echo "--------------------------------------------------------"
echo "4. Generating  VE-DC12-VPN0 template"
sdwancli template feature create vpn -t '["vedge-cloud"]' -n VE-DC12-VPN0-cli -id 0 -d "Transport VPN" -p "0.0.0.0/0" \
-nh '["vpn0_g0_next_hop_ip_address_0", "vpn0_g1_next_hop_ip_address_1"]'
echo "--------------------------------------------------------"
echo "5. Generating  VE-VPN1 template"
sdwancli template feature create vpn -t '["vedge-cloud"]' -n VE-VPN1-cli -id 1 -d "Data VPN" -nh '[]'
echo "--------------------------------------------------------"
echo "6. Generating  VE-VPN512 template"
sdwancli template feature create vpn -t '["vedge-cloud"]' -n VE-VPN512-cli -id 512 -d "Management VPN" -nh '[]'
echo "--------------------------------------------------------"
echo "7. Generating  VE-VPN512-E0 template"
sdwancli template feature create vpn-int -t '["vedge-cloud"]' -n VE-VPN512-E0-cli -i "eth0"
echo "--------------------------------------------------------"
echo "8. Generating  VE-VPN0-G0 template"
sdwancli template feature create vpn-int -t '["vedge-cloud"]' -n VE-VPN0-G0-cli -i "ge0/0" -d "MPLS" -ip "vpn0_g0_if_ipv4_address" -c "mpls"
echo "--------------------------------------------------------"
echo "9. Generating  VE-VPN0-G1 template"
sdwancli template feature create vpn-int -t '["vedge-cloud"]' -n VE-VPN0-G1-cli -i "ge0/1" -d "Internet" -ip "vpn0_g1_if_ipv4_address" -c "biz-internet"
echo "--------------------------------------------------------"
echo "10. Generating  VE-VPN0-G2 template"
sdwancli template feature create vpn-int -t '["vedge-cloud"]' -n VE-VPN0-G2-cli -i "ge0/2" -d "LTE" -ip "vpn0_g2_if_ipv4_address" -c "lte"
echo "--------------------------------------------------------"