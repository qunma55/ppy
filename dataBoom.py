# 字符模板
Str = "$prefix:{pre}*$loop:1000*[{\"value0\": $format:str*,\"value1\": $format:int*,\"value2\": " \
      "$format:uuid*}]$suffix:{suf}*"

Str.strip()

JsonStr = ""
# 判断是否有前缀
PrefixSub = Str.find('$prefix:')
# 命令起始值
command = 0
prefix = ""
if PrefixSub != -1:
    command += 1
    print("==开始生成前缀")
    PrefixEndSub = Str.find("*")
    prefix = Str[PrefixSub + len('$prefix:{'):PrefixEndSub - 1]

# 查找循环体
LoopSub = Str.find('$loop:')

LoopNumber = Str[LoopSub + len('$loop:'):]
