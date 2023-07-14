import config as cfg
import mne
from helper_functions import get_subject_paths, get_fs_average#, get_bem_surfaces

class mnEEG():
    """
    
    """

    def __init__(self, subject_id):
        self.id           = subject_id
        self.raw_files    =  []
        self.ica_files    =  []
        self.epoch_files  =  get_subject_paths(self.id)
        self.fsaverage    =  get_fs_average()


    def forward_modeling(self, subject_id, overwrite=False ):
        """
        Computes forward solution

        """ 

        for file in self.epoch_files:
            epochs = mne.read_epochs(file)
            mne.gui.coregistration(subject='fsaverage', subjects_dir='/local_mount/space/tapputi/1/users/sergio/MNE-sample-data/subjects', inst=file)
            
    def source_localization(self, overwrite=False):
        """
        Computes forward solution

        """ 