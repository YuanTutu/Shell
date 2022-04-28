#!/bin/bash
# 三种都可以
 grep -n '^\s*$' nowcoder.txt
 awk '/^\s*$/{print NR}' nowcoder.txt
 sed -n '/^\s*$/=' nowcoder.txt
