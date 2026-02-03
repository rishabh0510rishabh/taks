import customtkinter as ctk
import numpy as np
from tkinter import messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MatrixToolApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Matrix Operations Tool")
        self.geometry("900x700")

        # Layout Configuration
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(6, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar, text="Matrix OPs", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.op_var = ctk.StringVar(value="Add")
        operations = ["Add", "Subtract", "Multiply", "Transpose", "Determinant"]
        
        for i, op in enumerate(operations):
            btn = ctk.CTkRadioButton(self.sidebar, text=op, variable=self.op_var, value=op, command=self.update_ui)
            btn.grid(row=i+1, column=0, pady=10, padx=20, sticky="w")

        # Main Area
        self.main_frame = ctk.CTkScrollableFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        self.header = ctk.CTkLabel(self.main_frame, text="Matrix Addition", font=ctk.CTkFont(size=24, weight="bold"))
        self.header.pack(pady=20)

        # Input Frames Container
        self.inputs_container = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.inputs_container.pack(fill="x", padx=20)

        # Matrix Inputs (Will be dynamic)
        self.matrix_a_frame = None
        self.matrix_b_frame = None
        
        # Dimension Controls
        self.dims_frame = ctk.CTkFrame(self.main_frame)
        self.dims_frame.pack(pady=10, fill="x", padx=20)
        
        self.create_dimension_controls()
        
        # Generate Button
        self.gen_btn = ctk.CTkButton(self.main_frame, text="Generate Matrices", command=self.generate_matrices)
        self.gen_btn.pack(pady=10)

        # Calculate Button
        self.calc_btn = ctk.CTkButton(self.main_frame, text="Calculate Result", command=self.calculate, fg_color="green", hover_color="darkgreen")
        self.calc_btn.pack(pady=20)

        # Result Area
        self.result_label = ctk.CTkLabel(self.main_frame, text="Result:", font=ctk.CTkFont(size=18, weight="bold"))
        self.result_label.pack()
        
        self.result_text = ctk.CTkTextbox(self.main_frame, height=150, width=400)
        self.result_text.pack(pady=10)

        self.update_ui()

    def create_dimension_controls(self):
        # Matrix A Dimensions
        self.lbl_a = ctk.CTkLabel(self.dims_frame, text="Matrix A (RxC):")
        self.lbl_a.grid(row=0, column=0, padx=10, pady=10)
        self.rows_a = ctk.CTkEntry(self.dims_frame, width=50)
        self.rows_a.grid(row=0, column=1, padx=5)
        self.rows_a.insert(0, "2")
        self.cols_a = ctk.CTkEntry(self.dims_frame, width=50)
        self.cols_a.grid(row=0, column=2, padx=5)
        self.cols_a.insert(0, "2")

        # Matrix B Dimensions
        self.lbl_b = ctk.CTkLabel(self.dims_frame, text="Matrix B (RxC):")
        self.lbl_b.grid(row=0, column=3, padx=10, pady=10)
        self.rows_b = ctk.CTkEntry(self.dims_frame, width=50)
        self.rows_b.grid(row=0, column=4, padx=5)
        self.rows_b.insert(0, "2")
        self.cols_b = ctk.CTkEntry(self.dims_frame, width=50)
        self.cols_b.grid(row=0, column=5, padx=5)
        self.cols_b.insert(0, "2")

    def update_ui(self):
        op = self.op_var.get()
        self.header.configure(text=f"Matrix {op}")
        
        # Toggle Matrix B visibility
        if op in ["Transpose", "Determinant"]:
            self.lbl_b.grid_remove()
            self.rows_b.grid_remove()
            self.cols_b.grid_remove()
        else:
            self.lbl_b.grid()
            self.rows_b.grid()
            self.cols_b.grid()

    def generate_matrices(self):
        # Clear existing
        if self.matrix_a_frame: self.matrix_a_frame.destroy()
        if self.matrix_b_frame: self.matrix_b_frame.destroy()

        try:
            r1 = int(self.rows_a.get())
            c1 = int(self.cols_a.get())
            
            self.matrix_a_entries = self.create_matrix_grid("Matrix A", r1, c1)
            
            op = self.op_var.get()
            if op not in ["Transpose", "Determinant"]:
                r2 = int(self.rows_b.get())
                c2 = int(self.cols_b.get())
                self.matrix_b_entries = self.create_matrix_grid("Matrix B", r2, c2)

        except ValueError:
            messagebox.showerror("Error", "Invalid Dimensions")

    def create_matrix_grid(self, title, rows, cols):
        frame = ctk.CTkFrame(self.inputs_container)
        frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        ctk.CTkLabel(frame, text=title, font=("Arial", 14, "bold")).pack(pady=5)
        
        grid_frame = ctk.CTkFrame(frame, fg_color="transparent")
        grid_frame.pack()
        
        entries = []
        for r in range(rows):
            row_entries = []
            for c in range(cols):
                e = ctk.CTkEntry(grid_frame, width=40)
                e.grid(row=r, column=c, padx=2, pady=2)
                e.insert(0, "0")
                row_entries.append(e)
            entries.append(row_entries)
        
        # Store frame reference to destroy later
        if title == "Matrix A": self.matrix_a_frame = frame
        else: self.matrix_b_frame = frame
            
        return entries

    def get_matrix_from_entries(self, entries):
        data = []
        for row in entries:
            data_row = []
            for e in row:
                val = float(e.get())
                data_row.append(val)
            data.append(data_row)
        return np.array(data)

    def calculate(self):
        try:
            op = self.op_var.get()
            
            mat_a = self.get_matrix_from_entries(self.matrix_a_entries)
            
            result = None
            
            if op == "Transpose":
                result = np.transpose(mat_a)
            elif op == "Determinant":
                if mat_a.shape[0] != mat_a.shape[1]:
                    raise ValueError("Determinant requires a square matrix.")
                result = np.linalg.det(mat_a)
            else:
                mat_b = self.get_matrix_from_entries(self.matrix_b_entries)
                if op == "Add":
                    result = np.add(mat_a, mat_b)
                elif op == "Subtract":
                    result = np.subtract(mat_a, mat_b)
                elif op == "Multiply":
                    result = np.dot(mat_a, mat_b)

            # Display Result
            self.result_text.delete("0.0", "end")
            if isinstance(result, np.ndarray):
                # Format neatly
                text = ""
                for row in result:
                    text += "[ " + "  ".join([f"{x:.2f}" for x in row]) + " ]\n"
                self.result_text.insert("0.0", text)
            else:
                self.result_text.insert("0.0", f"{result:.4f}")

        except ValueError as e:
            messagebox.showerror("Math Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = MatrixToolApp()
    app.mainloop()
