"""温度换算小工具（含有已知缺陷，等待修复）"""

def celsius_to_fahrenheit(c):
    # BUG: 正确的公式是 c * 9/5 + 32，这里写错了
    return c * 9/5

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

if __name__ == "__main__":
    print("0°C =", celsius_to_fahrenheit(0), "°F")  # 应输出 32.0
