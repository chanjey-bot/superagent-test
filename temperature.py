"""温度换算小工具（已修复华氏换算公式，并加入 assert 自检）"""

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

if __name__ == "__main__":
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert celsius_to_fahrenheit(-40) == -40.0
    print("0°C =", celsius_to_fahrenheit(0), "°F")  # 应输出 32.0
