from os.path import join
import os.path as op
import config as cfg
import mne

def get_subject_paths(subject):
    """
    get paths to relevant files for the specified subject

    """
    subject
    epoch_path = join(cfg.subjects_dir )

    return epoch_path


def get_fs_average():
    """
    gets bem filepath
    """
    
    mne_dataset_dir = mne.get_config('MNE_DATASETS_SAMPLE_PATH')
    fsaverage_dir = [join(mne_dataset_dir, 'MNE-sample-data','subjects','fsaverage')]
    
    # bem_filepath = join(fsaverage_dir,'bem','fsaverage-ico-5-src.fif')
    print(f'The bem filepath is {fsaverage_dir}')
    
    return fsaverage_dir #, bem_filepath
