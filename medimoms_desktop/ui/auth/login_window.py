"""
Login Window for MediMoms Desktop Application
Modern professional login interface using CustomTkinter
"""

import customtkinter as ctk
from tkinter import messagebox
from services.auth_service import authenticate_user
from config import COLORS

class LoginWindow(ctk.CTkFrame):
    def __init__(self, parent, on_login_success, on_show_register):
        super().__init__(parent, fg_color="transparent")
        
        self.parent = parent
        self.on_login_success = on_login_success
        self.on_show_register = on_show_register
        self.password_visible = False
        
        self.pack(fill="both", expand=True)
        self.create_widgets()
    
    def create_widgets(self):
        """Create modern login form widgets"""
        
        # Main container with gradient background
        main_frame = ctk.CTkFrame(
            self, 
            fg_color=("#ECFDF5", "#ECFDF5"),
            corner_radius=0
        )
        main_frame.pack(fill="both", expand=True)
        
        # Center container
        center_container = ctk.CTkFrame(
            main_frame,
            fg_color="transparent"
        )
        center_container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Login card
        login_card = ctk.CTkFrame(
            center_container,
            fg_color="white",
            corner_radius=24,
            width=480,
        )
        login_card.pack(padx=40, pady=40)
        
        # Content frame inside card
        content_frame = ctk.CTkFrame(
            login_card,
            fg_color="transparent"
        )
        content_frame.pack(fill="both", expand=True, padx=50, pady=40)
        
        # Logo/Icon
        logo_frame = ctk.CTkFrame(
            content_frame,
            fg_color="#D1FAE5",
            corner_radius=20,
            width=80,
            height=80
        )
        logo_frame.pack(pady=(0, 20))
        logo_frame.pack_propagate(False)
        
        logo_icon = ctk.CTkLabel(
            logo_frame,
            text="🏥",
            font=("Segoe UI", 40)
        )
        logo_icon.place(relx=0.5, rely=0.5, anchor="center")
        
        # Title
        title_label = ctk.CTkLabel(
            content_frame,
            text="Welcome Back",
            font=("Segoe UI", 32, "bold"),
            text_color="#0F172A"
        )
        title_label.pack(pady=(0, 8))
        
        # Subtitle
        subtitle_label = ctk.CTkLabel(
            content_frame,
            text="MediMoms Healthcare System",
            font=("Segoe UI", 14),
            text_color="#64748B"
        )
        subtitle_label.pack(pady=(0, 40))
        
        # Username field
        username_label = ctk.CTkLabel(
            content_frame,
            text="Username or Email",
            font=("Segoe UI", 13, "bold"),
            text_color="#0F172A",
            anchor="w"
        )
        username_label.pack(fill="x", pady=(0, 8))
        
        self.username_entry = ctk.CTkEntry(
            content_frame,
            height=50,
            font=("Segoe UI", 14),
            placeholder_text="Enter your username or email",
            border_width=2,
            corner_radius=12,
            border_color="#E2E8F0",
            fg_color="white",
            text_color="#0F172A",
            placeholder_text_color="#94A3B8"
        )
        self.username_entry.pack(fill="x", pady=(0, 20))
        
        # Password field
        password_label = ctk.CTkLabel(
            content_frame,
            text="Password",
            font=("Segoe UI", 13, "bold"),
            text_color="#0F172A",
            anchor="w"
        )
        password_label.pack(fill="x", pady=(0, 8))
        
        password_container = ctk.CTkFrame(
            content_frame,
            fg_color="transparent"
        )
        password_container.pack(fill="x", pady=(0, 15))
        
        self.password_entry = ctk.CTkEntry(
            password_container,
            height=50,
            font=("Segoe UI", 14),
            placeholder_text="Enter your password",
            show="●",
            border_width=2,
            corner_radius=12,
            border_color="#E2E8F0",
            fg_color="white",
            text_color="#0F172A",
            placeholder_text_color="#94A3B8"
        )
        self.password_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        self.show_password_btn = ctk.CTkButton(
            password_container,
            text="👁",
            width=50,
            height=50,
            font=("Segoe UI", 18),
            fg_color="#F1F5F9",
            hover_color="#E2E8F0",
            text_color="#64748B",
            corner_radius=12,
            command=self.toggle_password_visibility
        )
        self.show_password_btn.pack(side="left")
        
        # Remember me & Forgot password
        options_frame = ctk.CTkFrame(
            content_frame,
            fg_color="transparent"
        )
        options_frame.pack(fill="x", pady=(0, 30))
        
        self.remember_var = ctk.BooleanVar(value=False)
        remember_checkbox = ctk.CTkCheckBox(
            options_frame,
            text="Remember me",
            variable=self.remember_var,
            font=("Segoe UI", 12),
            text_color="#475569",
            fg_color="#10B981",
            hover_color="#059669",
            border_color="#CBD5E1",
            corner_radius=6
        )
        remember_checkbox.pack(side="left")
        
        forgot_btn = ctk.CTkButton(
            options_frame,
            text="Forgot password?",
            font=("Segoe UI", 12, "bold"),
            fg_color="transparent",
            text_color="#10B981",
            hover_color="#ECFDF5",
            width=130,
            command=self.show_forgot_password
        )
        forgot_btn.pack(side="right")
        
        # Login button
        self.login_btn = ctk.CTkButton(
            content_frame,
            text="🚀  Sign In",
            height=54,
            font=("Segoe UI", 15, "bold"),
            fg_color="#10B981",
            hover_color="#059669",
            corner_radius=12,
            command=self.handle_login
        )
        self.login_btn.pack(fill="x", pady=(0, 20))
        
        # Divider
        divider_frame = ctk.CTkFrame(
            content_frame,
            fg_color="transparent"
        )
        divider_frame.pack(fill="x", pady=(0, 20))
        
        ctk.CTkFrame(
            divider_frame,
            fg_color="#CBD5E1",
            height=1
        ).pack(side="left", fill="x", expand=True, padx=(0, 12))
        
        ctk.CTkLabel(
            divider_frame,
            text="New here?",
            font=("Segoe UI", 11),
            text_color="#64748B"
        ).pack(side="left")
        
        ctk.CTkFrame(
            divider_frame,
            fg_color="#CBD5E1",
            height=1
        ).pack(side="left", fill="x", expand=True, padx=(12, 0))
        
        # Register button
        register_btn = ctk.CTkButton(
            content_frame,
            text="✍️  Register as Midwife",
            height=54,
            font=("Segoe UI", 14, "bold"),
            fg_color="white",
            hover_color="#F8FAFC",
            text_color="#10B981",
            border_width=2,
            border_color="#10B981",
            corner_radius=12,
            command=self.on_show_register
        )
        register_btn.pack(fill="x")
        
        # Bind Enter key
        self.username_entry.bind("<Return>", lambda e: self.password_entry.focus())
        self.password_entry.bind("<Return>", lambda e: self.handle_login())
        
        # Focus on username
        self.username_entry.focus()
    
    def toggle_password_visibility(self):
        """Toggle password visibility"""
        self.password_visible = not self.password_visible
        if self.password_visible:
            self.password_entry.configure(show="")
            self.show_password_btn.configure(text="🙈")
        else:
            self.password_entry.configure(show="●")
            self.show_password_btn.configure(text="👁")
    
    def handle_login(self):
        """Handle login button click"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        # Validation
        if not username:
            messagebox.showerror("Validation Error", "Please enter your username or email")
            self.username_entry.focus()
            return
        
        if not password:
            messagebox.showerror("Validation Error", "Please enter your password")
            self.password_entry.focus()
            return
        
        # Disable login button during authentication
        self.login_btn.configure(state="disabled", text="Signing in...")
        self.update()
        
        # Authenticate
        success, result = authenticate_user(username, password)
        
        if success:
            messagebox.showinfo("Success", f"Welcome back, {result['full_name']}!")
            self.on_login_success(result)
        else:
            messagebox.showerror("Login Failed", result)
            self.login_btn.configure(state="normal", text="Sign In")
            self.password_entry.delete(0, 'end')
            self.password_entry.focus()
    
    def show_forgot_password(self):
        """Show forgot password dialog"""
        messagebox.showinfo(
            "Forgot Password",
            "Please contact your administrator to reset your password.\n\n"
            "Email: admin@medimoms.com"
        )
    

