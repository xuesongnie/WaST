
# Wavelet-Driven Spatiotemporal Predictive Learning: Bridging Frequency and Time Variations

This codebase is based on [OpenSTL](https://github.com/chengtan9907/OpenSTL), thanks for their wonderful work.

## Installation

This project has provided an environment setting file of conda, users can easily reproduce the environment by the following commands:
```shell
git clone https://github.com/xuesongnie/WaST
cd WaST
conda env create -f environment.yml
conda activate WaST
python setup.py develop
```

<details close>
<summary>Dependencies</summary>

* argparse
* dask
* decord
* fvcore
* hickle
* lpips
* matplotlib
* netcdf4
* numpy
* opencv-python
* packaging
* pandas
* python<=3.10.8
* scikit-image
* scikit-learn
* torch
* timm
* tqdm
* xarray==0.19.0
</details>

Please refer to [install.md](docs/en/install.md) for more detailed instructions.

## Getting Started

Please see [get_started.md](docs/en/get_started.md) for the basic usage. Here is an example of single GPU non-distributed training SimVP+gSTA on Moving MNIST dataset.
```shell
bash tools/prepare_data/download_taxibj.sh
python tools/train.py -d mmnist --lr 1e-3 -c configs/taxibj/WaST.py --ex_name mmnist_wast
```

## License

This project is released under the [Apache 2.0 license](LICENSE). See `LICENSE` for more information.

## Citation

If you are interested in our repository or our paper, please cite the following paper:

```
@inproceedings{nie2024wast,
    title={Wavelet-Driven Spatiotemporal Predictive Learning: Bridging Frequency and Time Variations},
    author={Xuesong Nie and Yunfeng Yan and Siyuan Li and Cheng Tan and Xi Chen and Haoyuan Jin and Zhihang Zhu and Stan Z. Li and Donglian Qi},
    booktitle={Annual AAAI Conference on Artificial Intelligence (AAAI)},
    year={2024}
}
```