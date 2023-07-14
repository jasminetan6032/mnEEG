from os.path import join
import config as cfg
import glob

def get_subject_paths(subject):
    """
    get paths to relevant files for the specified subject

    """
    file = glob.glob(join(cfg.subjects_dir,subject,'*_epo.fif'))

    return file
