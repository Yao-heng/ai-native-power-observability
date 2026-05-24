# Technical Whitepaper: Mitigating Dynamic Power Wastage in Speculative Decoding Architectures

**Author:** Li Yao-Heng(李曜恆) 
**Classification:** Deep Infrastructure Engineering  

---

## 1. The Power-Efficiency Paradox of Speculative Decoding

Speculative Decoding has emerged as the standard acceleration paradigm for Large Language Model (LLM) inference in hyperscale deployments. The architecture pairs a computationally lightweight Draft Model (e.g., a 7B parameter model) with a high-capacity Target Model (e.g., a 70B or larger parameter model). 

The Draft Model speculates $K$ future tokens speculatively in parallel. The Target Model then evaluates these $K$ tokens concurrently within a single evaluation cycle, drastically reducing memory-bandwidth limitations.

```text
[Draft Model] ---- Speculates K Tokens ----> [Tensor Core Verification via Target Model]
                                                    |
                                    +---------------+---------------+
                                    |                               |
                       [Token Confirmed: SLA Lift]     [Token Rejected: Discarded Path]
                                                            🚨 POWER CONSUMED = WASTE