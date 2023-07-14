import config as cfg
import mne
from helper_functions import get_subject_paths

class mnEEG():
    """
    
    """

    def __init__(self, subject_id):
        self.id           = subject_id
        self.raw_files    =  []
        self.ica_files    =  []
        self.epoch_files  =  get_subject_paths(self.id)
        self.fsaverage    =  get_fs_average()
        self.bem_surfaces = get_bem_surfaces()


    def forward_modeling():
        """
        Computes forward solution

        """ 

        for file in self.epoch_files:
            epochs = mne.read_epochs(file)

    def source_localization():
        """
        Computes forward solution

        """ 