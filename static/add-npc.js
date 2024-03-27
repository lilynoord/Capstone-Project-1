function update_ability_modifier(e) {
	let n = Math.floor((e.target.value - 10) / 2);
	let sign = "";
	if (n >= 0) {
		sign = "+";
	}

	e.target.nextElementSibling.innerText = sign + n;
	var skill_tag = e.target.getAttribute("data-skill");
	console.log(`input.${skill_tag}`);
	var skills = document.querySelectorAll(`input.${skill_tag}`);
	console.log(skills);
	skills.forEach((element) => {
		console.log(element);
		if (!element.nextElementSibling.lastElementChild.checked) {
			element.value = n;
		} else {
			element.value =
				n + parseInt(document.querySelector("#proficiency_bonus").value);
		}
	});
}

function toggleProficiency(e) {
	if (e.target.checked) {
		console.log(
			e.target.parentNode.previousElementSibling.value,
			document.querySelector("#proficiency_bonus").value
		);
		e.target.parentNode.previousElementSibling.value =
			parseInt(e.target.parentNode.previousElementSibling.value) +
			parseInt(document.querySelector("#proficiency_bonus").value);
	} else {
		e.target.parentNode.previousElementSibling.value = Math.floor(
			(document.querySelector(
				`input[data-skill="${e.target.parentNode.previousElementSibling.classList[1]}"]`
			).value -
				10) /
				2
		);
	}
}

function update_skills(e) {
	let skills = document.querySelectorAll("input[type=checkbox]");
	skills.forEach((skill) => {
		if (skill.checked) {
			console.log(
				skill.parentNode.previousElementSibling.value,
				document.querySelector("#proficiency_bonus").value
			);
			skill.parentNode.previousElementSibling.value =
				Math.floor(
					(document.querySelector(
						`input[data-skill="${skill.parentNode.previousElementSibling.classList[1]}"]`
					).value -
						10) /
						2
				) + parseInt(document.querySelector("#proficiency_bonus").value);
		}
	});
}

//From stack exchange: https://stackoverflow.com/questions/8641729/how-to-avoid-the-need-for-ctrl-click-in-a-multi-select-box-using-javascript
window.onmousedown = function (e) {
	var el = e.target;
	if (
		el.tagName.toLowerCase() == "option" &&
		el.parentNode.hasAttribute("multiple")
	) {
		e.preventDefault();

		// toggle selection
		if (el.hasAttribute("selected")) el.removeAttribute("selected");
		else el.setAttribute("selected", "");

		// hack to correct buggy behavior
		var select = el.parentNode.cloneNode(true);
		el.parentNode.parentNode.replaceChild(select, el.parentNode);
	}
};
