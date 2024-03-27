// TODO: when hp is modified, send fetch request to server to update.
// TODO: expand monster row when clicked on to show actions and spells
// TODO: display monster details when name is clicked.
// TODO: when action or spell is clicked on, display details.
// TODO: highlight next row when end-turn is clicked

function show_action(e) {
	e.target.nextElementSibling.open = true;
}
