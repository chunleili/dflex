
# Copyright (c) 2022 NVIDIA CORPORATION.  All rights reserved.
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

import torch

t = torch.tensor((1.0), requires_grad=True)

i = t.item()

print(i)

# Compatibility patch for urdfpy with NumPy 2.x
import numpy as np
if not hasattr(np, 'float'):
    np.float = np.float64
if not hasattr(np, 'int'):
    np.int = np.int_
if not hasattr(np, 'bool'):
    np.bool = np.bool_
if not hasattr(np, 'infty'):
    np.infty = np.inf

from urdfpy import URDF


#robot = URDF.load("assets/trifinger/urdf/trifinger_with_stage.urdf")
# robot = URDF.load("assets/franka_description/robots/franka_panda.urdf")
#robot = URDF.load("assets/anymal_b_simple_description/urdf/anymal.urdf")
#robot = URDF.load("assets/kinova_description/urdf/kinova.urdf")
#robot = URDF.load("assets/ur5/urdf/ur5_robot.urdf")
# robot = URDF.load("assets/kuka_allegro_description/allegro.urdf")
# robot = URDF.load("assets/allegro_hand_description/allegro_hand_description_left.urdf")
robot = URDF.load("assets/cartpole_double.urdf")

for link in robot.links:
    dir(link)
    print(link)

for joint in robot.joints:
    print(joint)

robot.show()

