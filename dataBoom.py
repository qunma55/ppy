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
    print("开始生成前缀")
    PrefixEndSub = Str.find("*")
    prefix = Str[PrefixSub + len('$prefix:{'):PrefixEndSub - 1]

    # 查找循环体
    LoopSub = Str.find('$loop:')
    if LoopSub != -1:
        LoopEndSub = Str.find("*", LoopSub)
        # 数据量
        LoopNumber = Str[LoopSub + len('$loop:'): LoopEndSub]

        # 查找循环体里的内容
        LoopBodySub = Str.find('[', LoopEndSub)
        LoopBodyEndSub = Str.find(']', LoopEndSub)

        formatData = Str[LoopBodySub: LoopBodyEndSub + 1]
        List = formatData[2:-2].split(',')
        for item in List:
            m = item.find('\"')
            n = item.find('\":')
            KeyText = item[m + 1: n]
            k = item.find('$')
            j = item.find('*')
            valueText = item[k + 1: j]
            if valueText.find('format:') != -1:
                FormatStr = valueText.split(":")[1]
                if FormatStr == 'str':
                    print('字符串')
                if FormatStr == 'int':
                    print('数字')
                if FormatStr == 'uuid':
                    print('随机数')
