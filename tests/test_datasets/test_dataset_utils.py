import os.path as osp
import random
import string

from openstl.datasets.utils import check_integrity, rm_suffix


def test_dataset_utils():
    # test rm_suffix
    assert rm_suffix('a.jpg') == 'a'
    assert rm_suffix('a.bak.jpg') == 'a.bak'
    assert rm_suffix('a.bak.jpg', suffix='.jpg') == 'a.bak'
    assert rm_suffix('a.bak.jpg', suffix='.bak.jpg') == 'a'

    # test check_integrity
    rand_file = ''.join(random.sample(string.ascii_letters, 10))
    assert not check_integrity(rand_file, md5=None)
    assert not check_integrity(rand_file, md5=2333)
    test_file = osp.join(osp.dirname(__file__), '../../data/color.jpg')
    assert not check_integrity(test_file, md5=2333)