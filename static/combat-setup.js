let entity_list = [];
let entity_count = 0;
function monster_click(e) {
	let name = e.target.parentElement.getAttribute("data-name");
	let id = e.target.parentElement.getAttribute("data-id");
	add_to_initiative(name, id, "monster");
}
function pc_click(e) {
	let name = e.target.parentElement.getAttribute("data-name");
	let id = e.target.parentElement.getAttribute("data-id");
	add_to_initiative(name, id, "pc");
}
function npc_click(e) {
	let name = e.target.parentElement.getAttribute("data-name");
	let id = e.target.parentElement.getAttribute("data-id");
	add_to_initiative(name, id, "npc");
}

function add_to_initiative(name, id, kind) {
	initiative = document.querySelector("#init-body");
	console.log(name);
	newRow = initiative.insertRow();
	newCell1 = newRow.insertCell();
	newCell2 = newRow.insertCell();
	newCell3 = newRow.insertCell();
	newCell2.innerHTML = name;
	newCell1.innerHTML = `<input id='${entity_count}' type='number' class='init-input' oninput='update_initiative(event)' value=10>`;
	newCell3.innerHTML = `<button id='${entity_count}' class='contrast outline init-del' onclick='remove_from_initiative(event)'>x</button>`;
	entity_list.push({ name: name, id: id, kind: kind, initiative: 10 });
	entity_count += 1;
	console.log(entity_list);
}

function remove_from_initiative(e) {
	e.target.parentElement.parentElement.parentElement.deleteRow(
		e.target.parentElement.parentElement.rowIndex - 1
	);
	entity_list[e.target.id] = "REMOVED";
}

function update_initiative(e) {
	entity_list[e.target.id]["initiative"] = parseInt(e.target.value);
}
//When a creature is clicked, add an entry to the active box (Initiative - Name)
//When creature in active box is clicked, remove from active box
//keep a record of everything in the active box: Creature ID plus initiative
// When submit is clicked, send data from active box to server as json.

document
	.querySelector("form[name=submit-form]")
	.addEventListener("submit", async function (e) {
		e.preventDefault();
		const request_body = {
			method: "POST",
			body: JSON.stringify({
				entity_list: entity_list,
			}),
			headers: {
				"Content-type": "application/json; charset=UTF-8",
			},
		};
		console.log(entity_list);
		combatId = document.querySelector("input[name=combatId]").value;
		console.log(request_body);
		let pass = false;
		try {
			await fetch(`/games/combat/submit-combat/${combatId}`, request_body)
				.then((r) => console.log(r))
				.then((pass = true));
		} catch (error) {
			console.log(error);
			pass = false;
		}
		if (pass) {
			window.location.href = document.querySelector(
				"form[name=submit-form]"
			).action;
		}
	});
