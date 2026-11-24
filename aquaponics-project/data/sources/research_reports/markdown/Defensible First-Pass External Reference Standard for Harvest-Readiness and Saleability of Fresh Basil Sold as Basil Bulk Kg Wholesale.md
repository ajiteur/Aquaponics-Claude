# Defensible First-Pass External Reference Standard for Harvest-Readiness and Saleability of Fresh Basil Sold as Basil Bulk Kg Wholesale

## Executive summary

For a first-pass repo standard, the strongest defensible baseline is **not** a single basil-specific wholesale grade with tight numeric thresholds. Instead, it is a layered standard built from: **current EU general marketing-standard minimums for fresh produce**, **basil-specific postharvest guidance from UC Davis and Rutgers**, **a formal EU basil proxy in the Basilico Genovese PDO specification**, and **fresh-culinary-herb food-safety guidance from FDA**. In the current EU framework, the fruit-and-vegetable marketing-standard regime is governed by Delegated Regulation (EU) 2023/2429 and Implementing Regulation (EU) 2023/2430, which replaced the older 543/2011 framework from 1 January 2025. citeturn25search1turn25search3turn25search11

The strongest **harvest-readiness** conclusion is that fresh basil intended for bulk wholesale should be treated as **young vegetative, non-flowering material**, harvested as soft leafy stems or leaves, with harvest timed before flowering or with flower heads absent. The most defensible basil-specific proxy is the official Basilico Genovese PDO text, which requires basil for fresh sale or processing to have no more than four pairs of true leaves or four nodes and to be **without flower heads**. Rutgers fresh-market guidance independently aligns with this: flowers should be pinched off because they reduce flavour quality, and basil can become bitter during and after flowering. Operational extension indicators such as “about 10 inches tall” or “6–8 leaves / 6–8 inches” are useful grower heuristics, but they are too context-dependent to promote as universal canon. citeturn22view0turn14view0turn19view0turn7view6turn30view2turn30view3

The strongest **saleability** conclusion is that bulk wholesale basil must clear both a **general marketability screen** and a **basil-specific fragility screen**. The general screen is the EU minimum-quality baseline: intact, sound, clean, practically free from pests and pest damage, free of abnormal external moisture, free of foreign smell/taste, and able to withstand transport and arrive in satisfactory condition. The basil-specific fragility screen is dominated by freshness, turgidity, aroma retention, avoidance of mechanical injury, and avoidance of chilling injury. UC Davis identifies freshness, uniformity, colour, lack of yellowing, decay, insect damage, and wilting as core quality characteristics, and states that characteristic aroma is essential. citeturn26search1turn21view2turn27view0turn14view0

The strongest **rejection** triggers are: rotting or deterioration; moderate-to-severe chilling injury; visible decay or soft rot; visible pest presence or pest damage; visible foreign matter; serious wilting or loss of turgidity; yellowing/blackening beyond slight transit loss; off-smell/off-taste; and food-safety disqualification such as floodwater contact. UC Davis also warns that **visual shelf-life is longer than useful culinary shelf-life** for herbs, so visually acceptable basil can still be functionally weak if aroma has collapsed. That matters for bulk wholesale because basil is traded as a culinary herb, not merely as green biomass. citeturn21view2turn31view0turn31view1turn31view2turn31view4turn32view3

For repo design, the core implication is straightforward: **do not let runtime outputs pretend to “observe” saleability when the system is only modelling it**. Gross harvested biomass, observed saleable mass, observed rejected mass, and modelled saleable mass should remain separate concepts, because the acceptance criteria in the source set depend heavily on human or QA review of appearance, damage, aroma, contamination status, and handling history. citeturn14view0turn32view0turn32view1turn29view0

## Scope and exclusions

This synthesis is scoped to **fresh culinary basil**, primarily sweet basil where sources specify species or cultivar, in the product form **cut fresh basil sold by mass at the first wholesale transaction point where possible**. It excludes live-root basil, potted basil, ornamental basil, dried/processed basil, and consumer retail packs as target products, though those forms are used below for comparison where needed. citeturn29view0turn28view1

The evidence base reviewed here is strongest for four kinds of material: current EU marketing-standard texts and guidance, basil- or herb-specific postharvest university guidance, peer-reviewed basil postharvest literature, and fresh-culinary-herb food-safety/handling guidance. Within this source set, the most useful **formal** texts are the EU general marketing standard and the Basilico Genovese PDO specification; the most useful **basil-specific operational** texts are UC Davis, Rutgers, Texas A&M, and the Rutgers/Frontiers review; and the most useful **aquaponics-specific caution** is the UVI basil trial on repeated cutting, Pythium, and unmarketable harvest risk. citeturn25search1turn26search1turn22view0turn14view0turn20view0turn19view0turn29view3turn24view0

