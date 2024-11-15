# UAV-Operator-s-evaluation-system
Project made as a part of master thesis
The main aim of the project is to bring together two very fast-growing fields - drones and machine learning. The experience of the war in Ukraine shows us how important drones are. However, drones without properly trained operators are not very useful, even with the best avionics. The project was developed to verify the skills and aptitude of potential operators. The system also uses virtual reality (VR) to better reflect real-world flight conditions. The assessment of drone pilots takes place in two phases. 
The first assesses the operator's skills in controlling an unmanned aircraft and consists of ten challenging levels, consisting of a specific task. For example, the first task requires the test subject to fly to a selected position. The level of sophistication increases with each task. Therefore, wind gusts were simulated for four tasks, the strength of which increases with each challenge. During this stage of the test, the emotions and heart rate of the person being assessed are measured. The emotion measurement uses a deep learning model trained on the FER2013+ dataset. The heart rate measurement consists of three values: 
- The mean of the values documented during one task 
- The variance of the values documented during one task 
- The ratio of the difference between the maximum and minimum heart rate values documented during one task to the time between these values.
  
All three of the above values are documented during each task and saved to a .csv file. During the tasks, each is also communicated to the user via voice message.
The second task is to verify the pilot's reactions to the dynamically changing environment. VR was used to test these reactions. When controlling any aircraft, it is very important to maintain spatial orientation. The virtual reality test aims to verify how the test subject reacts to sudden changes in the position of the unmanned aircraft. The test is conducted by subjecting the testee to further, more advanced changes in angular position, speed or altitude. The test, like the first stage, consists of ten stages varying in stimulus intensity. During the test, the values received from the pulse sensor are checked to obtain the body's response to the changes. The same three values are checked as in the first stage. 
The values recorded during both stages of testing are the input values of the deep learning models. In order to create a model that can assess a subject's predisposition, it is necessary for the training data to have labels suitable for this purpose (the output on which the model learns), which is the most important step in the data preprocessing stage.  Since it is a very difficult and almost impossible task to train a single network that would operate on a single set consisting of all the data recorded during the survey without having a very large dataset, it was decided to create four smaller networks: 
- A network assessing the performance of the tasks set to the subject during the first stage
- Heart rate network for the first stage
- A network assessing the subject's emotions recorded during the first stage
- A network assessing the subject's heart rate during the virtual reality tests

All networks had to assign an output variable, which was their assessment, to the corresponding input data sets. Two categories of output variables were considered: positive and negative ratings. All output values from the neural networks evaluating the different factors were assigned the corresponding position in the binary system, thanks to this solution it is possible to directly decide which factor is more relevant to the BSP operator from our point of view. 

# Attention!
Repo is only for presentation purposes it may not work from many reasons such:
- you are supposed to be equipped with heart rate sensor
- you are supposed to have installed AirSim simulator
- you have to be equipped with VR googles

So if you dont mind, take code and read. However you will not withstand till the end because its my first very big project. Thanks for your forbearance!
