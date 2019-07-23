This is a deep learning mapping based speech enhancement

If your task is to do speech dereverberation, before run this code, you need cut data. 

Step 1. run ex_trac.sh to extract log spectrum features.

Step 2. run train.sh to train model and test.

Step 3. ca_pesq.sh evaluate your result with PESQ

I have test it in REVERB challenge dataset and it could improve PESQ about from 2 to 2.8