## Evidence hierarchy and source-quality notes

The strongest formal baseline for **marketability** is the EU general marketing standard. It is current in the post-2025 EU framework and requires produce to be intact, sound, clean, practically free from pests and pest damage, free of abnormal external moisture, free of foreign smell/taste, and able to withstand transport and handling. The older consolidated annex text and official explanatory guidance are still useful for reading those requirements in plain language and for confirming that they apply across the marketing chain, including wholesale and distribution. citeturn25search1turn26search1turn21view2turn27view0

The strongest basil-specific **formal proxy** is the Basilico Genovese PDO specification. It is not a universal wholesale standard for all basil, and it is partly aimed at whole-plant/bunched product, so it should not be over-promoted. But it is still highly valuable as a defensible proxy because it is official EU text and it encodes useful basil-specific maturity and quality cues: young vegetative material, no flower heads, strong characteristic odour, and fragility/proneness to drying. citeturn22view0

The strongest basil-specific **quality and storage** evidence comes from UC Davis and the 2023 Frontiers review. UC Davis provides direct herb-quality indices and basil-specific storage/disorder guidance. The Frontiers review consolidates the basil literature and is especially helpful on shelf life, chilling injury, harvest timing, and the trade-off between microbial control and cold damage. citeturn14view0turn31view0turn29view0turn13view4

The main limitation is that this source set does **not** yield a single pan-market, basil-only, bulk-wholesale grade with explicit tolerance percentages for defects such as broken stems, minor yellowing, or leaf blackening. Where the evidence is weaker, the safe move is to keep the repo item as **provisional**, **operator assumption**, or **open question** instead of inventing a hard threshold. citeturn26search1turn22view0turn14view0

## Harvest-readiness and saleability criteria

### Harvest-readiness criteria

The most defensible pre-harvest readiness rule is: **harvest fresh basil for bulk wholesale while the crop is still in young vegetative growth and before flowering**. Rutgers states that flowers should be pinched off because they reduce flavour quality and basil can become bitter during and after flowering. The Basilico Genovese PDO specification independently requires material for fresh sale or processing to be without flower heads. These two lines of evidence support a strong canon rule that “non-flowering” belongs in harvest-readiness logic. citeturn30view2turn30view3turn22view0

A second strong readiness rule is that basil should be harvested as **soft leafy stems or leaves**, not over-mature woody material. UC Davis describes culinary herbs such as basil as being harvested as soft or semi-woody leafy stems, while the PDO proxy constrains harvest to very young plants or plant portions. That combination supports “young, leafy, non-overdeveloped” as a defensible maturity concept, even though it does not justify one universal numeric height rule. citeturn14view0turn21view2turn22view0

Numeric harvest-readiness triggers are useful, but weaker. Texas A&M says basil is ready for harvest at about 10 inches tall. Utah State recommends beginning harvest at 6–8 leaves and leaving 2–4 leaves behind; Arizona gives a similar practical threshold of 6–8 inches tall. These are credible grower heuristics, but they vary enough by production context that they should stay **provisional** rather than promoted as canonical wholesale thresholds. citeturn19view0turn7view5turn7view6

### At-harvest cutting and selection criteria

At harvest, the strongest operational selection rule is to cut in ways that preserve repeat harvest and avoid excessive damage. Rutgers recommends not over-harvesting and leaving at least four sets of true leaves for continued growth. UVI’s aquaponics work also found that cutting stimulated branching and faster regrowth, which supports the use of repeated-cut logic in basil models. citeturn30view2turn24view0

The time of day also matters. The Frontiers review reports that harvesting basil in the afternoon or evening can extend postharvest shelf life nearly two-fold relative to very early-morning harvests under the cited studies, and that afternoon harvest reduced the severity of chilling symptoms during later storage. This is useful for an operations note, but it is not a buyer-grade threshold; it should sit in harvest-protocol logic, not saleability canon. citeturn29view2

Mechanical injury should be treated as a first-order at-harvest risk. UC Davis states that damage to herb leaves at harvest can lead to discolouration and increased susceptibility to decay. Rutgers similarly says rough handling injures leaves and significantly reduces shelf life and crop value. For repo purposes, “mechanical damage” belongs in `quality_exclusion_reasons`, and should be manually reviewed rather than inferred from biomass alone. citeturn31view0turn30view0

