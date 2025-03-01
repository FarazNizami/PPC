from django.db import models

# ✅ Main Blast Furnace Data Model
class BlastFurnaceData(models.Model):
    cold_blast_pressure = models.FloatField(null=True, blank=True)
    hot_blast_pressure = models.FloatField(null=True, blank=True)
    cold_blast_flow = models.FloatField(null=True, blank=True)
    hot_blast_flow = models.FloatField(null=True, blank=True)
    hot_blast_temperature = models.FloatField(null=True, blank=True)

    raft = models.FloatField(null=True, blank=True)
    new_calc = models.FloatField(null=True, blank=True)
    top_pressure = models.FloatField(null=True, blank=True)

    discharge_level = models.FloatField(null=True, blank=True)
    burden_level = models.FloatField(null=True, blank=True)

    coal_injection_rate = models.FloatField(null=True, blank=True)
    oxygen_injection = models.FloatField(null=True, blank=True)

    charge_A = models.FloatField(null=True, blank=True)
    charge_B = models.FloatField(null=True, blank=True)
    charge_C = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Blast Furnace Data {self.id}"

# ✅ Temperature Data Model
class BlastFurnace_TemperatureData(models.Model):
    tuyere_cooling_1 = models.FloatField(null=True, blank=True)
    tuyere_cooling_2 = models.FloatField(null=True, blank=True)

    stack_cooling_flow = models.FloatField(null=True, blank=True)
    stack_cooling_pressure = models.FloatField(null=True, blank=True)

    hearth_bottom_flow = models.FloatField(null=True, blank=True)
    hearth_bottom_pressure = models.FloatField(null=True, blank=True)

    secondary_cooling_flow = models.FloatField(null=True, blank=True)
    secondary_cooling_pressure = models.FloatField(null=True, blank=True)

    blt_cooling_flow = models.FloatField(null=True, blank=True)
    blt_cooling_pressure = models.FloatField(null=True, blank=True)

    heat_load_stack = models.FloatField(null=True, blank=True)
    heat_load_tuyere = models.FloatField(null=True, blank=True)
    heat_load_hearth = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Temperature Data {self.id}"

# ✅ Blast Flow Model
class BlastFurnace_BlastFlow(models.Model):
    hot_metal_temp_th1 = models.FloatField(null=True, blank=True)
    hot_metal_temp_th2 = models.FloatField(null=True, blank=True)
    hot_metal_temp_th3 = models.FloatField(null=True, blank=True)
    hot_metal_temp_th4 = models.FloatField(null=True, blank=True)

    uptake_temp_a = models.FloatField(null=True, blank=True)
    uptake_temp_b = models.FloatField(null=True, blank=True)
    uptake_temp_c = models.FloatField(null=True, blank=True)
    uptake_temp_d = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Blast Flow Data {self.id}"

# ✅ CPP PCI Weights Model (Linked to View)
class BlastFurnace_CPP_PCI_Weights(models.Model):
    feed_tank_1 = models.FloatField(null=True, blank=True)
    feed_tank_2 = models.FloatField(null=True, blank=True)
    feed_tank_3 = models.FloatField(null=True, blank=True)
    fcs_weight = models.FloatField(null=True, blank=True)
    rcs_1_wt = models.FloatField(null=True, blank=True)
    rcs_2_wt = models.FloatField(null=True, blank=True)
    pci_n2_supply_pr = models.FloatField(null=True, blank=True)
    inst_supply_pr = models.FloatField(null=True, blank=True)
    lances_on_coal = models.IntegerField(null=True, blank=True)
    hmt_production = models.FloatField(null=True, blank=True)
    low_pressure_n2 = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"PCI Weights Data {self.id}"
