
# Quantum K-Nearest Neighbors (q-KNN)

## Description
The $k$ nearest neighbor (KNN) classification is a widely-used supervised machine learning algorithm for classifying data points based on the proximity to their neighbors. This non-parametric method classifies samples by a majority vote of their neighbors, with the sample being assigned to the class most common among its $k$ nearest neighbors.

Qiskit, developed by IBM Quantum, is an open-source quantum computing software development kit (SDK) that facilitates gate-based quantum circuit design and execution. As one of the leading quantum computing frameworks, Qiskit enables users to implement quantum algorithms and provides specialized tools for various domains, such as finance and material science simulations.

In this project, we have harnessed the power of Qiskit to implement a quantum version of the KNN algorithm, often referred to as q-KNN. Our approach involves creating a quantum circuit tailored for executing the q-KNN algorithm. We begin by encoding a classical dataset into quantum states, taking advantage of quantum phenomena such as superposition and entanglement. The quantum circuit is then simulated, leveraging Qiskit's powerful simulation backend, to determine the $k$ nearest neighbors based on the quantum states' similarity.

This quantum version of the KNN algorithm aims to explore the potential speed-up and efficiency gains that quantum computing may offer over its classical counterpart. By exploiting quantum computing principles such as superposition and interference, we seek to perform the algorithm's operations in a fundamentally novel way that could only be achieved within a quantum computing framework.

![](/readme_visuals/knn_visual.png)

## Theoretical Background and Project Workflow
The K-Nearest Neighbors (KNN) algorithm is a cornerstone of machine learning, which classifies entities based on the closest training examples in the feature space. Quantum K-Nearest Neighbors (q-KNN) brings this principle into the quantum domain, harnessing the computational advantages of quantum states and entanglement.

#### Data Encoding:

In q-KNN, classical vectors $\vec{x}$ are encoded into quantum states using amplitude encoding. This process translates a classical vector into the amplitudes of a quantum state, leveraging the state's ability to exist in multiple states simultaneously (superposition). The encoding is represented as:
$$|\phi(\vec{x})\rangle=\sum_{i=1}^N \sqrt{x_i}|i\rangle,$$
where $|i\rangle$ denotes the computational basis states, and $N$ is the dimensionality of the vector space.

#### State Preparation:

The quantum state $|\psi\rangle$ of the training dataset is a superposed state of all training data points, enabling simultaneous computation:
$$|\psi\rangle=\frac{1}{\sqrt{N_{\text {train }}}} \sum_{i=1}^{N_{\text {train }}}\left|\phi\left(x^{(i)}\right)\right\rangle \otimes|i\rangle$$
with $\left|\phi\left(x^{(i)}\right)\right\rangle$ representing the amplitude-encoded quantum state of the $i$-th training sample, and $|i\rangle$ being the index qubit in superposition representing the label or the class of the training example.

#### Distance Evaluation:

The SWAP test is used to measure the overlap between quantum states, which correlates with the distance between data points in the classical space. It involves an ancillary qubit and controlled-SWAP operations to create an interference pattern from which the probability of the ancilla being in state $|0\rangle$ is indicative of the similarity between states.

#### Interference and Measurement:

Quantum interference is leveraged to measure the probability amplitude, which collapses due to the measurement postulate of quantum mechanics. The probability $P(|0\rangle)$ is computed and used to calculate the distance $D$ between the test and training samples:
$$P(|0\rangle)=\frac{1}{2}+\frac{1}{2}\left|\left\langle\phi_{\text {test }} \mid \phi_{\text {train }}\right\rangle\right|^2,$$
$$D=\sqrt{1-\left|\left\langle\phi_{\text {test }} \mid \phi_{\text {train }}\right\rangle\right|^2}$$

#### Classical Post-Processing:

After quantum measurement, classical algorithms sort the computed distances and determine the $k$ closest samples. The majority label among these nearest neighbors is assigned to the test sample.

#### Circuit Execution and Simulation:

The q-KNN algorithm is implemented on a quantum circuit and executed on a quantum simulator. The circuit consists of initialization routines, entanglement operations, SWAP tests, and measurements that collectively simulate the quantum classification process.

By integrating quantum algorithms into classical machine learning workflows, q-KNN represents a novel approach that may provide computational benefits as quantum technology evolves.

## Installation

To set up the necessary environment for running the q-KNN notebook, you need to have Python installed. All required Python libraries can be easily installed through the `requirements.txt` file included in the repository.

Please follow the steps below to install the dependencies:

```bash
# Clone the repository (if you haven't already done so)
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the required packages
pip install -r requirements.txt
```

## Code Overview

The notebook is structured into various sections, each performing a specific part of the q-KNN algorithm:

- **Data Preprocessing**: Loading and visualizing the Iris dataset. Scaling features and splitting the dataset into training and test sets.
- **Data Encoding**: Encoding the test vector and training data into quantum states.
- **Quantum Circuit Creation**: Setting up quantum registers and initializing them with the encoded data.
- **SWAP Test**: Implementing the SWAP test to compare the test vector with the training data quantum states.
- **Simulation and Measurement**: Executing the quantum circuit and measuring the results.
- **Postprocessing**: Decoding the results to compute distances and identifying the nearest neighbors.
- **Model Evaluation**: Running the q-KNN model to classify all test vectors and evaluating the model's accuracy.

Detailed explanations of each code cell are provided within the notebook, guiding you through the entire process.

## Features

- Quantum state encoding of classical data.
- Quantum circuit design for the SWAP test.
- Quantum simulation to compute distances in a quantum state space.
- Classification using the q-KNN algorithm.
- Model accuracy computation.
