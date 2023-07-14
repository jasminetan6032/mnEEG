from mnEEG import mnEEG

# subject identifier or function to get all subject identifiers
subjects = ['sub-05']  

for sub_i in subjects:

    # initialize mnEEG object
    sub = mnEEG(sub_i)

    # find bad channels

    # do ICA / SSP

    # epoch data

    # forward modeling
    sub.forward_modeling(overwrite=False)

    # source localization
    sub.source_localization(overwrite=False)
    