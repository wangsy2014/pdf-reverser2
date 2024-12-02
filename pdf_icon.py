from PIL import Image
import os

def create_simple_icon():
    # 创建一个 48x48 的图像
    img = Image.new('RGB', (48, 48), color='white')
    
    # 创建一个简单的红色边框
    for x in range(48):
        for y in range(48):
            # 创建边框
            if x < 3 or x > 44 or y < 3 or y > 44:
                img.putpixel((x, y), (220, 20, 60))  # 红色边框
            # 创建 "PDF" 文字效果
            if 15 <= y <= 35:
                if 10 <= x <= 15:  # P的竖线
                    img.putpixel((x, y), (0, 0, 0))
                if y in [15, 25] and 10 <= x <= 20:  # P的横线
                    img.putpixel((x, y), (0, 0, 0))
                if 25 <= x <= 30:  # D的竖线
                    img.putpixel((x, y), (0, 0, 0))
                if y in [15, 35] and 25 <= x <= 35:  # D的横线
                    img.putpixel((x, y), (0, 0, 0))

    # 保存为 ICO 文件
    try:
        img.save('pdf_reverser.ico', format='ICO', sizes=[(48, 48)])
        print("图标文件创建成功！")
    except Exception as e:
        print(f"创建图标文件时出错: {str(e)}")
        # 如果无法创建 ICO 文件，尝试保存为 PNG
        try:
            img.save('pdf_reverser.png', format='PNG')
            print("已创建 PNG 格式的图标文件")
            # 更新打包配置中的图标路径
            update_icon_in_configs()
        except Exception as e:
            print(f"创建 PNG 文件也失败: {str(e)}")

def update_icon_in_configs():
    """更新其他配置文件中的图标路径"""
    # 更新 build_config.py
    if os.path.exists('build_config.py'):
        with open('build_config.py', 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('pdf_reverser.ico', 'pdf_reverser.png')
        with open('build_config.py', 'w', encoding='utf-8') as f:
            f.write(content)
    
    # 更新 create_installer.py
    if os.path.exists('create_installer.py'):
        with open('create_installer.py', 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('pdf_reverser.ico', 'pdf_reverser.png')
        with open('create_installer.py', 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    create_simple_icon() 