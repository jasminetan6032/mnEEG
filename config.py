from os import getlogin

users_dictionary = {'jwt30' :'/local_mount/space/hypatia/2/users/Jasmine/mnEEG_subjects',
                    'sao42' : '/local_mount/space/tapputi/1/users/sergio/mnEEG_subjects' ,
                    'asus'  : '/D:/source_hackaton/mneEEG_subject/'}

subjects_dir = users_dictionary[getlogin()]

