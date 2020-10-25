echo "Generating VE-System template"
sdwancli template feature create system -t '["vedge-cloud"]' -n VE-System2 -time "Europe/London"
echo "--------------------------------------------------------"
echo "Generating VE-Banner template"
sdwancli template feature create banner -t '["vedge-cloud"]' -n VE-Banner2
echo "--------------------------------------------------------"
echo "Generating VPN-Banner template"
sdwancli template feature create vpn -t '["vedge-cloud"]' -n VE-BR123-VPN0 -id 0
echo "--------------------------------------------------------"