### Saleability and wholesale acceptance criteria

For first-pass saleability, the minimum defensible acceptance rule is the current EU-style produce baseline plus basil-specific freshness criteria. The EU baseline is: intact, sound, clean, practically free from pests, free from pest damage affecting the flesh, free of abnormal external moisture, free of any foreign smell or taste, and in condition to withstand transport and arrive satisfactorily. Importantly, the standard also allows a **slight** lack of freshness and turgidity after dispatch, which means that not every minor transit softness should be treated as automatic rejection. citeturn26search1turn21view2

UC Davis provides the best basil/herb quality descriptors for applying that baseline: freshness, uniformity of size/form/colour, lack of damaged leaves, lack of yellowing, lack of decay, lack of insect damage, and lack of wilting, with aroma treated as essential. That gives a practical saleability screen for bulk basil: **fresh-looking, cultivar-appropriate colour, undamaged, non-wilted, clean, and aromatic**. citeturn14view0

Postharvest handling is central to basil saleability because basil is chilling-sensitive and short-lived. UC Davis says basil should be stored above 10°C and that shelf life is typically only 1–2 weeks depending on water loss. The Frontiers review narrows the optimal storage zone to **12–15°C at high humidity**, notes that severe chilling injury occurs at 5°C and below, and reports that marketability at room temperature is often only a matter of days. That means saleability cannot be treated as independent from handling history. citeturn14view0turn13view4turn13view5

The most important basil-specific warning is that **visual acceptability is not enough**. UC Davis explicitly says visual shelf life is longer than useful culinary shelf life, because aroma can degrade before the product stops looking saleable. For a basil wholesale path, that makes aroma part of the reference standard even if aroma is not easily measurable in runtime. citeturn31view4

### Exclusion and rejection criteria

The strongest exclusion criteria are the official and basil-specific defects that clearly destroy marketability. These include rotting or deterioration that makes the product unfit for consumption; visible decay; serious pest presence or pest damage; visible foreign matter; abnormal external moisture; and foreign smell/taste. These are formal market or food-safety exclusions, not just operator preferences. citeturn26search1turn21view2turn32view1

Basil-specific rejection cues include moderate-to-severe chilling injury, leaf browning or blackening, bronzed veins, loss of gloss, major loss of turgidity, chilling-related wilting, and decay. The Frontiers review adds that moderate-to-severe chilling can render leaves inedible. UC Davis notes that on its basil chilling scale, a score of 3 was considered the limit of commercial acceptability. citeturn29view0turn31view0

Pathological rejection should also include bacterial soft rot and grey mould. UC Davis notes that bacterial soft rots cause slimy breakdown and that grey mould caused by *Botrytis cinerea* can occur commonly on basil. These are not “minor defects”; they are exclusion conditions for saleable wholesale mass. citeturn31view1turn31view2

Food-safety disqualification must be separated from visual grading. FDA’s fresh-culinary-herb guidance says crops that have come into contact with floodwaters are considered adulterated and cannot be sold for human consumption. That is a strong exclusion reason, but one that a simulator should never pretend to infer from plant appearance alone. It needs either scenario facts or QA input. citeturn32view3

### Repeated-cut basil considerations

Repeated-cut logic is relevant, but it belongs partly in biology and operations rather than pure wholesale canon. Rutgers says at least four sets of true leaves should remain after harvest to preserve continued growth, while UVI found that cutting stimulated branching and faster regrowth. That supports a repeated-cut readiness concept for basil. citeturn30view2turn24view0

However, UVI also found two saleability risks that matter to aquaponics: nutrient deficiencies in batch-grown basil could render much of the harvest unmarketable, and Pythium mortality was aggravated by cutting, especially under higher water temperatures. Those findings are strong evidence that a future aquaponics runtime should distinguish “biomass available to cut” from “saleable bulk mass actually accepted.” citeturn24view0

## Product-form differences and minimum defensible first-pass standard

### Differences from bunch retail, retail-packed, live-root, and potted basil

The source set supports a clean distinction between **bulk wholesale cut basil** and more processed or consumer-facing forms. FDA states that RTU and RTE fresh culinary herbs are minimally processed, cleaned, trimmed, and possibly cut before plastic protective packaging, while herbs packed at a packinghouse or in the field are primarily packed in bulk. It also distinguishes RTU from RTE by wash status: RTU may still need washing, whereas RTE has been washed and is ready for consumption. That makes bulk wholesale the safer default analogue for your first slice, not retail-packed basil. citeturn28view0turn28view1turn28view2

