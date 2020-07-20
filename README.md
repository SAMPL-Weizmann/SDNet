# About this repo
Spatial Decomposition Network (SDNet) for content (anatomy) and style (modality) disentanglement.

This repo delivers the **PyTorch implementation** of the SDNet model presented in this [paper](https://www.sciencedirect.com/science/article/abs/pii/S1361841519300684). The original SDNet is implemented in Keras by the first author of the paper [Agis85](https://github.com/agis85/anatomy_modality_decomposition). This version of SDNet focuses on the comparison between spatial and vectorized latent space for the anatomy encoding (many variants are included). To actually compare the different variants, the segmentation task is adopted, using the **ACDC cardiac imaging dataset** (as in the original paper).

## Prerequisites
All coding and experiments were using the following setup:
* PyTorch 1.5.1
* Cuda 10.1
* Python 3.7.5
* [Visdom](https://github.com/facebookresearch/visdom) - loss plots, images, etc.

## Training
To see all the available training (hyper)parameters use:
`python main.py -h`

Available SDNet variants:
1. Original architecture - UNet to encode anatomy in spatial latent variable (Variant A)
..* Gumbel Softmax is used instead of the binarization module for the UNet output --> smoother Dice loss convergence and a 3% increase in the validation accuracy
2. A VAE is used to encode the anatomy in a vector latent space (Variant B)
3. A VAE is used to re-encode the spatial output of the UNet - VAE output is used by the segmentor and the decoder (Variant C)
4. A VAE is used to re-encode the spatial output of the UNet - VAE output is used only by the segmentor, while the decoder uses UNet output(Variant D)
