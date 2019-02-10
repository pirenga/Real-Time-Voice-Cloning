import audio
import numpy as np
from vlibs import fileio
from ui.speaker_matrix_ui import SpeakerMatrixUI
from data_objects.speaker_verification_dataset import SpeakerVerificationDataLoader
from data_objects.speaker_verification_dataset import SpeakerVerificationDataset
from config import *

if __name__ == '__main__':
    dataset = SpeakerVerificationDataset(all_datasets)
    loader = SpeakerVerificationDataLoader(dataset, 3, 4, num_workers=3)
    for batch in loader:
        SpeakerMatrixUI(batch.speakers, batch.partial_utterances)
    