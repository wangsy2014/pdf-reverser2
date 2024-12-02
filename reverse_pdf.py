from PyPDF2 import PdfReader, PdfWriter
import os

def reverse_pdf_pages(input_path, output_path):
    try:
        # 创建PDF读取器对象
        pdf_reader = PdfReader(input_path)
        
        # 创建PDF写入器对象
        pdf_writer = PdfWriter()
        
        # 获取PDF总页数
        total_pages = len(pdf_reader.pages)
        
        # 从后往前遍历页面并添加到新的PDF中
        for page_num in range(total_pages - 1, -1, -1):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
        
        # 将反转后的页面写入新的PDF文件
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)
            
        print(f"PDF页面反转成功！新文件保存为: {output_path}")
        
    except Exception as e:
        print(f"处理PDF时发生错误: {str(e)}")

def main():
    # 获取用户输入
    input_pdf = input("请输入源PDF文件路径: ")
    
    # 生成输出文件名
    filename, ext = os.path.splitext(input_pdf)
    output_pdf = f"{filename}_reversed{ext}"
    
    # 检查输入文件是否存在
    if not os.path.exists(input_pdf):
        print("错误：输入文件不存在！")
        return
    
    # 执行PDF页面反转
    reverse_pdf_pages(input_pdf, output_pdf)

if __name__ == "__main__":
    main() 