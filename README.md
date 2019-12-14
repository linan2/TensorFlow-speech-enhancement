English | [中文](https://github.com/linan2/TensorFlow-speech-enhancement-Chinese.git) 
# This is a deep learning mapping based speech enhancement method.
The purpose of this project is to use the methods of DNN and CNN for speech enhancement, in which DNN uses three hidden layers with 512 nodes per hidden layer. CNN uses the network structure of R-CED and adds some resnet to prevent overfitting. 
You can also choose whether to use dropout or L2 and so on.
## Attention:
[make data](https://github.com/linan2/add_reverb2.git) before use this method you should have clean and corresponding noisy data.
If your task is to do speech dereverberation, before running this code, you need cut data. The script in the cut_wav is helpful for you. 
If your task is to do feature enhancement, you can replace the log spetragram feature to other feature, e.g. MFCC

## To use:
Step 1. run ex_trac.sh data prepare and extract log spectragram features.

Step 2. run train.sh to train model and test.

Step 3. ca_pesq.sh evaluate your result with PESQ

## Ps:
The code is not perfect, continue to update…

I have tested it in REVERB challenge dataset and it could improve PESQ about from 2 to 2.8

Lately, we will update some GAN, Multi-task learning, and Multi-object learning-based model, some attention mechanism-based model also will be updated.

In the decode stage, you can choose G&L vocoder and you also could use the noisy speech original phase to synthetic speech, but I have tried G&L method it will not get better performance compared with use for original phase.

[1] Li N., Ge M., Wang L., Dang J. (2019) [A Fast Convolutional Self-attention Based Speech Dereverberation Method for Robust Speech Recognition](https://link.springer.com/chapter/10.1007/978-3-030-36718-3_25). In: Gedeon T., Wong K., Lee M. (eds) Neural Information Processing. ICONIP 2019. Lecture Notes in Computer Science, vol 11955. Springer, Cham

[2] Wang, K., Zhang, J., Sun, S., Wang, Y., Xiang, F., Xie, L. (2018) Investigating Generative Adversarial Networks Based Speech Dereverberation for Robust Speech Recognition. Proc. Interspeech 2018, 1581-1585, DOI: 10.21437/Interspeech.2018-1780.

[3] Ge, M., Wang, L., Li, N., Shi, H., Dang, J., Li, X. (2019) Environment-Dependent Attention-Driven Recurrent Convolutional Neural Network for Robust Speech Enhancement. Proc. Interspeech 2019, 3153-3157, DOI: 10.21437/Interspeech.2019-1477.


Email: linanvae@163.com
