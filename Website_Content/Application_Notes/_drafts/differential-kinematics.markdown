---
layout: "Application Note"
title: "Differential Drive Kinematics"
Author: Gabriel Isko
date: "2018-11-07 16:40"
---

## Using Mixed Mode

When a single axis controls the steering of a differential drive, it is called mixed steering. We provide a mixed steering feature directly on our motor controllers called Mixed Mode. Mixed mode uses the channel 1 motor command as a throttle command, and the channel 2 motor command as a steering command. In mixed mode, the controller will automatically combine, or mix, the throttle and the steering commands and calculate what output should be submitted to each channel’s control loop. There are three separate versions of Mixed Mode you can choose from on RoboteQ controllers, and each of them mix the steering command and the throttle command into an output for each channel differently. Please reference Table 7-1 from our [User Manual], which displays the motor output that is produced by different throttle and steering combinations in each of the mixing modes:

|  Input   |          | Mode 1 |       | Mode 2 |       | Mode 3 |       |
|----------|----------|--------|-------|--------|-------|--------|-------|
| Throttle | Steering | M1     | M2    | M1     | M2    | M1     | M2    |
| 0        | 0        | 0      | 0     | 0      | 0     | 0      | 0     |
| 0        | 300      | 300    | -300  | 300    | -300  | 300    | -300  |
| 0        | 600      | 600    | -600  | 600    | -600  | 600    | -600  |
| 0        | 1000     | 1000   | -1000 | 1000   | -1000 | 1000   | -1000 |
| 0        | -300     | -300   | 300   | -300   | 300   | -300   | 300   |
| 0        | -600     | -600   | 600   | -300   | 300   | -600   | 600   |
| 0        | -1000    | -1000  | 1000  | -1000  | 1000  | -1000  | 1000  |
| 300      | 300      | 600    | 0     | 600    | 0     | 522    | 90    |
| 300      | 600      | 900    | -300  | 900    | -300  | 762    | -120  |
| 300      | 1000     | 1000   | -700  | 1000   | -1000 | 1000   | -400  |
| 300      | -300     | 0      | 600   | 0      | 600   | 90     | 522   |
| 300      | -600     | -300   | 900   | -300   | 900   | -120   | 762   |
| 300      | -1000    | -700   | 1000  | -1000  | 1000  | -400   | 1000  |
| 600      | 300      | 900    | 300   | 900    | 300   | 708    | 480   |
| 600      | 600      | 1000   | 0     | 1000   | -200  | 888    | 360   |
| 600      | 1000     | 1000   | -400  | 1000   | -1000 | 1000   | 200   |
| 600      | -300     | 300    | 900   | 300    | 900   | 480    | 708   |
| 600      | -600     | 0      | 1000  | -200   | 1000  | 360    | 888   |
| 600      | -1000    | -400   | 1000  | -1000  | 1000  | 200    | 1000  |
| 1000     | 300      | 1000   | 700   | 1000   | 400   | 900    | 1000  |
| 1000     | 600      | 1000   | 400   | 1000   | -200  | 1000   | 1000  |
| 1000     | 1000     | 1000   | 0     | 1000   | -1000 | 1000   | 1000  |
| 1000     | -300     | 700    | 1000  | 400    | 1000  | 1000   | 900   |
| 1000     | -600     | 400    | 1000  | -200   | 1000  | 1000   | 1000  |
| 1000     | -1000    | 0      | 1000  | -1000  | 1000  | 1000   | 1000  |



For most applications, Mixing Mode 1 will be the best option.
You can enable mixed mode from the configuration tab of Roborun+:

![](FAQ_Images/Mixed_Mode_Robroun.png "Mixed Mode 1")


## Calculating Rotational Velocity in Mixed Mode

If you would like to control the Robot's rotational velocity in mixed mode, calculating the steering is possible. The following is a guide to the calculation.

The first step is to define our terms. We will use $T_C$ for our throttle command and $S_C$ for our steering command. As you can see from the above table, the commands going to our indvidual motor outputs are calculated as follows in `Mixed Mode 1`:


$$M1 = T_C + S_C $$
$$M2 = T_C - S_C $$

$$\Delta M = M1 - M2 $$
$$\Delta M = 2S_C $$

Next Comes our rotational angle in radians, which can be calculated with $\Delta M$

$$\theta = $$



wheel speed is $v$ turn radius is $r$ period is $T$

$$v=\frac{2\pi r}{T}$$



angular velocity is $\omega$
$$\omega = \frac{2\pi}{T}$$

Robot angular velocity
$$\omega r= v $$

wheelbase is $l$
decomposing indvidual angular velocity per wheel:
$$\omega (R+\frac {l}{2}) = v_r$$
$$\omega (R-\frac {l}{2}) = v_r$$

<!--
Once we have the wheels we can calculate the forward kinematics. -->
<!-- FAQ Reference List -->

[User Manual]:https://www.roboteq.com/index.php/docman/motor-controllers-documents-and-files/documentation/user-manual/272-roboteq-controllers-user-manual-v17/file "User Manual"

[Differential Drive Kinematics]: http://www8.cs.umu.se/kurser/5DV122/HT13/material/Hellstrom-ForwardKinematics.pdf

[Differential Drive Dynamics]: https://www.omicsonline.org/open-access/dynamic-modelling-of-differentialdrive-mobile-robots-using-lagrange-and-newtoneuler-methodologies-a-unified-framework-2168-9695.1000107.pdf
