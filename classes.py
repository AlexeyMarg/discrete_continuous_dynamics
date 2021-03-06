import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext

class main_window():
    def __init__(self, app):
        self.app = app
        self.app.title('Continuous plant with discrete controller')
        self.app.geometry('700x500')
        self.parse_parameters()
        self.init_ui()

    def parse_parameters(self):
        f = open('modeling_parameters.txt', 'r')
        temp = f.readlines()
        self.x0 = temp[0].split(':')[1].split(',')
        for i in range(len(self.x0)):
            self.x0[i] = float(self.x0[i])
        self.input_delay_status = temp[1].split()[1]
        self.input_delay = float(temp[2].split()[1])
        self.output_delay_status = temp[3].split()[1]
        self.output_delay = float(temp[4].split()[1])
        self.saturation_input_lower = float(temp[5].split()[1])
        self.saturation_input_upper = float(temp[6].split()[1])
        self.input_quantizing_status = temp[7].split()[1]
        self.input_quantizing = float(temp[8].split()[1])
        self.output_quantizing_status = temp[9].split()[1]
        self.output_quantizing = float(temp[10].split()[1])
        self.controller_sample_time = float(temp[11].split()[1])
        self.plant_sample_time = float(temp[12].split()[1])
        self.modeling_time = float(temp[13].split()[1])
        f.close()

    def init_ui(self):
        self.tab_control = ttk.Notebook(self.app)
        self.tab_model = ttk.Frame(self.tab_control)
        self.tab_plant = ttk.Frame(self.tab_control)
        self.tab_controller = ttk.Frame(self.tab_control)
        self.tab_input = ttk.Frame(self.tab_control)
        self.tab_parameters = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_model, text='Modeling')
        self.tab_control.add(self.tab_plant, text='Plant')
        self.tab_control.add(self.tab_controller, text='Controller')
        self.tab_control.add(self.tab_input, text='Input')
        self.tab_control.add(self.tab_parameters, text='Parameters')
        self.tab_control.pack(expand=1, fill='both')

        # Parameters tab init UI
        #sample time
        self.lbl_sample_time = tk.Label(self.tab_parameters, text='Sample time')
        self.lbl_sample_time.grid(row=0, column=0, padx=10)
        self.ent_sample_time = tk.Entry(self.tab_parameters)
        self.ent_sample_time.grid(row=0, column=1)
        self.ent_sample_time.insert(0, str(self.plant_sample_time))
        # Controller sample time
        self.lbl_cont_sample_time = tk.Label(self.tab_parameters, text='Controller sample time')
        self.lbl_cont_sample_time.grid(row=1, column=0, padx=10)
        self.ent_cont_sample_time = tk.Entry(self.tab_parameters)
        self.ent_cont_sample_time.grid(row=1, column=1)
        self.ent_cont_sample_time.insert(0, str(self.controller_sample_time))
        # Modeling time
        self.lbl_modeling_time = tk.Label(self.tab_parameters, text='Modeling time')
        self.lbl_modeling_time.grid(row=2, column=0, padx=10)
        self.ent_modeling_time = tk.Entry(self.tab_parameters)
        self.ent_modeling_time.grid(row=2, column=1)
        self.ent_modeling_time.insert(0, str(self.modeling_time))
        # Initial conditions
        self.lbl_init_cond = tk.Label(self.tab_parameters, text='Initial conditions')
        self.lbl_init_cond.grid(row=3, column=0, padx=10)
        self.ent_init_cond = tk.Entry(self.tab_parameters)
        self.ent_init_cond.grid(row=3, column=1)
        self.ent_init_cond.insert(0, str(self.x0))
        # Input delay
        self.lbl_input_delay = tk.Label(self.tab_parameters, text='Input delay')
        self.lbl_input_delay.grid(row=4, column=0, padx=10)
        self.ent_input_delay = tk.Entry(self.tab_parameters)
        self.ent_input_delay.grid(row=4, column=1)
        self.ent_input_delay.insert(0, str(self.input_delay))
        self.status_input_delay = tk.BooleanVar()
        if self.input_delay_status =='True':
            self.status_input_delay.set(True)
        else:
            self.status_input_delay.set(False)
        self.chb_input_delay = tk.Checkbutton(self.tab_parameters, var=self.status_input_delay)
        self.chb_input_delay.grid(row=4, column=2, padx=10)
        # Output delay
        self.lbl_output_delay = tk.Label(self.tab_parameters, text='Output delay')
        self.lbl_output_delay.grid(row=5, column=0, padx=10)
        self.ent_output_delay = tk.Entry(self.tab_parameters)
        self.ent_output_delay.grid(row=5, column=1)
        self.ent_output_delay.insert(0, str(self.output_delay))
        self.status_output_delay = tk.BooleanVar()
        if self.output_delay_status == 'True':
            self.status_output_delay.set(True)
        else:
            self.status_output_delay.set(False)
        self.chb_output_delay = tk.Checkbutton(self.tab_parameters, var=self.status_output_delay)
        self.chb_output_delay.grid(row=5, column=2, padx=10)
        # Input quantizing
        self.lbl_input_quant = tk.Label(self.tab_parameters, text='Input quantizing')
        self.lbl_input_quant.grid(row=6, column=0, padx=10)
        self.ent_input_quant = tk.Entry(self.tab_parameters)
        self.ent_input_quant.grid(row=6, column=1)
        self.ent_input_quant.insert(0, str(self.input_quantizing))
        self.status_input_quant = tk.BooleanVar()
        if self.input_quantizing_status == 'True':
            self.status_input_quant.set(True)
        else:
            self.status_input_quant.set(False)
        self.chb_input_quant = tk.Checkbutton(self.tab_parameters, var=self.status_input_quant)
        self.chb_input_quant.grid(row=6, column=2, padx=10)
        # Output quantizing
        self.lbl_output_quant = tk.Label(self.tab_parameters, text='Output quantizing')
        self.lbl_output_quant.grid(row=7, column=0, padx=10)
        self.ent_output_quant = tk.Entry(self.tab_parameters)
        self.ent_output_quant.grid(row=7, column=1)
        self.ent_output_quant.insert(0, str(self.output_quantizing))
        self.status_output_quant = tk.BooleanVar()
        if self.output_quantizing_status == 'True':
            self.status_output_quant.set(True)
        else:
            self.status_output_quant.set(False)
        self.chb_output_quant = tk.Checkbutton(self.tab_parameters, var=self.status_output_quant)
        self.chb_output_quant.grid(row=7, column=2, padx=10)
        # Upper control saturation
        self.lbl_saturation_input_upper = tk.Label(self.tab_parameters, text='Upper control bound')
        self.lbl_saturation_input_upper.grid(row=8, column=0, padx=10)
        self.ent_saturation_input_upper = tk.Entry(self.tab_parameters)
        self.ent_saturation_input_upper.grid(row=8, column=1)
        self.ent_saturation_input_upper.insert(0, str(self.saturation_input_upper))
        # Lower control saturation
        self.lbl_saturation_input_lower = tk.Label(self.tab_parameters, text='Lower control bound')
        self.lbl_saturation_input_lower.grid(row=9, column=0, padx=10)
        self.ent_saturation_input_lower = tk.Entry(self.tab_parameters)
        self.ent_saturation_input_lower.grid(row=9, column=1)
        self.ent_saturation_input_lower.insert(0, str(self.saturation_input_lower))
        # Save button
        self.btn_save_parameters = tk.Button(self.tab_parameters, text='Save')
        self.btn_save_parameters.grid(row=10, column=0, columnspan=3, sticky='we', padx=10, pady=10)

        # Controller tab
        self.txt_controller = scrolledtext.ScrolledText(self.tab_controller, width=45, height=20)
        self.txt_controller.grid(row=0, column=0, sticky='we', padx=10, pady=10)
        self.btn_save_controller = tk.Button(self.tab_controller, text='Save')
        self.btn_save_controller.grid(row=1, column=0, sticky='we', padx=10)
        self.btn_reset_controller = tk.Button(self.tab_controller, text='Reset')
        self.btn_reset_controller.grid(row=2, column=0, sticky='we', padx=10, pady=10)

        # Plant tab
        self.txt_plant = scrolledtext.ScrolledText(self.tab_plant, width=45, height=20)
        self.txt_plant.grid(row=0, column=0, sticky='we', padx=10, pady=10)
        self.btn_save_plant = tk.Button(self.tab_plant, text='Save')
        self.btn_save_plant.grid(row=1, column=0, sticky='we', padx=10)
        self.btn_reset_plant = tk.Button(self.tab_plant, text='Reset')
        self.btn_reset_plant.grid(row=2, column=0, sticky='we', padx=10, pady=10)

        #Input tab
        self.txt_input = scrolledtext.ScrolledText(self.tab_input, width=45, height=20)
        self.txt_input.grid(row=0, column=0, sticky='we', padx=10, pady=10)
        self.btn_save_input = tk.Button(self.tab_input, text='Save')
        self.btn_save_input.grid(row=1, column=0, sticky='we', padx=10)
        self.btn_reset_input = tk.Button(self.tab_input, text='Reset')
        self.btn_reset_input.grid(row=2, column=0, sticky='we', padx=10, pady=10)

        #Modeling tab
        self.model_cns = tk.Canvas(self.tab_model, width=600, height=400, bg='white')
        self.model_cns.grid(row=0, column=0)
        self.model_cns.create_line(10, 50, 70, 50, width=2, arrow='last', arrowshape='5 10 5')
        self.model_cns.create_oval(70, 40, 90, 60)
        self.model_cns.create_line(90, 50, 110, 50, width=2, arrow='last', arrowshape='5 10 5')
        self.model_cns.create_rectangle(110, 30, 180, 70)
        self.model_cns.create_text(145, 50, text='Controller')
        self.model_cns.create_line(180, 50, 350, 50, width=2, arrow='last', arrowshape='5 10 5')
        self.model_cns.create_rectangle(350, 30, 420, 70)
        self.model_cns.create_text(385, 50, text='Plant')
        self.model_cns.create_line(420, 50, 480, 50, width=2, arrow='last', arrowshape='5 10 5')
        self.model_cns.create_line(450, 50, 450, 130, width=2)
        self.model_cns.create_line(450, 130, 80, 130, width=2)
        self.model_cns.create_line(80, 130, 80, 60, width=2, arrow='last', arrowshape='5 10 5')
        self.model_cns.create_text(80, 55, text='-')
        self.model_cns.create_text(75, 50, text='+')
        self.model_cns.create_text(40, 35, text='g(t)')
        self.model_cns.create_text(100, 35, text='e(t)')
        self.model_cns.create_text(195, 35, text='u(t)')
        self.model_cns.create_text(435, 35, text='y(t)')