Live-root and potted basil are separate product classes. The Frontiers review notes that a large share of basil is sold as fresh-cut leaves, live rooted plants, or cuttings, which itself shows that these are recognised distinct forms. The Basilico Genovese PDO specification further shows how whole-plant product can carry different structural expectations, including whole plants, roots, bunches, and bouquet definitions. Those product forms should not be silently merged with cut bulk basil in repo logic. citeturn29view0turn22view0

Bunch retail is also not the same thing as bulk kg wholesale. Rutgers describes bunch display practices such as standing stems in water and using bags or clamshells quickly to limit moisture loss. That is useful operationally, but it is channel-specific handling, not a universal saleability rule for bulk wholesale. citeturn30view0turn30view1

### Minimum defensible first-pass standard

A practical first-pass external reference standard for `basil bulk kg wholesale` can therefore be stated as follows:

A lot is **harvest-ready** if it is young vegetative basil intended for fresh culinary use, harvested as leafy stems/leaves before flowering, with no flower heads, and cut in a way that preserves acceptable regrowth where repeated harvest is intended. Numeric height or leaf-count triggers may be recorded as contextual grower heuristics, but should remain provisional rather than canonical. citeturn22view0turn30view2turn30view3turn19view0turn7view6

A lot is **saleable for first-pass bulk wholesale** if it meets the general marketability baseline of being sound, clean, practically free from pests and visible foreign matter, not rotten, without abnormal external moisture or foreign odour/taste, and with enough freshness/turgidity to survive handling and arrive satisfactorily; and if, for basil specifically, it retains fresh appearance, cultivar-appropriate colour, no important yellowing/wilting/decay/insect damage, and acceptable culinary aroma. citeturn26search1turn21view2turn14view0turn31view4

A lot is **excluded / non-saleable** if it is rotten, seriously decayed, contaminated with floodwater, visibly moulded or soft-rotted, seriously wilted, materially yellowed/blackened/browned, mechanically damaged to the point that decay risk or presentation is compromised, materially contaminated with foreign matter, or clearly off-aroma/off-odour for culinary use. citeturn31view0turn31view1turn31view2turn32view1turn32view3

## Evidence-strength table

