
cpu=$(cat /sys/class/thermal/thermal_zone0/temp | sed 's/\(.\)..$/.\1°C/')
echo "CPU : $cpu"
