import os

import torch

from flash.text import TextClassifier

# ======== Mock functions ========


class DummyDataset(torch.utils.data.Dataset):

    def __getitem__(self, index):
        return {
            "input_ids": torch.randint(1000, size=(100, )),
            "labels": torch.randint(2, size=(1, )).item(),
        }

    def __len__(self):
        return 100


# ==============================

TEST_BACKBONE = "prajjwal1/bert-tiny"  # super small model for testing


def test_init_train(tmpdir):
    if os.name == "nt":
        # TODO: huggingface stuff timing out on windows
        #
        return True
    model = TextClassifier(2, backbone=TEST_BACKBONE)
    train_dl = torch.utils.data.DataLoader(DummyDataset())
    model.fit(train_dl, fast_dev_run=True, default_root_dir=tmpdir)