| criterion | candidate field name | definition | unit or value type | product context | observation/review mode | evidence strength | source basis | recommended repo disposition |
|---|---|---|---|---|---|---|---|---|
| Non-flowering harvest stage | `harvest_readiness_basis.stage_non_flowering` | Basil intended for fresh sale should be harvested before flowering; flower heads absent. | boolean / enum | fresh cut basil; wholesale bulk; repeated-cut systems | grower inspection; harvest crew grading | **strong** | Basilico Genovese PDO requires material “without flower heads”; Rutgers says flowers reduce flavour and basil gets bitter after flowering. citeturn22view0turn30view2turn30view3 | **canonical** |
| Young vegetative material | `harvest_readiness_basis.young_vegetative_material` | Material should be young, leafy, not overdeveloped. | boolean / enum | fresh cut basil | grower inspection; harvest crew grading | **medium** | EU general standard requires sufficiently developed but not over-developed produce; UC Davis describes basil/herbs as soft or semi-woody leafy stems; PDO proxy restricts true-leaf/node stage. citeturn21view2turn14view0turn22view0 | **canonical** as concept, not as one numeric trigger |
| Numeric cut-size threshold | `harvest_readiness_basis.size_proxy` | Contextual proxy such as ~10 inches tall or 6–8 leaves / 6–8 inches. | numeric + provenance | grower operations | grower inspection | **weak to medium** | Texas A&M: harvestable at about 10 inches; Utah/Arizona extension offer 6–8 leaf / 6–8 inch heuristics. citeturn19view0turn7view5turn7view6 | **provisional** |
| Leave regrowth nodes | `harvest_readiness_basis.regrowth_reserve` | Leave sufficient true leaves/nodes after cutting for regrowth. | integer / enum | repeated-cut basil | harvest crew grading | **medium** | Rutgers advises leaving at least four sets of true leaves; UVI found cutting stimulated branching and faster regrowth. citeturn30view2turn24view0 | **canonical** for repeated-cut context |
| Freshness / turgidity | `saleability_basis.visual_freshness_turgidity` | Fresh-looking, adequately turgid material suitable for transport and arrival. | ordinal / enum | first wholesale transfer | harvest crew grading; receiving inspection | **strong** | EU general marketing standard; later stages may show only slight lack of freshness/turgidity; UC Davis freshness is a core quality index. citeturn21view2turn14view0 | **canonical** |
| Visual defect screen | `quality_exclusion_reasons.visual_defects` | Reject or downgrade for important yellowing, wilting, decay, insect damage, serious mechanical damage. | categorical list | first wholesale transfer | harvest crew grading; receiving inspection | **strong** | UC Davis quality indices name damaged/yellowed leaves, decay, insect damage, wilting; UC Davis also warns harvest damage increases decay risk. citeturn14view0turn31view0 | **canonical** |
| Aroma suitability | `saleability_basis.aroma_acceptability` | Culinary basil should retain characteristic aroma; visual acceptability alone is insufficient. | ordinal / enum | culinary basil | human sensory review only | **medium** | UC Davis says characteristic aroma is essential and visual shelf life can exceed useful culinary shelf life; PDO proxy stresses strong characteristic odour. citeturn14view0turn31view4turn22view0 | **canonical**, but **manual-review only** |
| Chilling injury rejection | `quality_exclusion_reasons.chilling_injury` | Reject when chilling causes meaningful browning/blackening, necrosis, severe wilt/turgor loss, or decay. | categorical severity | postharvest basil | receiving inspection; QA review | **strong** | Frontiers: <12°C causes injury, <10°C severe injury; moderate-to-severe cases render leaves inedible; UC Davis gives commercial-acceptability limit on basil chilling scale. citeturn29view0turn31view0 | **canonical** |
| Storage/handling band | `postharvest_handling_basis.temp_humidity_band` | Basil needs cool-but-not-cold storage, high RH, rapid shading/cooling, careful handling. | numeric range + note | bulk wholesale handling | operator config; manual review | **strong** | UC Davis: store above 10°C, >95% RH; Frontiers: 12–15°C at >90% RH; Rutgers: keep cool, remove from sun, avoid rough handling. citeturn14view0turn13view4turn30view0 | **canonical** for reference handling, not buyer-grade guarantee |
| Food-safety contamination exclusion | `quality_exclusion_reasons.food_safety_contamination` | Exclude for floodwater adulteration, foreign objects, debris, other contamination events. | categorical list | all fresh culinary herbs | QA review; compliance review | **strong** | FDA herbs guidance: floodwater-contact crop cannot be sold; guidance addresses foreign objects and trash/debris hazards. citeturn32view3turn32view1turn32view2 | **canonical** |
| Bulk-vs-processed saleability basis | `saleability_basis.product_form_context` | Distinguish bulk packed herbs from RTU/RTE washed/trimmed/retail-packed herbs. | enum | bulk wholesale vs RTU vs RTE | config / manual review | **strong** | FDA distinguishes bulk-packed herbs from RTU/RTE forms and distinguishes RTU from RTE by wash status. citeturn28view0turn28view1turn28view2 | **canonical** |
| Aquaponics repeated-cut failure risk | `quality_exclusion_reasons.production_failure_flags` | Nutrient deficiency and Pythium can reduce marketable share in repeated-cut aquaponic basil. | categorical list | aquaponics repeated-cut basil | grower inspection; QA review; model support | **medium** | UVI: cutting improved branching/regrowth, but Pythium aggravated by cutting remained serious; nutrient deficiency could render much harvest unmarketable. citeturn24view0 | **canonical** for aquaponics stress model, not universal wholesale grade |

## What this implies for repo field naming

The repository should keep the mass terms and the review-status terms separate.

`gross_harvest_mass_kg` should mean **all harvested basil biomass entering the post-cut handling stream before quality exclusion**. It should never imply saleability by itself.

`observed_saleable_harvest_mass_kg` should mean **mass actually accepted as saleable after human grading / QA / buyer-facing inspection using the active saleability basis**. This should only be populated when a human-reviewed or system-recorded acceptance event exists.

`observed_rejected_harvest_mass_kg` should mean **mass explicitly rejected or downgraded out of the target sale form**, with reasons stored alongside it. Those reasons should include items such as `wilting`, `yellowing`, `mechanical_damage`, `chilling_injury`, `pest_damage`, `decay`, `foreign_matter`, `off_odour`, `food_safety_contamination`, and `other_manual_reject_reason`. These categories are grounded in the EU/FDA/UC Davis source set. citeturn26search1turn14view0turn31view0turn32view1turn32view3

