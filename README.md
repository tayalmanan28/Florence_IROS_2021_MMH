# FLORENCE (Fast Learning and Observant Robot for Empowering and Nursing in Containment Environments) 
<a href="https://iros2021-mmh.pal-robotics.com/">IROS 2021 Mobile Manipulation Hackathon</a> by <a href="https://pal-robotics.com/">PAL Robotics</a>

## Overview
In the light of the present pandemic, it has become a key necessity to control the spread and decrease the impact of the virus in the greatest manner possible. We present an intelligent nurse, FLORENCE, who, in a containment facility, detects the face of each patient and administers the patient’s unique set of medicines from a separate trolley based on a predetermined database. She further checks the patient’s temperature and updates the information in the database. This prevents the need for a human nurse to approach the patient and hence reduces the risk of spreading the disease. On detection or by request, FLORENCE sprays sanitizer on the hands of patients and visitors. For the purpose of serving the patient, she also uses a hybrid of the original hand and a specially designed hand with three fingers. We intend to perform the simulations on the WeBots platform prior to the implementation of FLORENCE on the TIAGo++ robot by PAL Robotics.

## System Flowcharts
FLORENCE is an automated robotic nurse who is capable of providing several amenities to visitors and patients in a containment facility. As a result of her multifaceted nature, her design is heavily modular. The main functionality of FLORENCE is controlled by the MAIN loop whereas two INTERRUPTS may break the loop
at any instant the trigger (mentioned in the interrupt block) is provided. On a regular basis, FLORENCE attends the beds in the room one after the other. At each 
bed, she searches for the presence of a patient corresponding to the bed.
- If there is an unknown person on the bed despite there being no entry for the same in the database, FLORENCE alerts a human nurse for inspection.
- If a patient is detected on a non-empty bed, FLORENCE detects their face and updates the patient number. Furthermore, she checks the temperature of the patient and serves medicine if the patient has not had their dose for that time of the day. Finally, she updates the patient’s report in the database and moves to the next bed.
![image](https://user-images.githubusercontent.com/42448031/126081273-482a812c-13ae-4c6e-a647-9d082b92e19a.png)

## Simulations and Results

We have performed the robot simulations on the Webots platform to demonstrate the working of FLORENCE. On the other hand, we have performed tests of the face recognition algorithm on Python using the Google Colabs platform. At the same time, we present a demonstration of the working of the database that contains a list of patients and visitors along with data points that represent the last time of detection, whether the patient’s medicine has been served, and other critical functionalities. We intend to merge these three processes for the TIAGo++ robot at the finals of the hackathon.

### [Project Documentation](https://github.com/tayalmanan28/Florence_IROS_2021_MMH/blob/main/Documentation.pdf)
### [Simulation Video](https://youtu.be/tGd-sEsKtbg)
### [Open Sourced Code](https://github.com/tayalmanan28/Florence_IROS_2021_MMH)

<p align='center'>Created with :heart: by <a href="https://github.com/tayalmanan28">Manan Tayal</a>, <a href="https://github.com/aaronjohnsabu1999">Aaron John Sabu</a>, & <a href="https://github.com/rnambilakshmi">Nambilakshmi Ramachandran</a></p>
