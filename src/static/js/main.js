async function create_url(input_name){

    // получаем введеное в поле имя и возраст
    const long_url = document.getElementById(input_name).value;

    // отправляем запрос
    const response = await fetch("/create/", {
            method: "POST",
            headers: { "Accept": "application/json", "Content-Type": "application/json" },
            body: JSON.stringify({
                long_url: long_url,
            })
        });
        if (response.ok) {
            const data = await response.json();
            document.getElementById("short_url").textContent = data.short_url;
        }
        else
            console.log(response);
}