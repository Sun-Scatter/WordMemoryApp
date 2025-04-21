import json
import os
import random
from tkinter import Tk, Label, Button, Entry, StringVar, messagebox, Frame

class WordMemoryApp:
    def __init__(self, master):
        self.master = master
        master.title("单词记忆应用")
        
        # 初始化变量
        self.words = []
        self.current_word = {}
        self.score = 0
        self.total_attempts = 0
        
        # 创建UI元素
        self.create_widgets()
        self.load_words()
        self.next_word()
        
    def create_widgets(self):
        """创建应用界面"""
        # 顶部框架
        top_frame = Frame(self.master)
        top_frame.pack(pady=10)
        
        # 单词显示
        self.word_label = Label(top_frame, text="", font=("Arial", 24))
        self.word_label.pack()
        
        # 翻译输入
        self.answer_var = StringVar()
        self.answer_entry = Entry(self.master, textvariable=self.answer_var, font=("Arial", 16))
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", self.check_answer)
        
        # 底部按钮
        bottom_frame = Frame(self.master)
        bottom_frame.pack(pady=10)
        
        self.check_btn = Button(bottom_frame, text="检查", command=self.check_answer)
        self.check_btn.pack(side="left", padx=5)
        
        self.next_btn = Button(bottom_frame, text="跳过", command=self.next_word)
        self.next_btn.pack(side="left", padx=5)
        
        self.score_label = Label(self.master, text="得分: 0/0", font=("Arial", 12))
        self.score_label.pack(pady=5)
        
    def load_words(self):
        """加载单词数据"""
        if os.path.exists("words.json"):
            with open("words.json", "r", encoding="utf-8") as f:
                self.words = json.load(f)
        else:
            # 默认单词库
            self.words = [
                {"word": "apple", "translation": "苹果"},
                {"word": "banana", "translation": "香蕉"},
                {"word": "computer", "translation": "电脑"},
                {"word": "hello", "translation": "你好"},
                {"word": "thank you", "translation": "谢谢"}
            ]
            self.save_words()
    
    def save_words(self):
        """保存单词数据"""
        with open("words.json", "w", encoding="utf-8") as f:
            json.dump(self.words, f, ensure_ascii=False, indent=2)
    
    def next_word(self):
        """显示下一个单词"""
        if not self.words:
            messagebox.showinfo("提示", "单词库为空!")
            return
            
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word["word"])
        self.answer_var.set("")
        self.answer_entry.focus()
    
    def check_answer(self, event=None):
        """检查答案"""
        user_answer = self.answer_var.get().strip()
        correct_answer = self.current_word["translation"]
        
        self.total_attempts += 1
        
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            messagebox.showinfo("正确", f"✓ 正确!\n{self.current_word['word']} = {correct_answer}")
        else:
            messagebox.showerror("错误", f"✗ 错误!\n{self.current_word['word']} = {correct_answer}")
        
        self.update_score()
        self.next_word()
    
    def update_score(self):
        """更新分数显示"""
        self.score_label.config(text=f"得分: {self.score}/{self.total_attempts}")

if __name__ == "__main__":
    root = Tk()
    app = WordMemoryApp(root)
    root.mainloop()