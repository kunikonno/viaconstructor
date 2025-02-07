def setup_defaults(_) -> dict:
    return {
        "mill": {
            "active": {
                "default": True,
                "type": "bool",
                "per_object": True,
                "title": _("Active"),
                "tooltip": _("enable/disable this object"),
            },
            "depth": {
                "default": -9.0,
                "type": "float",
                "min": -999.0,
                "max": 0.0,
                "per_object": True,
                "title": _("Depth"),
                "tooltip": _("the end depth for milling"),
                "unit": "LINEARMEASURE",
            },
            "step": {
                "default": -9.0,
                "type": "float",
                "min": -999.0,
                "max": 0.0,
                "per_object": True,
                "title": _("Step"),
                "tooltip": _("the maximum depth in one move"),
                "unit": "LINEARMEASURE",
            },
            "start_depth": {
                "default": 0.0,
                "type": "float",
                "min": -999.0,
                "max": 0.0,
                "per_object": True,
                "title": _("Start-Depth"),
                "tooltip": _("the start depth for milling"),
                "unit": "LINEARMEASURE",
            },
            "passes": {
                "default": 1,
                "type": "int",
                "min": 1,
                "max": 99,
                "per_object": True,
                "title": _("Passes"),
                "tooltip": _("Passes / in Laser-Mode"),
            },
            "helix_mode": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Helix"),
                "tooltip": _("Helix"),
            },
            "fast_move_z": {
                "default": 5.0,
                "type": "float",
                "min": 0.0,
                "max": 999.0,
                "title": _("Fast-Move Z"),
                "tooltip": _("the Z-Position for fast moves"),
                "unit": "LINEARMEASURE",
            },
            "G64": {
                "default": 0.020000,
                "type": "float",
                "min": 0.0,
                "max": 0.1,
                "title": _("G64-Value"),
                "tooltip": _("value for the G64 command"),
            },
            "reverse": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Reverse"),
                "tooltip": _("Reverse"),
            },
            "back_home": {
                "default": True,
                "type": "bool",
                "title": _("Back-Home"),
                "tooltip": _("move tool back to Zero-Possition after milling"),
            },
            "small_circles": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Small-Circles"),
                "tooltip": _("milling small circles even if the tool is bigger"),
            },
            "overcut": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Overcut"),
                "tooltip": _("Overcuting edges"),
            },
            "offset": {
                "default": "auto",
                "type": "select",
                "per_object": True,
                "options": (
                    ("auto", _("auto")),
                    ("inside", _("inside")),
                    ("outside", _("outside")),
                    ("none", _("none")),
                ),
                "title": _("Offset"),
                "tooltip": _("tool offset"),
            },
            "objectorder": {
                "default": "nearest",
                "type": "select",
                "options": (
                    ("nearest", _("nearest")),
                    ("unordered", _("unordered")),
                    ("per_object", _("per_object")),
                ),
                "title": _("Object-Order"),
                "tooltip": _("how order the objects"),
            },
        },
        "tool": {
            "number": {
                "default": 1,
                "type": "int",
                "min": 1,
                "max": 99,
                "title": _("Number"),
                "tooltip": _("setting the Tool-Number to load in gcode"),
                "per_object": True,
            },
            "speed": {
                "default": 10000,
                "type": "int",
                "min": 100,
                "max": 100000,
                "title": _("Speed"),
                "tooltip": _("setting the Tool-Speed in RPM"),
                "unit": "RPM",
                "per_object": True,
            },
            "rate_h": {
                "default": 1000,
                "type": "int",
                "min": 1,
                "max": 10000,
                "title": _("Feed-Rate(Horizontal)"),
                "tooltip": _("the Horizotal Feetrate"),
                "unit": "mm/min",
                "per_object": True,
            },
            "rate_v": {
                "default": 100,
                "type": "int",
                "min": 1,
                "max": 10000,
                "title": _("Feed-Rate(Vertical)"),
                "tooltip": _("the Vertical Feetrate"),
                "unit": "mm/min",
                "per_object": True,
            },
            "pause": {
                "default": 3,
                "type": "int",
                "min": 0,
                "max": 60,
                "title": _("Pause"),
                "tooltip": _("tool spin up time (G04 Pn)"),
                "unit": "s",
                "per_object": True,
            },
            "mist": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Mist"),
                "tooltip": _("activate mist"),
            },
            "flood": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Flood"),
                "tooltip": _("activate flood"),
            },
            "tooltable": {
                "type": "table",
                "selectable": True,
                "default": [
                    {
                        "name": "Wood cutter (small)",
                        "number": 1,
                        "diameter": 2.5,
                        "lenght": 10.0,
                        "blades": 3,
                    },
                    {
                        "name": "Wood cutter (big)",
                        "number": 2,
                        "diameter": 4.0,
                        "lenght": 12.0,
                        "blades": 2,
                    },
                    {
                        "name": "Alu cutter (big)",
                        "number": 3,
                        "diameter": 6.0,
                        "lenght": 12.0,
                        "blades": 1,
                    },
                    {
                        "name": "Laser",
                        "number": 10,
                        "diameter": 0.1,
                        "lenght": 10.0,
                        "blades": 0,
                    },
                ],
                "columns": {
                    "name": {"type": "str"},
                    "number": {"type": "int"},
                    "diameter": {"type": "float"},
                    "lenght": {"type": "float"},
                    "blades": {"type": "int"},
                },
                "column_defaults": {
                    "name": "",
                    "number": 99,
                    "diameter": 1.0,
                    "lenght": 1.0,
                    "blades": 1,
                },
                "title": _("Tools"),
                "tooltip": _("tooltable"),
            },
        },
        "workpiece": {
            "zero": {
                "default": "bottomLeft",
                "type": "select",
                "options": (
                    ("original", _("original")),
                    ("bottomLeft", _("bottomLeft")),
                    ("center", _("center")),
                    ("bottomRight", _("bottomRight")),
                    ("topLeft", _("topLeft")),
                    ("topRight", _("topRight")),
                ),
                "title": _("Zero-Position"),
                "tooltip": _("setting the Zero-Postition of the Workpiece"),
            },
            "offset_x": {
                "default": 0.0,
                "type": "float",
                "min": -100000.0,
                "max": 100000.0,
                "title": _("Offset X"),
                "tooltip": _("Offset X (G54)"),
                "unit": "LINEARMEASURE",
            },
            "offset_y": {
                "default": 0.0,
                "type": "float",
                "min": -100000.0,
                "max": 100000.0,
                "title": _("Offset Y"),
                "tooltip": _("Offset Y (G54)"),
                "unit": "LINEARMEASURE",
            },
            "offset_z": {
                "default": 0.0,
                "type": "float",
                "min": -100000.0,
                "max": 100000.0,
                "title": _("Offset Z"),
                "tooltip": _("Offset Z (G54)"),
                "unit": "LINEARMEASURE",
            },
            "materialtable": {
                "type": "table",
                "selectable": True,
                "default": [
                    {
                        "name": "Aluminum(Long.)",
                        "vc": 200,
                        "fz4": 0.04,
                        "fz8": 0.05,
                        "fz12": 0.10,
                    },
                    {
                        "name": "Aluminum(Short.)",
                        "vc": 150,
                        "fz4": 0.04,
                        "fz8": 0.05,
                        "fz12": 0.10,
                    },
                    {
                        "name": "NF-Metals",
                        "vc": 150,
                        "fz4": 0.04,
                        "fz8": 0.05,
                        "fz12": 0.10,
                    },
                    {
                        "name": "VA-Steel",
                        "vc": 100,
                        "fz4": 0.05,
                        "fz8": 0.06,
                        "fz12": 0.07,
                    },
                    {
                        "name": "Thermoset plastic",
                        "vc": 125,
                        "fz4": 0.04,
                        "fz8": 0.08,
                        "fz12": 0.10,
                    },
                    {
                        "name": "Plexiglass",
                        "vc": 250,
                        "fz4": 0.1,
                        "fz8": 0.2,
                        "fz12": 0.3,
                    },
                    {"name": "GFK", "vc": 125, "fz4": 0.04, "fz8": 0.08, "fz12": 0.10},
                    {"name": "CFK", "vc": 125, "fz4": 0.04, "fz8": 0.08, "fz12": 0.10},
                    {
                        "name": "Wood",
                        "vc": 2000,
                        "fz4": 0.04,
                        "fz8": 0.08,
                        "fz12": 0.10,
                    },
                ],
                "columns": {
                    "name": {"type": "str"},
                    "vc": {"type": "int"},
                    "fz4": {"type": "float"},
                    "fz8": {"type": "float"},
                    "fz12": {"type": "float"},
                },
                "column_defaults": {
                    "name": "",
                    "vc": 100,
                    "fz4": 0.05,
                    "fz8": 0.05,
                    "fz12": 0.05,
                },
                "title": _("Materials"),
                "tooltip": _("materialtable"),
            },
        },
        "pockets": {
            "active": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Pocket"),
                "tooltip": _("do pocket operation on this object"),
            },
            "zigzag": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Zickzack"),
                "tooltip": _("Zickzack"),
            },
            "islands": {
                "default": True,
                "type": "bool",
                "per_object": True,
                "title": _("Islands"),
                "tooltip": _("keep islands"),
            },
            "insideout": {
                "default": True,
                "type": "bool",
                "per_object": True,
                "title": _("insideout"),
                "tooltip": _("from inside to out"),
            },
        },
        "tabs": {
            "active": {
                "default": True,
                "type": "bool",
                "title": _("active"),
                "tooltip": _("activate tabs"),
                "per_object": True,
            },
            "width": {
                "default": 10,
                "type": "float",
                "min": 0.1,
                "max": 20,
                "title": _("Width"),
                "tooltip": _("width of the tabs"),
                "per_object": True,
                "unit": "LINEARMEASURE",
            },
            "height": {
                "default": 2,
                "type": "float",
                "min": 0.1,
                "max": 10000,
                "title": _("Height"),
                "tooltip": _("height of the tabs"),
                "per_object": True,
                "unit": "LINEARMEASURE",
            },
            "type": {
                "default": "rectangle",
                "type": "select",
                "options": (
                    ("rectangle", _("rectangle")),
                    ("triangle", _("triangle")),
                ),
                "title": _("Type"),
                "per_object": True,
                "tooltip": _("type of the tab"),
            },
        },
        "leads": {
            "in": {
                "default": "off",
                "type": "select",
                "options": (
                    ("off", _("off")),
                    ("arc", _("arc")),
                    ("straight", _("straight")),
                ),
                "title": _("in-type"),
                "tooltip": _("type of the lead-in's"),
            },
            "in_lenght": {
                "default": 3.0,
                "type": "float",
                "min": 0.1,
                "max": 100,
                "title": _("in-lenght"),
                "tooltip": _("lenght of the lead-in's"),
                "per_object": True,
                "unit": "LINEARMEASURE",
            },
            "out": {
                "default": "off",
                "type": "select",
                "options": (
                    ("off", _("off")),
                    ("arc", _("arc")),
                    ("straight", _("straight")),
                ),
                "title": _("out-type"),
                "tooltip": _("type of the lead-out's"),
            },
            "out_lenght": {
                "default": 3.0,
                "type": "float",
                "min": 0.1,
                "max": 100,
                "title": _("out-lenght"),
                "tooltip": _("lenght of the lead-out's"),
                "per_object": True,
                "unit": "LINEARMEASURE",
            },
        },
        "machine": {
            "feedrate": {
                "default": 1000,
                "type": "int",
                "min": 10,
                "max": 10000,
                "title": _("Feedrate"),
                "tooltip": _("maximum feedrate while milling"),
            },
            "tool_speed": {
                "default": 15000,
                "type": "int",
                "min": 100,
                "max": 100000,
                "title": _("Tool-Speed"),
                "tooltip": _("maximum tool-speed"),
            },
            "plugin": {
                "default": "gcode_linuxcnc",
                "type": "select",
                "options": (
                    ("gcode_linuxcnc", _("gcode_linuxcnc")),
                    ("gcode_grbl", _("gcode_grbl")),
                    ("hpgl", _("hpgl")),
                ),
                "title": _("Plugin"),
                "tooltip": _("output plugin selection"),
            },
            "mode": {
                "default": "mill",
                "type": "select",
                "options": (
                    ("mill", _("mode")),
                    ("laser", _("laser")),
                    ("laser_z", _("laser+z")),
                ),
                "title": _("Tool-Mode"),
                "tooltip": _("Tool-Mode"),
            },
            "unit": {
                "default": "mm",
                "type": "select",
                "options": (
                    ("mm", _("mm")),
                    ("inch", _("inch")),
                ),
                "title": _("Unit"),
                "tooltip": _("Unit of the machine"),
            },
            "arcs": {
                "default": "ij",
                "type": "select",
                "options": (
                    ("ij", _("offset")),
                    ("r", _("radius")),
                ),
                "title": _("Arcs-Mode (G2/G3)"),
                "tooltip": _("Arcs-Mode - G2/G3 with IJ or R (experimental)"),
            },
            "g54": {
                "default": False,
                "type": "bool",
                "title": _("machine supports g54"),
                "tooltip": _("machine supports g54"),
            },
            "supports_toolchange": {
                "default": True,
                "type": "bool",
                "title": _("machine supports toolchange"),
                "tooltip": _("machine supports toolchange"),
            },
            "toolchange_pre": {
                "default": "",
                "type": "mstr",
                "title": _("toolchange pre cmd"),
                "tooltip": _("add gcode before tool-change"),
            },
            "toolchange_post": {
                "default": "",
                "type": "mstr",
                "title": _("toolchange post cmd"),
                "tooltip": _("add gcode after tool-change"),
            },
            "spindle_on_pre": {
                "default": "",
                "type": "mstr",
                "title": _("spindle on pre cmd"),
                "tooltip": _("add gcode before turning the spindle on"),
            },
            "spindle_off_post": {
                "default": "",
                "type": "mstr",
                "title": _("spindle off post cmd"),
                "tooltip": _("add gcode after turning the spindle off"),
            },
            "comments": {
                "default": True,
                "type": "bool",
                "title": _("Comments in output"),
                "tooltip": _("add comments to output"),
            },
            "numbers": {
                "default": False,
                "type": "bool",
                "title": _("line numbers"),
                "tooltip": _("adding line numbers"),
            },
            "postcommand": {
                "default": "",
                "type": "str",
                "title": _("Post-Command"),
                "tooltip": _("Post-Command to do things after save like upload to cnc"),
            },
        },
        "view": {
            "autocalc": {
                "default": True,
                "type": "bool",
                "title": _("Auto-Recalculation"),
                "tooltip": _("update drawing automatically"),
            },
            "path": {
                "default": "simple",
                "type": "select",
                "options": (
                    ("minimal", _("minimal")),
                    ("simple", _("simple")),
                    ("full", _("full")),
                ),
                "title": _("Path"),
                "tooltip": _("how to show the gcode path in the 3d-View"),
            },
            "colors_show": {
                "default": True,
                "type": "bool",
                "title": _("Colors-Show"),
                "tooltip": _("showing colors in 3D preview"),
            },
            "ruler_show": {
                "default": True,
                "type": "bool",
                "title": _("Ruler-Show"),
                "tooltip": _("showing ruler in 3D preview"),
            },
            "grid_show": {
                "default": True,
                "type": "bool",
                "title": _("Grid-Show"),
                "tooltip": _("showing grid in 3D preview"),
            },
            "grid_size": {
                "default": 10,
                "type": "int",
                "min": 1,
                "max": 1000,
                "title": _("Grid-Size"),
                "tooltip": _("size of the grid"),
            },
            "polygon_show": {
                "default": True,
                "type": "bool",
                "title": _("Show as Polygon"),
                "tooltip": _("showing as polygon in 3D preview"),
            },
            "object_ids": {
                "default": True,
                "type": "bool",
                "title": _("Show Object-ID's"),
                "tooltip": _("shows id of each object"),
            },
            "arcs": {
                "default": True,
                "type": "bool",
                "title": _("arcs"),
                "tooltip": _("draw arcs / Interpolation"),
            },
            "3d_show": {
                "default": False,
                "type": "bool",
                "title": _("Show inputfile in 3d"),
                "tooltip": _("Show inputfile in 3d if possible"),
            },
            "color": {
                "default": (0.5, 0.5, 0.5),
                "type": "color",
                "title": _("color"),
                "tooltip": _("color of the workpeace in 3d view"),
            },
            "alpha": {
                "default": 0.6,
                "type": "float",
                "step": 0.1,
                "decimals": 1,
                "min": 0,
                "max": 1.0,
                "title": _("transparency"),
                "tooltip": _("transparency of the workpeace in 3d view"),
            },
        },
    }
