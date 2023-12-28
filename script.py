import mne

def convert_edf_to_csv(edf_file, csv_file):
    # Load the EEG data from the .edf file
    raw = mne.io.read_raw_edf(edf_file, preload=True)

    # Save the EEG data to a .csv file
    raw.to_data_frame().to_csv(csv_file, index=False)

# Replace 'input_file.edf' and 'output_file.csv' with your file names
convert_edf_to_csv('rsvp_10Hz_02a.edf', 'op.csv')
