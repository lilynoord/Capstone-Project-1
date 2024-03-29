// TODO: when hp is modified, send fetch request to server to update.
// TODO: expand monster row when clicked on to show actions and spells
// TODO: display monster details when name is clicked.
// TODO: when action or spell is clicked on, display details.
// TODO: highlight next row when end-turn is clicked

function show_action(e) {
	e.target.nextElementSibling.open = true;
}

async function update_health(e) {
	e.preventDefault();
	let num = 0 - e.target.nextElementSibling.value;
	request_body = {
		method: "POST",
		body: JSON.stringify({
			value: num,
			eType: e.target.dataset.etype,
			combat: e.target.dataset.combat,
			eid: e.target.dataset.temp,
			initiative: e.target.dataset.initiative,
		}),
		headers: {
			"Content-type": "application/json; charset=UTF-8",
		},
	};
	let hp = await fetch("/update-health", request_body);
	document.querySelector(`#hp-${e.target.dataset.initiative}`).innerHTML =
		await hp.json();
}
