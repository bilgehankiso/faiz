#!/bin/bash
# Basit Faiz Hesaplama Scripti

echo "Ana para miktarını girin: "
read principal
echo "Faiz oranını girin (%): "
read rate
echo "Zaman dilimini girin (yıl): "
read time

# Basit faiz formülü: faiz = ana_para * oran * zaman / 100
interest=$(echo "scale=2; $principal * $rate * $time / 100" | bc)
total=$(echo "scale=2; $principal + $interest" | bc)

echo "-----------------------------"
echo "Hesaplanan Faiz: $interest TL"
echo "Toplam Tutar: $total TL"
echo "-----------------------------"
