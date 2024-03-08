#!/bin/bash

# 读取trackers.txt文件每一行作为Tracker地址
while IFS= read -r tracker; do
    trackers="$trackers,$tracker"
done < trackers_best.txt

# 删除第一个多余的逗号
trackers=${trackers#,}

# 构造aria2c命令
aria2c_command="aria2c --bt-tracker=$trackers magnet:?xt=urn:btih:C168B7AD1413C99338EAEFA9C1A0E781F27D3072"

# 执行aria2c命令
eval $aria2c_command