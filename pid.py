"""
PID Aim Settings Module

This module provides the GUI components for PID (Proportional-Integral-Derivative) 
controller-based aiming settings with dynamic Kp adjustment.
"""

import customtkinter as ctk
from gui_constants import NEON


class PIDAimSection:
    """PID aim settings section with dynamic Kp adjustment and comprehensive parameter controls."""
    
    def __init__(self, parent_frame, config, gui_instance=None):
        """
        Initialize the PID aim section.
        
        Args:
            parent_frame: The parent frame to add controls to
            config: Configuration object to read/write settings
            gui_instance: Reference to the main GUI instance for callbacks
        """
        self.parent_frame = parent_frame
        self.config = config
        self.gui_instance = gui_instance
        
        # Store widget references for real-time updates
        self.real_time_kp_label = None
        self.real_time_ki_label = None
    
    def create_section(self):
        """
        Create the PID aim settings section.
        
        Returns:
            The created frame containing all controls
        """
        f = ctk.CTkFrame(self.parent_frame, fg_color="#1a1a1a")
        f.pack(fill="x", pady=5)
        f.grid_columnconfigure(1, weight=1)
        
        # Title
        ctk.CTkLabel(f, text="🎯 PID Controller Settings", 
                    font=("Segoe UI", 14, "bold"), 
                    text_color="#00e676").grid(row=0, column=0, columnspan=3, 
                                             pady=(10, 5), padx=10, sticky="w")
        
        # Dynamic Kp Adjustment Area
        self._create_dynamic_kp_area(f)
        
        # PID Core Parameters
        self._create_pid_parameters(f)
        
        # Movement Parameters
        self._create_movement_parameters(f)
        
        # Real-time Display
        self._create_realtime_display(f)
        
        return f
    
    def _create_dynamic_kp_area(self, parent_frame):
        """Create the dynamic Kp adjustment area."""
        # Dynamic Kp Adjustment Area Title
        ctk.CTkLabel(parent_frame, text="📊 Dynamic Kp Adjustment Area", 
                    font=("Segoe UI", 12, "bold"), 
                    text_color="#ff073a").grid(row=1, column=0, columnspan=3, 
                                             pady=(15, 5), padx=10, sticky="w")
        
        # P Min Value
        ctk.CTkLabel(parent_frame, text="P Min Value:", text_color="#fff").grid(
            row=2, column=0, sticky="w", padx=10, pady=2)
        p_min_slider = ctk.CTkSlider(parent_frame, from_=0.001, to=1.0, number_of_steps=999)
        p_min_slider.set(getattr(self.config, "pid_p_min", 0.155))
        p_min_slider.grid(row=2, column=1, sticky="ew", padx=(5, 5), pady=2)
        p_min_entry = ctk.CTkEntry(parent_frame, width=80, justify="center", 
                                  font=("Segoe UI", 11, "bold"), text_color=NEON)
        p_min_entry.grid(row=2, column=2, padx=10, pady=2)
        p_min_entry.insert(0, f"{getattr(self.config, 'pid_p_min', 0.155):.3f}")
        
        # P Max Value
        ctk.CTkLabel(parent_frame, text="P Max Value:", text_color="#fff").grid(
            row=3, column=0, sticky="w", padx=10, pady=2)
        p_max_slider = ctk.CTkSlider(parent_frame, from_=0.001, to=5.0, number_of_steps=4999)
        p_max_slider.set(getattr(self.config, "pid_p_max", 0.601))
        p_max_slider.grid(row=3, column=1, sticky="ew", padx=(5, 5), pady=2)
        p_max_entry = ctk.CTkEntry(parent_frame, width=80, justify="center", 
                                  font=("Segoe UI", 11, "bold"), text_color=NEON)
        p_max_entry.grid(row=3, column=2, padx=10, pady=2)
        p_max_entry.insert(0, f"{getattr(self.config, 'pid_p_max', 0.601):.3f}")
        
        # P Growth Slope
        ctk.CTkLabel(parent_frame, text="P Growth Slope:", text_color="#fff").grid(
            row=4, column=0, sticky="w", padx=10, pady=2)
        p_slope_slider = ctk.CTkSlider(parent_frame, from_=0.001, to=0.5, number_of_steps=499)
        p_slope_slider.set(getattr(self.config, "pid_p_slope", 0.100))
        p_slope_slider.grid(row=4, column=1, sticky="ew", padx=(5, 5), pady=2)
        p_slope_entry = ctk.CTkEntry(parent_frame, width=80, justify="center", 
                                    font=("Segoe UI", 11, "bold"), text_color=NEON)
        p_slope_entry.grid(row=4, column=2, padx=10, pady=2)
        p_slope_entry.insert(0, f"{getattr(self.config, 'pid_p_slope', 0.100):.3f}")
        
        # Integral (I) Max Value
        ctk.CTkLabel(parent_frame, text="Integral (I) Max:", text_color="#fff").grid(
            row=5, column=0, sticky="w", padx=10, pady=2)
        i_max_slider = ctk.CTkSlider(parent_frame, from_=0.0, to=5.0, number_of_steps=5000)
        i_max_slider.set(getattr(self.config, "pid_i_max", 2.000))
        i_max_slider.grid(row=5, column=1, sticky="ew", padx=(5, 5), pady=2)
        i_max_entry = ctk.CTkEntry(parent_frame, width=80, justify="center", 
                                  font=("Segoe UI", 11, "bold"), text_color=NEON)
        i_max_entry.grid(row=5, column=2, padx=10, pady=2)
        i_max_entry.insert(0, f"{getattr(self.config, 'pid_i_max', 2.000):.3f}")
        
        # Derivative (D)
        ctk.CTkLabel(parent_frame, text="Derivative (D):", text_color="#fff").grid(
            row=6, column=0, sticky="w", padx=10, pady=2)
        d_slider = ctk.CTkSlider(parent_frame, from_=0.0, to=0.1, number_of_steps=1000)
        d_slider.set(getattr(self.config, "pid_d", 0.004))
        d_slider.grid(row=6, column=1, sticky="ew", padx=(5, 5), pady=2)
        d_entry = ctk.CTkEntry(parent_frame, width=80, justify="center", 
                              font=("Segoe UI", 11, "bold"), text_color=NEON)
        d_entry.grid(row=6, column=2, padx=10, pady=2)
        d_entry.insert(0, f"{getattr(self.config, 'pid_d', 0.004):.3f}")
        
        # Bind update functions
        self._bind_slider_entry_updates(p_min_slider, p_min_entry, "pid_p_min")
        self._bind_slider_entry_updates(p_max_slider, p_max_entry, "pid_p_max")
        self._bind_slider_entry_updates(p_slope_slider, p_slope_entry, "pid_p_slope")
        self._bind_slider_entry_updates(i_max_slider, i_max_entry, "pid_i_max")
        self._bind_slider_entry_updates(d_slider, d_entry, "pid_d")
    
    def _create_pid_parameters(self, parent_frame):
        """Create PID-specific parameter controls."""
        # PID Parameters Title
        ctk.CTkLabel(parent_frame, text="⚙️ PID Parameters", 
                    font=("Segoe UI", 12, "bold"), 
                    text_color="#00e676").grid(row=7, column=0, columnspan=3, 
                                             pady=(15, 5), padx=10, sticky="w")
        
        # Max Pixel Movement
        ctk.CTkLabel(parent_frame, text="Max Pixel Movement:", text_color="#fff").grid(
            row=8, column=0, sticky="w", padx=10, pady=2)
        max_pixel_slider = ctk.CTkSlider(parent_frame, from_=1, to=100, number_of_steps=99)
        max_pixel_slider.set(getattr(self.config, "pid_max_pixel", 10))
        max_pixel_slider.grid(row=8, column=1, sticky="ew", padx=(5, 5), pady=2)
        max_pixel_entry = ctk.CTkEntry(parent_frame, width=80, justify="center", 
                                      font=("Segoe UI", 11, "bold"), text_color=NEON)
        max_pixel_entry.grid(row=8, column=2, padx=10, pady=2)
        max_pixel_entry.insert(0, f"{getattr(self.config, 'pid_max_pixel', 10):.0f}")
        
        # Movement Segments X
        ctk.CTkLabel(parent_frame, text="Movement Segments (X):", text_color="#fff").grid(
            row=9, column=0, sticky="w", padx=10, pady=2)
        seg_x_slider = ctk.CTkSlider(parent_frame, from_=1, to=50, number_of_steps=49)
        seg_x_slider.set(getattr(self.config, "pid_segments_x", 1))
        seg_x_slider.grid(row=9, column=1, sticky="ew", padx=(5, 5), pady=2)
        seg_x_entry = ctk.CTkEntry(parent_frame, width=80, justify="center", 
                                  font=("Segoe UI", 11, "bold"), text_color=NEON)
        seg_x_entry.grid(row=9, column=2, padx=10, pady=2)
        seg_x_entry.insert(0, f"{getattr(self.config, 'pid_segments_x', 1):.0f}")
        
        # Movement Segments Y
        ctk.CTkLabel(parent_frame, text="Movement Segments (Y):", text_color="#fff").grid(
            row=10, column=0, sticky="w", padx=10, pady=2)
        seg_y_slider = ctk.CTkSlider(parent_frame, from_=1, to=50, number_of_steps=49)
        seg_y_slider.set(getattr(self.config, "pid_segments_y", 1))
        seg_y_slider.grid(row=10, column=1, sticky="ew", padx=(5, 5), pady=2)
        seg_y_entry = ctk.CTkEntry(parent_frame, width=80, justify="center", 
                                  font=("Segoe UI", 11, "bold"), text_color=NEON)
        seg_y_entry.grid(row=10, column=2, padx=10, pady=2)
        seg_y_entry.insert(0, f"{getattr(self.config, 'pid_segments_y', 1):.0f}")
        
        # Bind update functions
        self._bind_slider_entry_updates(max_pixel_slider, max_pixel_entry, "pid_max_pixel", is_int=True)
        self._bind_slider_entry_updates(seg_x_slider, seg_x_entry, "pid_segments_x", is_int=True)
        self._bind_slider_entry_updates(seg_y_slider, seg_y_entry, "pid_segments_y", is_int=True)
    
    def _create_movement_parameters(self, parent_frame):
        """Create movement-related parameter controls."""
        # Movement Parameters Title
        ctk.CTkLabel(parent_frame, text="🎮 Movement Parameters", 
                    font=("Segoe UI", 12, "bold"), 
                    text_color="#00e676").grid(row=11, column=0, columnspan=3, 
                                             pady=(15, 5), padx=10, sticky="w")
        
        # X Speed
        ctk.CTkLabel(parent_frame, text="X Speed:", text_color="#fff").grid(
            row=12, column=0, sticky="w", padx=10, pady=2)
        x_speed_slider = ctk.CTkSlider(parent_frame, from_=0.001, to=2.0, number_of_steps=1999)
        x_speed_slider.set(getattr(self.config, "pid_x_speed", 0.789))
        x_speed_slider.grid(row=12, column=1, sticky="ew", padx=(5, 5), pady=2)
        x_speed_entry = ctk.CTkEntry(parent_frame, width=80, justify="center", 
                                    font=("Segoe UI", 11, "bold"), text_color=NEON)
        x_speed_entry.grid(row=12, column=2, padx=10, pady=2)
        x_speed_entry.insert(0, f"{getattr(self.config, 'pid_x_speed', 0.789):.3f}")
        
        # Y Speed
        ctk.CTkLabel(parent_frame, text="Y Speed:", text_color="#fff").grid(
            row=13, column=0, sticky="w", padx=10, pady=2)
        y_speed_slider = ctk.CTkSlider(parent_frame, from_=0.001, to=2.0, number_of_steps=1999)
        y_speed_slider.set(getattr(self.config, "pid_y_speed", 0.666))
        y_speed_slider.grid(row=13, column=1, sticky="ew", padx=(5, 5), pady=2)
        y_speed_entry = ctk.CTkEntry(parent_frame, width=80, justify="center", 
                                    font=("Segoe UI", 11, "bold"), text_color=NEON)
        y_speed_entry.grid(row=13, column=2, padx=10, pady=2)
        y_speed_entry.insert(0, f"{getattr(self.config, 'pid_y_speed', 0.666):.3f}")
        
        # Max Pixels
        ctk.CTkLabel(parent_frame, text="Max Pixels:", text_color="#fff").grid(
            row=14, column=0, sticky="w", padx=10, pady=2)
        max_pixels_slider = ctk.CTkSlider(parent_frame, from_=1, to=200, number_of_steps=199)
        max_pixels_slider.set(getattr(self.config, "pid_max_pixels", 50))
        max_pixels_slider.grid(row=14, column=1, sticky="ew", padx=(5, 5), pady=2)
        max_pixels_entry = ctk.CTkEntry(parent_frame, width=80, justify="center", 
                                       font=("Segoe UI", 11, "bold"), text_color=NEON)
        max_pixels_entry.grid(row=14, column=2, padx=10, pady=2)
        max_pixels_entry.insert(0, f"{getattr(self.config, 'pid_max_pixels', 50):.0f}")
        
        # Bind update functions
        self._bind_slider_entry_updates(x_speed_slider, x_speed_entry, "pid_x_speed")
        self._bind_slider_entry_updates(y_speed_slider, y_speed_entry, "pid_y_speed")
        self._bind_slider_entry_updates(max_pixels_slider, max_pixels_entry, "pid_max_pixels", is_int=True)
    
    def _create_realtime_display(self, parent_frame):
        """Create real-time Kp and Ki display."""
        # Real-time Display Title
        ctk.CTkLabel(parent_frame, text="📈 Real-time Display", 
                    font=("Segoe UI", 12, "bold"), 
                    text_color="#ff073a").grid(row=15, column=0, columnspan=3, 
                                             pady=(15, 5), padx=10, sticky="w")
        
        # Real-time Kp
        ctk.CTkLabel(parent_frame, text="Real-time Kp:", text_color="#fff").grid(
            row=16, column=0, sticky="w", padx=10, pady=2)
        self.real_time_kp_label = ctk.CTkLabel(parent_frame, text="0.000000", 
                                              text_color=NEON, font=("Segoe UI", 12, "bold"))
        self.real_time_kp_label.grid(row=16, column=1, sticky="w", padx=(5, 5), pady=2)
        
        # Real-time Ki
        ctk.CTkLabel(parent_frame, text="Real-time Ki:", text_color="#fff").grid(
            row=17, column=0, sticky="w", padx=10, pady=2)
        self.real_time_ki_label = ctk.CTkLabel(parent_frame, text="0.000000", 
                                              text_color=NEON, font=("Segoe UI", 12, "bold"))
        self.real_time_ki_label.grid(row=17, column=1, sticky="w", padx=(5, 5), pady=2)
        
        # Help text
        help_text = "Ctrl + Left Mouse Button can directly modify slider values"
        ctk.CTkLabel(parent_frame, text=help_text, 
                    text_color="#ccc", font=("Segoe UI", 10)).grid(
            row=18, column=0, columnspan=3, pady=(10, 5), padx=10, sticky="w")
    
    def _bind_slider_entry_updates(self, slider, entry, config_key, is_int=False):
        """Bind slider and entry updates for a parameter."""
        # Guard to prevent feedback loops
        _updating = False
        
        def update_from_slider(val):
            nonlocal _updating
            if _updating:
                return
            if is_int:
                val = int(round(float(val)))
            else:
                val = round(float(val), 3)
            setattr(self.config, config_key, val)
            if not _updating:
                _updating = True
                entry.delete(0, "end")
                if is_int:
                    entry.insert(0, f"{val:.0f}")
                else:
                    entry.insert(0, f"{val:.3f}")
                _updating = False
            self._update_realtime_display()
        
        def update_from_entry(event=None):
            nonlocal _updating
            if _updating:
                return
            try:
                val = float(entry.get().strip())
                if is_int:
                    val = int(round(val))
                else:
                    val = round(val, 3)
                _updating = True
                setattr(self.config, config_key, val)
                slider.set(val)
                entry.delete(0, "end")
                if is_int:
                    entry.insert(0, f"{val:.0f}")
                else:
                    entry.insert(0, f"{val:.3f}")
            except ValueError:
                # Reset to current config value on invalid input
                entry.delete(0, "end")
                current_val = getattr(self.config, config_key, 0)
                if is_int:
                    entry.insert(0, f"{current_val:.0f}")
                else:
                    entry.insert(0, f"{current_val:.3f}")
            finally:
                _updating = False
            self._update_realtime_display()
        
        slider.configure(command=update_from_slider)
        entry.bind("<Return>", update_from_entry)
        entry.bind("<FocusOut>", update_from_entry)
    
    def _update_realtime_display(self):
        """Update real-time Kp and Ki display values."""
        if self.real_time_kp_label and self.real_time_ki_label:
            # Simplified display using configured values
            current_kp = getattr(self.config, "pid_p_min", 0.155)
            current_ki = getattr(self.config, "pid_i_max", 2.000)
            
            self.real_time_kp_label.configure(text=f"{current_kp:.6f}")
            self.real_time_ki_label.configure(text=f"{current_ki:.6f}")
    
    def update_realtime_values(self, kp_value, ki_value):
        """
        Update real-time display with actual calculated values.
        
        Args:
            kp_value: Current Kp value
            ki_value: Current Ki value
        """
        if self.real_time_kp_label and self.real_time_ki_label:
            self.real_time_kp_label.configure(text=f"{kp_value:.6f}")
            self.real_time_ki_label.configure(text=f"{ki_value:.6f}")


