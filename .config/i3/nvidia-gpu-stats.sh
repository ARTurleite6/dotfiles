#!/usr/bin/env bash
while :; do
    nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits \
        | head -n1 > /tmp/gpu_temp
    nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits \
        | head -n1 > /tmp/gpu_usage
    sleep 2
done

