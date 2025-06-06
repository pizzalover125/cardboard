---
title: "Cardboard"
author: "pizzalover125"
description: "A credit-card-sized keyboard. "
created_at: "2025-06-02"
---
**Time Spent: 8 hours**

## 6/2/25
### Idea
I actually thought of this project while sitting in a car. I already have built a macropad on a card, so I thought, "why not go further?." That's exactly what I did. So I began as all other projects and did research. 

### Research
I was trying to find the smallest button commerically available. After some quick math, I came up with the B3U-1000P. They're used in microcontrollers for resetting and stuff. I then began schematic design. I originally wanted to use a bare RP2040, but realized it wouldn't be worth risking. Then I thought about using a Orpheus Pico. However, it was just too big. So I ended up using a Xiao with a GPIO extender. Note that I made a layout and schematic for all 3 PCB iterations. 

### Schematic
Ok then I made the schematic. It was super easy, and I mostly modeled it off my prior keyboard I designed. 

### PCB
Then, I made the PCB. That was also super easy. However, I have to use vias as i'm using SMD components, which is bad for signal integrity. However, I'm just going to roll with it as this keyboard is near impossible to type on. Finally, I added some logos. 

### Firmware
I also made the firmware with previous firmware I had designed. Note that the Keyboard Layout was made by ChatGPT originally, and then I edited it a bit. Here is the finished product:

![image](https://github.com/user-attachments/assets/f2a174b7-7085-4089-a3dc-0c98b2d84c02)
