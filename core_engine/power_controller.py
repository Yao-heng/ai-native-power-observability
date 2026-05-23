import time
import random
from typing import Dict, Any

class InfrastructurePowerController:
    """
    Infrastructure Power Controller Component (AIOps-Power Framework)
    
    Architecture Layer: Enforcement & Actuation Layer
    Design Philosophy: Microsecond-level hardware state orchestration. 
    This engine receives verdicts from the Telemetry Spy and executes live migration 
    and hardware registry throttling to eliminate infrastructure power wastage.
    """
    
    def __init__(self):
        # 模擬實體硬體的功耗狀態暫存器 (Power Registers)
        self.HARDWARE_P_STATES = {
            "P0": "MAX_PERFORMANCE_VOLTAGE", # 滿載運算
            "P1": "BALANCED_COMPUTE",       # 輕度運算
            "P8": "LOW_POWER_IDLE",         # 傳統待機（依舊耗電）
            "D3Cold": "DEEP_SILICON_SLEEP"   # 極限省電（軌道關閉）
        }

    def execute_live_migration(self, node_id: str, app_context_id: str) -> bool:
        """
        Simulates virtualization-level Live Migration (vGPU / MIG Context Shifting).
        Moves the AI Agent context to a low-power shared hosting cluster seamlessly.
        """
        print(f"🔄 [Action: Live Migration] Initiating hot-migration for App Context [{app_context_id}] from Node [{node_id}]...")
        # 模擬網路與記憶體狀態拷貝時序 (Microsecond simulation)
        time.sleep(0.1) 
        print(f"✅ [Action: Live Migration] Context successfully migrated to LOW_POWER_SHARED_POOL. Zero downtime achieved.")
        return True

    def throttle_hardware_power_rail(self, node_id: str, target_state: str) -> str:
        """
        Simulates direct register manipulation via BMC Redfish/IPMI or Hardware Drivers.
        """
        if target_state not in self.HARDWARE_P_STATES:
            raise ValueError(f"Invalid hardware power state: {target_state}")
        
        print(f"⚡ [Action: Firmware Dispatch] Writing to Hardware Power Registers on Node [{node_id}]...")
        print(f"🔌 [Action: Firmware Dispatch] Shifting Rail State: P8 ➔ **{target_state}** ({self.HARDWARE_P_STATES[target_state]})")
        
        # 模擬實體功耗下降的物理反饋
        return target_state

    def enforce_power_policy(self, telemetry_data: Dict[str, Any], evaluation_result: Dict[str, Any]):
        """
        Orchestrates the entire enforcement pipeline based on AI-Native telemetry analysis.
        """
        node_id = telemetry_data["node_id"]
        verdict = evaluation_result["verdict"]
        recommendation = evaluation_result["action_recommendation"]
        
        print(f"\n[🚨 Enforcement Core] Processing Alert for Node: {node_id}")
        print(f"[🚨 Enforcement Core] Verdict: {verdict} | Recommended Action: {recommendation}")

        if recommendation == "TRIGGER_LIVE_MIGRATION_AND_FORCE_DEEP_C_STATE":
            # 實施閉環控制：先移轉任務，再關閉硬體電力軌
            app_id = f"MOCK_AGENT_{random.randint(1000, 9999)}"
            migration_success = self.execute_live_migration(node_id, app_id)
            
            if migration_success:
                # 任務移走了，強制硬體進入極限省電狀態 D3Cold
                self.throttle_hardware_power_rail(node_id, "D3Cold")
                saved_watts = telemetry_data["actual_power_draw_watts"] - 15.0 # 假設降到基礎功耗 15W
                print(f"📉 [ROI Insight] Dynamically reclaimed ~{saved_watts:.1f}W from this zombie cluster segment!")
        
        elif recommendation == "MAINTAIN_POWER_PROFILE_P0":
            print(f"🟢 [Enforcement Core] Node is performing valid mathematical computation. Maintaining P0 high-voltage rail.")
            
        print("==================================================================\n")

# 模擬軟硬體串接測試
if __name__ == "__main__":
    # 1. 引入我們前一步做好的 Telemetry Spy 模組
    from telemetry_spy import HardwareTelemetrySpy
    
    spy = HardwareTelemetrySpy(node_id="AI_FACTORY_CLUSTER_01_NODE_B4")
    controller = InfrastructurePowerController()

    print("==================================================================")
    print("🚀 RUNNING AI-NATIVE CLOSED-LOOP POWER CONTROLLER TEST")
    print("==================================================================")

    # 模擬測試：當抓到作弊（dummy_busy）時，控制層如何即時反應
    scenarios = ["legit", "dummy_busy"]
    for scenario in scenarios:
        # Step 1: 捕獲硬體遙測數據
        raw_telemetry = spy.fetch_live_telemetry(mock_scenario=scenario)
        # Step 2: AI 推理引擎判定結果
        ai_verdict = spy.analyze_workload_authenticity(raw_telemetry)
        # Step 3: 控制層強行介入執行
        controller.enforce_power_policy(raw_telemetry, ai_verdict)