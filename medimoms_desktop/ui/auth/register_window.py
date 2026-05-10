"""
Registration Window for MediMoms Desktop Application
Ultra modern professional registration interface matching web app design
"""

import customtkinter as ctk
from tkinter import messagebox
from services.registration_service import register_midwife, get_barangay_list
from config import COLORS

class RegisterWindow(ctk.CTkFrame):
    def __init__(self, parent, on_back_to_login):
        super().__init__(parent, fg_color="transparent")
        
        self.parent = parent
        self.on_back_to_login = on_back_to_login
        self.password_visible = False
        self.confirm_password_visible = False
        self.barangays = []
        self.selected_barangays = []
        
        self.pack(fill="both", expand=True)
        self.load_barangays()
        self.create_widgets()
    
    def load_barangays(self):
        """Load barangays from database"""
        self.barangays = get_barangay_list()
    
    def create_widgets(self):
        """Create ultra modern registration form"""
        
        # Main container with gradient background
        main_frame = ctk.CTkFrame(
            self, 
            fg_color=("#ECFDF5", "#ECFDF5"),
            corner_radius=0
        )
        main_frame.pack(fill="both", expand=True)
        
        # Scrollable container
        scroll_frame = ctk.CTkScrollableFrame(
            main_frame,
            fg_color="transparent",
            scrollbar_button_color="#10B981",
            scrollbar_button_hover_color="#059669"
        )
        scroll_frame.pack(fill="both", expand=True, padx=60, pady=40)
        
        # Center container
        center_container = ctk.CTkFrame(
            scroll_frame,
            fg_color="transparent"
        )
        center_container.pack(expand=True)
        
        # Header section
        header_frame = ctk.CTkFrame(
            center_container,
            fg_color="transparent"
        )
        header_frame.pack(pady=(0, 30))
        
        # Icon
        icon_frame = ctk.CTkFrame(
            header_frame,
            fg_color="white",
            corner_radius=24,
            width=90,
            height=90,
            border_width=3,
            border_color="#10B981"
        )
        icon_frame.pack(pady=(0, 15))
        icon_frame.pack_propagate(False)
        
        icon_label = ctk.CTkLabel(
            icon_frame,
            text="✨",
            font=("Segoe UI", 48)
        )
        icon_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Title
        title_label = ctk.CTkLabel(
            header_frame,
            text="Register as Midwife",
            font=("Segoe UI", 36, "bold"),
            text_color="#1F2937"
        )
        title_label.pack(pady=(0, 8))
        
        # Subtitle
        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Join the health system and start managing records",
            font=("Segoe UI", 14),
            text_color="#6B7280"
        )
        subtitle_label.pack()
        
        # Registration card
        register_card = ctk.CTkFrame(
            center_container,
            fg_color="white",
            corner_radius=28,
            width=900,
            border_width=1,
            border_color="white"
        )
        register_card.pack(padx=40, pady=20)
        
        # Content frame
        content_frame = ctk.CTkFrame(
            register_card,
            fg_color="transparent"
        )
        content_frame.pack(fill="both", expand=True, padx=48, pady=48)
        
        # SECTION 1: Personal Information
        self.create_section_header(content_frame, "👤", "Personal Information")
        
        # Name fields row
        name_row = ctk.CTkFrame(content_frame, fg_color="transparent")
        name_row.pack(fill="x", pady=(0, 20))
        
        # First Name
        first_col = ctk.CTkFrame(name_row, fg_color="transparent")
        first_col.pack(side="left", fill="x", expand=True, padx=(0, 12))
        
        ctk.CTkLabel(
            first_col,
            text="First Name *",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151",
            anchor="w"
        ).pack(fill="x", pady=(0, 10))
        
        self.first_name_entry = self.create_modern_entry(first_col, "Juan")
        
        # Last Name
        last_col = ctk.CTkFrame(name_row, fg_color="transparent")
        last_col.pack(side="left", fill="x", expand=True)
        
        ctk.CTkLabel(
            last_col,
            text="Last Name *",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151",
            anchor="w"
        ).pack(fill="x", pady=(0, 10))
        
        self.last_name_entry = self.create_modern_entry(last_col, "Dela Cruz")
        
        # Middle Name
        ctk.CTkLabel(
            content_frame,
            text="Middle Name (Optional)",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151",
            anchor="w"
        ).pack(fill="x", pady=(0, 10))
        
        self.middle_name_entry = self.create_modern_entry(content_frame, "Santos")
        self.middle_name_entry.pack(fill="x", pady=(0, 20))
        
        # Username and Contact row
        contact_row = ctk.CTkFrame(content_frame, fg_color="transparent")
        contact_row.pack(fill="x", pady=(0, 20))
        
        # Username
        username_col = ctk.CTkFrame(contact_row, fg_color="transparent")
        username_col.pack(side="left", fill="x", expand=True, padx=(0, 12))
        
        ctk.CTkLabel(
            username_col,
            text="Username *",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151",
            anchor="w"
        ).pack(fill="x", pady=(0, 10))
        
        self.username_entry = self.create_modern_entry(username_col, "Choose a username")
        self.username_entry.bind("<KeyRelease>", self.validate_username_realtime)
        
        self.username_hint = ctk.CTkLabel(
            username_col,
            text="3-50 characters, letters, numbers, underscores",
            font=("Segoe UI", 10),
            text_color="#6B7280",
            anchor="w"
        )
        self.username_hint.pack(fill="x", pady=(5, 0))
        
        # Contact Number
        contact_col = ctk.CTkFrame(contact_row, fg_color="transparent")
        contact_col.pack(side="left", fill="x", expand=True)
        
        ctk.CTkLabel(
            contact_col,
            text="Contact Number *",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151",
            anchor="w"
        ).pack(fill="x", pady=(0, 10))
        
        self.contact_entry = self.create_modern_entry(contact_col, "09XXXXXXXXX")
        
        ctk.CTkLabel(
            contact_col,
            text="📱 Enter 11-digit phone number",
            font=("Segoe UI", 10),
            text_color="#6B7280",
            anchor="w"
        ).pack(fill="x", pady=(5, 0))
        
        # Email
        ctk.CTkLabel(
            content_frame,
            text="Email Address *",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151",
            anchor="w"
        ).pack(fill="x", pady=(0, 10))
        
        self.email_entry = self.create_modern_entry(content_frame, "your.email@gmail.com")
        self.email_entry.pack(fill="x", pady=(0, 5))
        self.email_entry.bind("<KeyRelease>", self.validate_email_realtime)
        
        self.email_hint = ctk.CTkLabel(
            content_frame,
            text="📧 Must be a valid email with @ and domain",
            font=("Segoe UI", 10),
            text_color="#6B7280",
            anchor="w"
        )
        self.email_hint.pack(fill="x", pady=(0, 20))
        
        # Password row
        password_row = ctk.CTkFrame(content_frame, fg_color="transparent")
        password_row.pack(fill="x", pady=(0, 20))
        
        # Password
        pass_col = ctk.CTkFrame(password_row, fg_color="transparent")
        pass_col.pack(side="left", fill="x", expand=True, padx=(0, 12))
        
        ctk.CTkLabel(
            pass_col,
            text="Password *",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151",
            anchor="w"
        ).pack(fill="x", pady=(0, 10))
        
        pass_container = ctk.CTkFrame(pass_col, fg_color="transparent")
        pass_container.pack(fill="x")
        
        self.password_entry = self.create_modern_entry(pass_container, "Minimum 6 characters", show="●")
        self.password_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.password_entry.bind("<KeyRelease>", self.validate_password_strength)
        
        self.show_password_btn = ctk.CTkButton(
            pass_container,
            text="👁",
            width=48,
            height=48,
            font=("Segoe UI", 16),
            fg_color="#F3F4F6",
            hover_color="#E5E7EB",
            text_color="#6B7280",
            corner_radius=14,
            command=self.toggle_password_visibility
        )
        self.show_password_btn.pack(side="left")
        
        self.password_strength = ctk.CTkLabel(
            pass_col,
            text="🔒 Minimum 6 characters",
            font=("Segoe UI", 10),
            text_color="#6B7280",
            anchor="w"
        )
        self.password_strength.pack(fill="x", pady=(5, 0))
        
        # Confirm Password
        confirm_col = ctk.CTkFrame(password_row, fg_color="transparent")
        confirm_col.pack(side="left", fill="x", expand=True)
        
        ctk.CTkLabel(
            confirm_col,
            text="Confirm Password *",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151",
            anchor="w"
        ).pack(fill="x", pady=(0, 10))
        
        confirm_container = ctk.CTkFrame(confirm_col, fg_color="transparent")
        confirm_container.pack(fill="x")
        
        self.confirm_password_entry = self.create_modern_entry(confirm_container, "Re-enter password", show="●")
        self.confirm_password_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        self.show_confirm_password_btn = ctk.CTkButton(
            confirm_container,
            text="👁",
            width=48,
            height=48,
            font=("Segoe UI", 16),
            fg_color="#F3F4F6",
            hover_color="#E5E7EB",
            text_color="#6B7280",
            corner_radius=14,
            command=self.toggle_confirm_password_visibility
        )
        self.show_confirm_password_btn.pack(side="left")
        
        ctk.CTkLabel(
            confirm_col,
            text="🔐 Must match password",
            font=("Segoe UI", 10),
            text_color="#6B7280",
            anchor="w"
        ).pack(fill="x", pady=(5, 0))
        
        # Divider
        ctk.CTkFrame(
            content_frame,
            fg_color="#F3F4F6",
            height=2
        ).pack(fill="x", pady=30)
        
        # SECTION 2: Barangay Assignment
        self.create_section_header(content_frame, "📍", "Barangay Assignment")
        
        # Instruction
        instruction_frame = ctk.CTkFrame(
            content_frame,
            fg_color="#FEF3C7",
            corner_radius=14,
            border_width=2,
            border_color="#FBBF24"
        )
        instruction_frame.pack(fill="x", pady=(0, 25))
        
        instruction_content = ctk.CTkFrame(instruction_frame, fg_color="transparent")
        instruction_content.pack(fill="x", padx=20, pady=18)
        
        ctk.CTkLabel(
            instruction_content,
            text="ℹ️",
            font=("Segoe UI", 24)
        ).pack(side="left", padx=(0, 14))
        
        ctk.CTkLabel(
            instruction_content,
            text="Select 1-3 barangays you will manage",
            font=("Segoe UI", 13, "bold"),
            text_color="#92400E"
        ).pack(side="left")
        
        # Barangay grid
        barangay_scroll = ctk.CTkScrollableFrame(
            content_frame,
            height=300,
            fg_color="#F9FAFB",
            corner_radius=14,
            border_width=2,
            border_color="#E5E7EB",
            scrollbar_button_color="#10B981",
            scrollbar_button_hover_color="#059669"
        )
        barangay_scroll.pack(fill="x", pady=(0, 30))
        
        # Create barangay checkboxes in grid
        self.barangay_vars = {}
        barangay_container = ctk.CTkFrame(barangay_scroll, fg_color="transparent")
        barangay_container.pack(fill="both", expand=True, padx=8, pady=8)
        
        for idx, barangay in enumerate(self.barangays):
            var = ctk.BooleanVar(value=False)
            self.barangay_vars[barangay['id']] = var
            
            checkbox_frame = ctk.CTkFrame(
                barangay_container,
                fg_color="white",
                corner_radius=14,
                border_width=2,
                border_color="#E5E7EB"
            )
            checkbox_frame.grid(row=idx//3, column=idx%3, padx=8, pady=8, sticky="ew")
            
            checkbox = ctk.CTkCheckBox(
                checkbox_frame,
                text=f"📍 {barangay['name']}",
                variable=var,
                font=("Segoe UI", 13, "bold"),
                text_color="#374151",
                fg_color="#10B981",
                hover_color="#059669",
                border_color="#E5E7EB",
                corner_radius=8,
                command=lambda: self.limit_barangay_selection()
            )
            checkbox.pack(padx=18, pady=16, anchor="w")
        
        # Configure grid columns
        for i in range(3):
            barangay_container.grid_columnconfigure(i, weight=1, uniform="col")
        
        # Action buttons
        button_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        button_frame.pack(fill="x")
        
        # Submit button
        self.register_btn = ctk.CTkButton(
            button_frame,
            text="📝  Submit Registration",
            height=56,
            font=("Segoe UI", 16, "bold"),
            fg_color="#10B981",
            hover_color="#059669",
            corner_radius=14,
            command=self.handle_register
        )
        self.register_btn.pack(side="left", fill="x", expand=True, padx=(0, 12))
        
        # Back button
        back_btn = ctk.CTkButton(
            button_frame,
            text="←  Back to Login",
            height=56,
            font=("Segoe UI", 15, "bold"),
            fg_color="white",
            hover_color="#F9FAFB",
            text_color="#374151",
            border_width=2,
            border_color="#E5E7EB",
            corner_radius=14,
            command=self.on_back_to_login
        )
        back_btn.pack(side="left", fill="x")
        
        # Notice
        notice_frame = ctk.CTkFrame(
            center_container,
            fg_color="white",
            corner_radius=20,
            border_width=1,
            border_color="white"
        )
        notice_frame.pack(fill="x", padx=40, pady=(20, 0))
        
        notice_content = ctk.CTkFrame(notice_frame, fg_color="transparent")
        notice_content.pack(fill="x", padx=28, pady=24)
        
        ctk.CTkLabel(
            notice_content,
            text="⚠️",
            font=("Segoe UI", 28)
        ).pack(side="left", padx=(0, 18))
        
        ctk.CTkLabel(
            notice_content,
            text="Your registration will be reviewed by an administrator. You'll receive an email notification once approved.",
            font=("Segoe UI", 13),
            text_color="#6B7280",
            wraplength=700,
            justify="left"
        ).pack(side="left", fill="x", expand=True)
        
        # Focus
        self.first_name_entry.focus()
    
    def create_section_header(self, parent, icon, title):
        """Create section header"""
        header_frame = ctk.CTkFrame(parent, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 28))
        
        icon_frame = ctk.CTkFrame(
            header_frame,
            fg_color="#ECFDF5",
            corner_radius=16,
            border_width=2,
            border_color="#10B981",
            width=56,
            height=56
        )
        icon_frame.pack(side="left", padx=(0, 16))
        icon_frame.pack_propagate(False)
        
        ctk.CTkLabel(
            icon_frame,
            text=icon,
            font=("Segoe UI", 28)
        ).place(relx=0.5, rely=0.5, anchor="center")
        
        ctk.CTkLabel(
            header_frame,
            text=title,
            font=("Segoe UI", 22, "bold"),
            text_color="#1F2937"
        ).pack(side="left", anchor="w")
    
    def create_modern_entry(self, parent, placeholder, show=None):
        """Create modern styled entry"""
        entry = ctk.CTkEntry(
            parent,
            height=48,
            font=("Segoe UI", 14),
            placeholder_text=placeholder,
            border_width=2,
            corner_radius=14,
            border_color="#E5E7EB",
            fg_color="white",
            text_color="#1F2937",
            placeholder_text_color="#9CA3AF"
        )
        if show:
            entry.configure(show=show)
        return entry
    
    def validate_username_realtime(self, event=None):
        """Real-time username validation"""
        username = self.username_entry.get()
        
        if not username:
            self.username_hint.configure(text="3-50 characters, letters, numbers, underscores", text_color="#6B7280")
            self.username_entry.configure(border_color="#E5E7EB")
            return
        
        if len(username) < 3:
            self.username_hint.configure(text="✗ Too short (minimum 3 characters)", text_color="#EF4444")
            self.username_entry.configure(border_color="#EF4444")
        elif len(username) > 50:
            self.username_hint.configure(text="✗ Too long (maximum 50 characters)", text_color="#EF4444")
            self.username_entry.configure(border_color="#EF4444")
        elif not username.replace('_', '').isalnum():
            self.username_hint.configure(text="✗ Only letters, numbers, and underscores allowed", text_color="#EF4444")
            self.username_entry.configure(border_color="#EF4444")
        else:
            self.username_hint.configure(text="✓ Valid username format", text_color="#10B981")
            self.username_entry.configure(border_color="#10B981")
    
    def validate_email_realtime(self, event=None):
        """Real-time email validation"""
        email = self.email_entry.get()
        
        if not email:
            self.email_hint.configure(text="📧 Must be a valid email with @ and domain", text_color="#6B7280")
            self.email_entry.configure(border_color="#E5E7EB")
            return
        
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if re.match(pattern, email):
            self.email_hint.configure(text="✓ Valid email format", text_color="#10B981")
            self.email_entry.configure(border_color="#10B981")
        else:
            self.email_hint.configure(text="✗ Invalid email format", text_color="#EF4444")
            self.email_entry.configure(border_color="#EF4444")
    
    def validate_password_strength(self, event=None):
        """Real-time password strength validation"""
        password = self.password_entry.get()
        
        if not password:
            self.password_strength.configure(text="🔒 Minimum 6 characters", text_color="#6B7280")
            self.password_entry.configure(border_color="#E5E7EB")
            return
        
        if len(password) < 6:
            self.password_strength.configure(text="✗ Too weak (minimum 6 characters)", text_color="#EF4444")
            self.password_entry.configure(border_color="#EF4444")
        elif len(password) < 8:
            self.password_strength.configure(text="⚠️ Weak password", text_color="#F59E0B")
            self.password_entry.configure(border_color="#F59E0B")
        elif len(password) < 12:
            self.password_strength.configure(text="✓ Medium strength", text_color="#3B82F6")
            self.password_entry.configure(border_color="#3B82F6")
        else:
            self.password_strength.configure(text="✓ Strong password", text_color="#10B981")
            self.password_entry.configure(border_color="#10B981")
    
    def limit_barangay_selection(self):
        """Limit barangay selection to 3"""
        selected = sum(1 for var in self.barangay_vars.values() if var.get())
        if selected > 3:
            messagebox.showwarning("Selection Limit", "⚠️ You can only select up to 3 barangays.")
            # Uncheck the last one
            for var in self.barangay_vars.values():
                if var.get():
                    var.set(False)
                    break
    
    def toggle_password_visibility(self):
        """Toggle password visibility"""
        self.password_visible = not self.password_visible
        if self.password_visible:
            self.password_entry.configure(show="")
            self.show_password_btn.configure(text="🙈")
        else:
            self.password_entry.configure(show="●")
            self.show_password_btn.configure(text="👁")
    
    def toggle_confirm_password_visibility(self):
        """Toggle confirm password visibility"""
        self.confirm_password_visible = not self.confirm_password_visible
        if self.confirm_password_visible:
            self.confirm_password_entry.configure(show="")
            self.show_confirm_password_btn.configure(text="🙈")
        else:
            self.confirm_password_entry.configure(show="●")
            self.show_confirm_password_btn.configure(text="👁")
    
    def handle_register(self):
        """Handle registration button click"""
        
        # Get selected barangays
        selected_barangay_ids = [
            barangay_id for barangay_id, var in self.barangay_vars.items() 
            if var.get()
        ]
        
        # Quick validation
        if not self.first_name_entry.get().strip():
            messagebox.showerror("Validation Error", "First name is required")
            self.first_name_entry.focus()
            return
        
        if not self.last_name_entry.get().strip():
            messagebox.showerror("Validation Error", "Last name is required")
            self.last_name_entry.focus()
            return
        
        if not self.username_entry.get().strip():
            messagebox.showerror("Validation Error", "Username is required")
            self.username_entry.focus()
            return
        
        if not self.email_entry.get().strip():
            messagebox.showerror("Validation Error", "Email is required")
            self.email_entry.focus()
            return
        
        if not self.password_entry.get():
            messagebox.showerror("Validation Error", "Password is required")
            self.password_entry.focus()
            return
        
        if not self.confirm_password_entry.get():
            messagebox.showerror("Validation Error", "Please confirm your password")
            self.confirm_password_entry.focus()
            return
        
        if not selected_barangay_ids:
            messagebox.showerror("Validation Error", "Please select at least one barangay")
            return
        
        # Confirmation dialog
        barangay_names = [b['name'] for b in self.barangays if b['id'] in selected_barangay_ids]
        confirm_msg = (
            f"Please confirm your registration details:\n\n"
            f"Name: {self.first_name_entry.get()} {self.middle_name_entry.get()} {self.last_name_entry.get()}\n"
            f"Username: {self.username_entry.get()}\n"
            f"Email: {self.email_entry.get()}\n"
            f"Barangay(s): {', '.join(barangay_names)}\n\n"
            f"Your account will be pending admin approval.\n\n"
            f"Do you want to proceed?"
        )
        
        if not messagebox.askyesno("Confirm Registration", confirm_msg):
            return
        
        # Prepare registration data
        registration_data = {
            'first_name': self.first_name_entry.get(),
            'middle_name': self.middle_name_entry.get(),
            'last_name': self.last_name_entry.get(),
            'username': self.username_entry.get(),
            'email': self.email_entry.get(),
            'password': self.password_entry.get(),
            'confirm_password': self.confirm_password_entry.get(),
            'contact_number': self.contact_entry.get(),
            'barangay_ids': selected_barangay_ids
        }
        
        # Disable button
        self.register_btn.configure(state="disabled", text="Creating account...")
        self.update()
        
        try:
            # Register
            success, message = register_midwife(registration_data)
            
            if success:
                messagebox.showinfo(
                    "Registration Successful", 
                    f"{message}\n\n"
                    f"You will receive a notification once your account is approved.\n"
                    f"Please check your email for updates."
                )
                self.on_back_to_login()
            else:
                messagebox.showerror("Registration Failed", message)
                self.register_btn.configure(state="normal", text="📝  Submit Registration")
        except Exception as e:
            messagebox.showerror(
                "Registration Error", 
                f"An unexpected error occurred:\n{str(e)}\n\n"
                f"Please try again or contact support."
            )
            self.register_btn.configure(state="normal", text="📝  Submit Registration")
