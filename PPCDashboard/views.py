from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import BlastFurnace_CPP_PCI_Weights  # ✅ Added import

# Home Page View
def home(request):
    return render(request, 'Pages/home.html')

# RMHS Page View
def rmhs(request):
    return render(request, 'Pages/rmhs.html')

# Blast Furnace Page View
def blastfurnace(request):
    return render(request, 'Pages/blastfurnace.html')

# ✅ View to Handle PCI Weights Data Submission
@csrf_exempt
def cpp_pci_weights(request):
    if request.method == "POST":
        try:
            # ✅ Parse JSON data safely
            data = json.loads(request.body.decode("utf-8"))

            # ✅ Validate Data
            required_fields = [
                "feed_tank_1", "feed_tank_2", "feed_tank_3", "fcs_weight", 
                "rcs_1_wt", "rcs_2_wt", "pci_n2_supply_pr", "inst_supply_pr",
                "lances_on_coal", "hmt_production", "low_pressure_n2"
            ]
            
            # ✅ Ensure all required fields are present
            for field in required_fields:
                if field not in data:
                    return JsonResponse({"error": f"Missing field: {field}"}, status=400)

            # ✅ Save Data to Database
            new_entry = BlastFurnace_CPP_PCI_Weights.objects.create(
                feed_tank_1=float(data.get("feed_tank_1", 0)),
                feed_tank_2=float(data.get("feed_tank_2", 0)),
                feed_tank_3=float(data.get("feed_tank_3", 0)),
                fcs_weight=float(data.get("fcs_weight", 0)),
                rcs_1_wt=float(data.get("rcs_1_wt", 0)),
                rcs_2_wt=float(data.get("rcs_2_wt", 0)),
                pci_n2_supply_pr=float(data.get("pci_n2_supply_pr", 0)),
                inst_supply_pr=float(data.get("inst_supply_pr", 0)),
                lances_on_coal=int(data.get("lances_on_coal", 0)),
                hmt_production=float(data.get("hmt_production", 0)),
                low_pressure_n2=float(data.get("low_pressure_n2", 0))
            )

            return JsonResponse({"message": "Data saved successfully", "id": new_entry.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
