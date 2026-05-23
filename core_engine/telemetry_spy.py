import time
import random
import json
from typing import Dict, Any

class HardwareTelemetrySpy:
    """
    Hardware Telemetry Spy Component (AIOps-Power Framework)
    
    Architecture Layer: Input & Feature Extraction Layer
    Design Philosophy: 'Hardware Never Lies'. Even if the software layer (OS/Container) 
    reports 100% GPU utilization, this engine cross-references microarchitectural performance 
    counters (Tensor Cores, HBM Bandwidth) to detect fraudulent 'Keep-Alive' loops or zombie agents.
    """
    
    def __init__(self, node_id: str):
        self.node_id = node_id
        # 基準線閾值：真正有效率的 AI 推理/訓練，Tensor Core 與 HBM 必須同步活絡
        self.TENSOR_CORE_IDLE_THRESHOLD = 15.0  # 百分比 (%)
        self.HBM_BANDWIDTH_MIN_THRESHOLD = 100.0 # GB/s

    def fetch_live_telemetry(self, mock_scenario: str = "legit") -> Dict[str, Any]:
        """
        Simulates the ingestion of cross-layer telemetry registers via PCIe, CXL, or Redfish APIs.
        """
        timestamp = time.time()
        
        if mock_scenario == "legit":
            # 情境一：真正的高負載運算（如大模型矩陣乘法）
            return {
                "node_id": self.node_id,
                "timestamp": timestamp,
                "reported_gpu_util": 98.5,
                "tensor_core_activity_pct": 84.2,
                "hbm_bandwidth_gbps": 612.4,
                "actual_power_draw_watts": 345.0
            }
        elif mock_scenario == "dummy_busy":
            # 情境二：AI Agent 寫無窮迴圈「假裝很忙」試圖霸佔算力資源
            return {
                "node_id": self.node_id,
                "timestamp": timestamp,
                "reported_gpu_util": 100.0, # 軟體層顯示滿載
                "tensor_core_activity_pct": 4.1,   # 物理特徵：Tensor Core 根本沒在動！
                "hbm_bandwidth_gbps": 12.8,   # 物理特徵：沒有大量記憶體吞吐
                "actual_power_draw_watts": 280.0  # 物理特徵：白白燒電，產生巨大靜態功耗熵
            }
        else:
            # 情境三：真正的閒置狀態
            return {
                "node_id": self.node_id,
                "timestamp": timestamp,
                "reported_gpu_util": 0.0,
                "tensor_core_activity_pct": 0.0,
                "hbm_bandwidth_gbps": 1.5,
                "actual_power_draw_watts": 95.0
            }

    def analyze_workload_authenticity(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """
        AI-Native Reasoning Engine: Analyzes the hardware footprint to evaluate 
        if the current power draw is justified by valid mathematical computations.
        """
        gpu_util = metrics["reported_gpu_util"]
        tensor_act = metrics["tensor_core_activity_pct"]
        hbm_bw = metrics["hbm_bandwidth_gbps"]
        
        is_fraudulent = False
        verdict = "LEGIT_WORKLOAD"
        action_recommendation = "MAINTAIN_POWER_PROFILE_P0"

        # 核心算法：當軟體報告利用率極高，但底層矩陣運算與記憶體吞吐低於閾值，判定為作弊
        if gpu_util > 70.0:
            if tensor_act < self.TENSOR_CORE_IDLE_THRESHOLD and hbm_bw < self.HBM_BANDWIDTH_MIN_THRESHOLD:
                is_fraudulent = True
                verdict = "DUMMY_BUSY_ZOMBIE_AGENT"
                action_recommendation = "TRIGGER_LIVE_MIGRATION_AND_FORCE_DEEP_C_STATE"

        return {
            "verdict": verdict,
            "is_fraudulent": is_fraudulent,
            "action_recommendation": action_recommendation,
            "power_wastage_risk": "HIGH" if is_fraudulent else "LOW"
        }

# 測試腳本的執行
if __name__ == "__main__":
    spy = HardwareTelemetrySpy(node_id="AI_FACTORY_CLUSTER_01_NODE_B4")
    
    print("==================================================================")
    print("🚀 RUNNING AI-NATIVE POWER OBSERVABILITY SYSTEM TEST")
    print("==================================================================\n")

    # 模擬測試兩種極端情境
    for scenario in ["legit", "dummy_busy"]:
        print(f"📡 [Scenario: {scenario.upper()}] Fetching Hardware Telemetry Registers...")
        raw_data = spy.fetch_live_telemetry(mock_scenario=scenario)
        analysis = spy.analyze_workload_authenticity(raw_data)
        
        print(f"   📋 Reported GPU Util : {raw_data['reported_gpu_util']}%")
        print(f"   🔬 Physical Tensor Core: {raw_data['tensor_core_activity_pct']}%")
        print(f"   💾 HBM R/W Bandwidth  : {raw_data['hbm_bandwidth_gbps']} GB/s")
        print(f"   ⚡ Actual Power Draw  : {raw_data['actual_power_draw_watts']} W")
        print(f"   ⚠️  AI Engine Verdict : **{analysis['verdict']}**")
        print(f"   🛠️  Enforcement Act   : {analysis['action_recommendation']}")
        print("-" * 66)