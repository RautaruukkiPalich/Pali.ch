async function create_url(inputName){

    const long_url = document.getElementById(inputName).value;

    const response = await fetch("/create/", {
            method: "POST",
            headers: { "Accept": "application/json", "Content-Type": "application/json" },
            body: JSON.stringify({
                long_url: long_url,
            })
        });
        default_form(inputName)
        if (response.ok) {
            const data = await response.json();
            const error_mess = data.error;
            switch (error_mess) {
                case null:
                    document.getElementById("div-short-url").style.display = "block";
                    document.getElementById("short_url").textContent = data.short_url;
                default:
                    document.getElementById("error").textContent = error_mess;
            }
        }
        else {
            document.getElementById("error").textContent = "Unexpected Error";
        }
    }

function default_form(long_url) {
    document.getElementById("long_url").textContent = long_url;
    document.getElementById("error").textContent = null;
    document.getElementById("short_url").textContent = null;
    document.getElementById("div-short-url").style.display = "none";
}


async function copyTextToClipboard(id) {
    var textToCopy = document.getElementById(id).innerText
    try {
        await navigator.clipboard.writeText(textToCopy);
        console.log('copied to clipboard: ' + textToCopy)
    } catch (error) {
        console.log('failed to copy to clipboard. error=' + error);
    }
}