`modeled_saleable_harvest_mass_kg` should mean **an estimate derived from gross harvested mass via a modelled saleability adjustment**, not an observed fact. This matters because the sources rely on human-observable appearance, aroma, contamination status, and handling history. A simulator can model a probability or expected fraction; it cannot honestly claim to have observed those quality outcomes unless a reviewed record exists. citeturn14view0turn31view4turn32view0

`saleability_basis` should encode **how acceptance was determined**, not whether the lot was good. A practical enum could include: `observed_visual_grade`, `observed_receiving_acceptance`, `observed_buyer_acceptance`, `modeled_quality_adjustment`, `operator_assumption`, `not_assessed`. That keeps provenance explicit.

`harvest_readiness_basis` should encode **why the crop was considered ready to cut**. A practical structure could include fields such as `stage_non_flowering`, `young_vegetative_material`, `size_proxy_type`, `size_proxy_value`, `regrowth_leaves_left`, and `basis_confidence`.

`harvest_quality_review_status` should explicitly distinguish `not_reviewed`, `grower_checked`, `harvest_crew_graded`, `postharvest_qc_reviewed`, `buyer_rejected`, and `buyer_accepted`.

`saleability_confidence` should be an explicit confidence flag for the saleability output, not a vague model score. A simple enum such as `high_observed`, `medium_reviewed`, `low_modeled`, `assumption_only` would be more honest.

`evidence_strength` should remain attached to schema interpretations or reference standards, not to a physical batch itself. For batches, use review/provenance; for standards, use evidence strength.

## What this implies for future runtime output design

Future runtime output should avoid collapsing distinct epistemic states. A safe and reviewable pattern is:

- **measured / observed output**: values directly recorded from harvest or weighing events, such as `gross_harvest_mass_kg`.
- **manually reviewed output**: values confirmed by a human grading or QA step, such as `observed_saleable_harvest_mass_kg` and `observed_rejected_harvest_mass_kg`.
- **modelled output**: values estimated from a quality model using handling/stress assumptions, such as `modeled_saleable_harvest_mass_kg`.
- **estimated output**: values inferred from partial observation plus assumptions, clearly marked as such.
- **quality-adjusted output**: values produced by applying a quality or saleability function to gross mass.
- **rejected biomass**: mass excluded from the target sale form for explicit reasons.
- **assumptions used**: storage-temperature assumptions, shrink assumptions, handling quality assumptions, and review confidence. citeturn14view0turn29view0turn32view0

The runtime should also separate **quality state** from **commercial acceptance state**. A lot may be biologically harvestable and visually decent, yet commercially weak because aroma collapsed, handling was rough, or the lot missed buyer-specific product-form expectations. That distinction is strongly implied by the source set, especially the gap between visual shelf life and useful culinary shelf life, and the distinction between bulk, RTU, RTE, and whole-plant forms. citeturn31view4turn28view1

## Open questions and recommended next step

The main unresolved point is the absence, in this reviewed source set, of a **generic basil-only bulk-wholesale buyer specification** with explicit defect tolerances for stem breakage, minor yellowing, allowed wilt, leaf-size mix, or stem/leaf ratio. That means your first-pass canon should stay at the level of **minimum defensible acceptance criteria**, not pretend to have precise buyer-grade tolerances.

A second unresolved point is **numeric harvest stage calibration**. The reviewed sources support non-flowering, young vegetative harvest very well, but they do **not** support one universal numeric rule for cut height, plant height, or leaf count across greenhouse, hydroponic, aquaponic, and field contexts. Those should remain contextual.

A third unresolved point is **aroma grading**. Aroma is clearly essential to basil saleability, but the source set does not offer a simple wholesale-ready numeric aroma threshold for bulk lots. For now, aroma should stay a manual-review concept, not a deterministic runtime output.

The recommended next repo-side step is to create a **basil saleability reference note** and a **schema stub** that promotes only the strong concepts now: `non_flowering`, `young_vegetative_material`, `visual_freshness_turgidity`, `visual_defect_screen`, `chilling_injury`, `food_safety_contamination`, explicit provenance for `saleability_basis`, and a strict separation between observed and modelled saleable mass. Leave numeric cut thresholds, aroma scoring thresholds, and buyer-specific tolerance bands as provisional or open questions until you have high-trust buyer specs or audited receiving records.