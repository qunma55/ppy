# 字符模板
import random
import string
import uuid


def boom_str():
    return ''.join(random.sample(string.ascii_letters + string.digits, 8))


def boom_int():
    return random.randint(0, 100000)


f = open('template.txt', 'r')
# 去除所有blank字符
Str = f.read().replace(" ", "").replace("\n", "")
# 判断是否有前缀
PrefixSub = Str.find('$prefix:')
# 命令起始值
command = 0
prefix = ""
if PrefixSub != -1:
    PrefixEndSub = Str.find("*")
    prefix = Str[PrefixSub + len('$prefix:{'):PrefixEndSub - 1]
    # 查找循环体
    LoopSub = Str.find('$loop:')
    if LoopSub != -1:
        LoopEndSub = Str.find("*", LoopSub)
        # 数据量
        LoopNumber = int(Str[LoopSub + len('$loop:'): LoopEndSub])
        # 查找循环体里的内容
        LoopBodySub = Str.find('[', LoopEndSub)
        LoopBodyEndSub = Str.find(']', LoopEndSub)

        formatData = Str[LoopBodySub: LoopBodyEndSub + 1]
        formatBody = formatData[2:-2]
        LoopBody = ''
        for x in list(range(LoopNumber)):
            random.seed(x)
            itemFormatBody = formatBody.replace("$format:str*", "\"" + boom_str() + "\"") \
                .replace("$format:int*", str(boom_int())) \
                .replace("$format:uuid*", "\"" + str(uuid.uuid4()) + "\"")
            itemFormatBody = "{" + itemFormatBody + "},"
            LoopBody += itemFormatBody
        LoopBody = "[" + LoopBody[0:-1] + "]"
        SufStartSub = Str.find("$suffix:{")
        SufEndSub = Str.rfind("*")
        SufStr = Str[SufStartSub + len('$prefix:{'):SufEndSub - 1]
        BoomStr = prefix + LoopBody + SufStr
        print(BoomStr)
