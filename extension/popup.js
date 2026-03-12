async function checkSpam() {

    const text = document.getElementById("message").value;

    const response = await fetch("http://localhost:8000/scan", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({text})
    });

    const data = await response.json();

    document.getElementById("result").innerText =
        `Result: ${data.prediction} (${data.confidence})`
}

document.getElementById("scan").onclick = checkSpam