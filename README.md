<div align="center">

<img src="assets/banner.png" width="100%">

# Safety in Embodied AI: A Survey of Risks, Attacks, and Defenses

[![arXiv](https://img.shields.io/badge/arXiv-2605.02900-b31b1b.svg)](https://arxiv.org/abs/2605.02900)
[![Website](https://img.shields.io/badge/Website-Project%20Page-blue.svg)](https://x-zheng16.github.io/Awesome-Embodied-AI-Safety/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Papers](https://img.shields.io/badge/Papers-559-blue.svg)](#surveyed-papers)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/x-zheng16/Awesome-Embodied-AI-Safety/pulls)
[![GitHub stars](https://img.shields.io/github/stars/x-zheng16/Awesome-Embodied-AI-Safety?style=social)](https://github.com/x-zheng16/Awesome-Embodied-AI-Safety)

**A comprehensive survey and the first unified safety framework for embodied AI, covering 500+ key works across perception, cognition, planning, interaction, and agentic systems.**

[[arXiv]](https://arxiv.org/abs/2605.02900) | [[Website]](https://x-zheng16.github.io/Awesome-Embodied-AI-Safety/)

</div>

## Authors

<div align="center">

<a href="https://openreview.net/profile?id=~Xiao_Li22" target="_blank" rel="noopener">Xiao Li</a><sup>1,&#42;</sup>,
<a href="https://x-zheng16.github.io/" target="_blank" rel="noopener">Xiang Zheng</a><sup>4,&#42;</sup>,
<a href="https://github.com/SFTJBD" target="_blank" rel="noopener">Yifeng Gao</a><sup>1</sup>,
<a href="https://xinyuxia97.github.io/" target="_blank" rel="noopener">Xinyu Xia</a><sup>5</sup>,
<a href="https://scholar.google.com/citations?hl=zh-CN&user=EYP7wNIAAAAJ&view_op=list_works&sortby=pubdate" target="_blank" rel="noopener">Yixu Wang</a><sup>1</sup>,
<a href="https://xinwong.github.io/" target="_blank" rel="noopener">Xin Wang</a><sup>1</sup>,
<a href="https://openreview.net/profile?id=%7EYe_Sun1" target="_blank" rel="noopener">Ye Sun</a><sup>1</sup>,
<a href="https://github.com/Vinsonzyh" target="_blank" rel="noopener">Yunhan Zhao</a><sup>1</sup>,
<a href="https://scholar.google.com/citations?hl=en&user=7b8QWAMAAAAJ&view_op=list_works&sortby=pubdate" target="_blank" rel="noopener">Ming Wen</a><sup>1,3</sup>,
<a href="https://github.com/lijayuTnT" target="_blank" rel="noopener">Jiayu Li</a><sup>1</sup>,
<a href="https://openreview.net/profile?id=~Zixing_Chen2" target="_blank" rel="noopener">Zixing Chen</a><sup>1</sup>,
<a href="https://sites.google.com/view/xungong-jlu-ai/home" target="_blank" rel="noopener">Xun Gong</a><sup>5</sup>,
<a href="https://scholars.cityu.edu.hk/en/persons/yiliu247/" target="_blank" rel="noopener">Yi Liu</a><sup>4</sup>,
<a href="https://github.com/bboylyg" target="_blank" rel="noopener">Yige Li</a><sup>6</sup>,
<a href="https://github.com/wuyoscar" target="_blank" rel="noopener">Yutao Wu</a><sup>7</sup>,
<a href="https://www.cs.cityu.edu.hk/~congwang/" target="_blank" rel="noopener">Cong Wang</a><sup>4</sup>,
<a href="https://sunjun.site/" target="_blank" rel="noopener">Jun Sun</a><sup>6</sup>,
<a href="https://taominer.github.io" target="_blank" rel="noopener">Yixin Cao</a><sup>1,2,3</sup>,
<a href="https://zhinchenfd.github.io/" target="_blank" rel="noopener">Zhineng Chen</a><sup>1,3</sup>,
<a href="https://jingjing1.github.io/" target="_blank" rel="noopener">Jingjing Chen</a><sup>1,3</sup>,
<a href="https://guitaowufeng.github.io/" target="_blank" rel="noopener">Tao Gui</a><sup>1,2,3</sup>,
<a href="http://qizhang.info/" target="_blank" rel="noopener">Qi Zhang</a><sup>1,3</sup>,
<a href="https://zxwu.azurewebsites.net/" target="_blank" rel="noopener">Zuxuan Wu</a><sup>1,2,3</sup>,
<a href="https://xpqiu.github.io/" target="_blank" rel="noopener">Xipeng Qiu</a><sup>1,2,3</sup>,
<a href="https://xuanjing-huang.github.io/" target="_blank" rel="noopener">Xuanjing Huang</a><sup>1,3</sup>,
<a href="https://tiehuaz.github.io" target="_blank" rel="noopener">Tiehua Zhang</a><sup>8</sup>,
<a href="https://zhipeng-wei.github.io/" target="_blank" rel="noopener">Zhipeng Wei</a><sup>10</sup>,
<a href="https://home-gamma-ten.vercel.app/" target="_blank" rel="noopener">Kun Wang</a><sup>11</sup>,
<a href="https://letterligo.github.io/" target="_blank" rel="noopener">Xinfeng Li</a><sup>11</sup>,
<a href="https://hanxunh.github.io/" target="_blank" rel="noopener">Hanxun Huang</a><sup>13</sup>,
<a href="https://people.eng.unimelb.edu.au/smonazam/" target="_blank" rel="noopener">Sarah Erfani</a><sup>13</sup>,
<a href="https://people.eng.unimelb.edu.au/baileyj/" target="_blank" rel="noopener">James Bailey</a><sup>13</sup>,
<a href="https://www.cs.cityu.edu.hk/~jianwang/index.html" target="_blank" rel="noopener">Jianping Wang</a><sup>4</sup>,
<a href="https://xiaocw11.github.io/" target="_blank" rel="noopener">Chaowei Xiao</a><sup>14</sup>,
<a href="https://rhe-web.github.io/" target="_blank" rel="noopener">Ran He</a><sup>12</sup>,
<a href="https://aisecure.github.io/" target="_blank" rel="noopener">Bo Li</a><sup>9</sup>,
<a href="http://xingjunma.com/" target="_blank" rel="noopener">Xingjun Ma</a><sup>1,2,3,&dagger;</sup>,
<a href="https://scholar.google.com/citations?hl=en&user=f3_FP8AAAAAJ&view_op=list_works&sortby=pubdate" target="_blank" rel="noopener">Yu-Gang Jiang</a><sup>1,3,&dagger;</sup>

<sup>1</sup>Institute of Trustworthy Embodied AI, Fudan University, <sup>2</sup>Shanghai Innovation Institute, <sup>3</sup>Shanghai Key Laboratory of Multimodal Embodied AI, <sup>4</sup>City University of Hong Kong, <sup>5</sup>Jilin University, <sup>6</sup>Singapore Management University, <sup>7</sup>Deakin University, <sup>8</sup>Tongji University, <sup>9</sup>UIUC, <sup>10</sup>UC Berkeley, <sup>11</sup>Nanyang Technological University, <sup>12</sup>Chinese Academy of Sciences, <sup>13</sup>The University of Melbourne, <sup>14</sup>Johns Hopkins University

<sup>&#42;</sup>Equal Contribution, <sup>&dagger;</sup>Corresponding Authors

</div>

## 🔥 News

- **[2026/06/01]** Added an interactive **At a Glance** dashboard to the [project page](https://x-zheng16.github.io/Awesome-Embodied-AI-Safety/): papers-per-year, a clickable taxonomy sunburst, and venue-type and top-venue charts, all rendered live from the paper list and cross-filtering it on click. Author citations across the list were also standardized.
- **[2026/05/30]** Added a **Paper Reader** page ([papers.html](https://x-zheng16.github.io/Awesome-Embodied-AI-Safety/papers.html)) for browsing abstracts and keywords, with search across titles, authors, venues, and keywords, plus taxonomy-layer filtering.
- **[2026/05/25]** Featured by Chinese AI & tech media: [机器之心](https://mp.weixin.qq.com/s/N_F0JG_-0R6tiI6b5-HFWg), [专知](https://mp.weixin.qq.com/s/ysMbG6ryVpy5t6Ug6IMwpA), [机器学习算法与自然语言处理](https://mp.weixin.qq.com/s/oHa9LLTnKkvaDqkXVaP08g), [AI与安全](https://mp.weixin.qq.com/s/lXkKpvotnsJNmAzUZloufw), [AI思想会](https://mp.weixin.qq.com/s/z6dCPpK-9JOOJbZqsDR42A), [非具身不智能](https://mp.weixin.qq.com/s/5JFjNUHDSOnF7F6M3lWdzw), [诺亚星辰](https://mp.weixin.qq.com/s/i_5QV1T_Nh7I-gYnueGyMA), and [小红书](https://www.xiaohongshu.com/discovery/item/69ff39f6000000001a03681e?xsec_token=CBI2FPaypbvuiLoumuwww7qzhVgtPFgtWVxoWRh5zCSmw%3D&xsec_source=app_share).
- **[2026/05/24]** arXiv v2 released; integrated further 2026-04 / 2026-05 arXiv papers across all 5 layers; URL re-verification across the paper list fixed title truncations and shifted Google Scholar links to arXiv where available. Survey now indexes **500+ papers** across **38 co-authors** from **13 institutions**.
- **[2026/05/11]** Updated with 29 new arXiv papers (2026-04 / 2026-05) across all 5 layers, including HazardArena, RedVLA, JailWAM, DTap, IPI-in-Wild, MCP function-hijacking, and skill-safety literature; renamed `Tool Use` to `Tool Use and Skill` to track the agentic-skill threat surface. Survey then indexed **481 papers** across **38 co-authors** from **13 institutions**.
- **[2026/05/09]** Paper posted on [arXiv](https://arxiv.org/abs/2605.02900).
- **[2026/04/01]** Beautified paper list with layer icons and visual separators.
- **[2026/03/31]** Added `llms.txt` and SEO meta tags for AI discoverability.
- **[2026/03/28]** Added 11 missing safety papers; unified paper counts to 400+.
- **[2026/03/27]** Repository and paper released!
- **[2026/03/27]** Launched [project website](https://x-zheng16.github.io/Awesome-Embodied-AI-Safety/) with GitHub Pages.
- **[2026/03/27]** Added automated paper review [GitHub Action](https://github.com/x-zheng16/Awesome-Embodied-AI-Safety/actions) for community contributions.
- **[2026/03/26]** [ISC-Bench](https://github.com/wuyoscar/ISC-Bench) paper on [arXiv](https://arxiv.org/abs/2603.23509) -- 400+ stars in 48 hours!
- **[2026/03/22]** [ISC-Bench](https://github.com/wuyoscar/ISC-Bench) repository released -- Internal Safety Collapse benchmark for frontier LLMs.
- **[2025/09/15]** [Safety at Scale](https://github.com/xingjunm/Awesome-Large-Model-Safety) survey published in [Foundations and Trends in Security](https://www.emerald.com/ftsec/article/8/3-4/1/1335095).
- **[2025/02/02]** [Safety at Scale](https://github.com/xingjunm/Awesome-Large-Model-Safety) survey on [arXiv](https://arxiv.org/abs/2502.05206) -- large model & agent safety.

## Table of Contents

- [News](#-news)
- [Overview](#overview)
- [Surveyed Papers](#surveyed-papers) -- Perception, Cognition, Planning, Action & Interaction, Agentic
- [Other Related Works](#other-related-works)
- [Open Challenges](#open-challenges)
- [Contributing](#contributing)
- [Citation](#citation)
- [Related Projects](#related-projects)
- [Recommended Reading & Viewing](#recommended-reading--viewing)
- [Star History](#star-history)

## Overview

Embodied AI integrates perception, cognition, planning, and interaction into agents that operate in open-world, safety-critical environments.
As these systems gain autonomy and enter domains such as autonomous driving, healthcare, and robotics, ensuring their safety becomes both technically challenging and socially indispensable.

**Capability-Risk Duality**: each layer of the embodied pipeline represents a capability expansion that introduces corresponding new vulnerabilities.

<div align="center">
<img src="assets/fig_capability_risk.png" width="95%">
<p><em>Capability vs. risk duality in embodied AI systems. As capabilities expand outward from perception to agentic systems, the attack surface grows correspondingly -- vulnerabilities at inner layers cascade to outer layers.</em></p>
</div>

<div align="center">
<img src="assets/structure.png" width="95%">
<p><em>Illustration of safety threats and attack surfaces across capability layers of embodied AI systems.</em></p>
</div>

<div align="center">
<img src="assets/overview.png" width="80%">
<p><em>Overview of representative attack and defense methods across perception, cognition, planning, action & interaction, and agentic system layers. The width of the strips is proportional to the number of reviewed works.</em></p>
</div>

## Surveyed Papers

We review **533** papers across five capability layers of embodied AI. The taxonomy below organizes the core attack and defense literature; the remaining cited works (background and capability models, datasets, simulators, and related surveys) are collected under [Other Related Works](#other-related-works).

|     | Layer                      | Subcategories                                                    | Papers |
|:---:|----------------------------|------------------------------------------------------------------|-------:|
| 👁️ | **Perception**             | Visual, Auditory, Spatial, Motion, Cross-Modal                   |    195 |
| 🧠 | **Cognition**              | Instruction Understanding, World Model, Reasoning                |     37 |
| 🗺️ | **Planning**               | Task, Trajectory, Multi-Agent                                    |     81 |
| 🤖 | **Action and Interaction** | Robot Control, Human-Agent, Multi-Agent Collaboration             |    109 |
| ⚡  | **Agentic**                | Tool Use and Skill, Memory, Self-Evolving, Cascading Risks       |     91 |

<details open>
<summary>👁️ <b>Perception</b> (199 papers)</summary>

<details open>
<summary>Visual Perception (58)</summary>

- [Adversarial Attacks and Detection in Visual Place Recognition for Safer Robot Navigation](https://arxiv.org/abs/2506.15988). Malone et al. *arXiv 2506.15988*, 2025.
- [Embodied Active Defense: Leveraging Recurrent Feedback to Counter Adversarial Patches](https://arxiv.org/abs/2404.00540). Wu et al. *arXiv 2404.00540*, 2024.
- [Physical Adversarial Clothing Evades Visible-Thermal Detectors via Non-Overlapping RGB-T Pattern](https://arxiv.org/abs/2605.04675). Zhu et al. *arXiv 2605.04675*, 2026.
- [Securing the Lane: Defences Against Patch Attacks on Autonomous Vehicle's Lane Detection](https://scholar.google.com/scholar?q=Securing+the+Lane%3A+Defences+Against+Patch+Attacks+on+Autonomous+Vehicle%27s+Lane+Detection). Blazevic et al. *In EuroS&PW*, 2025.
- [Detecting Adversarial Attacks Based on Tracking Differences in Frequency Bands](https://scholar.google.com/scholar?q=Detecting+Adversarial+Attacks+Based+on+Tracking+Differences+in+Frequency+Bands). Li et al. *IEEE Transactions on Multimedia (TMM)*, 2025.
- [Multi-view Feature Discrepancy Attack for Single Object Tracking](https://scholar.google.com/scholar?q=Multi-view+Feature+Discrepancy+Attack+for+Single+Object+Tracking). Li et al. *In ICASSP*, 2025.
- [Towards Stealthy and Effective Backdoor Attacks on Lane Detection: A Naturalistic Data Poisoning Approach](https://arxiv.org/abs/2508.15778). Liao et al. *arXiv 2508.15778*, 2025.
- [Stealthy backdoor attack in self-supervised learning vision encoders for large vision language models](https://scholar.google.com/scholar?q=Stealthy+Backdoor+Attack+in+Self-Supervised+Learning+Vision+Encoders+for+Large+Vision+Language+Models). Liu et al. *In CVPR*, 2025.
- [PB-UAP: Hybride Universal Adversarial Attack for Image Segmentation](https://scholar.google.com/scholar?q=PB-UAP%3A+Hybride+Universal+Adversarial+Attack+for+Image+Segmentation). Song et al. *In ICASSP*, 2025.
- [Test-Time Multimodal Backdoor Detection by Contrastive Prompting](https://arxiv.org/abs/2405.15269). Niu et al. *In ICML*, 2025.
- [Anyattack: Towards Large-scale Self-supervised Adversarial Attacks on Vision-language Models](https://arxiv.org/abs/2410.05346). Zhang et al. *In CVPR*, 2025.
- [RP-PGD: Boosting Segmentation Robustness with a Region-and-Prototype Based Adversarial Attack](https://scholar.google.com/scholar?q=RP-PGD%3A+Boosting+Segmentation+Robustness+with+a+Region-and-Prototype+Based+Adversarial+Attack). Zhang et al. *In AAAI*, 2025.
- [A Robust UAV Tracking Solution in the Adversarial Environment](https://scholar.google.com/scholar?q=A+Robust+UAV+Tracking+Solution+in+the+Adversarial+Environment). Jia et al. *In ICTAI*, 2024.
- [BadCLIP: Dual-Embedding Guided Backdoor Attack on Multimodal Contrastive Learning](https://arxiv.org/abs/2311.12075). Liang et al. *In CVPR*, 2024.
- [ControlLoc: Physical-World Hijacking Attack on Visual Perception in Autonomous Driving](https://arxiv.org/abs/2406.05810). Ma et al. *arXiv 2406.05810*, 2024.
- [Uncertainty-weighted Loss Functions for Improved Adversarial Attacks on Semantic Segmentation](https://arxiv.org/abs/2310.17436). Maag and Fischer. *In WACV*, 2024.
- [Discovering New Shadow Patterns for Black-Box Attacks on Lane Detection of Autonomous Vehicles](https://arxiv.org/abs/2409.18248). MohajerAnsari et al. *arXiv 2409.18248*, 2024.
- [TrackPGD: Efficient Adversarial Attack using Object Binary Masks against Robust Transformer Trackers](https://arxiv.org/abs/2407.03946). Nokabadi et al. *arXiv 2407.03946*, 2024.
- [Robust CLIP: Unsupervised Adversarial Fine-Tuning of Vision Embeddings for Robust Large Vision-Language Models](https://arxiv.org/abs/2402.12336). Schlarmann et al. *In ICML*, 2024.
- [Embodied Laser Attack:Leveraging Scene Priors to Achieve Agent-based Robust Non-contact Attacks](https://arxiv.org/abs/2312.09554). Sun et al. *In MM*, 2024.
- [Cascaded Adversarial Attack: Simultaneously Fooling Rain Removal and Semantic Segmentation Networks](https://scholar.google.com/scholar?q=Cascaded+adversarial+attack%3A+Simultaneously+fooling+rain+removal+and+semantic+segmentation+networks). Wang et al. *In MM*, 2024.
- [Physical ID-Transfer Attacks against Multi-Object Tracking via Adversarial Trajectory](https://arxiv.org/abs/2512.01934). Wang et al. *In ACSAC*, 2024.
- [A Human-in-the-Middle Attack Against Object Detection Systems](https://arxiv.org/abs/2208.07174). Wu et al. *Artificial Intelligence (AIJ)*, 2022.
- [Not All Prompts Are Secure: A Switchable Backdoor Attack Against Pre-trained Vision Transformers](https://arxiv.org/abs/2405.10612). Yang et al. *In CVPR*, 2024.
- [Towards Robust Physical-world Backdoor Attacks on Lane Detection](https://arxiv.org/abs/2405.05553). Zhang et al. *In MM*, 2024.
- [CleanCLIP: Mitigating Data Poisoning Attacks in Multimodal Contrastive Learning](https://arxiv.org/abs/2303.03323). Bansal et al. *In ICCV*, 2023.
- [Defending Backdoor Attacks on Vision Transformer via Patch Processing](https://arxiv.org/abs/2206.12381). Doan et al. *In AAAI*, 2023.
- [PSO-Based Black-Box Lane Detection Adversarial Attack](https://scholar.google.com/scholar?q=PSO-Based+Black-Box+Lane+Detection+Adversarial+Attack). Fang et al. *In AIHCIR*, 2023.
- [DECREE: Detecting Backdoors in Pre-trained Encoders](https://arxiv.org/abs/2303.15180). Feng et al. *In CVPR*, 2023.
- [Detection-Friendly Dehazing: Object Detection in Real-World Hazy Scenes](https://scholar.google.com/scholar?q=Detection-friendly+dehazing%3A+Object+detection+in+real-world+hazy+scenes). Li et al. *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)*, 2023.
- [WIP: Towards the Practicality of the Adversarial Attack on Object Tracking in Autonomous Driving](https://scholar.google.com/scholar?q=Wip%3A+Towards+the+practicality+of+the+adversarial+attack+on+object+tracking+in+autonomous+driving). Ma et al. *In VehicleSec*, 2023.
- [Understanding Zero-Shot Adversarial Robustness for Large-Scale Models](https://arxiv.org/abs/2212.07016). Mao et al. *In ICLR*, 2023.
- [Adversarial Detection: Attacking Object Detection in Real Time](https://arxiv.org/abs/2209.01962). Wu et al. *In IV*, 2023.
- [You Are Catching My Attention: Are Vision Transformers Bad Learners under Backdoor Attacks?](https://scholar.google.com/scholar?q=You+Are+Catching+My+Attention%3A+Are+Vision+Transformers+Bad+Learners+under+Backdoor+Attacks%3F). Yuan et al. *In CVPR*, 2023.
- [TrojViT: Trojan Insertion in Vision Transformers](https://arxiv.org/abs/2208.13049). Zheng et al. *In CVPR*, 2023.
- [Physical Backdoor Attacks to Lane Detection Systems in Autonomous Driving](https://arxiv.org/abs/2203.00858). Han et al. *In MM*, 2022.
- [BadEncoder: Backdoor Attacks to Pre-trained Encoders in Self-Supervised Learning](https://arxiv.org/abs/2108.00352). Jia et al. *In IEEE S&P*, 2022.
- [Image-Adaptive YOLO for Object Detection in Adverse Weather Conditions](https://arxiv.org/abs/2112.08088). Liu et al. *In AAAI*, 2022.
- [A Perturbation Constrained Adversarial Attack for Evaluating the Robustness of Optical Flow](https://arxiv.org/abs/2203.13214). Schmalfuss et al. *In ECCV*, 2022.
- [Automating defense against adversarial attacks: discovery of vulnerabilities and application of multi-INT imagery to protect deployed models](https://arxiv.org/abs/2103.15897). Kalin et al. *Disruptive Technologies in Information Sciences V*, 2021.
- [SLAP: Improving Physical Adversarial Examples with Short-Lived Adversarial Perturbations](https://arxiv.org/abs/2007.04137). Lovisotto et al. *In USENIX Security*, 2021.
- [Dirty Road Can Attack: Security of Deep Learning based Automated Lane Centering under Physical-World Attack](https://arxiv.org/abs/2009.06701). Sato et al. *In USENIX Security*, 2021.
- [Model-Agnostic Defense for Lane Detection against Adversarial Attack](https://arxiv.org/abs/2103.00663). Xu et al. *arXiv 2103.00663*, 2021.
- [SentiNet: Detecting Localized Universal Attacks Against Deep Learning Systems](https://arxiv.org/abs/1812.00292). Chou et al. *In SPW*, 2018.
- [DSNet: Joint Semantic Learning for Object Detection in Inclement Weather Conditions](https://scholar.google.com/scholar?q=DSNet%3A+Joint+semantic+learning+for+object+detection+in+inclement+weather+conditions). Huang et al. *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)*, 2020.
- [Fooling Detection Alone is Not Enough: Adversarial Attack against Multiple Object Tracking](https://scholar.google.com/scholar?q=Fooling+detection+alone+is+not+enough%3A+Adversarial+attack+against+multiple+object+tracking). Jia et al. *In ICLR*, 2020.
- [Robust Tracking against Adversarial Attacks](https://arxiv.org/abs/2007.09919). Jia et al. *In ECCV*, 2020.
- [Phantom of the ADAS: Securing Advanced Driver-Assistance Systems from Split-Second Phantom Attacks](https://scholar.google.com/scholar?q=Phantom+of+the+adas%3A+Securing+advanced+driver-assistance+systems+from+split-second+phantom+attacks). Nassi et al. *In CCS*, 2020.
- [Adversarial T-Shirt! Evading Person Detectors in a Physical World](https://scholar.google.com/scholar?q=Adversarial+t-shirt%21+evading+person+detectors+in+a+physical+world). Xu et al. *In ECCV*, 2020.
- [MobilBye: Attacking ADAS with Camera Spoofing](https://arxiv.org/abs/1906.09765). Nassi et al. *arXiv 1906.09765*, 2019.
- [Fooling Automated Surveillance Cameras: Adversarial Patches to Attack Person Detection](https://arxiv.org/abs/1904.08653). Thys et al. *In CVPR workshops*, 2019.
- [ShapeShifter: Robust Physical Adversarial Attack on Faster R-CNN Object Detector](https://arxiv.org/abs/1804.05810). Chen et al. *In ECML PKDD*, 2018.
- [Robust Physical-World Attacks on Deep Learning Visual Classification](https://scholar.google.com/scholar?q=Robust+physical-world+attacks+on+deep+learning+visual+classification). Eykholt et al. *In CVPR*, 2018.
- [Robust Camera Lidar Sensor Fusion Via Deep Gated Information Fusion Network](https://scholar.google.com/scholar?q=Robust+camera+lidar+sensor+fusion+via+deep+gated+information+fusion+network). Kim et al. *In IV*, 2018.
- [DARTS: Deceiving Autonomous Cars with Toxic Signs](https://arxiv.org/abs/1802.06430). Sitawarin et al. *arXiv 1802.06430*, 2018.
- [CAMOU: Learning Physical Vehicle Camouflages to Adversarially Attack Detectors in the Wild](https://scholar.google.com/scholar?q=CAMOU%3A+Learning+physical+vehicle+camouflages+to+adversarially+attack+detectors+in+the+wild). Zhang et al. *In ICLR*, 2018.
- [AOD-Net: All-in-One Dehazing Network](https://scholar.google.com/scholar?q=Aod-net%3A+All-in-one+dehazing+network). Li et al. *In ICCV*, 2017.
- [Is Deep Learning Safe for Robot Vision? Adversarial Examples Against the iCub Humanoid](https://arxiv.org/abs/1708.06939). Melis et al. *In ICCV*, 2017.

</details>

<details open>
<summary>Auditory Perception (21)</summary>

- [Watch Your Speed: Injecting Malicious Voice Commands via Time-Scale Modification](https://scholar.google.com/scholar?q=Watch+your+speed%3A+Injecting+malicious+voice+commands+via+time-scale+modification). Ji et al. *IEEE Transactions on Information Forensics and Security (TIFS)*, 2024.
- [Hello Me, Meet the Real Me: Audio Deepfake Attacks on Voice Assistants](https://arxiv.org/abs/2302.10328). Bilika et al. *arXiv 2302.10328*, 2023.
- [BarrierBypass: Out-of-Sight Clean Voice Command Injection Attacks through Physical Barriers](https://arxiv.org/abs/2302.02042). Walker et al. *In WiSec*, 2023.
- [Defending against Adversarial Audio via Diffusion Model](https://arxiv.org/abs/2303.01507). Wu et al. *arXiv 2303.01507*, 2023.
- [AntiFake: Using Adversarial Audio to Prevent Unauthorized Speech Synthesis](https://scholar.google.com/scholar?q=Antifake%3A+Using+adversarial+audio+to+prevent+unauthorized+speech+synthesis). Yu et al. *In CCS*, 2023.
- [TrojanModel: A Practical Trojan Attack against Automatic Speech Recognition Systems](https://scholar.google.com/scholar?q=Trojanmodel%3A+A+practical+trojan+attack+against+automatic+speech+recognition+systems). Zong et al. *In S&P*, 2023.
- [SPECPATCH: Human-In-The-Loop Adversarial Audio Spectrogram Patch Attack on Speech Recognition](https://scholar.google.com/scholar?q=Specpatch%3A+Human-in-the-loop+adversarial+audio+spectrogram+patch+attack+on+speech+recognition). Guo et al. *In CCS*, 2022.
- [Black-box Adversarial Attacks on Commercial Speech Platforms with Minimal Information](https://arxiv.org/abs/2110.09714). Zheng et al. *In CCS*, 2021.
- [Devil's Whisper: A General Approach for Physical Adversarial Attacks against Commercial Black-box Speech Recognition Devices](https://scholar.google.com/scholar?q=Devil%27s+Whisper%3A+A+General+Approach+for+Physical+Adversarial+Attacks+against+Commercial+Black-box+Speech+Recognition+Devices). Chen et al. *In USENIX Security*, 2020.
- [Metamorph: Injecting Inaudible Commands into Over-the-air Voice Controlled Systems](https://scholar.google.com/scholar?q=Metamorph%3A+Injecting+inaudible+commands+into+over-the-air+voice+controlled+systems). Chen et al. *In NDSS*, 2020.
- [AdvPulse: Universal, Synchronization-free, and Targeted Audio Adversarial Attacks via Subsecond Perturbations](https://scholar.google.com/scholar?q=Advpulse%3A+Universal%2C+synchronization-free%2C+and+targeted+audio+adversarial+attacks+via+subsecond+perturbations). Li et al. *In CCS*, 2020.
- [Practical Adversarial Attacks Against Speaker Recognition Systems](https://scholar.google.com/scholar?q=Practical+adversarial+attacks+against+speaker+recognition+systems). Li et al. *In HotMobile*, 2020.
- [Adversarial Example Detection by Classification for Deep Speech Recognition](https://arxiv.org/abs/1910.10013). Samizade et al. *In ICASSP*, 2020.
- [When the Differences in Frequency Domain are Compensated: Understanding and Defeating Modulated Replay Attacks on Automatic Speech Recognition](https://arxiv.org/abs/2009.00718). Wang et al. *In CCS*, 2020.
- [Practical Hidden Voice Attacks against Speech and Speaker Recognition Systems](https://arxiv.org/abs/1904.05734). Abdullah et al. *arXiv 1904.05734*, 2019.
- [A Multiversion Programming Inspired Approach to Detecting Audio Adversarial Examples](https://arxiv.org/abs/1812.10199). Zeng et al. *In DSN*, 2019.
- [Who Activated My Voice Assistant? A Stealthy Attack on Android Phones Without Users' Awareness](https://scholar.google.com/scholar?q=Who+activated+my+voice+assistant%3F+A+stealthy+attack+on+android+phones+without+users%E2%80%99+awareness). Zhang et al. *In ML4CS*, 2019.
- [Characterizing Audio Adversarial Examples Using Temporal Dependency](https://arxiv.org/abs/1809.10875). Yang et al. *arXiv 1809.10875*, 2018.
- [CommanderSong: A Systematic Approach for Practical Adversarial Voice Recognition](https://arxiv.org/abs/1801.08535). Yuan et al. *In USENIX Security*, 2018.
- [Hidden Voice Commands](https://scholar.google.com/scholar?q=Hidden+voice+commands). Carlini et al. *In USENIX security*, 2016.
- [Cocaine Noodles: Exploiting the Gap between Human and Machine Speech Recognition](https://scholar.google.com/scholar?q=Cocaine+noodles%3A+exploiting+the+gap+between+human+and+machine+speech+recognition). Vaidya et al. *In WOOT*, 2015.

</details>

<details open>
<summary>Spatial Perception (61)</summary>

- [SLAMSpoof: Practical LiDAR Spoofing Attacks on Localization Systems Guided by Scan Matching Vulnerability Analysis](https://arxiv.org/abs/2502.13641). Nagata et al. *arXiv 2502.13641*, 2025.
- [BadDepth: Backdoor Attacks Against Monocular Depth Estimation in the Physical World](https://arxiv.org/abs/2505.16154). Guo et al. *arXiv 2505.16154*, 2025.
- [Semantically Safe Robot Manipulation: From Semantic Scene Understanding to Motion Safeguards](https://arxiv.org/abs/2410.15185). Brunke et al. *IEEE Robotics and Automation Letters (RA-L)*, 2025.
- [LiDAttack: Robust Black-Box Attack on LiDAR-Based Object Detection](https://arxiv.org/abs/2411.01889). Chen et al. *In ITSC*, 2025.
- [Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps](https://arxiv.org/abs/2403.02751). Chen et al. *IEEE Transactions on Robotics (T-RO)*, 2025.
- [Black-Box Explainability-Guided Adversarial Attack for 3D Object Tracking](https://scholar.google.com/scholar?q=Black-box+explainability-guided+adversarial+attack+for+3D+object+tracking). Cheng et al. *IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)*, 2025.
- [LiDAR Light Scattering Augmentation (LISA): Physics-based Simulation of Adverse Weather Conditions for 3D Object Detection](https://arxiv.org/abs/2107.07004). Kilic et al. *In ICASSP*, 2021.
- [Invisible but Detected: Physical Adversarial Shadow Attack and Defense on LiDAR Object Detection](https://scholar.google.com/scholar?q=Invisible+but+Detected%3A+Physical+Adversarial+Shadow+Attack+and+Defense+on+LiDAR-based+3D+Object+Detection). Kobayashi et al. *In USENIX Security*, 2025.
- [Enhancing the Robustness of LiDAR-based Object Detection under Disappearing Attacks](https://scholar.google.com/scholar?q=Enhancing+the+Robustness+of+LiDAR-based+Object+Detection+under+Disappearing+Attacks). Wang et al. *In ICASSP*, 2025.
- [An Imperceptible Adversarial Attack Against 3-D Object Detectors in Autonomous Driving](https://doi.org/10.1109/JIOT.2025.3547966). Wang et al. *IEEE Internet of Things Journal (IoT-J)*, 2025.
- [Towards Real-Time Defense against Object-Based LiDAR Attacks in Autonomous Driving](https://scholar.google.com/scholar?q=Towards+Real-Time+Defense+against+Object-Based+LiDAR+Attacks+in+Autonomous+Driving). Zhang et al. *In CCS*, 2025.
- [A New Adversarial Perspective for LiDAR-based 3D Object Detection](https://scholar.google.com/scholar?q=A+New+Adversarial+Perspective+for+LiDAR-based+3D+Object+Detection). Zheng et al. *In AAAI*, 2025.
- [Diffusion Models-Based Purification for Common Corruptions on Robust 3D Object Detection](https://scholar.google.com/scholar?q=Diffusion+models-based+purification+for+common+corruptions+on+robust+3D+object+detection). Cai et al. *Sensors*, 2024.
- [Adversary is on the Road: Attacks on Visual SLAM with Robust Perturbations on Point Clouds](https://scholar.google.com/scholar?q=Adversary+is+on+the+Road%3A+Attacks+on+Visual+SLAM+with+Robust+Perturbations+on+Point+Clouds). Chen et al. *In USENIX Security*, 2024.
- [CATNIPS: Collision Avoidance Through Neural Implicit Probabilistic Scenes](https://arxiv.org/abs/2302.12931). Chen et al. *IEEE Transactions on Robotics (T-RO)*, 2024.
- [Safer-Splat: A Control Barrier Function for Safe Navigation with Online Gaussian Splatting Maps](https://arxiv.org/abs/2409.09868). Chen et al. *arXiv 2409.09868*, 2024.
- [Random Spoofing Attack against LiDAR-Based Scan Matching SLAM](https://scholar.google.com/scholar?q=Random+Spoofing+Attack+against+LiDAR-Based+Scan+Matching+SLAM). Fukunaga and Sugawara. *In VehicleSec*, 2024.
- [SpotAttack: Covering Spots on Surface to Attack LiDAR-Based Autonomous Driving Systems](https://scholar.google.com/scholar?q=SpotAttack%3A+Covering+Spots+on+Surface+to+Attack+LiDAR+Based+Autonomous+Driving+Systems). Huang et al. *IEEE Internet of Things Journal (IoT-J)*, 2024.
- [Adv3D: Generating 3D Adversarial Examples for 3D Object Detection in Driving Scenarios with NeRF](https://arxiv.org/abs/2309.01351). Li et al. *In IROS*, 2024.
- [Beyond Uncertainty: Risk-Aware Active View Acquisition for Safe Robot Navigation and 3D Scene Understanding with FisherRF](https://arxiv.org/abs/2403.11396). Liu et al. *arXiv 2403.11396*, 2024.
- [A First Physical-World Trajectory Prediction Attack via LiDAR-induced Deceptions in Autonomous Driving](https://arxiv.org/abs/2406.11707). Lou et al. *In USENIX Security Symposium*, 2024.
- [Poison-splat: Computation Cost Attack on 3D Gaussian Splatting](https://arxiv.org/abs/2410.08190). Lu et al. *arXiv 2410.08190*, 2024.
- [Adversarial Attacks on LiDAR-Based Tracking Across Road Users: Robustness Evaluation and Target-Aware Black-Box Method](https://arxiv.org/abs/2410.20893). Tian et al. *arXiv 2410.20893*, 2024.
- [Benchmarking Robustness in Neural Radiance Fields](https://arxiv.org/abs/2301.04075). Wang et al. *In CVPR*, 2024.
- [Mobile Cooperative Robot Safe Interaction Method Based on Embodied Perception](https://scholar.google.com/scholar?q=Mobile+Cooperative+Robot+Safe+Interaction+Method+Based+on+Embodied+Perception). Wang et al. *In ICCA*, 2024.
- [A Comprehensive Study of the Robustness for LiDAR-Based 3D Object Detectors Against Adversarial Attacks](https://arxiv.org/abs/2212.10230). Zhang et al. *International Journal of Computer Vision (IJCV)*, 2022.
- [Control-Barrier-Aided Teleoperation with Visual-Inertial SLAM for Safe MAV Navigation in Complex Environments](https://arxiv.org/abs/2403.04331). Zhou et al. *In ICRA*, 2024.
- [AE-Morpher: Improve Physical Robustness of Adversarial Objects against LiDAR-based Detectors via Object Reconstruction](https://scholar.google.com/scholar?q=AE-Morpher). Zhu et al. *In USENIX Security*, 2024.
- [ADoPT: LiDAR Spoofing Attack Detection Based on Point-Level Temporal Consistency](https://arxiv.org/abs/2310.14504). Cho et al. *arXiv 2310.14504*, 2023.
- [Targeted Adversarial Attacks on Generalizable Neural Radiance Fields](https://arxiv.org/abs/2310.03578). Horvath. *In CVPR*, 2023.
- [BadLiDet: A Simple Backdoor Attack against LiDAR Object Detection in Autonomous Driving](https://scholar.google.com/scholar?q=Badlidet%3A+A+simple+backdoor+attack+against+lidar+object+detection+in+autonomous+driving). Li et al. *In TrustCom*, 2023.
- [Towards Dynamic Backdoor Attacks against LiDAR Semantic Segmentation in Autonomous Driving](https://scholar.google.com/scholar?q=Towards+dynamic+backdoor+attacks+against+lidar+semantic+segmentation+in+autonomous+driving). Li et al. *In TrustCom*, 2023.
- [SlowLiDAR: Increasing the Latency of LiDAR-Based Detection Using Adversarial Examples](https://scholar.google.com/scholar?q=Slowlidar%3A+Increasing+the+latency+of+lidar-based+detection+using+adversarial+examples). Liu et al. *In CVPR*, 2023.
- [Transferable Adversarial Attack on 3D Object Tracking in Point Cloud](https://scholar.google.com/scholar?q=Transferable+adversarial+attack+on+3D+object+tracking+in+point+cloud). Liu et al. *In MMM*, 2023.
- [Scene Augmentation Methods for Interactive Embodied AI Tasks](https://scholar.google.com/scholar?q=Scene+augmentation+methods+for+interactive+embodied+AI+tasks). Sang et al. *IEEE Transactions on Instrumentation and Measurement*, 2023.
- [Exorcising "Wraith": Protecting LiDAR-based Object Detector in Automated Driving System from Appearing Attacks](https://arxiv.org/abs/2303.09731). Xiao et al. *In USENIX Security*, 2023.
- [Vision-Only Robot Navigation in a Neural Radiance World](https://arxiv.org/abs/2110.00168). Adamkiewicz et al. *IEEE Robotics and Automation Letters (RA-L)*, 2022.
- [Adversarial Attacks on Monocular Pose Estimation](https://arxiv.org/abs/2207.07032). Chawla et al. *In IROS*, 2022.
- [Physical Attack on Monocular Depth Estimation with Optimal Adversarial Patches](https://arxiv.org/abs/2207.04718). Cheng et al. *In ECCV*, 2022.
- [ViewFool: Evaluating the Robustness of Visual Recognition to Adversarial Viewpoints](https://arxiv.org/abs/2210.03895). Dong et al. *In NeurIPS*, 2022.
- [Perceptual Aliasing++: Adversarial Attack for Visual SLAM Front-End and Back-End](https://scholar.google.com/scholar?q=Perceptual+aliasing%2B%2B%3A+Adversarial+attack+for+visual+slam+front-end+and+back-end). Ikram et al. *IEEE Robotics and Automation Letters (RA-L)*, 2022.
- [3D-VField: Adversarial Augmentation of Point Clouds for Domain Generalization in 3D Object Detection](https://arxiv.org/abs/2112.04764). Lehner et al. *In CVPR*, 2022.
- [Enforcing safety for vision-based controllers via Control Barrier Functions and Neural Radiance Fields](https://arxiv.org/abs/2209.12266). Tong et al. *arXiv 2209.12266*, 2022.
- [Adversarial Scan Attack against Scan Matching Algorithm for Pose Estimation in LiDAR-Based SLAM](https://scholar.google.com/scholar?q=Adversarial+scan+attack+against+scan+matching+algorithm+for+pose+estimation+in+lidar-based+slam). Yoshida et al. *Science*, 2022.
- [PointCutMix: Regularization Strategy for Point Cloud Classification](https://arxiv.org/abs/2101.01461). Zhang et al. *Neurocomputing*, 2022.
- [Towards Backdoor Attacks against LiDAR Object Detection in Autonomous Driving](https://scholar.google.com/scholar?q=Towards+backdoor+attacks+against+lidar+object+detection+in+autonomous+driving). Zhang et al. *In SenSys*, 2022.
- [DoubleStar: Long-Range Attack Towards Depth Estimation based Obstacle Avoidance in Autonomous Systems](https://arxiv.org/abs/2110.03154). Zhou et al. *In USENIX Security*, 2022.
- [Universal Adversarial Attack Against 3D Object Tracking](https://scholar.google.com/scholar?q=Universal+adversarial+attack+against+3D+object+tracking). Cheng et al. *In HPCC*, 2021.
- [Fog Simulation on Real LiDAR Point Clouds for 3D Object Detection in Adverse Weather](https://arxiv.org/abs/2108.05249). Hahner et al. *In CVPR*, 2021.
- [Object Removal Attacks on LiDAR-based 3D Object Detectors](https://arxiv.org/abs/2102.03722). Hau et al. *arXiv 2102.03722*, 2021.
- [Shadow-Catcher: Looking into Shadows to Detect Ghost Objects in Autonomous Vehicle 3D Sensing](https://scholar.google.com/scholar?q=Shadow-catcher%3A+Looking+into+shadows+to+detect+ghost+objects+in+autonomous+vehicle+3d+sensing). Hau et al. *In ESORICS*, 2021.
- [Fooling LiDAR Perception via Adversarial Trajectory Perturbation](https://arxiv.org/abs/2103.15326). Li et al. *In CVPR*, 2021.
- [PointGuard: Provably Robust 3D Point Cloud Classification](https://arxiv.org/abs/2103.03046). Liu et al. *In CVPR*, 2021.
- [Adversarially Robust 3D Point Cloud Recognition Using Self-Supervisions](https://scholar.google.com/scholar?q=Adversarially+robust+3d+point+cloud+recognition+using+self-supervisions). Sun et al. *In NeurIPS*, 2021.
- [I Can See the Light: Attacks on Autonomous Vehicles Using Invisible Lights](https://scholar.google.com/scholar?q=I+can+see+the+light%3A+Attacks+on+autonomous+vehicles+using+invisible+lights). Wang et al. *In CCS*, 2021.
- [Temporal Consistency Checks to Detect LiDAR Spoofing Attacks on Autonomous Vehicle Perception](https://arxiv.org/abs/2106.07833). You et al. *In Workshop on Security and Privacy for Mobile AI*, 2021.
- [AcousticFusion: Fusing Sound Source Localization to Visual SLAM in Dynamic Environments](https://arxiv.org/abs/2108.01246). Zhang et al. *In IROS*, 2021.
- [CNN-Based Lidar Point Cloud De-Noising in Adverse Weather](https://arxiv.org/abs/1912.03874). Heinzler et al. *IEEE Robotics and Automation Letters (RA-L)*, 2020.
- [Physically Realizable Adversarial Examples for LiDAR Object Detection](https://arxiv.org/abs/2004.00543). Tu et al. *In CVPR*, 2020.
- [Adversarial Objects Against LiDAR-Based Autonomous Driving Systems](https://arxiv.org/abs/1907.05418). Cao et al. *arXiv 1907.05418*, 2019.
- [Defense-PointNet: Protecting PointNet Against Adversarial Attacks](https://arxiv.org/abs/2002.11881). Zhang et al. *In Big Data*, 2019.

</details>

<details open>
<summary>Motion Perception (48)</summary>

- [Safety Interventions against Adversarial Patches in an Open-Source Driver Assistance System](https://arxiv.org/abs/2504.18990). Chen et al. *In DSN*, 2025.
- [Attacking mmWave Imaging With Neural Meta-Material Rendering](https://scholar.google.com/scholar?q=Attacking+mmWave+Imaging+with+Neural+Meta-Material+Rendering). Geng et al. *IEEE Transactions on Information Forensics and Security (TIFS)*, 2025.
- [A Spoofing Detection and Direction-Finding Approach for Global Navigation Satellite System Signals Using Off-the-Shelf Anti-Jamming Antennas](https://scholar.google.com/scholar?q=A+Spoofing+Detection+and+Direction-Finding+Approach+for+Global+Navigation+Satellite+System+Signals+Using+Off-the-Shelf+Anti-Jamming+Antennas). Jin et al. *Remote Sensing*, 2025.
- [GNSS Spoofing Detection Based on Opportunistic Position Information](https://arxiv.org/abs/2506.12580). Liu and Papadimitratos. *arXiv 2506.12580*, 2025.
- [SecureTrack: Protecting Vehicular Sensors From Noninvasive EMI Attacks](https://scholar.google.com/scholar?q=SecureTrack%3A+Protecting+Vehicular+Sensors+from+Non-Invasive+EMI+Attacks). Singh and Mishra. *IEEE Sensors Journal*, 2025.
- [GNSS Jammer Localization and Identification With Airborne Commercial GNSS Receivers](https://arxiv.org/abs/2503.20352). Spanghero et al. *IEEE Transactions on Information Forensics and Security (TIFS)*, 2025.
- [Practical Spoofing Attacks on Galileo Open Service Navigation Message Authentication](https://arxiv.org/abs/2501.09246). Wang et al. *arXiv 2501.09246*, 2025.
- [Analysis and Validation of Distributed GNSS Spoofing Threat](https://scholar.google.com/scholar?q=Analysis+and+Validation+of+Distributed+GNSS+Spoofing+Threat). Zhong et al. *In Engineering Proceedings*, 2025.
- [Unveiling the Stealthy Threat: Analyzing Slow Drift GPS Spoofing Attacks for Autonomous Vehicles in Urban Environments and Enabling the Resilience](https://arxiv.org/abs/2401.01394). Dasgupta et al. *arXiv 2401.01394*, 2024.
- [A Deep Learning Based Induced GNSS Spoof Detection Framework](https://scholar.google.com/scholar?q=A+deep+learning+based+induced+GNSS+spoof+detection+framework). Iqbal et al. *Machine Learning (MLJ)*, 2024.
- [Acoustic Attack Mitigation Approach for MEMS Inertial Sensors Using Change Point Detection on MhIMU Framework](https://scholar.google.com/scholar?q=Acoustic+Attack+Mitigation+Approach+for+MEMS+Inertial+Sensors+Using+Change+Point+Detection+on+MhIMU+Framework). Sahu and Poddar. *IEEE Transactions on Aerospace and Electronic Systems*, 2024.
- [VIMU: Effective Physics-based Realtime Detection and Recovery against Stealthy Attacks on UAVs](https://arxiv.org/abs/2504.20569). Wang et al. *In ACSAC*, 2024.
- [MetaWave: Attacking mmWave Sensing with Meta-material-enhanced Tags](https://scholar.google.com/scholar?q=Metawave%3A+Attacking+mmwave+sensing+with+meta-material-enhanced+tags). Chen et al. *In NDSS*, 2023.
- [Exploring Practical Acoustic Transduction Attacks on Inertial Sensors in MDOF Systems](https://scholar.google.com/scholar?q=Exploring+practical+acoustic+transduction+attacks+on+inertial+sensors+in+MDOF+systems). Gao et al. *IEEE Transactions on Mobile Computing*, 2023.
- [Paralyzing Drones via EMI Signal Injection on Sensory Communication Channels](https://scholar.google.com/scholar?q=Paralyzing+Drones+via+EMI+Signal+Injection+on+Sensory+Communication+Channels). Jang et al. *In NDSS*, 2023.
- [Un-Rocking Drones: Foundations of Acoustic Injection Attacks and Recovery Thereof](https://scholar.google.com/scholar?q=Un-Rocking+Drones%3A+Foundations+of+Acoustic+Injection+Attacks+and+Recovery+Thereof). Jeong et al. *In NDSS*, 2023.
- [mmSpoof: Resilient Spoofing of Automotive Millimeter-wave Radars using Reflect Array](https://scholar.google.com/scholar?q=mmspoof%3A+Resilient+spoofing+of+automotive+millimeter-wave+radars+using+reflect+array). Vennam et al. *In S&P*, 2023.
- [Anti-Spoofing Technique Based on Vector Tracking Loop](https://scholar.google.com/scholar?q=Anti-spoofing+technique+based+on+vector+tracking+loop). Zhou et al. *IEEE Transactions on Instrumentation and Measurement*, 2023.
- [TileMask: A Passive-Reflection-based Attack against mmWave Radar Object Detection in Autonomous Driving](https://scholar.google.com/scholar?q=TileMask%3A+A+passive-reflection-based+attack+against+mmWave+radar+object+detection+in+autonomous+driving). Zhu et al. *In CCS*, 2023.
- [ESP Spoofing: Covert Acoustic Attack on MEMS Gyroscopes in Vehicles](https://scholar.google.com/scholar?q=ESP+spoofing%3A+Covert+acoustic+attack+on+MEMS+gyroscopes+in+vehicles). Hong et al. *IEEE Transactions on Information Forensics and Security (TIFS)*, 2022.
- [Combating Single-Frequency Jamming through a Multi-Frequency, Multi-Constellation Software Receiver: A Case Study for Maritime Navigation in the Gulf of Finland](https://scholar.google.com/scholar?q=Combating+single-frequency+jamming+through+a+multi-frequency%2C+multi-constellation+software+receiver%3A+a+case+study+for+maritime+navigation+in+the+Gulf+of+Finland). Islam et al. *Sensors*, 2022.
- [DeepPOSE: Detecting GPS spoofing attack via deep recurrent neural network](https://scholar.google.com/scholar?q=DeepPOSE%3A+Detecting+GPS+spoofing+attack+via+deep+recurrent+neural+network). Jiang et al. *Digital Communications and Networks*, 2022.
- [A Traceability Localization Method of Acoustic Attack Source for MEMS Gyroscope](https://scholar.google.com/scholar?q=A+traceability+localization+method+of+acoustic+attack+source+for+mems+gyroscope). Liu et al. *IEEE Embedded Systems Letters*, 2022.
- [Spoofing Attacks Against Vehicular FMCW Radar](https://arxiv.org/abs/2104.13318). Komissarov and Wool. *In Workshop on Attacks and Solutions in Hardware Security*, 2021.
- [Relay/replay attacks on GNSS signals](https://arxiv.org/abs/2202.10897). Lenhart et al. *In WiSec*, 2021.
- [SoundFence: Securing Ultrasonic Sensors in Vehicles Using Physical-Layer Defense](https://arxiv.org/abs/2105.07574). Lou et al. *In SECON*, 2021.
- [A Frequency-Domain Spoofing Attack on FMCW Radars and Its Mitigation Technique Based on a Hybrid-Chirp Waveform](https://scholar.google.com/scholar?q=A+frequency-domain+spoofing+attack+on+FMCW+radars+and+its+mitigation+technique+based+on+a+hybrid-chirp+waveform). Nallabolu and Li. *IEEE Transactions on Microwave Theory and Techniques (TMTT)*, 2021.
- [Who Is in Control? Practical Physical Layer Attack and Defense for mmWave-Based Sensing in Autonomous Vehicles](https://arxiv.org/abs/2011.10947). Sun et al. *IEEE Transactions on Information Forensics and Security (TIFS)*, 2021.
- [GNSS Jamming Classification via CNN, Transfer Learning & the Novel Concatenation of Signal Representations](https://scholar.google.com/scholar?q=GNSS+jamming+classification+via+CNN%2C+transfer+learning+%26+the+novel+concatenation+of+signal+representations). Swinney and Woods. *In CyberSA*, 2021.
- [Machine learning-based approach to GPS antijamming](https://scholar.google.com/scholar?q=Machine+learning-based+approach+to+GPS+antijamming). Wang et al. *GPS Solutions*, 2021.
- [Spoofing Attack on Ultrasonic Distance Sensors Using a Continuous Signal](https://scholar.google.com/scholar?q=Spoofing+attack+on+ultrasonic+distance+sensors+using+a+continuous+signal). Gluck et al. *Sensors*, 2020.
- [Drift with Devil: Security of Multi-Sensor Fusion based Localization in High-Level Autonomous Driving under GPS Spoofing (Extended Version)](https://arxiv.org/abs/2006.10318). Shen et al. *In USENIX Security*, 2020.
- [Sensor Defense In-Software (SDI): Practical Software Based Detection of Spoofing Attacks on Position Sensor](https://arxiv.org/abs/1905.04691). Tharayil et al. *Artificial Intelligence (AIJ)*, 2020.
- [DeepSIM: GPS Spoofing Detection on UAVs using Satellite Imagery Matching](https://scholar.google.com/scholar?q=Deepsim%3A+Gps+spoofing+detection+on+uavs+using+satellite+imagery+matching). Xue et al. *In ACSAC*, 2020.
- [VANET-Assisted Interference Mitigation for Millimeter-Wave Automotive Radar Sensors](https://scholar.google.com/scholar?q=VANET-assisted+interference+mitigation+for+millimeter-wave+automotive+radar+sensors). Zhang et al. *IEEE Network*, 2020.
- [Drones in Distress: A Game-Theoretic Countermeasure for Protecting UAVs Against GPS Spoofing](https://arxiv.org/abs/1904.11568). Eldosouky et al. *IEEE Internet of Things Journal (IoT-J)*, 2019.
- [A Dual Antenna GNSS Spoofing Detector Based on the Dispersion of Double Difference Measurements](https://scholar.google.com/scholar?q=A+dual+antenna+GNSS+spoofing+detector+based+on+the+dispersion+of+double+difference+measurements). Nguyen et al. *In NAVITEC*, 2018.
- [Development of a GPS spoofing apparatus to attack a DJI Matrice 100 Quadcopter](https://scholar.google.com/scholar?q=Development+of+a+GPS+spoofing+apparatus+to+attack+a+DJI+Matrice+100+Quadcopter). Horton and Ranganathan. *The Journal of Global Positioning Systems*, 2018.
- [Crowd-GPS-Sec: Leveraging Crowdsourcing to Detect and Localize GPS Spoofing Attacks](https://scholar.google.com/scholar?q=Crowd-GPS-Sec%3A+Leveraging+crowdsourcing+to+detect+and+localize+GPS+spoofing+attacks). Jansen et al. *In S&P*, 2018.
- [Autonomous vehicle ultrasonic sensor vulnerability and impact assessment](https://scholar.google.com/scholar?q=Autonomous+vehicle+ultrasonic+sensor+vulnerability+and+impact+assessment). Lim et al. *In WF-IoT*, 2018.
- [Analyzing and Enhancing the Security of Ultrasonic Sensors for Autonomous Vehicles](https://scholar.google.com/scholar?q=Analyzing+and+enhancing+the+security+of+ultrasonic+sensors+for+autonomous+vehicles). Xu et al. *IEEE Internet of Things Journal (IoT-J)*, 2018.
- [Chips-Message Robust Authentication (Chimera) for GPS Civilian Signals](https://scholar.google.com/scholar?q=Chips-message+robust+authentication+%28Chimera%29+for+GPS+civilian+signals). Anderson et al. *In GNSS+*, 2017.
- [WALNUT: Waging Doubt on the Integrity of MEMS Accelerometers with Acoustic Injection Attacks](https://scholar.google.com/scholar?q=WALNUT%3A+Waging+doubt+on+the+integrity+of+MEMS+accelerometers+with+acoustic+injection+attacks). Trippel et al. *In EuroS&P*, 2017.
- [GNSS Spoofing Detection and Mitigation Based on Maximum Likelihood Estimation](https://scholar.google.com/scholar?q=GNSS+spoofing+detection+and+mitigation+based+on+maximum+likelihood+estimation). Wang et al. *Sensors*, 2017.
- [A Navigation Message Authentication Proposal for the Galileo Open Service](https://scholar.google.com/scholar?q=A+navigation+message+authentication+proposal+for+the+Galileo+open+service). Fernández‐Hernández et al. *NAVIGATION: Journal of the Institute of Navigation*, 2016.
- [Can You Trust Autonomous Vehicles : Contactless Attacks against Sensors of Self-driving Vehicle](https://scholar.google.com/scholar?q=Can+you+trust+autonomous+vehicles%3A+Contactless+attacks+against+sensors+of+self-driving+vehicle). Yan et al. *In DEF CON*, 2016.
- [Rocking Drones with Intentional Sound Noise on Gyroscopic Sensors](https://scholar.google.com/scholar?q=Rocking+drones+with+intentional+sound+noise+on+gyroscopic+sensors). Son et al. *In USENIX Security*, 2015.
- [Anti-spoofing and open GNSS signal authentication with signal authentication sequences](https://scholar.google.com/scholar?q=Anti-spoofing+and+open+GNSS+signal+authentication+with+signal+authentication+sequences). Pozzobon et al. *In NAVITEC*, 2010.

</details>

<details open>
<summary>Cross-Modal Perception (11)</summary>

- [Temporal Misalignment Attacks against Multimodal Perception in Autonomous Driving](https://arxiv.org/abs/2507.09095). Shahriar et al. *arXiv 2507.09095*, 2025.
- [Malicious Attacks against Multi-Sensor Fusion in Autonomous Driving](https://scholar.google.com/scholar?q=Malicious+Attacks+against+Multi-Sensor+Fusion+in+Autonomous+Driving). Zhu et al. *In Proceedings of the ACM International Conference on Mobile Computing and Networking (MobiCom)*, 2024.
- [MMCert: Provable Defense Against Adversarial Attacks to Multi-Modal Models](https://arxiv.org/abs/2403.19080). Wang et al. *In CVPR*, 2024.
- [A robust multi-sensor fusion model against adversarial patch attack](https://scholar.google.com/scholar?q=A+robust+multi-sensor+fusion+model+against+adversarial+patch+attack). El-Fatyany et al. *ResearchGate preprint*, 2024.
- [Security Analysis of Camera-LiDAR Fusion Against Black-Box Attacks on Autonomous Vehicles](https://arxiv.org/abs/2106.07098). Hallyburton et al. *In USENIX Security*, 2022.
- [Adversarial Robustness of Deep Sensor Fusion Models](https://arxiv.org/abs/2006.13192). Wang et al. *In WACV*, 2020.
- [Invisible for both Camera and LiDAR: Security of Multi-Sensor Fusion based Perception in Autonomous Driving Under Physical-World Attacks](https://arxiv.org/abs/2106.09249). Cao et al. *In S&P*, 2021.

- [Not What You Asked For: Typographic Attacks in Household Robot Manipulation](https://arxiv.org/abs/2605.18593). Iranmanesh and Liu. *arXiv 2605.18593*, 2026.
- [BlueSuffix: Reinforced Blue Teaming for Vision-Language Models Against Jailbreak Attacks](https://scholar.google.com/scholar?q=BlueSuffix%3A+Reinforced+Blue+Teaming+for+Vision-Language+Models+Against+Jailbreak+Attacks). Zhao et al. *In ICLR*, 2025.
- [MMCert](https://scholar.google.com/scholar?q=MMCert). Wang et al. *In CVPR*, 2024.
- [On Evaluating the Robustness of Large Vision-Language Models via Untargeted Modality Alignment Breaking Adversarial Attack](https://scholar.google.com/scholar?q=On+Evaluating+the+Robustness+of+Large+Vision-Language+Models+via+Untargeted+Modality+Alignment+Breaking+Adversarial+Attack). Li et al. *In USENIX Security*, 2026.
</details>

</details>

---

<details open>
<summary>🧠 <b>Cognition</b> (39 papers)</summary>

<details open>
<summary>Instruction Understanding (16)</summary>

- [Advancing Embodied Agent Security: From Safety Benchmarks to Input Moderation](https://arxiv.org/abs/2504.15699). Wang et al. *arXiv 2504.15699*, 2025.
- [Semantic Denial of Service in LLM-Controlled Robots](https://arxiv.org/abs/2604.24790). Steinberg and Gal. *arXiv 2604.24790*, 2026.
- [Seeing No Evil: Blinding Large Vision-Language Models to Safety Instructions via Adversarial Attention Hijacking](https://arxiv.org/abs/2604.10299). Li et al. *In ACL*, 2026.
- [Mitigating Trust Boundary Confusion from Visual Injections on Vision-Language Agentic Systems](https://arxiv.org/abs/2604.19844). Chang et al. *arXiv 2604.19844*, 2026.
- [Safe LLM-Controlled Robots with Formal Guarantees via Reachability Analysis](https://arxiv.org/abs/2503.03911). Hafez et al. *arXiv 2503.03911*, 2025.
- [BadNAVer: Exploring Jailbreak Attacks On Vision-and-Language Navigation](https://arxiv.org/abs/2505.12443). Lyu et al. *arXiv 2505.12443*, 2025.
- [AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697). Liu et al. *arXiv 2506.14697*, 2025.
- [Embodied Scene Understanding for Vision Language Models via MetaVQA](https://arxiv.org/abs/2501.09167). Wang et al. *In CVPR*, 2025.
- [Preventing Robotic Jailbreaking via Multimodal Domain Adaptation](https://arxiv.org/abs/2509.23281). Marchiori et al. *arXiv 2509.23281*, 2025.
- [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://arxiv.org/abs/2502.09560). Yang et al. *arXiv preprint*, 2025.
- [CHAI: Command Hijacking against embodied AI](https://arxiv.org/abs/2510.00181). Burbano et al. *arXiv 2510.00181*, 2025.
- [IndustryEQA: Pushing the Frontiers of Embodied Question Answering in Industrial Scenarios](https://arxiv.org/abs/2505.20640). Li et al. *arXiv preprint*, 2024.
- [MMRo: Are Multimodal LLMs Eligible as the Brain for In-Home Robotics?](https://arxiv.org/abs/2406.19693). Li et al. *arXiv 2406.19693*, 2024.
- [SQA3D: Situated Question Answering in 3D Scenes](https://arxiv.org/abs/2210.07474). Ma et al. *In ICLR*, 2023.

- [Safety Guardrails for LLM-Enabled Robots](https://scholar.google.com/scholar?q=Safety+Guardrails+for+LLM-Enabled+Robots). Ravichandran et al. *IEEE RA-L*, 2026.
- [A Survey of Large Audio Language Models: Generalization, Trustworthiness, and Outlook](https://arxiv.org/abs/2605.20266). Luo et al. *arXiv 2605.20266*, 2026.
</details>

<details open>
<summary>World Model (19)</summary>

- [SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model](https://arxiv.org/abs/2606.20698). Tang et al. *arXiv 2606.20698*, 2026.
- [Safety, Security, and Cognitive Risks in World Models](https://arxiv.org/abs/2604.01346). Parmar. *arXiv 2604.01346*, 2026.
- [TRAP: Tail-aware Ranking Attack for World-Model Planning](https://arxiv.org/abs/2605.01950). Duan et al. *arXiv 2605.01950*, 2026.
- [Benchmarking Vision-Language Models under Contradictory Virtual Content Attacks in AR](https://arxiv.org/abs/2604.05510). Xiu et al. *arXiv 2604.05510*, 2026.
- [The Safety Challenge of World Models for Embodied AI Agents: A Review](https://arxiv.org/abs/2510.05865). Baraldi et al. *arXiv 2510.05865*, 2025.
- [MASH-VLM: Mitigating Action-Scene Hallucination in Video-LLMs through Disentangled Spatial-Temporal Representations](https://arxiv.org/abs/2503.15871). Bae et al. *In CVPR*, 2025.
- [A Comprehensive Survey on World Models for Embodied AI](https://arxiv.org/abs/2510.16732). Li et al. *arXiv 2510.16732*, 2025.
- [VLM-SAFE: Vision-Language Model-Guided Safety-Aware Reinforcement Learning with World Models for Autonomous Driving](https://arxiv.org/abs/2505.16377). Qu et al. *arXiv preprint*, 2025.
- [Multi-Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2407.06192). Chen et al. *In NeurIPS*, 2024.
- [SafeDreamer: Safe Reinforcement Learning with World Models](https://arxiv.org/abs/2307.07176). Huang et al. *In ICLR*, 2024.
- [Learning Latent Dynamic Robust Representations for World Models](https://arxiv.org/abs/2405.06263). Sun et al. *In ICML*, 2024.
- [Driving Into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving](https://arxiv.org/abs/2311.17918). Wang et al. *In CVPR*, 2024.
- [Scalable Policy Evaluation with Video World Models](https://arxiv.org/abs/2511.11520). Tseng et al. *arXiv 2511.11520*, 2024.

- [CtrlAttack: A Unified Attack on World-Model Control in Diffusion Models](https://arxiv.org/abs/2603.13435). Xu et al. *arXiv 2603.13435*, 2026.
- [HomeGuard: VLM-Based Embodied Safeguard for Identifying Contextual Risk in Household Task](https://arxiv.org/abs/2603.14367). Lu et al. *arXiv 2603.14367*, 2026.
- [SafeDream: Safety World Model for Proactive Early Jailbreak Detection](https://arxiv.org/abs/2604.16824). Yan et al. *arXiv 2604.16824*, 2026.
- [When World Models Dream Wrong: Physical-Conditioned Adversarial Attacks against World Models](https://arxiv.org/abs/2602.18739). Guo et al. *arXiv 2602.18739*, 2026.
- [World Model Robustness via Surprise Recognition](https://arxiv.org/abs/2512.01119). Zollicoffer et al. *arXiv 2512.01119*, 2025.
- [Generating Robot Constitutions & Benchmarks for Semantic Safety](https://arxiv.org/abs/2503.08663). Sermanet et al. *arXiv 2503.08663*, 2025.
</details>

<details open>
<summary>Reasoning (4)</summary>

- [HEAL: An Empirical Study on Hallucinations in Embodied Agents Driven by Large Language Models](https://arxiv.org/abs/2506.15065). Chakraborty et al. *In Findings of the Association for Computational Linguistics: EMNLP*, 2025.
- [H-CoT: Hijacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models, Including OpenAI o1/o3, DeepSeek-R1, and Gemini 2.0 Flash Thinking](https://arxiv.org/abs/2502.12893). Kuo et al. *arXiv 2502.12893*, 2025.
- [π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164). Black et al. *arXiv 2410.24164*, 2024.

- [Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation](https://arxiv.org/abs/2603.12717). Trinh et al. *arXiv 2603.12717*, 2026.
</details>

</details>

---

<details open>
<summary>🗺️ <b>Planning</b> (80 papers)</summary>

<details open>
<summary>Task Planning (32)</summary>

- [Using Large Language Models for Embodied Planning Introduces Systematic Safety Risks](https://arxiv.org/abs/2604.18463). Zhang et al. *arXiv 2604.18463*, 2026.
- [SafeMind: Benchmarking and Mitigating Safety Risks in Embodied LLM Agents](https://arxiv.org/abs/2509.25885). Chen et al. *arXiv 2509.25885*, 2025.
- [A Framework for Benchmarking and Aligning Task-Planning Safety in LLM-Based Embodied Agents](https://arxiv.org/abs/2504.14650). Huang et al. *arXiv 2504.14650*, 2025.
- [HASARD: A Benchmark for Vision-Based Safe Reinforcement Learning in Embodied Agents](https://arxiv.org/abs/2503.08241). Tomilin et al. *In ICLR*, 2025.
- [Robo-Troj: Attacking LLM-based Task Planners](https://arxiv.org/abs/2504.17070). Nahian et al. *arXiv 2504.17070*, 2025.
- [SafePlan: Leveraging Formal Logic and Chain-of-Thought Reasoning for Enhanced Safety in LLM-based Robotic Task Planning](https://arxiv.org/abs/2503.06892). Obi et al. *arXiv 2503.06892*, 2025.
- [RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic](https://arxiv.org/abs/2512.21220). Wang et al. *arXiv 2512.21220*, 2025.
- [CEE: An Inference-Time Jailbreak Defense for Embodied Intelligence via Subspace Concept Rotation](https://arxiv.org/abs/2504.13201). Yang et al. *arXiv 2504.13201*, 2025.
- [Enhancing reliability in LLM-integrated robotic systems: A unified approach to security and safety](https://arxiv.org/abs/2509.02163). Zhang et al. *Journal of Systems and Software*, 2025.
- [Malicious Path Manipulations via Exploitation of Representation Vulnerabilities of Vision-Language Navigation Systems](https://arxiv.org/abs/2407.07392). Islam et al. *In IROS*, 2024.
- [Can We Trust Embodied Agents? Exploring Backdoor Attacks against Embodied LLM-Based Decision-Making Systems](https://arxiv.org/abs/2405.20774). Jiao et al. *arXiv 2405.20774*, 2024.
- [Compromising Embodied Agents with Contextual Backdoor Attacks](https://arxiv.org/abs/2408.02882). Liu et al. *arXiv 2408.02882*, 2024.
- [Exploring the Robustness of Decision-Level Through Adversarial Attacks on LLM-Based Embodied Models](https://arxiv.org/abs/2405.19802). Liu et al. *In MM*, 2024.
- [POEX: Towards Policy Executable Jailbreak Attacks Against the LLM-based Robots](https://arxiv.org/abs/2412.16633). Lu et al. *arXiv 2412.16633*, 2024.
- [Jailbreaking LLM-Controlled Robots](https://arxiv.org/abs/2410.13691). Robey et al. *arXiv 2410.13691*, 2024.
- [BadRobot: Jailbreaking Embodied LLMs in the Physical World](https://arxiv.org/abs/2407.20242). Zhang et al. *arXiv 2407.20242*, 2024.
- [SafeEmbodAI: a Safety Framework for Mobile Robots in Embodied AI Systems](https://arxiv.org/abs/2409.01630). Zhang et al. *arXiv 2409.01630*, 2024.
- [Adversarial Attacks on Optimization based Planners](https://arxiv.org/abs/2011.00095). Vemprala and Kapoor. *In ICRA*, 2021.

- [Adversarial Flow Matching for Imperceptible Attacks on End-to-End Autonomous Driving](https://arxiv.org/abs/2605.00880). Zeng et al. *arXiv 2605.00880*, 2026.
- [Benchmarking the Safety of Large Language Models for Robotic Health Attendant Control](https://arxiv.org/abs/2604.26577). Nakao and Takemoto. *arXiv 2604.26577*, 2026.
- [AgentSafe: Safeguarding Large Language Model-Based Multi-Agent Systems via Hierarchical Data Management](https://arxiv.org/abs/2503.04392). Mao et al. *arXiv 2503.04392*, 2025.
- [Generating Explanations for Embodied Action Decision from Visual Observation](https://scholar.google.com/scholar?q=Generating+Explanations+for+Embodied+Action+Decision+from+Visual+Observation). Wang et al. *In MM*, 2023.
- [RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents](https://arxiv.org/abs/2605.19328). Yeke et al. *arXiv 2605.19328*, 2026.
- [MuJoCo: A Physics Engine for Model-Based Control](https://scholar.google.com/scholar?q=MuJoCo%3A+A+Physics+Engine+for+Model-Based+Control). Todorov et al. *In IROS*, 2012.
- [Design and Use Paradigms for Gazebo, an Open-Source Multi-Robot Simulator](https://scholar.google.com/scholar?q=Design+and+Use+Paradigms+for+Gazebo%2C+an+Open-Source+Multi-Robot+Simulator). Koenig and Howard. *In IROS*, 2004.
- [M3Bench: Benchmarking Whole-Body Motion Generation for Mobile Manipulation in 3D Scenes](https://scholar.google.com/scholar?q=M3Bench%3A+Benchmarking+Whole-Body+Motion+Generation+for+Mobile+Manipulation+in+3D+Scenes). Zhang et al. *IEEE Robotics and Automation Letters (RA-L)*, 2025.
- [PyBullet, a Python Module for Physics Simulation for Games, Robotics and Machine Learning](https://scholar.google.com/scholar?q=PyBullet%2C+a+Python+Module+for+Physics+Simulation+for+Games%2C+Robotics+and+Machine+Learning). Coumans and Bai. *http://pybullet.org*, 2021.
- [iGibson 2.0: Object-Centric Simulation for Robot Learning of Everyday Household Tasks](https://scholar.google.com/scholar?q=iGibson+2.0%3A+Object-Centric+Simulation+for+Robot+Learning+of+Everyday+Household+Tasks). Li et al. *In CoRL*, 2022.
- [Habitat 3.0: A Co-Habitat for Humans, Avatars and Robots](https://arxiv.org/abs/2310.13724). Puig et al. *arXiv 2310.13724*, 2023.
- [Isaac Sim](https://scholar.google.com/scholar?q=Isaac+Sim). NVIDIA.
- [Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making](https://scholar.google.com/scholar?q=Embodied+Agent+Interface%3A+Benchmarking+LLMs+for+Embodied+Decision+Making). Li et al. *In NeurIPS*, 2024.
- [VestaBench: An Embodied Benchmark for Safe Long-Horizon Planning Under Multi-Constraint and Adversarial Settings](https://scholar.google.com/scholar?q=VestaBench%3A+An+Embodied+Benchmark+for+Safe+Long-Horizon+Planning). Sadhu et al. *In EMNLP*, 2025.
</details>

<details open>
<summary>Trajectory Planning (34)</summary>

- [SafeBench: A Benchmarking Platform for Safety Evaluation of Autonomous Vehicles](https://arxiv.org/abs/2206.09682). Xu et al. *In NeurIPS*, 2022.
- [PINA: Prompt Injection Attack against Navigation Agents](https://arxiv.org/abs/2601.13612). Liu et al. *In ICASSP*, 2026.
- [Beyond Crash: Hijacking Your Autonomous Vehicle for Fun and Profit](https://arxiv.org/abs/2602.07249). Sun et al. *arXiv 2602.07249*, 2026.
- [Universal Closed-Box Adversarial Attack for Trajectory Representation via Controlling High-Dimensional Iterative Constraints](https://scholar.google.com/scholar?q=Universal+Closed-Box+Adversarial+Attack+for+Trajectory+Representation+via+Controlling+High-Dimensional+Iterative+Constraints). Bai et al. *IEEE Internet of Things Journal (IoT-J)*, 2025.
- [Avatar: Adversarial Vehicle Trajectory Attack Targeting Autonomous Driving Planner](https://scholar.google.com/scholar?q=Avatar%3A+Adversarial+Vehicle+Trajectory+Attack+Targeting+Autonomous+Driving+Planner). Liu and Mori. *In EuroS&PW*, 2025.
- [Adversarial Attack on Trajectory Prediction for Autonomous Vehicles with Generative Adversarial Networks](https://scholar.google.com/scholar?q=Adversarial+Attack+on+Trajectory+Prediction+for+Autonomous+Vehicles+with+Generative+Adversarial+Networks). Fan et al. *In IROS*, 2024.
- [How Secure Are Large Language Models (LLMs) for Navigation in Urban Environments?](https://arxiv.org/abs/2402.09546). Wen et al. *arXiv 2402.09546*, 2024.
- [Characterizing Physical Adversarial Attacks on Robot Motion Planners](https://scholar.google.com/scholar?q=Characterizing+Physical+Adversarial+Attacks+on+Robot+Motion+Planners). Wu et al. *In ICRA*, 2024.
- [AdvDiffuser: Generating Adversarial Safety-Critical Driving Scenarios via Guided Diffusion](https://arxiv.org/abs/2410.08453). Xie et al. *In IROS*, 2024.
- [Robust Inverse Constrained Reinforcement Learning under Model Misspecification](https://scholar.google.com/scholar?q=Robust+inverse+constrained+reinforcement+learning+under+model+misspecification). Xu and Liu. *In ICML*, 2024.
- [A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems](https://arxiv.org/abs/2408.03515). Zhang et al. *In ISSREW*, 2024.
- [Visual Adversarial Attack on Vision-Language Models for Autonomous Driving](https://arxiv.org/abs/2411.18275). Zhang et al. *arXiv 2411.18275*, 2024.
- [Vehicle Trajectory Prediction based Predictive Collision Risk Assessment for Autonomous Driving in Highway Scenarios](https://arxiv.org/abs/2304.05610). Meng et al. *arXiv 2304.05610*, 2023.
- [Reducing Safety Interventions in Provably Safe Reinforcement Learning](https://arxiv.org/abs/2303.03339). Thumm et al. *In IROS*, 2023.
- [Robustness of Trajectory Prediction Models Under Map-Based Attacks](https://scholar.google.com/scholar?q=Robustness+of+trajectory+prediction+models+under+map-based+attacks). Zheng et al. *In WACV*, 2023.
- [AdvDO: Realistic Adversarial Attacks for Trajectory Prediction](https://arxiv.org/abs/2209.08744). Cao et al. *In ECCV*, 2022.
- [KING: Generating Safety-Critical Driving Scenarios for Robust Imitation via Kinematics Gradients](https://arxiv.org/abs/2204.13683). Hanselmann et al. *In ECCV*, 2022.
- [Generating Useful Accident-Prone Driving Scenarios via a Learned Traffic Prior](https://arxiv.org/abs/2112.05077). Rempe et al. *In CVPR*, 2022.
- [On Adversarial Robustness of Trajectory Prediction for Autonomous Vehicles](https://arxiv.org/abs/2201.05057). Zhang et al. *In CVPR*, 2022.
- [Stochastic Model Predictive Control With a Safety Guarantee for Automated Driving](https://arxiv.org/abs/2009.09381). Br{\"u}digam et al. *In IV*, 2021.
- [Intelligent driving intelligence test for autonomous vehicles with naturalistic and adversarial environment](https://scholar.google.com/scholar?q=Intelligent+driving+intelligence+test+for+autonomous+vehicles+with+naturalistic+and+adversarial+environment). Feng et al. *Nature Communications*, 2021.
- [AdvSim: Generating Safety-Critical Scenarios for Self-Driving Vehicles](https://arxiv.org/abs/2101.06549). Wang et al. *In CVPR*, 2021.
- [Learning to Collide: An Adaptive Safety-Critical Scenarios Generating Method](https://arxiv.org/abs/2003.01197). Ding et al. *In IROS*, 2020.
- [Risky Action Recognition in Lane Change Video Clips using Deep Spatiotemporal Networks with Segmentation Mask Transfer](https://arxiv.org/abs/1906.02859). Yurtsever et al. *In ITSC*, 2019.

- [Exploring Adversarial Obstacle Attacks in Search-Based Path Planning for Autonomous Mobile Robots](https://scholar.google.com/scholar?q=Exploring+Adversarial+Obstacle+Attacks+in+Search-Based+Path+Planning+for+Autonomous+Mobile+Robots). Szvoren et al. *In ICRA*, 2025.
- [NavSim: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking](https://scholar.google.com/scholar?q=NavSim%3A+Data-Driven+Non-Reactive+Autonomous+Vehicle+Simulation+and+Benchmarking). Dauner et al. *In NeurIPS*, 2024.
- [CommonRoad-RL: A Configurable Reinforcement Learning Environment for Motion Planning of Autonomous Vehicles](https://scholar.google.com/scholar?q=CommonRoad-RL%3A+A+Configurable+Reinforcement+Learning+Environment+for+Motion+Planning+of+Autonomous+Vehicles). Wang et al. *In ITSC*, 2021.
- [Scenic: A Language for Scenario Specification and Data Generation](https://scholar.google.com/scholar?q=Scenic%3A+A+Language+for+Scenario+Specification+and+Data+Generation). Fremont et al. *Machine Learning (MLJ)*, 2023.
- [Microscopic Traffic Simulation Using SUMO](https://scholar.google.com/scholar?q=Microscopic+Traffic+Simulation+Using+SUMO). Lopez et al. *In ITSC*, 2018.
- [CARLA: An Open Urban Driving Simulator](https://scholar.google.com/scholar?q=CARLA%3A+An+Open+Urban+Driving+Simulator). Dosovitskiy et al. *In CoRL*, 2017.
- [An Environment for Autonomous Driving Decision-Making](https://scholar.google.com/scholar?q=An+Environment+for+Autonomous+Driving+Decision-Making). Leurent. 2018.
- [Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-to-End Autonomous Driving](https://scholar.google.com/scholar?q=Bench2Drive%3A+Towards+Multi-Ability+Benchmarking+of+Closed-Loop+End-to-End+Autonomous+Driving). Jia et al. *In NeurIPS*, 2024.
- [MetaDrive: Composing Diverse Driving Scenarios for Generalizable Reinforcement Learning](https://scholar.google.com/scholar?q=MetaDrive%3A+Composing+Diverse+Driving+Scenarios+for+Generalizable+Reinforcement+Learning). Li et al. *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)*, 2022.
- [SUMMIT: A Simulator for Urban Driving in Massive Mixed Traffic](https://scholar.google.com/scholar?q=SUMMIT%3A+A+Simulator+for+Urban+Driving+in+Massive+Mixed+Traffic). Cai et al. *In ICRA*, 2020.
</details>

<details open>
<summary>Multi-Agent Planning (14)</summary>

- [RoboRebound: Multi-Robot System Defense with Bounded-Time Interaction](https://scholar.google.com/scholar?q=RoboRebound). Gandhi et al. *In Proceedings of the European Conference on Computer Systems (EuroSys)*, 2025.
- [Multi-Robot Coordination with Adversarial Perception](https://arxiv.org/abs/2504.09047). Bahrami et al. *In International Conference on Unmanned Aircraft Systems (ICUAS)*, 2025.
- [Red-Teaming LLM Multi-Agent Systems via Communication Attacks](https://arxiv.org/abs/2502.14847). He et al. *In ACL*, 2025.
- [Distributed Resilience-Aware Control in Multi-Robot Networks](https://arxiv.org/abs/2504.03120). Lee and Panagou. *In IEEE Conference on Decision and Control (CDC)*, 2025.
- [Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents](https://arxiv.org/abs/2505.02077). Witt. *arXiv 2505.02077*, 2025.
- [A Systematic Literature Review on Multi-Robot Task Allocation](https://scholar.google.com/scholar?q=A+Systematic+Literature+Review+on+Multi-Robot+Task+Allocation). KA, Athira and Subramaniam, Umashankar. *ACM Computing Surveys (CSUR)*, 2024.
- [Adversarial Machine Learning Attacks and Defences in Multi-Agent Reinforcement Learning](https://scholar.google.com/scholar?q=Adversarial+Machine+Learning+Attacks+and+Defences+in+Multi-Agent+Reinforcement+Learning). Standen et al. *ACM Computing Surveys (CSUR)*, 2024.
- [Robot swarms neutralize harmful Byzantine robots using a blockchain-based token economy](https://scholar.google.com/scholar?q=Robot+swarms+neutralize+harmful+Byzantine+robots+using+a+blockchain-based+token+economy). Strobel et al. *Science Robotics*, 2023.
- [Dynamic multi-robot task allocation under uncertainty and temporal constraints](https://arxiv.org/abs/2005.13109). Choudhury et al. *Autonomous Robots*, 2020.
- [The Emergence of Adversarial Communication in Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2008.02616). Blumenkamp and Prorok. *In CoRL*, 2021.
- [Multi-robot Coordination and Planning in Uncertain and Adversarial Environments](https://arxiv.org/abs/2105.00389). Zhou and Tokekar. *In Robotics*, 2021.
- [Resilient Distributed Diffusion for Multi-Robot Systems Using Centerpoint](https://scholar.google.com/scholar?q=Resilient+Distributed+Diffusion+for+Multi-Robot+Systems+Using+Centerpoint). Li et al. *In RSS*, 2020.
- [Blockchain Technology Secures Robot Swarms: A Comparison of Consensus Protocols and Their Resilience to Byzantine Robots](https://scholar.google.com/scholar?q=Blockchain+Technology+Secures+Robot+Swarms%3A+A+Comparison+of+Consensus+Protocols+and+Their+Resilience+to+Byzantine+Robots). Strobel et al. *In Robotics*, 2020.

- [Hierarchical Attacks for Multi-Modal Multi-Agent Reasoning](https://scholar.google.com/scholar?q=Hierarchical+Attacks+for+Multi-Modal+Multi-Agent+Reasoning). Zhou et al. *In CVPR*, 2026.
</details>

</details>

---

<details open>
<summary>🤖 <b>Action and Interaction</b> (112 papers)</summary>

<details open>
<summary>Robot Control (97)</summary>

- [AdvGrasp: Adversarial Attacks on Robotic Grasping from a Physical Perspective](https://arxiv.org/abs/2507.09857). Wang et al. *arXiv 2507.09857*, 2025.
- [Optimal Actuator Attacks on Autonomous Vehicles Using Reinforcement Learning](https://arxiv.org/abs/2502.07839). Wang et al. *arXiv 2502.07839*, 2025.
- [RedVLA: Physical Red Teaming of Vision-Language-Action Models](https://arxiv.org/abs/2604.22591). Zhang et al. *arXiv 2604.22591*, 2026.
- [HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2604.12447). Chen et al. *arXiv 2604.12447*, 2026.
- [Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming](https://arxiv.org/abs/2604.05595). Tong et al. *arXiv 2604.05595*, 2026.
- [JailWAM: Jailbreaking World Action Models in Robot Control](https://arxiv.org/abs/2604.05498). Liu et al. *arXiv 2604.05498*, 2026.
- [From Prompt to Physical Action: Structured Backdoor Attacks on LLM-Mediated Robotic Control Systems](https://arxiv.org/abs/2604.03890). Xie and Wei-Kocsis. *arXiv 2604.03890*, 2026.
- [Tex3D: Objects as Attack Surfaces via Adversarial 3D Textures for Vision-Language-Action Models](https://arxiv.org/abs/2604.01618). Chen et al. *arXiv 2604.01618*, 2026.
- [UniAda: Universal Adaptive Multi-objective Adversarial Attack for End-to-End Autonomous Driving Systems](https://arxiv.org/abs/2604.23362). Zhang et al. *arXiv 2604.23362*, 2026.
- [STRONG-VLA: Decoupled Robustness Learning for Vision-Language-Action Models under Multimodal Perturbations](https://arxiv.org/abs/2604.10055). Xie et al. *arXiv 2604.10055*, 2026.
- [BEAT: Visual Backdoor Attacks on VLM-based Embodied Agents via Contrastive Trigger Learning](https://arxiv.org/abs/2510.27623). Zhan et al. *In ICLR*, 2026.
- [Regret-based Defense in Adversarial Reinforcement Learning](https://arxiv.org/abs/2302.06912). Belaire et al. *In AAMAS*, 2024.
- [Train Hard, Fight Easy: Robust Meta Reinforcement Learning](https://arxiv.org/abs/2301.11147). Greenberg et al. *In NeurIPS*, 2023.
- [Who Is the Strongest Enemy? Towards Optimal and Efficient Evasion Attacks in Deep RL](https://arxiv.org/abs/2106.05087). Sun et al. *In ICLR*, 2022.
- [Natural Actor-Critic for Robust Reinforcement Learning with Function Approximation](https://arxiv.org/abs/2307.08875). Zhou et al. *In NeurIPS*, 2023.
- [LIBERO-X: Robustness Litmus for Vision-Language-Action Models](https://arxiv.org/abs/2602.06556). Wang et al. *arXiv 2602.06556*, 2026.
- [On Minimizing Adversarial Counterfactual Error in Adversarial Reinforcement Learning](https://arxiv.org/abs/2406.04724). Belaire et al. *In ICLR*, 2025.
- [PNAct: Crafting Backdoor Attacks in Safe Reinforcement Learning](https://arxiv.org/abs/2507.00485). Guo et al. *In IJCAI*, 2025.
- [ANNIE: Be Careful of Your Robots](https://arxiv.org/abs/2509.03383). Huang et al. 2025.
- [Adversarial Attacks on Robotic Vision Language Action Models](https://arxiv.org/abs/2506.03350). Jones et al. 2025.
- [Embodied Red Teaming for Auditing Robotic Foundation Models](https://arxiv.org/abs/2411.18676). Karnik et al. 2025.
- [Robust Multi-Agent Reinforcement Learning via Minimax Deep Deterministic Policy Gradient](https://scholar.google.com/scholar?q=Robust+Multi-Agent+Reinforcement+Learning). Li et al. *IEEE Transactions on Neural Networks and Learning Systems (TNNLS)*, 2025.
- [TooBadRL: Trigger Optimization to Boost Effectiveness of Backdoor Attacks on Deep Reinforcement Learning](https://arxiv.org/abs/2506.09562). Li et al. 2025.
- [AERMANI-VLM: Structured Prompting and Reasoning for Aerial Manipulation with Vision Language Models](https://arxiv.org/abs/2511.01472). Mishra et al. *arXiv preprint arXiv.2511.01472*, 2025.
- [Off-Policy Actor-Critic for Adversarial Observation Robustness: Virtual Alternative Training via Symmetric Policy Evaluation](https://arxiv.org/abs/2506.16753). Nakanishi et al. *In ICML*, 2025.
- [Action Robust Reinforcement Learning via Optimal Adversary Aware Policy Optimization](https://arxiv.org/abs/2507.03372). Nie et al. 2025.
- [How Vulnerable Is My Learned Policy? Universal Adversarial Perturbation Attacks On Modern Behavior Cloning Policies](https://arxiv.org/abs/2502.03698). Patil et al. 2025.
- [Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://arxiv.org/abs/2411.13587). Wang et al. *In ICCV*, 2025.
- [Towards Robust Deep Reinforcement Learning against Environmental State Perturbation](https://arxiv.org/abs/2506.08961). Wang and Liu. 2025.
- [LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626). Fei et al. *arXiv 2510.13626*, 2025.
- [Run-time Observation Interventions Make Vision-Language-Action Models More Visually Robust](https://arxiv.org/abs/2410.01971). Hancock et al. *In ICRA*, 2025.
- [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891). Hu et al. *arXiv 2512.11891*, 2025.
- [AttackVLA: Benchmarking Adversarial and Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.12149). Li et al. *arXiv:2511.12149*, 2025.
- [When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.21192). Lu et al. *arXiv:2511.21192*, 2025.
- [ADVEDM:Fine-grained Adversarial Attack against VLM-based Embodied Agents](https://arxiv.org/abs/2509.16645). Wang et al. *arXiv 2509.16645*, 2025.
- [FreezeVLA: Action-Freezing Attacks against Vision-Language-Action Models](https://arxiv.org/abs/2509.19870). Wang et al. *arXiv 2509.19870*, 2025.
- [Model-agnostic Adversarial Attack and Defense for Vision-Language-Action Models](https://arxiv.org/abs/2510.13237). Xu et al. *arXiv 2510.13237*, 2025.
- [BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization](https://arxiv.org/abs/2505.16640). Xu et al. *arXiv:2510.10932*, 2025.
- [When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.16203). Yan et al. *arXiv:2511.16203*, 2025.
- [Attention-Guided Patch-Wise Sparse Adversarial Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.21663). Zhang et al. *arXiv:2511.21663*, 2025.
- [SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning](https://arxiv.org/abs/2503.03480). Zhang et al. *In NeurIPS*, 2025.
- [Goal-oriented Backdoor Attack against Vision-Language-Action Models via Physical Objects](https://arxiv.org/abs/2510.09269). Zhou et al. *arXiv 2510.09269*, 2025.
- [Diffusion Policy Attacker: Crafting Adversarial Attacks for Diffusion-based Policies](https://arxiv.org/abs/2405.19424). Chen et al. *In NeurIPS*, 2024.
- [Manipulation Facing Threats: Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models](https://arxiv.org/abs/2409.13174). Cheng et al. 2024.
- [Bring Your Own (Non-Robust) Algorithm to Solve Robust MDPs by Estimating The Worst Kernel](https://arxiv.org/abs/2306.05859). Gadot et al. *In ICML*, 2024.
- [Baffle: Hiding Backdoors in Offline Reinforcement Learning Datasets](https://arxiv.org/abs/2210.04688). Gong et al. *In S&P*, 2024.
- [Game-Theoretic Robust Reinforcement Learning Handles Temporally-Coupled Perturbations](https://scholar.google.com/scholar?q=Game-Theoretic+Robust+Reinforcement+Learning+Handles+Temporally-Coupled+Perturbations). Liang et al. *In ICLR*, 2024.
- [Rethinking Adversarial Policies: A Generalized Attack Formulation and Provable Defense in RL](https://arxiv.org/abs/2305.17342). Liu et al. *In ICLR*, 2024.
- [Beyond Worst-case Attacks: Robust RL with Adaptive Defense via Non-dominated Policies](https://arxiv.org/abs/2402.12673). Liu et al. *In ICLR*, 2024.
- [Mitigating Adversarial Perturbations for Deep Reinforcement Learning via Vector Quantization](https://arxiv.org/abs/2410.03376). Luu et al. *In IROS*, 2024.
- [SUB-PLAY: Adversarial Policies against Partially Observed Multi-Agent Reinforcement Learning Systems](https://arxiv.org/abs/2402.03741). Ma et al. *In CCS*, 2024.
- [Adversarially Robust Decision Transformer](https://arxiv.org/abs/2407.18414). Tang et al. *In NeurIPS*, 2024.
- [Towards Robust Offline Reinforcement Learning under Diverse Data Corruption](https://arxiv.org/abs/2310.12955). Yang et al. *In ICLR*, 2024.
- [Uncertainty-based Offline Variational Bayesian Reinforcement Learning for Robustness under Diverse Data Corruptions](https://arxiv.org/abs/2411.00465). Yang et al. *In NeurIPS*, 2024.
- [Rethinking the Intermediate Features in Adversarial Attacks: Misleading Robotic Models via Adversarial Distillation](https://arxiv.org/abs/2411.15222). Zhao et al. 2024.
- [Toward Evaluating Robustness of Reinforcement Learning with Adversarial Policy](https://arxiv.org/abs/2305.02605). Zheng et al. *In DSN*, 2024.
- [Robot Collapse: Supply Chain Backdoor Attacks Against VLM-based Robotic Manipulation](https://arxiv.org/abs/2411.11683). Wang et al. *arXiv 2411.11683*, 2024.
- [MARNet: Backdoor Attacks Against Cooperative Multi-Agent Reinforcement Learning](https://scholar.google.com/scholar?q=MARNet). Chen et al. *IEEE Transactions on Dependable and Secure Computing (TDSC)*, 2023.
- [PATROL: Provable Defense against Adversarial Policy in Two-player Games](https://scholar.google.com/scholar?q=PATROL). Guo et al. *In USENIX Security*, 2023.
- [PolicyCleanse: Backdoor Detection and Mitigation for Competitive Reinforcement Learning](https://arxiv.org/abs/2202.03609). Guo et al. *In ICCV*, 2023.
- [Trade-Off Between Robustness and Rewards Adversarial Training for Deep Reinforcement Learning Under Large Perturbations](https://scholar.google.com/scholar?q=Trade-Off+Between+Robustness). Huang et al. *IEEE Robotics and Automation Letters (RA-L)*, 2023.
- [Revisiting Domain Randomization via Relaxed State-Adversarial Policy Optimization](https://scholar.google.com/scholar?q=Revisiting+Domain+Randomization+Via+Relaxed+State-AdversarialPolicy+Optimization). Lien et al. *In ICML*, 2023.
- [Certifiably Robust Policy Learning against Adversarial Multi-Agent Communication](https://scholar.google.com/scholar?q=Certifiably+Robust+Policy+Learning+Against+Adversarial+Multi-Agent+Communication). Sun et al. *In ICLR*, 2023.
- [Robust multi-agent coordination via evolutionary generation of auxiliary adversarial attackers](https://arxiv.org/abs/2305.05909). Yuan et al. *In AAAI*, 2023.
- [A Robust Mean-Field Actor-Critic Reinforcement Learning Against Adversarial Perturbations on Agent States](https://arxiv.org/abs/2205.07229). Zhou et al. *IEEE Transactions on Neural Networks and Learning Systems (TNNLS)*, 2023.
- [Distributionally Adaptive Meta Reinforcement Learning](https://arxiv.org/abs/2210.03104). Ajay et al. *In NeurIPS*, 2022.
- [Learning Robust Policy against Disturbance in Transition Dynamics via State-Conservative Policy Optimization](https://arxiv.org/abs/2112.10513). Kuang et al. *In AAAI*, 2022.
- [Efficient Adversarial Training without Attacking: Worst-Case-Aware Robust Reinforcement Learning](https://arxiv.org/abs/2210.05927). Liang et al. *In NeurIPS*, 2022.
- [CROP: Certifying Robust Policies for Reinforcement Learning through Functional Smoothing](https://arxiv.org/abs/2106.09292). Wu et al. *In ICLR*, 2022.
- [Monotonic Robust Policy Optimization with Model Discrepancy](https://scholar.google.com/scholar?q=Monotonic+Robust+Policy+Optimization+with+Model+Discrepancy). Jiang et al. *In ICML*, 2021.
- [Robust Deep Reinforcement Learning through Adversarial Loss](https://arxiv.org/abs/2008.01976). Oikarinen et al. *In NeurIPS*, 2021.
- [BACKDOORL: Backdoor Attack against Competitive Reinforcement Learning](https://arxiv.org/abs/2105.00579). Wang et al. *In IJCAI*, 2021.
- [Robust Reinforcement Learning on State Observations with Learned Optimal Adversary](https://arxiv.org/abs/2101.08452). Zhang et al. *In ICLR*, 2021.
- [Adversarial Policies: Attacking Deep Reinforcement Learning](https://arxiv.org/abs/1905.10615). Gleave et al. *In ICLR*, 2020.
- [Spatiotemporally Constrained Action Space Attacks on Deep Reinforcement Learning Agents](https://arxiv.org/abs/1909.02583). Lee et al. *In AAAI*, 2020.
- [Stealthy and Efficient Adversarial Attacks against Deep Reinforcement Learning](https://arxiv.org/abs/2005.07099). Sun et al. *In AAAI*, 2020.
- [Robustifying Reinforcement Learning Agents via Action Space Adversarial Training](https://arxiv.org/abs/2007.07176). Tan et al. *In ACC*, 2020.
- [Robust Reinforcement Learning using Adversarial Populations](https://arxiv.org/abs/2008.01825). Vinitsky et al. 2020.
- [Robust Deep Reinforcement Learning against Adversarial Perturbations on State Observations](https://arxiv.org/abs/2003.08938). Zhang et al. *In NeurIPS*, 2020.
- [Action Robust Reinforcement Learning and Applications in Continuous Control](https://arxiv.org/abs/1901.09184). Tessler et al. *In ICML*, 2019.
- [Adversarially Robust Policy Learning through Active Construction of Physically-Plausible Perturbations](https://scholar.google.com/scholar?q=Adversarially+Robust+Policy+Learning+through+Active+Construction+of+Physically-Plausible+Perturbations). Mandlekar et al. *In IROS*, 2017.
- [Robust Adversarial Reinforcement Learning](https://arxiv.org/abs/1703.02702). Pinto et al. *In ICML*, 2017.
- [EPOpt: Learning Robust Neural Network Policies Using Model Ensembles](https://arxiv.org/abs/1610.01283). Rajeswaran et al. *In ICLR*, 2017.

- [Dreaming the Unseen: World Model-Regularized Diffusion Policy for Out-of-Distribution Robustness](https://arxiv.org/abs/2603.21017). Hu et al. *arXiv 2603.21017*, 2026.
- [FlowHijack: A Dynamics-Aware Backdoor Attack on Flow-Matching Vision-Language-Action Models](https://scholar.google.com/scholar?q=FlowHijack%3A+A+Dynamics-Aware+Backdoor+Attack+on+Flow-Matching+Vision-Language-Action+Models). An et al. *In CVPR*, 2026.
- [SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2601.14323). Xu et al. *arXiv 2601.14323*, 2026.
- [Backdoors in DRL: Four Environments Focusing on In-Distribution Triggers](https://arxiv.org/abs/2505.17248). Ashcraft et al. *arXiv 2505.17248*, 2025.
- [DropVLA: An Action-Level Backdoor Attack on Vision-Language-Action Models](https://arxiv.org/abs/2510.10932). Xu et al. *arXiv 2510.10932*, 2025.
- [RAT: Adversarial Attacks on Deep Reinforcement Agents for Targeted Behaviors](https://scholar.google.com/scholar?q=RAT%3A+Adversarial+Attacks+on+Deep+Reinforcement+Agents+for+Targeted+Behaviors). Bai et al. *In AAAI*, 2025.
- [Robust Multi-Agent Reinforcement Learning by Mutual Information Regularization](https://scholar.google.com/scholar?q=Robust+Multi-Agent+Reinforcement+Learning+by+Mutual+Information+Regularization). Li et al. *IEEE Transactions on Neural Networks and Learning Systems (TNNLS)*, 2025.
- [Breaking the Barrier: Enhanced Utility and Robustness in Smoothed DRL Agents](https://scholar.google.com/scholar?q=Breaking+the+Barrier%3A+Enhanced+Utility+and+Robustness+in+Smoothed+DRL+Agents). Sun et al. *In ICML*, 2024.
- [User-Oriented Robust Reinforcement Learning](https://scholar.google.com/scholar?q=User-Oriented+Robust+Reinforcement+Learning). You et al. *In AAAI*, 2023.
- [Robust Reinforcement Learning as a Stackelberg Game via Adaptively-Regularized Adversarial Training](https://scholar.google.com/scholar?q=Robust+Reinforcement+Learning+as+a+Stackelberg+Game+via+Adaptively-Regularized+Adversarial+Training). Huang et al. *In IJCAI*, 2022.
- [Toward Evaluating Robustness of Deep Reinforcement Learning with Continuous Control](https://scholar.google.com/scholar?q=Toward+Evaluating+Robustness+of+Deep+Reinforcement+Learning+with+Continuous+Control). Weng et al. *In ICLR*, 2020.
- [Deep Reinforcement Learning in the Era of Foundation Models: A Survey](https://scholar.google.com/scholar?q=Deep+Reinforcement+Learning+in+the+Era+of+Foundation+Models%3A+A+Survey). Mienye et al. *Computers*, 2026.
- [Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts](https://arxiv.org/abs/2605.22446). Sun et al. *arXiv 2605.22446*, 2026.
- [IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks](https://arxiv.org/abs/2506.16402). Lu et al. *arXiv 2506.16402*, 2025.
</details>

<details open>
<summary>Human-Agent Interaction (12)</summary>

- [Biomimetic Approach to Designing Trust-Based Robot-to-Human Object Handover in a Collaborative Assembly Task](https://scholar.google.com/scholar?q=Biomimetic+Approach+to+Designing+Trust-Based+Robot-to-Human+Object+Handover+in+a+Collaborative+Assembly+Task). Rahman et al. *In Robotics*, 2025.
- [LLM-Based Human-Agent Collaboration and Interaction Systems: A Survey](https://arxiv.org/abs/2505.00753). Zou et al. *arXiv 2505.00753*, 2025.
- [Compliant Blind Handover Control for Human-Robot Collaboration](https://arxiv.org/abs/2409.07155). Ferrari et al. *In IROS*, 2024.
- [Fast and Comfortable Robot-to-Human Handover for Mobile Cooperation Robot System](https://scholar.google.com/scholar?q=Fast+and+Comfortable+Robot-to-Human+Handover+for+Mobile+Cooperation+Robot+System). Meng et al. *Cyborg and Bionic Systems*, 2024.
- [Human-robot object handover: Recent progress and future direction](https://scholar.google.com/scholar?q=Human--Robot+Object+Handover%3A+Recent+Progress+and+Future+Direction). Duan et al. *In Robotics*, 2024.
- [PsySafe: A Comprehensive Framework for Psychological-based Attack, Defense, and Evaluation of Multi-agent System Safety](https://arxiv.org/abs/2401.11880). Zhang et al. *In ACL*, 2024.
- [Optimizing human-robot handovers: the impact of adaptive transport methods](https://scholar.google.com/scholar?q=Optimizing+Human-Robot+Handovers%3A+The+Impact+of+Adaptive+Transport+Methods). Käppler et al. *In Robotics*, 2023.
- [A Novel Human Intention Prediction Approach Based on Fuzzy Rules through Wearable Sensing in Human–Robot Handover](https://scholar.google.com/scholar?q=A+Novel+Human+Intention+Prediction+Approach+Based+on+Fuzzy+Rules+Through+Wearable+Sensing+in+Human--Robot+Handover). Zou et al. *In Robotics*, 2023.
- [A Taxonomy of Factors Influencing Perceived Safety in Human–Robot Interaction](https://scholar.google.com/scholar?q=A+Taxonomy+of+Factors+Influencing+Perceived+Safety+in+Human--Robot+Interaction). Akalin et al. *In Robotics*, 2023.
- [Handover Control for Human-Robot and Robot-Robot Collaboration](https://scholar.google.com/scholar?q=Handover+Control+for+Human-Robot+and+Robot-Robot+Collaboration). Costanzo et al. *In Robotics*, 2021.
- [Perceived Safety in Physical Human Robot Interaction - A Survey](https://arxiv.org/abs/2105.14499). Rubagotti et al. *In Robotics and Autonomous Systems*, 2021.
- [A Review on Trust in Human-Robot Interaction](https://arxiv.org/abs/2105.10045). Khavas et al. *arXiv 2105.10045*, 2021.

</details>

<details open>
<summary>Multi-Agent Collaboration (3)</summary>

- [When Autonomy Goes Rogue: Preparing for Risks of Multi-Agent Collusion in Social Systems](https://arxiv.org/abs/2507.14660). Ren et al. *arXiv 2507.14660*, 2025.
- [Distributional AGI Safety](https://arxiv.org/abs/2512.16856). Tomasev et al. *arXiv 2512.16856*, 2025.
- [Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast](https://arxiv.org/abs/2402.08567). Gu et al. *In ICML*, 2024.

</details>

</details>

---

<details open>
<summary>⚡ <b>Agentic</b> (96 papers)</summary>

<details open>
<summary>Tool Use and Skill (22)</summary>

- [DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents](https://arxiv.org/abs/2605.04808). Chen et al. *arXiv 2605.04808*, 2026.
- [Indirect Prompt Injection in the Wild: An Empirical Study of Prevalence, Techniques, and Objectives](https://arxiv.org/abs/2604.27202). Khodayari et al. *arXiv 2604.27202*, 2026.
- [Breaking MCP with Function Hijacking Attacks: Novel Threats for Function Calling and Agentic Models](https://arxiv.org/abs/2604.20994). Belkhiter et al. *arXiv 2604.20994*, 2026.
- [Structured Security Auditing and Robustness Enhancement for Untrusted Agent Skills](https://arxiv.org/abs/2604.25109). Lv et al. *arXiv 2604.25109*, 2026.
- [RouteGuard: Internal-Signal Detection of Skill Poisoning in LLM Agents](https://arxiv.org/abs/2604.22888). Xiao et al. *arXiv 2604.22888*, 2026.
- [Black-Box Skill Stealing Attack from Proprietary LLM Agents: An Empirical Study](https://arxiv.org/abs/2604.21829). Wang et al. *arXiv 2604.21829*, 2026.
- [Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems](https://arxiv.org/abs/2604.03081). Qu et al. *arXiv 2604.03081*, 2026.
- [Towards Secure Agent Skills: Architecture, Threat Taxonomy, and Security Analysis](https://arxiv.org/abs/2604.02837). Li et al. *arXiv 2604.02837*, 2026.
- [AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents](https://arxiv.org/abs/2503.18666). Wang et al. *In ICSE*, 2026.
- [BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents](https://arxiv.org/abs/2601.04566). Feng et al. *In Findings of the Association for Computational Linguistics: ACL*, 2026.
- [Prompt Injection Attack to Tool Selection in LLM Agents](https://arxiv.org/abs/2504.19793). Shi et al. *arXiv 2504.19793*, 2025.
- [SELP: Generating Safe and Efficient Task Plans for Robot Agents with Large Language Models](https://arxiv.org/abs/2409.19471). Wu et al. *arXiv preprint*, 2024.
- [Plug in the Safety Chip: Enforcing Constraints for LLM-driven Robot Agents](https://arxiv.org/abs/2309.09919). Yang et al. *Brown University Technical Report*, 2024.
- [RoboCodeX: Multimodal Code Generation for Robotic Behavior Synthesis](https://arxiv.org/abs/2402.16117). Mu et al. *In ICML*, 2024.

- [MalTool: Malicious Tool Attacks on LLM Agents](https://arxiv.org/abs/2602.12194). Hu et al. *arXiv 2602.12194*, 2026.
- [STAC: When Innocent Tools Form Dangerous Chains to Jailbreak LLM Agents](https://arxiv.org/abs/2509.25624). Li et al. *arXiv 2509.25624*, 2025.
- [RoboCodeX](https://scholar.google.com/scholar?q=RoboCodeX). Mu et al. *In ICML*, 2024.
- [Agent Harness Engineering: A Survey](https://scholar.google.com/scholar?q=Agent+Harness+Engineering%3A+A+Survey). Li et al. *OpenReview preprint*, 2026.
- [SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces](https://arxiv.org/abs/2605.12015). Jin et al. *arXiv 2605.12015*, 2026.
- [Toward Efficient Agents: Memory, Tool Learning, and Planning](https://arxiv.org/abs/2601.14192). Yang et al. *arXiv 2601.14192*, 2026.
- [OWASP](https://scholar.google.com/scholar?q=OWASP). Project. *https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/*, 2026.
- [AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills](https://arxiv.org/abs/2605.13940). Zhuang et al. *arXiv 2605.13940*, 2026.
</details>

<details open>
<summary>Memory (22)</summary>

- [SafeHarbor: Hierarchical Memory-Augmented Guardrail for LLM Agent Safety](https://arxiv.org/abs/2605.05704). Liu et al. *In ICML*, 2026.
- [How Far Are VLMs from Privacy Awareness in the Physical World? An Empirical Study](https://arxiv.org/abs/2605.05340). Wang et al. *arXiv 2605.05340*, 2026.
- [From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms](https://arxiv.org/abs/2605.06716). Luo et al. *Preprints.org*, 2026.
- [Just Ask: Curious Code Agents Reveal System Prompts in Frontier LLMs](https://arxiv.org/abs/2601.21233). Zheng et al. *In ICML*, 2026.
- [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110). Xu et al. *In NeurIPS*, 2026.
- [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564). Hu et al. *arXiv 2512.13564*, 2025.
- [MemOS: An Operating System for Memory-Augmented Generation (MAG) in Large Language Models](https://arxiv.org/abs/2505.22101). Li et al. *arXiv 2507.03724*, 2025.
- [Topology Matters: Measuring Memory Leakage in Multi-Agent LLMs](https://arxiv.org/abs/2512.04668). Liu et al. *arXiv 2512.04668*, 2025.
- [Unveiling Privacy Risks in LLM Agent Memory](https://arxiv.org/abs/2502.13172). Wang et al. *In ACL*, 2025.
- [Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2502.14321). Wu and Shu. *TechRxiv preprint*, 2025.
- ["Ghost of the past": identifying and resolving privacy leakage from LLM's memory through proactive user interaction](https://arxiv.org/abs/2410.14931). Zhang et al. *arXiv 2410.14931*, 2025.
- [A Survey on the Memory Mechanism of Large Language Model-based Agents](https://arxiv.org/abs/2404.13501). Zhang et al. *ACM Transactions on Information Systems*, 2025.
- [Embodied Agents Meet Personalization: Exploring Memory Utilization for Personalized Assistance](https://scholar.google.com/scholar?q=Embodied+Agents+Meet+Personalization%3A+Exploring+Memory+Utilization+for+Personalized+Assistance). Kwon et al. *arXiv 2505.16348*, 2025.
- [AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases](https://arxiv.org/abs/2407.12784). Chen et al. *In NeurIPS*, 2024.

- [Hidden in Memory: Sleeper Memory Poisoning in LLM Agents](https://arxiv.org/abs/2605.15338). Pulipaka et al. *arXiv 2605.15338*, 2026.
- [PRISM: Generation-Time Detection and Mitigation of Secret Leakage in Multi-Agent LLM Pipelines](https://arxiv.org/abs/2605.10614). Tapwal et al. *arXiv 2605.10614*, 2026.
- [MemOS: A Memory OS for AI System](https://arxiv.org/abs/2507.03724). Li et al. *arXiv 2507.03724*, 2025.
- [Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](https://arxiv.org/abs/2604.08224). Zhou et al. *arXiv 2604.08224*, 2026.
- [Cascading Failures in Agentic AI](https://scholar.google.com/scholar?q=Cascading+Failures+in+Agentic+AI). AI. *https://adversa.ai/blog/cascading-failures-in-agentic-ai-complete-owasp-asi08-security-guide-2026/*, 2025.
- [Memory in LLM-Based Multi-Agent Systems: Mechanisms, Challenges, and Collective Intelligence](https://scholar.google.com/scholar?q=Memory+in+LLM-Based+Multi-Agent+Systems%3A+Mechanisms%2C+Challenges%2C+and+Collective+Intelligence). Wu and Shu. *Authorea Preprints*, 2025.
- [SmartAgent: Chain-of-User-Thought for Embodied Personalized Agent in Cyber World](https://scholar.google.com/scholar?q=SmartAgent%3A+Chain-of-User-Thought+for+Embodied+Personalized+Agent+in+Cyber+World). Zhang et al. *In AAAI*, 2026.
- [Remembering More, Risking More: Longitudinal Safety Risks in Memory-Equipped LLM Agents](https://arxiv.org/abs/2605.17830). Al-Tawaha et al. *arXiv 2605.17830*, 2026.
</details>

<details open>
<summary>Self-Evolving (17)</summary>

- [A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems](https://arxiv.org/abs/2508.07407). Fang et al. *arXiv 2508.07407*, 2025.
- [Safe Continual Reinforcement Learning Methods for Nonstationary Environments. Towards a Survey of the State of the Art](https://arxiv.org/abs/2601.05152). Tomashevskiy. *arXiv 2601.05152*, 2025.
- [Self-Improving Embodied Foundation Models](https://arxiv.org/abs/2509.15155). Ghasemipour et al. 2025.
- [Your Agent May Misevolve: Emergent Risks in Self-evolving LLM Agents](https://arxiv.org/abs/2509.26354). Shao et al. *arXiv 2509.26354*, 2025.
- [C3AI: Crafting and Evaluating Constitutions for Constitutional AI](https://arxiv.org/abs/2502.15861). Kyrychenko et al. *In ACM Web Conference*, 2025.
- [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547). Zhang et al. *arXiv 2509.02547*, 2025.
- [Lifelong Learning of Large Language Model Based Agents: A Roadmap](https://arxiv.org/abs/2501.07278). Zheng et al. *arXiv 2501.07278*, 2025.
- [Red-Teaming Vision-Language-Action Models via Quality Diversity Prompt Generation for Robust Robot Policies](https://arxiv.org/abs/2603.12510). Srikanth et al. 2024.
- [Moral Anchor System: A Predictive Framework for AI Value Alignment and Drift Prevention](https://arxiv.org/abs/2510.04073). Ravindran. *arXiv 2510.04073*, 2024.
- [R2AI: Towards Resistant and Resilient AI in an Evolving World](https://arxiv.org/abs/2509.06786). Anonymous. *OpenReview Preprint*, 2024.
- [Agent-SafetyBench: Evaluating the Safety of LLM Agents](https://arxiv.org/abs/2412.14470). Zhang et al. *arXiv 2412.14470*, 2024.

- [OEP: Poisoning Self-Evolving LLM Agents via Locally Correct but Non-Transferable Experiences](https://arxiv.org/abs/2605.18930). Wang et al. *arXiv 2605.18930*, 2026.
- [Aligning AI Agents with Humans through Law as Information](https://scholar.google.com/scholar?q=Aligning+AI+Agents+with+Humans+through+Law+as+Information). Nay. *Stanford Law School Working Paper*, 2025.
- [A Systematic Survey of Self-Evolving Agents: From Model-Centric to Environment-Driven Co-Evolution](https://scholar.google.com/scholar?q=A+Systematic+Survey+of+Self-Evolving+Agents%3A+From+Model-Centric+to+Environment-Driven+Co-Evolution). Xiang et al. *TechRxiv preprint*, 2025.
- [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046). Gao et al. *arXiv 2507.21046*, 2025.
- [2025 AI Safety Index](https://scholar.google.com/scholar?q=2025+AI+Safety+Index). Institute. *https://futureoflife.org/ai-safety-index-summer-2025/*, 2025.
- [EmbodiedGovBench: A Benchmark for Governance, Recovery, and Upgrade Safety in Embodied Agent Systems](https://arxiv.org/abs/2604.11174). Qin et al. *arXiv 2604.11174*, 2026.
</details>

<details open>
<summary>Cascading Risks (35)</summary>

- [ShieldNet: Network-Level Guardrails against Emerging Supply-Chain Injections in Agentic Systems](https://arxiv.org/abs/2604.04426). Yuan et al. *arXiv 2604.04426*, 2026.
- [ARMs: Adaptive Red-Teaming Agent against Multimodal Models with Plug-and-Play Attacks](https://arxiv.org/abs/2510.02677). Chen et al. *arXiv 2510.02677*, 2025.
- [RedCodeAgent: Automatic Red-teaming Agent against Diverse Code Agents](https://arxiv.org/abs/2510.02609). Guo et al. *arXiv 2510.02609*, 2025.
- [Position: Embodied AI Requires a Privacy-Utility Trade-off](https://arxiv.org/abs/2605.05017). Fan et al. *arXiv 2605.05017*, 2026.
- [A Survey of Agentic AI and Cybersecurity: Challenges, Opportunities and Use-case Prototypes](https://arxiv.org/abs/2601.05293). Lazer et al. *arXiv 2601.05293*, 2026.
- [A Survey on Agentic Security: Applications, Threats and Defenses](https://arxiv.org/abs/2510.06445). Shahriar. *arXiv 2510.06445*, 2025.
- [SkillJect: Automating Stealthy Skill-Based Prompt Injection for Coding Agents with Trace-Driven Closed-Loop Refinement](https://arxiv.org/abs/2602.14211). Jia et al. *arXiv 2602.14211*, 2026.
- [SoK: Agentic Skills - Beyond Tool Use in LLM Agents](https://arxiv.org/abs/2602.20867). Jiang et al. *arXiv 2602.20867*, 2026.
- [Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale](https://arxiv.org/abs/2601.10338). Liu et al. *arXiv 2601.10338*, 2026.
- [Cascading Failures in Agentic AI: ASI08 Security Guide](https://scholar.google.com/scholar?q=Cascading+Failures+in+Agentic+AI%3A+ASI08+Security+Guide). OWASP. 2026.
- [A white-box prompt injection attack on embodied AI agents driven by large language models](https://scholar.google.com/scholar?q=White-Box+Prompt+Injection+Attack+on+Embodied+AI+Agents). Geng et al. *Science*, 2026.
- [Securing (vision-based) autonomous systems: taxonomy, challenges, and defense mechanisms against adversarial threats](https://scholar.google.com/scholar?q=Securing+Vision-Based+Autonomous+Systems%3A+A+Comprehensive+Taxonomy). Lopez Pellicer et al. *Artificial Intelligence (AIJ)*, 2025.
- [From Failure Modes to Reliability Awareness in Generative and Agentic AI System](https://arxiv.org/abs/2511.05511). Lin and Zhang. 2025.
- [The Adolescence of Technology](https://scholar.google.com/scholar?q=The+Adolescence+of+Technology). Amodei. 2025.
- [International AI Safety Report 2025: Second Key Update: Technical Safeguards and Risk Management](https://arxiv.org/abs/2511.19863). Bengio et al. *arXiv 2511.19863*, 2025.
- [Revisiting Adversarial Perception Attacks and Defense Methods on Autonomous Driving Systems](https://arxiv.org/abs/2505.11532). Chen et al. *arXiv 2505.11532*, 2025.
- [Attacking Autonomous Driving Agents with Adversarial Machine Learning: A Holistic Evaluation with the CARLA Leaderboard](https://arxiv.org/abs/2511.14876). Wong et al. *arXiv 2511.14876*, 2025.
- [SoK: How Sensor Attacks Disrupt Autonomous Vehicles: An End-to-end Analysis, Challenges, and Missed Threats](https://arxiv.org/abs/2509.11120). Zhang et al. *arXiv 2509.11120*, 2025.
- [Towards Robust and Secure Embodied AI: A Survey on Vulnerabilities and Attacks](https://dl.acm.org/doi/abs/10.1145/3806048). Xing et al. *ACM Computing Surveys*, 2026.
- [SoK: Cybersecurity Assessment of Humanoid Ecosystem](https://arxiv.org/abs/2508.17481). Surve et al. *arXiv 2508.17481*, 2025.
- [Automated Discovery of Semantic Attacks in Multi-Robot Navigation Systems](https://scholar.google.com/scholar?q=Automated+Discovery+of+Semantic+Attacks+in+Multi-Robot+Navigation). Yeke et al. *In USENIX Security*, 2025.
- [Secure Robotics: Navigating Challenges at the Nexus of Safety, Trust, and Cybersecurity in Cyber-Physical Systems](https://scholar.google.com/scholar?q=Secure+Robotics%3A+Nexus+of+Safety%2C+Trust%2C+and+Cybersecurity). Haskard et al. *ACM Computing Surveys (CSUR)*, 2024.
- [Towards Physically Realizable Adversarial Attacks in Embodied Vision Navigation](https://arxiv.org/abs/2409.10071). Chen et al. *In IROS*, 2024.
- [Toward Robust 3D Perception for Autonomous Vehicles: A Review of Adversarial Attacks and Countermeasures](https://scholar.google.com/scholar?q=Toward+Robust+3D+Perception+for+Autonomous+Vehicles). Mahima et al. *IEEE Transactions on Intelligent Transportation Systems (T-ITS)*, 2024.
- [SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178). Yin et al. *arXiv 2412.13178*, 2024.
- [Dynamic Adversarial Attacks on Autonomous Driving Systems](https://arxiv.org/abs/2312.06701). Chahe et al. *In RSS*, 2023.
- [Security Considerations in AI-Robotics: A Survey of Current Methods, Challenges, and Opportunities](https://arxiv.org/abs/2310.08565). Neupane et al. *IEEE Access*, 2023.
- [Adversarial Driving: Attacking End-to-End Autonomous Driving](https://arxiv.org/abs/2103.09151). Wu et al. *In IEEE Intelligent Vehicle Symposium*, 2021.
- [Robotics cyber security: vulnerabilities, attacks, countermeasures, and recommendations](https://scholar.google.com/scholar?q=Robotics+Cyber+Security%3A+Vulnerabilities%2C+Attacks%2C+Countermeasures%2C+and+Recommendations). Yaacoub et al. *International Journal of Information Security*, 2021.
- [Spatiotemporal Attacks for Embodied Agents](https://scholar.google.com/scholar?q=Spatiotemporal+Attacks+for+Embodied+Agents). Liu et al. *In ECCV*, 2020.

- [Auditing Agent Harness Safety](https://arxiv.org/abs/2605.14271). Liu et al. *arXiv 2605.14271*, 2026.
- [Safety at Scale: A Comprehensive Survey of Large Model and Agent Safety](https://scholar.google.com/scholar?q=Safety+at+Scale%3A+A+Comprehensive+Survey+of+Large+Model+and+Agent+Safety). Ma et al. *Foundations and Trends*, 2025.
- [Internal Safety Collapse in Frontier Large Language Models](https://arxiv.org/abs/2603.23509). Wu et al. *arXiv 2603.23509*, 2026.
- [The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey](https://scholar.google.com/scholar?q=The+Attack+and+Defense+Landscape+of+Agentic+AI%3A+A+Comprehensive+Survey). Kim et al. *In USENIX Security*, 2026.
- [The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents](https://arxiv.org/abs/2605.20544). Yeke et al. *arXiv 2605.20544*, 2026.
</details>

</details>

## Other Related Works

33 cited works beyond the five-layer attack and defense taxonomy, grouped by type.

<details open>
<summary><b>Surveys & Reviews</b> (13)</summary>

- [A Survey on Adversarial Robustness of LiDAR-based Machine Learning Perception in Autonomous Vehicles](https://arxiv.org/abs/2411.13778). Kim and Kaur. *arXiv 2411.13778*, 2024.
- [SoK: Rethinking Sensor Spoofing Attacks against Robotic Vehicles from a Systematic View](https://scholar.google.com/scholar?q=SoK%3A+Rethinking+Sensor+Spoofing+Attacks+against+Robotic+Vehicles+from+a+Systematic+View). Xu et al. *In IEEE EuroS&P*, 2022.
- [AI Agents under Threat: A Survey of Key Security Challenges and Future Pathways](https://scholar.google.com/scholar?q=AI+Agents+under+Threat%3A+A+Survey+of+Key+Security+Challenges+and+Future+Pathways). Deng et al. *ACM Computing Surveys*, 2025.
- [Navigating the Risks: A Survey of Security, Privacy, and Ethics Threats in LLM-Based Agents](https://arxiv.org/abs/2411.09523). Gan et al. *arXiv 2411.09523*, 2024.
- [Trust in LLM-Controlled Robotics: A Survey of Security Threats, Defenses and Challenges](https://arxiv.org/abs/2601.02377). Huang et al. *arXiv 2601.02377*, 2026.
- [Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms](https://arxiv.org/abs/2604.23775). Li et al. *arXiv 2604.23775*, 2026.
- [Towards Safe and Trustworthy Embodied AI: Foundations, Status, and Prospects](https://scholar.google.com/scholar?q=Towards+Safe+and+Trustworthy+Embodied+AI%3A+Foundations%2C+Status%2C+and+Prospects). Tan et al. *OpenReview preprint*, 2025.
- [Adversarial Robustness in Embodied AI: A Closed-Loop Perspective on Attacks and Defenses](https://scholar.google.com/scholar?q=Adversarial+Robustness+in+Embodied+AI%3A+A+Closed-Loop+Perspective+on+Attacks+and+Defenses). Wang et al. *TechRxiv preprint*, 2026.
- [Navigating Embodied Intelligence: Enabling Technologies, Security and Privacy, and Emerging Trends](https://scholar.google.com/scholar?q=Navigating+Embodied+Intelligence%3A+Enabling+Technologies%2C+Security+and+Privacy%2C+and+Emerging+Trends). Wang et al. *IEEE Internet of Things Journal (IoT-J)*, 2026.
- [A Comprehensive Survey in LLM (-Agent) Full Stack Safety: Data, Training and Deployment](https://arxiv.org/abs/2504.15585). Wang et al. *arXiv 2504.15585*, 2025.
- [Safety of Embodied Navigation: A Survey](https://arxiv.org/abs/2508.05855). Wang et al. *arXiv 2508.05855*, 2025.
- [A Survey of Safety on Large Vision-Language Models: Attacks, Defenses and Evaluations](https://arxiv.org/abs/2502.14881). Ye et al. *arXiv 2502.14881*, 2025.
- [A Survey on Predictive Safety in Embodied AI](https://scholar.google.com/scholar?q=A+Survey+on+Predictive+Safety+in+Embodied+AI). da Costa et al. *SSRN*, 2026.

</details>

<details open>
<summary><b>Benchmarks & Datasets</b> (2)</summary>

- [Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](https://scholar.google.com/scholar?q=Vision-and-Language+Navigation%3A+Interpreting+Visually-Grounded+Navigation+Instructions+in+Real+Environments). Anderson et al. *In CVPR*, 2018.
- [VizWiz Grand Challenge: Answering Visual Questions from Blind People](https://scholar.google.com/scholar?q=VizWiz+Grand+Challenge%3A+Answering+Visual+Questions+from+Blind+People). Gurari et al. *In CVPR*, 2018.

</details>

<details open>
<summary><b>Foundation, World, World-Action & VLA Models</b> (10)</summary>

- [OpenVLA: An Open-Source Vision-Language-Action Model](https://scholar.google.com/scholar?q=OpenVLA%3A+An+Open-Source+Vision-Language-Action+Model). Kim and Pertsch. *In CoRL*, 2025.
- [Dolphins: Multimodal Language Model for Driving](https://scholar.google.com/scholar?q=Dolphins%3A+Multimodal+Language+Model+for+Driving). Ma et al. *In ECCV*, 2024.
- [FAST: Efficient Action Tokenization for Vision-Language-Action Models](https://arxiv.org/abs/2501.09747). Pertsch et al. *arXiv 2501.09747*, 2025.
- [SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model](https://scholar.google.com/scholar?q=SpatialVLA%3A+Exploring+Spatial+Representations+for+Visual-Language-Action+Model). Qu et al. *In RSS*, 2025.
- [Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020). Team et al. *arXiv 2503.20020*, 2025.
- [DriveVLM: The Convergence of Autonomous Driving and Large Vision-Language Models](https://scholar.google.com/scholar?q=DriveVLM%3A+The+Convergence+of+Autonomous+Driving+and+Large+Vision-Language+Models). Tian et al. *In CoRL*, 2024.
- [World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090). Wang et al. *arXiv 2605.12090*, 2026.
- [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://scholar.google.com/scholar?q=DiffusionVLA%3A+Scaling+Robot+Foundation+Models+via+Unified+Diffusion+and+Autoregression). Wen et al. *In ICML*, 2025.
- [TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation](https://scholar.google.com/scholar?q=TinyVLA%3A+Towards+Fast%2C+Data-Efficient+Vision-Language-Action+Models+for+Robotic+Manipulation). Wen et al. *IEEE Robotics and Automation Letters (RA-L)*, 2025.
- [OpenDriveVLA: Towards End-to-End Autonomous Driving with Large Vision Language Action Model](https://arxiv.org/abs/2503.23463). Zhou et al. *arXiv 2503.23463*, 2025.

</details>

<details open>
<summary><b>Other & Foundational</b> (8)</summary>

- [Your Robot Therapist Will See You Now: Ethical Implications of Embodied Artificial Intelligence in Psychiatry, Psychology, and Psychotherapy](https://scholar.google.com/scholar?q=Your+Robot+Therapist+Will+See+You+Now%3A+Ethical+Implications+of+Embodied+Artificial+Intelligence+in+Psychiatry%2C+Psychology%2C+and+Psychotherapy). Fiske et al. *Journal of Medical Internet Research (JMIR)*, 2019.
- [Service Robots in the Healthcare Sector](https://scholar.google.com/scholar?q=Service+Robots+in+the+Healthcare+Sector). Holland et al. *In Robotics*, 2021.
- [Healthcare Robots to Combat COVID-19](https://scholar.google.com/scholar?q=Healthcare+Robots+to+Combat+COVID-19). Kaiser et al. *COVID-19*, 2020.
- [A Safety Report on GPT-5.2, Gemini 3 Pro, Qwen3-VL, Grok 4.1 Fast, Nano Banana Pro, and Seedream 4.5](https://arxiv.org/abs/2601.10527). Ma et al. *arXiv 2601.10527*, 2026.
- [What Breaks Embodied AI Security: LLM Vulnerabilities, CPS Flaws, or Something Else?](https://arxiv.org/abs/2602.17345). Ma et al. *arXiv 2602.17345*, 2026.
- [Emerging Risks from Embodied AI Require Urgent Policy Action](https://arxiv.org/abs/2509.00117). Perlo et al. *In NeurIPS*, 2025.
- [Beyond Alignment: Why Robotic Foundation Models Need Context-Aware Safety](https://scholar.google.com/scholar?q=Beyond+Alignment%3A+Why+Robotic+Foundation+Models+Need+Context-Aware+Safety). Robey et al. *Science Robotics*, 2026.
- [Computing Machinery and Intelligence](https://scholar.google.com/scholar?q=Computing+Machinery+and+Intelligence). Turing. *Parsing the Turing test*, 1950.

</details>

## Open Challenges

- **Multimodal Perception Fusion Fragility**: Cross-modal attacks exploiting inconsistencies between visual, auditory, and spatial perception remain underexplored.
- **Planning Under Jailbreak**: LLM-based planners are vulnerable to instruction manipulation that bypasses safety constraints in physical execution.
- **Human-Agent Interaction Trust**: Open-ended scenarios where agents must negotiate trust with humans lack standardized safety evaluation.
- **Agentic Cascading Failures**: Self-evolving agents with persistent memory and tool use can propagate inner-layer compromises to system-wide failures.
- **Benchmark Standardization**: Lack of unified safety benchmarks across the full embodied AI pipeline hinders reproducible evaluation.

## Contributing

Contributions are welcome and encouraged! If you find relevant papers missing from our list or spot any errors:

- **Add a paper**: Open a [pull request](https://github.com/x-zheng16/Awesome-Embodied-AI-Safety/pulls) with the paper title, authors, venue, year, and a Google Scholar link.
- **Report an issue**: Open an [issue](https://github.com/x-zheng16/Awesome-Embodied-AI-Safety/issues) describing what needs to be corrected or added.
- **Suggest a category**: If a paper does not fit existing subcategories, propose a new one in your PR description.

Please follow the existing format: `[Paper Title](Google Scholar link). Authors. *Venue*, Year.`

## Citation

If you find this survey useful, please cite our paper:

```bibtex
@article{li2026safety,
  title={Safety in Embodied AI: A Survey of Risks, Attacks, and Defenses},
  author={Li, Xiao and Zheng, Xiang and Gao, Yifeng and Xia, Xinyu and Wang, Yixu and Wang, Xin and Sun, Ye and Zhao, Yunhan and Wen, Ming and Li, Jiayu and Chen, Zixing and Gong, Xun and Liu, Yi and Li, Yige and Wu, Yutao and Wang, Cong and Sun, Jun and Cao, Yixin and Chen, Zhineng and Chen, Jingjing and Gui, Tao and Zhang, Qi and Wu, Zuxuan and Qiu, Xipeng and Huang, Xuanjing and Zhang, Tiehua and Wei, Zhipeng and Wang, Kun and Li, Xinfeng and Huang, Hanxun and Erfani, Sarah and Bailey, James and Wang, Jianping and Xiao, Chaowei and He, Ran and Li, Bo and Ma, Xingjun and Jiang, Yu-Gang},
  journal={arXiv preprint arXiv:2605.02900},
  year={2026},
  url={https://arxiv.org/abs/2605.02900}
}
```

## Related Projects

From the same team:

| Project | Description | Stars |
| --- | --- | --- |
| [ISC-Bench](https://github.com/wuyoscar/ISC-Bench) | Internal Safety Collapse in Frontier LLMs | ![](https://img.shields.io/github/stars/wuyoscar/ISC-Bench?style=social) |
| [Awesome-Large-Model-Safety](https://github.com/xingjunm/Awesome-Large-Model-Safety) | Safety at Scale: A Comprehensive Survey of Large Model and Agent Safety | ![](https://img.shields.io/github/stars/xingjunm/Awesome-Large-Model-Safety?style=social) |
| [BackdoorLLM](https://github.com/bboylyg/BackdoorLLM) | A Comprehensive Benchmark for Backdoor Attacks on LLMs (NeurIPS 2025) | ![](https://img.shields.io/github/stars/bboylyg/BackdoorLLM?style=social) |
| [BackdoorAgent](https://github.com/Yunhao-Feng/BackdoorAgent) | Backdoor Attacks on LLM-based Agent Workflows (ACL Findings 2026) | ![](https://img.shields.io/github/stars/Yunhao-Feng/BackdoorAgent?style=social) |
| [JustAsk](https://github.com/x-zheng16/JustAsk) | Curious Code Agents Reveal System Prompts in Frontier LLMs (ICML 2026) | ![](https://img.shields.io/github/stars/x-zheng16/JustAsk?style=social) |
| [Unlearnable-Examples](https://github.com/HanxunH/Unlearnable-Examples) | Making Personal Data Unexploitable (ICLR 2021) | ![](https://img.shields.io/github/stars/HanxunH/Unlearnable-Examples?style=social) |
| [XTransferBench](https://github.com/HanxunH/XTransferBench) | Super Transferable Adversarial Attacks on CLIP (ICML 2025) | ![](https://img.shields.io/github/stars/HanxunH/XTransferBench?style=social) |

## Recommended Reading & Viewing

Curated external resources on frontier AI safety beyond the surveyed papers:

- [Frontier AI Safety Policies](https://metr.org/fsp) -- METR's resource on frontier AI developers' safety policies and commitments.

## Star History

<a href="https://star-history.com/#x-zheng16/Awesome-Embodied-AI-Safety&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=x-zheng16/Awesome-Embodied-AI-Safety&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=x-zheng16/Awesome-Embodied-AI-Safety&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=x-zheng16/Awesome-Embodied-AI-Safety&type=Date" width="800" />
 </picture>
</a>
