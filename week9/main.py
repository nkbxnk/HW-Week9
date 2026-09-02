# -*- coding: utf-8 -*-
"""
โปรแกรม GUI รวมคะแนนและตัดเกรด นักศึกษาวิชาเบสิกคอมพิวเตอร์ จำนวน 20 คน
คะแนนที่ใช้ = คะแนนสอบกลางภาค (Midterm) + คะแนนสอบปลายภาค (Final)
เกณฑ์การตัดเกรด (คะแนนเต็ม 100):
    80-100  -> A
    75-79   -> B+
    70-74   -> B
    65-69   -> C+
    60-64   -> C
    55-59   -> D+
    50-54   -> D
    0-49    -> F
"""

import tkinter as tk
from tkinter import ttk, messagebox

NUM_STUDENTS = 20


def calculate_grade(total: float) -> str:
    """คืนค่าเกรดตามคะแนนรวม (เต็ม 100)"""
    if total >= 80:
        return "A"
    elif total >= 75:
        return "B+"
    elif total >= 70:
        return "B"
    elif total >= 65:
        return "C+"
    elif total >= 60:
        return "C"
    elif total >= 55:
        return "D+"
    elif total >= 50:
        return "D"
    else:
        return "F"


class GradeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("โปรแกรมรวมคะแนนและตัดเกรด วิชาเบสิกคอมพิวเตอร์ (20 คน)")
        self.geometry("820x680")
        self.resizable(False, False)

        # เก็บ Entry / Label widget ของแต่ละแถว
        self.name_entries = []
        self.midterm_entries = []
        self.final_entries = []
        self.total_labels = []
        self.grade_labels = []

        self._build_header()
        self._build_table()
        self._build_footer()

    # ---------------------------------------------------------
    def _build_header(self):
        title = tk.Label(
            self,
            text="รวมคะแนนและตัดเกรด นักศึกษาวิชาเบสิกคอมพิวเตอร์",
            font=("TH Sarabun New", 20, "bold"),
        )
        title.pack(pady=(10, 0))

        subtitle = tk.Label(
            self,
            text="คะแนนที่ใช้ตัดเกรด = คะแนนสอบกลางภาค (Midterm) + คะแนนสอบปลายภาค (Final) เต็ม 100 คะแนน",
            font=("TH Sarabun New", 14),
            fg="#444444",
        )
        subtitle.pack(pady=(0, 10))

    # ---------------------------------------------------------
    def _build_table(self):
        container = tk.Frame(self)
        container.pack(fill="both", expand=True, padx=15)

        # ---- Scrollable area ----
        canvas = tk.Canvas(container, borderwidth=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
        )
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # ---- Table header ----
        headers = ["ลำดับ", "ชื่อ-สกุล", "มิดเทอม (50)", "ไฟนอล (50)", "รวม (100)", "เกรด"]
        widths = [6, 26, 12, 12, 10, 8]
        for col, (text, w) in enumerate(zip(headers, widths)):
            lbl = tk.Label(
                scroll_frame,
                text=text,
                font=("TH Sarabun New", 13, "bold"),
                width=w,
                relief="ridge",
                bg="#dceeff",
            )
            lbl.grid(row=0, column=col, sticky="nsew", padx=1, pady=1)

        # ---- Rows for 20 students ----
        for i in range(NUM_STUDENTS):
            row = i + 1

            no_lbl = tk.Label(scroll_frame, text=str(row), width=6, relief="ridge")
            no_lbl.grid(row=row, column=0, sticky="nsew", padx=1, pady=1)

            name_entry = tk.Entry(scroll_frame, width=26, justify="left")
            name_entry.insert(0, f"นักศึกษาคนที่ {row}")
            name_entry.grid(row=row, column=1, sticky="nsew", padx=1, pady=1)
            self.name_entries.append(name_entry)

            mid_entry = tk.Entry(scroll_frame, width=12, justify="center")
            mid_entry.grid(row=row, column=2, sticky="nsew", padx=1, pady=1)
            self.midterm_entries.append(mid_entry)

            final_entry = tk.Entry(scroll_frame, width=12, justify="center")
            final_entry.grid(row=row, column=3, sticky="nsew", padx=1, pady=1)
            self.final_entries.append(final_entry)

            total_lbl = tk.Label(scroll_frame, text="-", width=10, relief="ridge", bg="#f5f5f5")
            total_lbl.grid(row=row, column=4, sticky="nsew", padx=1, pady=1)
            self.total_labels.append(total_lbl)

            grade_lbl = tk.Label(scroll_frame, text="-", width=8, relief="ridge", bg="#f5f5f5")
            grade_lbl.grid(row=row, column=5, sticky="nsew", padx=1, pady=1)
            self.grade_labels.append(grade_lbl)

    # ---------------------------------------------------------
    def _build_footer(self):
        footer = tk.Frame(self)
        footer.pack(fill="x", pady=10)

        calc_btn = tk.Button(
            footer,
            text="คำนวณคะแนนและตัดเกรด",
            font=("TH Sarabun New", 13, "bold"),
            bg="#4CAF50",
            fg="white",
            command=self.calculate_all,
        )
        calc_btn.pack(side="left", padx=15)

        clear_btn = tk.Button(
            footer,
            text="ล้างคะแนน",
            font=("TH Sarabun New", 13),
            bg="#f44336",
            fg="white",
            command=self.clear_all,
        )
        clear_btn.pack(side="left", padx=5)

        self.summary_label = tk.Label(
            footer,
            text="",
            font=("TH Sarabun New", 13),
            fg="#003366",
        )
        self.summary_label.pack(side="left", padx=20)

    # ---------------------------------------------------------
    def calculate_all(self):
        grade_count = {"A": 0, "B+": 0, "B": 0, "C+": 0, "C": 0, "D+": 0, "D": 0, "F": 0}
        total_sum = 0
        valid_count = 0

        for i in range(NUM_STUDENTS):
            mid_text = self.midterm_entries[i].get().strip()
            final_text = self.final_entries[i].get().strip()

            # ถ้าทั้งสองช่องว่าง ให้ข้ามแถวนี้ (ยังไม่กรอกข้อมูล)
            if mid_text == "" and final_text == "":
                self.total_labels[i].config(text="-")
                self.grade_labels[i].config(text="-", bg="#f5f5f5")
                continue

            try:
                mid = float(mid_text) if mid_text != "" else 0.0
                final = float(final_text) if final_text != "" else 0.0
            except ValueError:
                messagebox.showerror(
                    "ข้อมูลไม่ถูกต้อง",
                    f"กรุณากรอกคะแนนเป็นตัวเลขเท่านั้น (แถวที่ {i + 1})",
                )
                return

            if not (0 <= mid <= 50) or not (0 <= final <= 50):
                messagebox.showerror(
                    "คะแนนเกินขอบเขต",
                    f"คะแนนแต่ละส่วนต้องอยู่ระหว่าง 0-50 (แถวที่ {i + 1})",
                )
                return

            total = mid + final
            grade = calculate_grade(total)

            self.total_labels[i].config(text=f"{total:.2f}")
            self.grade_labels[i].config(text=grade, bg=self._grade_color(grade))

            grade_count[grade] += 1
            total_sum += total
            valid_count += 1

        if valid_count == 0:
            self.summary_label.config(text="ยังไม่มีการกรอกคะแนน")
            return

        avg = total_sum / valid_count
        summary_text = f"จำนวนที่กรอกครบ: {valid_count}/{NUM_STUDENTS} คน | คะแนนเฉลี่ย: {avg:.2f}  |  " + \
            "  ".join(f"{g}:{c}" for g, c in grade_count.items() if c > 0)
        self.summary_label.config(text=summary_text)

    # ---------------------------------------------------------
    @staticmethod
    def _grade_color(grade: str) -> str:
        colors = {
            "A": "#c8f7c5",
            "B+": "#d9f2c4",
            "B": "#eaf7c4",
            "C+": "#fff2b3",
            "C": "#ffe0b3",
            "D+": "#ffc9b3",
            "D": "#ffb3b3",
            "F": "#ff8080",
        }
        return colors.get(grade, "#f5f5f5")

    # ---------------------------------------------------------
    def clear_all(self):
        for i in range(NUM_STUDENTS):
            self.midterm_entries[i].delete(0, tk.END)
            self.final_entries[i].delete(0, tk.END)
            self.total_labels[i].config(text="-")
            self.grade_labels[i].config(text="-", bg="#f5f5f5")
        self.summary_label.config(text="")


if __name__ == "__main__":
    app = GradeApp()
    app.mainloop()