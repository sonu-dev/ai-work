
$mcpServerUri = "http://127.0.0.1:8080/mcp"
$greet = [PSCustomObject]@{
    name = "greet"
    arguments = @{
        name = $env:USERNAME
    }
}
$addTool = [PSCustomObject]@{
    name = "add"
    arguments = @{
        a = 5
        b = 7
    }
}

function Initialize-Session { 
   
    $initBody = @{
    jsonrpc = "2.0"
    method = "initialize"
    params = @{
        protocolVersion = "2024-11-05"
        capabilities = @{}
        clientInfo = @{
            name = "powershell-client"
            version = "1.0"
            }
        }
        id = 1
    } | ConvertTo-Json -Compress

    $initResponse = Invoke-WebRequest `
        -Uri $mcpServerUri `
        -Method POST `
        -ContentType "application/json" `
        -Headers @{ Accept = "application/json,text/event-stream" } `
        -Body $initBody

    # Extract session ID from response headers
    $sessionId = $initResponse.Headers["Mcp-Session-Id"]

    Write-Host "SessionId: {$sessionId}" 
    return $sessionId
}

function Invoke-Tool {
    param(
     [Parameter(Mandatory=$true)]
     $sessionId,
     [Parameter(Mandatory=$true)]
     [PSCustomObject]$tool)

     $runBody = @{
     jsonrpc = "2.0"
     method  = "tools/call"
     params  = $tool
     id = 2
} | ConvertTo-Json -Compress

Invoke-RestMethod `
    -Uri $mcpServerUri `
    -Method POST `
    -ContentType "application/json" `
    -Headers @{
        Accept = "application/json,text/event-stream"
        "Mcp-Session-Id" = $sessionId
    } `
    -Body $runBody
}

$sessionId = Initialize-Session

Write-Host "SessionId:{$sessionId}" 

Invoke-Tool $sessionId $addTool

Invoke-Tool $sessionId $greet
