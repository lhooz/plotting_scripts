"""script for mesh and convergence figure plots"""

import os

from tplotting_functions import cf_plotter, read_cfd_data

#-------------input plot control----------
kinematics_file = 'kinematics.dat'
cfd_data_list = [
    'ar1.5_ofs0.0_r1h0.5__Re100.0_pt0.25',
    'ar1.5_ofs1.0_r1h0.5__Re100.0_pt0.25',
    'ar1.5_ofs2.0_r1h0.5__Re100.0_pt0.25',
    'ar1.5_ofs3.0_r1h0.5__Re100.0_pt0.25',
]
#-----------------------------------------
mistake_scales2 = []
for name in cfd_data_list:
    ari = name.split('_')[0].split('ar')[1]
    ari = float(ari)
    ofsi = name.split('_')[1].split('ofs')[1]
    ofsi = float(ofsi)
    mscalei = ((ari + ofsi) / ari)**2
    mistake_scales2.append(mscalei)
#-----------------------------------------
legends = [
    r'$\hat r_R$ = 0',
    r'$\hat r_R$ = 1',
    r'$\hat r_R$ = 2',
    r'$\hat r_R$ = 3',
]
#-----------------------------------------
time_to_plot = 'all'
coeffs_show_range = 'all'
time_to_plot = [4.0, 5.0]
show_range_cl = [-1.5, 4.5]
show_range_cd = [-1.5, 4.5]
cycle_time = 1.0
#---------------------------------------
show_range = [show_range_cl, show_range_cd]
#-----------------------------------------
cwd = os.getcwd()
kinematics_dir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(cwd))),
    'geometry_effect_fw_data/1_kinematic_cases')
data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(cwd))),
                        'geometry_effect_fw_data/5_SIM_RESULTS')
image_out_path = cwd
#-----------------------------------------
kinematics_data = os.path.join(kinematics_dir, kinematics_file)
CF_file_names = [f.name for f in os.scandir(data_dir) if f.is_file()]
cf_array = []
for cfi, mscale in zip(cfd_data_list, mistake_scales2):
    for CF_name in CF_file_names:
        if CF_name.startswith(cfi):
            cfd_datai = os.path.join(data_dir, CF_name)
            cf_arrayi = read_cfd_data(kinematics_data, cfd_datai, mscale)
            cf_array.append(cf_arrayi)

data_array = cf_array
#---------------------------------------

cf_plotter(data_array, legends, time_to_plot, show_range, image_out_path,
           cycle_time, 'against_t')
