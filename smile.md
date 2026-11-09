---
layout: page
title: SMILE training tools
nav_title: SMILE tools
permalink: /smile/
eyebrow: Cleanroom education
intro: Semiconductor Manufacturing via Innovative Learning Experience
---
SMILE provides three levels of cleanroom training, from browser-based exploration to augmented reality guidance during a procedure. The tools are being adapted and tested for use in the Mines Nanofabrication Facility.

For more information and materials, visit [Zafer Mutlu’s training resources](https://zafermutlu.arizona.edu/annlab/training).

<section class="resource" markdown="1">
<span class="tag">Level 1 · Browser · Complete as of November 2026</span>

## Interactive videos


<figure class="slide-figure">
<a href="https://hpss.mines.edu/smile-2dvp/demo.html"><img src="{{ '/assets/images/smile-interactive-video.jpg' | relative_url }}" width="1600" height="980" loading="lazy" alt="SMILE browser video showing labeled equipment in a yellow-lit cleanroom."></a>
<figcaption>Interactive video demo: equipment is outlined and labeled in the cleanroom video.</figcaption>
</figure>

A neural network outlines and labels equipment in a cleanroom video. Selecting a tool opens its process description, photos, and components. The demo runs in a browser without a headset or app installation.

[Open the interactive video demo](https://hpss.mines.edu/smile-2dvp/demo.html)
</section>

<section class="resource" markdown="1">
<span class="tag">Level 2 · Browser or VR · Complete as of November 2026</span>

## 360° cleanroom tour


<figure class="slide-figure">
<a href="https://hpss.mines.edu/smile-2dvp/tour.html"><img src="{{ '/assets/images/smile-cleanroom-tour.jpg' | relative_url }}" width="1600" height="777" loading="lazy" alt="360-degree tour interface with cleanroom view, navigation floor plan, and equipment information panel."></a>
<figcaption>The browser tour combines a panoramic cleanroom view, a floor plan, and equipment details.</figcaption>
</figure>

Explore a photo-mapped cleanroom with a floor plan and tool information panels. The tour is available in a regular browser and through WebXR on a Meta Quest 3 headset.

[Open the browser tour](https://hpss.mines.edu/smile-2dvp/tour.html) · [Open the WebXR tour](https://hpss.mines.edu/smile-2dvp/webxr.html)
</section>

<section class="resource" markdown="1">
<span class="tag">Level 3 · HoloLens 2 · Research system</span>

## AR cleanroom assistant (ARCA)


<figure class="slide-figure">
<img src="{{ '/assets/images/arca-cleanroom-assistant.png' | relative_url }}" width="2252" height="1268" loading="lazy" alt="ARCA headset view with labeled spin coater, controller, pump, and wafer, alongside instructions for step 3 of a 44-step procedure.">
<figcaption>ARCA guides the learner to the spin coater. The panel shows completed, current, and next steps while boxes identify the equipment and wafer.</figcaption>
</figure>

ARCA displays the current procedure step and outlines the equipment needed for it. Gaze interaction and virtual buttons let learners move through instructions and request help. The spin-coating demonstration guides a learner through a 44-step procedure.


<figure class="slide-figure">
<img src="{{ '/assets/images/arca-pipeline.jpg' | relative_url }}" width="1600" height="690" loading="lazy" alt="ARCA pipeline linking vendor images and captured frames to object recognition, and course modules to live instructions on HoloLens.">
<figcaption>ARCA pipeline: equipment images support object recognition; course modules supply instructions displayed on the headset.</figcaption>
</figure>

ARCA uses equipment detection rather than requiring a digital twin of the cleanroom. Contact the project team about the headset system and research collaboration.
</section>

## Research in progress

The team is studying spatial awareness and verification of trainee actions. Current work combines hand-object detection with cleanroom tool detection to identify which object a hand holds or touches. Planned work includes depth, eye tracking, spatial maps, and procedure-step checks in ARCA.

Student research topics include reducing detection latency, moving models to edge devices, and evaluating the tools with cleanroom trainees.

## People and support

SMILE is led by project PI **[Zafer Mutlu](https://zafermutlu.arizona.edu/)** (University of Arizona). Other project investigators include **Mehmet E. Belviranli** (Colorado School of Mines) and **B. Kim** (University of Arizona). SMILE is funded by the **DoD Microelectronics Commons through the ASU SWAP Hub**. Its integration into CoRTEX is part of the [NNME Southwest](https://nnme.org/nnme-southwest/) effort.

[Contact Mehmet Belviranli](mailto:belviranli@mines.edu) · [HPSS Lab](https://hpss.mines.edu/)
