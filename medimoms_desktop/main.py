"""  
MediMoms Desktop Application
Main entry point
"""

import customtkinter as ctk
from tkinter import messagebox
from database.connection import init_connection_pool, test_connection
from ui.auth.login_window import LoginWindow
from ui.auth.register_window import RegisterWindow
from config import APP_NAME, WINDOW_SIZE, MIN_WINDOW_SIZE, COLORS

# Set appearance mode and color theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

class MediMomsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title(APP_NAME)
        self.geometry(WINDOW_SIZE)
        self.minsize(*MIN_WINDOW_SIZE)
        
        # Center window
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
        
        # Configure window
        self.configure(fg_color=COLORS['background'])
        
        # Current user data
        self.current_user = None
        
        # Initialize database
        if not self.init_database():
            messagebox.showerror(
                "Database Error",
                "Failed to connect to the database.\n\n"
                "Please check your database configuration and try again."
            )
            self.quit()
            return
        
        # Show login window
        self.show_login()
    
    def init_database(self):
        """Initialize database connection"""
        print("Initializing database connection...")
        if init_connection_pool():
            if test_connection():
                print("[OK] Database connection successful")
                return True
            else:
                print("[ERROR] Database connection test failed")
                return False
        return False
    
    def show_login(self):
        """Show login window"""
        # Clear window
        for widget in self.winfo_children():
            widget.destroy()
        
        # Show login frame
        login_frame = LoginWindow(self, self.on_login_success, self.show_register)
    
    def show_register(self):
        """Show registration window"""
        # Clear window
        for widget in self.winfo_children():
            widget.destroy()
        
        # Show register frame
        register_frame = RegisterWindow(self, self.show_login)
    
    def on_login_success(self, user_data):
        """Handle successful login"""
        self.current_user = user_data
        print(f"[OK] User logged in: {user_data['full_name']} ({user_data['role']})")
        
        # Show main dashboard based on role
        self.show_dashboard()
    
    def show_dashboard(self):
        """Show appropriate dashboard based on user role"""
        # Clear window
        for widget in self.winfo_children():
            widget.destroy()
        
        # Create welcome screen (temporary)
        welcome_frame = ctk.CTkFrame(self, fg_color=COLORS['background'])
        welcome_frame.pack(fill="both", expand=True, padx=50, pady=50)
        
        # Welcome message
        welcome_label = ctk.CTkLabel(
            welcome_frame,
            text=f"Welcome, {self.current_user['full_name']}!",
            font=("Segoe UI", 32, "bold"),
            text_color=COLORS['accent']
        )
        welcome_label.pack(pady=(100, 20))
        
        role_label = ctk.CTkLabel(
            welcome_frame,
            text=f"Role: {self.current_user['role'].upper()}",
            font=("Segoe UI", 18),
            text_color=COLORS['text_secondary']
        )
        role_label.pack(pady=(0, 50))
        
        info_label = ctk.CTkLabel(
            welcome_frame,
            text="Dashboard will be implemented in the next steps.",
            font=("Segoe UI", 14),
            text_color=COLORS['text']
        )
        info_label.pack(pady=(0, 30))
        
        # Logout button
        logout_btn = ctk.CTkButton(
            welcome_frame,
            text="Logout",
            height=45,
            width=200,
            font=("Segoe UI", 14, "bold"),
            fg_color=COLORS['danger'],
            hover_color="#dc2626",
            command=self.logout
        )
        logout_btn.pack()
    
    def logout(self):
        """Logout current user"""
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.current_user = None
            self.show_login()

def main():
    """Main application entry point"""
    app = MediMomsApp()
    app.mainloop()

if __name__ == "__main__":
    main()
