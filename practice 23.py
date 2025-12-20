import re

def mask_privacy(text):
    # 手机号规则：1开头，第二位是3-9，后面跟9位数字
    phone_pattern = re.compile(r'1[3-9]\d{9}')
    
    # 身份证规则：简单的18位数字匹配（为了简单，不考虑X）
    id_pattern = re.compile(r'\d{17}[\dXx]')

    # 1. 手机号打码：保留前3位和后4位，中间用****代替
    # \g<1> 代表第一个括号里的内容
    text = phone_pattern.sub(r'\g<1>****\g<2>', text)
    
    # 2. 身份证打码：保留前3位和后4位，中间用*代替
    text = id_pattern.sub(r'\g<1>*********\g<2>', text)
    
    return text

# === 第三步：实战演练 ===
if __name__ == '__main__':
    raw_text = """
    王哥，我的手机号 13987654321，身份证 110101199001011234，明天发红包给你。
    李姐的号码是 13511112222，别搞错了。
    """
    
    result = mask_privacy(raw_text)
    print(result)
