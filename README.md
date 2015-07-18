## Overview of the Project:

Prigogine is a domain-specific language and development environment for scientists wanting to develop large-scale agent-based models but lacking the knowledge neccessary to take advantage of high-performance computing technology.

By utilising Python's multiprocessing module and the NumPy package for n-dimensional arrays, it is hoped that the performance capabilities of modelling frameworks like Repast HPC and FLAME, and the productiveness of a high-level language like NetLogo, can be brought together in one convenient package.

The project is at a relatively early stage and is presently focussed on getting single-core functionality up and running. The target timeframe for getting the first version released is mid-september 2015.

#### Example of Proposed Syntax:

    population "workers" [

        attributes [
            "reserveWages"
        ]

        state "employed" [
            transition to "unemployed" if uniform(1,100) >= 75
            action [
                newRW = get("reserveWages") * 1.1
                update("reserveWages", newRW)
            ]
        ]

        state "unemployed" [
            transition to "employed" if get("reserveWages") < 15
            action [
                newRW = get("reserveWages") * 0.9
                update("reserveWages", newRW)
            ]
        ]

    ]


