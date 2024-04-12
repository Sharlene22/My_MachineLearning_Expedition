# Brain Tumor Detection using Deep Convolutional Neural Network
In this research, a deep convolutional neural network (CNN) architecture is implemented for the purpose of classifying brain tumors, such as gliomas, meningiomas, and pituitary disorders. Achieving high classification accuracy in a short amount of time is the main goal.

Dataset Preparation and Collection: We gathered a large Brain MRI dataset from Kaggle to use as the foundation for our model's training and testing. We used pre-processing methods on the dataset before training. In order to focus on the appropriate brain areas, the pictures had to be cropped after extreme contour points were found.

Model Architecture: Pre-trained on the ImageNet dataset, the EfficientNet-B1 model was adopted. This model balances computational economy and accuracy, which makes it appropriate for our classification job.

Training and Validation: Using a different validation dataset, the model was validated after being trained on the pre-processed training dataset. We obtained a remarkable training accuracy of 99.53% during the training process.

![image](https://github.com/KapaBhavana01/My_MachineLearning_Journey/assets/163066152/4460b989-aa53-4a59-8f39-ff9a0eadfc6c)

