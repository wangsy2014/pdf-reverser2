import customtkinter as ctk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
import os

# 设置主题和默认颜色
ctk.set_appearance_mode("dark")  # 模式: dark, light
ctk.set_default_color_theme("blue")  # 主题: blue, dark-blue, green

class PDFReverserGUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("PDF页面顺序反转工具")
        self.root.geometry("800x500")
        
        # 创建主框架
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # 标题标签
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="PDF页面顺序反转工具",
            font=ctk.CTkFont(size=24, weight="bold"),
        )
        self.title_label.pack(pady=30)
        
        # 说明文本
        self.info_label = ctk.CTkLabel(
            self.main_frame,
            text="选择一个PDF文件，将其页面顺序反转",
            font=ctk.CTkFont(size=14),
        )
        self.info_label.pack(pady=10)
        
        # 文件选择框架
        self.file_frame = ctk.CTkFrame(self.main_frame)
        self.file_frame.pack(fill="x", padx=30, pady=20)
        
        # 文件路径输入框
        self.file_entry = ctk.CTkEntry(
            self.file_frame,
            placeholder_text="选择PDF文件...",
            width=500,
            height=40,
        )
        self.file_entry.pack(side="left", padx=(0, 10))
        
        # 浏览按钮
        self.browse_button = ctk.CTkButton(
            self.file_frame,
            text="浏览",
            width=100,
            height=40,
            command=self.browse_file,
            font=ctk.CTkFont(size=14),
        )
        self.browse_button.pack(side="left")
        
        # 进度条
        self.progress_bar = ctk.CTkProgressBar(
            self.main_frame,
            width=600,
        )
        self.progress_bar.pack(pady=20)
        self.progress_bar.set(0)
        
        # 转换按钮
        self.convert_button = ctk.CTkButton(
            self.main_frame,
            text="开始转换",
            width=200,
            height=50,
            command=self.reverse_pdf,
            font=ctk.CTkFont(size=16),
        )
        self.convert_button.pack(pady=20)
        
        # 状态标签
        self.status_label = ctk.CTkLabel(
            self.main_frame,
            text="",
            font=ctk.CTkFont(size=14),
        )
        self.status_label.pack(pady=10)

    def browse_file(self):
        filename = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")]
        )
        if filename:
            self.file_entry.delete(0, "end")
            self.file_entry.insert(0, filename)

    def reverse_pdf(self):
        input_path = self.file_entry.get()
        
        if not input_path:
            messagebox.showerror("错误", "请先选择PDF文件！")
            return
            
        if not os.path.exists(input_path):
            messagebox.showerror("错误", "所选文件不存在！")
            return
            
        try:
            # 重置进度条
            self.progress_bar.set(0)
            self.status_label.configure(text="正在处理中...")
            self.root.update()
            
            # 生成输出文件名
            filename, ext = os.path.splitext(input_path)
            output_path = f"{filename}_reversed{ext}"
            
            # 创建PDF读取器对象
            pdf_reader = PdfReader(input_path)
            pdf_writer = PdfWriter()
            
            # 获取总页数
            total_pages = len(pdf_reader.pages)
            
            # 从后往前遍历页面
            for i, page_num in enumerate(range(total_pages - 1, -1, -1)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
                
                # 更新进度条
                progress = (i + 1) / total_pages
                self.progress_bar.set(progress)
                self.root.update()
            
            # 保存新文件
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
            
            self.status_label.configure(
                text=f"转换成功！新文件已保存为：\n{output_path}",
                text_color=("green", "lightgreen")
            )
            self.progress_bar.set(1)
            messagebox.showinfo("成功", "PDF页面反转完成！")
            
        except Exception as e:
            self.status_label.configure(
                text=f"转换失败：{str(e)}",
                text_color=("red", "pink")
            )
            messagebox.showerror("错误", f"处理PDF时发生错误：{str(e)}")

def main():
    app = PDFReverserGUI()
    app.root.mainloop()

if __name__ == "__main__":
    main() 