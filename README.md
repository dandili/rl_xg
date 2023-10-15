# Rocket League xG Model

This repository contains code to create a simplified expected goals (xG) model for Rocket League matches based on JSON data.

## Table of Contents
- [Introduction](#introduction)
- [Data](#data)
- [Assumptions](#assumptions)
- [Building the xG Model](#building-the-xg-model)
- [Usage](#usage)
- [License](#license)

## Introduction
Expected Goals (xG) is a statistical model used in sports analytics to estimate the probability of a shot resulting in a goal. In this repository, we create a simplified xG model for Rocket League matches using JSON data.

## Data
The xG model is built using JSON data from Rocket League matches. The JSON data contains information about player and ball positions, as well as events like shots.

## Assumptions
1. A "shot" is identified when the ball is within a certain distance of the goal.
2. A "goal" is identified when the ball's y-coordinate surpasses the goal line.

## Building the xG Model
The xG model is created in the following steps:
- Loading JSON data from Rocket League matches.
- Identifying shot events based on assumptions.
- Simulating goal outcomes based on the distance to the goal.
- Training a logistic regression model using the simulated goal outcomes and distance to goal as features.
- Evaluating the model's accuracy.

## Usage
1. Clone this repository: git clone https://github.com/yourusername/rocket-league-xg-model.git
2. Replace `'your_file_path_here.json'` in the script with the actual path to your JSON data file.
3. Run the script to build the xG model and evaluate its accuracy: python xg_model.py
4. The model will be saved as `'xG_model.joblib'` in the repository.
