from WBT.whitebox_tools import WhiteboxTools

wbt = WhiteboxTools()
print(wbt.list_tools()) # List all tools in WhiteboxTools
print(wbt.tool_help("elev_percentile"))
