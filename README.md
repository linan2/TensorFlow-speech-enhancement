This is a deep learning mapping based speech enhancement

If your task is to do speech dereverberation, before running this code, you need cut data. 

Step 1. run ex_trac.sh to extract log spectrum features.

Step 2. run train.sh to train model and test.

Step 3. ca_pesq.sh evaluate your result with PESQ

I have tested it in REVERB challenge dataset and it could improve PESQ about from 2 to 2.8

Lately, we will update some GAN, Multi-task learning, and Multi-object learning-based model, some attention mechanism-based model also will be updated.

In the decode stage, you can choose G&L vocoder and you also could use the noisy speech original phase to synthetic speech, but I have tried G&L method it will not get better performance compared with use for original phase.
