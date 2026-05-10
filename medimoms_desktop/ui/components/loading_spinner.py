"""
Loading spinner component for async operations
"""

import customtkinter as ctk
import threading
import time

class LoadingSpinner(ctk.CTkToplevel):
    def __init__(self, parent, message="Processing..."):
        super().__init__(parent)
        
        self.title("")
        self.geometry("300x150")
        self.resizable(False, False)
        
        # Center window
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (150)
        y = (self.winfo_screenheight() // 2) - (75)
        self.geometry(f'300x150+{x}+{y}')
        
        # Make modal
        self.transient(parent)
        self.grab_set()
        
        # Remove window decorations
        self.overrideredirect(True)
        
        # Configure
        self.configure(fg_color="white")
        
        # Create content
        content_frame = ctk.CTkFrame(
            self,
            fg_color="white",
            corner_radius=16,
            border_width=2,
            border_color="#E2E8F0"
        )
        content_frame.pack(fill="both", expand=True, padx=2, pady=2)
        
        # Spinner
        self.spinner_label = ctk.CTkLabel(
            content_frame,
            text="⏳",
            font=("Segoe UI", 48)
        )
        self.spinner_label.pack(pady=(20, 10))
        
        # Message
        self.message_label = ctk.CTkLabel(
            content_frame,
            text=message,
            font=("Segoe UI", 14, "bold"),
            text_color="#0F172A"
        )
        self.message_label.pack(pady=(0, 20))
        
        # Start animation
        self.animating = True
        self.animation_thread = threading.Thread(target=self.animate, daemon=True)
        self.animation_thread.start()
    
    def animate(self):
        """Animate the spinner"""
        spinners = ["⏳", "⌛", "⏳", "⌛"]
        index = 0
        
        while self.animating:
            try:
                self.spinner_label.configure(text=spinners[index])
                index = (index + 1) % len(spinners)
                time.sleep(0.3)
            except:
                break
    
    def close(self):
        """Close the spinner"""
        self.animating = False
        self.destroy()
