## Pytorch Basics
Tensor is an important data structure of Pytorch. Pytorch tensors is like Numpy arrays but with more deep learning functionalities and is GPU friendly. GPU allows most operations with nn module and any calculations. Use model.to(device) and data.to(device) to move model and data to GPU (device='cuda') or cpu (device='cpu'). Must move model and data together, either both to cpu or both to gpu. Use `assert device == 'cuda'` to check if device is set to GPU. 

Pytorch Tensor is like Numpy array but with more functionalities including but not limited to: GPU acceleration, auto grad - automatic differentation, automatic gradient calculation, makes it easy for tensors to be a part of the forward pass and backward pass. 

There are different Pytorch libraries for different tasks such as NLP, computer vision, torch text. These are called Pytorch domain libraries. 

Pytorch has been used in both research and production. Facebook (Meta) uses Pytorch internally as well. Adoption is on the rise : At ICLR 2019, PyTorch appeared as a citation in 252 papers, up from 87 (the previous year). 

## Data Visualization, TensorBoard
[Use Tensorboard with Pytorch (Background, history) \[public\]](https://ml.learn-to-code.co/skillView.html?skill=IruUXVdkmBoenUoCGcE0)

## More Pytorch Knowledge
- **torch.nn.DataParallel** and **torch.distributed**
- **Flatten --> TORCH.FLATTEN** "Flattens input by reshaping it into a one-dimensional tensor." Python torch.flatten to turn into fully connected layer 
- **Hook --> Pytorch hooks** [Pytorch hooks (definition) use case \[public\]](https://ml.learn-to-code.co/skillView.html?skill=IcihTl4NenwDnRT3gyc7)
- **With --> Pytorch WITH** [Pytorch WITH (Definition) \[public\]](https://ml.learn-to-code.co/skillView.html?skill=6hCvXsHis0oa87reButo)
- 
