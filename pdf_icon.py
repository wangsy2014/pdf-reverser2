from PIL import Image, ImageDraw

def create_icon():
    # 创建一个 48x48 的图像，使用 RGBA 模式支持透明度
    size = 48
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 绘制圆形背景
    margin = 2
    draw.ellipse([margin, margin, size-margin, size-margin], fill='#2B2B2B')
    
    # 绘制 "PDF" 文字
    text_color = '#FFFFFF'
    draw.text((10, 15), "PDF", fill=text_color, font=None)
    
    # 绘制箭头
    arrow_color = '#FF6B6B'
    points = [(35, 20), (40, 25), (35, 30)]  # 箭头坐标
    draw.line(points, fill=arrow_color, width=2)
    
    # 保存为 PNG 文件
    try:
        img.save('pdf_reverser.png', 'PNG')
        print("图标文件创建成功！")
        return True
    except Exception as e:
        print(f"创建图标文件时出错: {str(e)}")
        return False

if __name__ == "__main__":
    create_icon() 