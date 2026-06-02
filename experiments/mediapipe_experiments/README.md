# MediaPipe Experiments

## Overview

This directory contains a simple experiment created to explore the basic functionality of MediaPipe Hands. The purpose of this exercise was to understand how hand landmark detection works and how landmark data can be accessed and used within a Python application.

## Experiment

### Hand Tracking Demo

The experiment performs the following tasks:

* Captures live video from a webcam
* Detects hands using MediaPipe Hands
* Tracks the 21 hand landmarks provided by the model
* Draws the detected landmarks and hand connections
* Extracts landmark coordinates for further processing

## Purpose

This experiment served as the foundation for the final gesture recognition system developed in this repository. Understanding how to access and interpret hand landmark data was essential before implementing gesture classification logic such as Palm, Fist, and Pinch detection.

## Technologies

* Python
* MediaPipe
* OpenCV

## Learning Outcomes

Through this experiment, I gained familiarity with:

* MediaPipe Hands API
* Hand landmark indexing
* Landmark coordinate extraction
* Real-time hand tracking
* Integration of MediaPipe with OpenCV video streams

## Notes

This folder contains only the initial hand-tracking prototype used to understand MediaPipe's landmark detection capabilities before moving on to more advanced gesture recognition applications.
