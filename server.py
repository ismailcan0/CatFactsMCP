from mcp.server.fastmcp import FastMCP
from app import get_cat_fact

# MCP sunucusunu başlat
mcp = FastMCP("cat-facts-mcp")

@mcp.tool()
async def cat_fact() -> dict:
    """
    Cat Facts API'den rastgele kedi bilgisi alır.
    """
    # app.py'deki fonksiyonu çağırıyoruz (sync olduğu için await yok)
    result = get_cat_fact()
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")
