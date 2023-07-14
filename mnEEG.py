import config as cfg
import mne

class mnEEG():
    """
    
    """

    def __init__(self, subject_id):
        self.id          = subject_id
        self.raw_files   =  [] #function to get subject paths#
        self.ica_files   =  []
        self.epoch_files =  [] #function to get subject paths#


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