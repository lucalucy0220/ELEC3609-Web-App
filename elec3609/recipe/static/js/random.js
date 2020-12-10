// random recipe api taking from https://www.themealdb.com/

const meal_container = document.getElementById("meal");
const shuffle_btn = document.getElementById("shuffle");
const spinner = document.getElementById("spinner");

shuffle_btn.addEventListener("click", () => {
  meal_container.style.display="none";
  spinner.removeAttribute('hidden');
  fetch("https://www.themealdb.com/api/json/v1/1/random.php")
    .then((res) => res.json())
    .then((res) => {
      createMeal(res.meals[0]);
      meal_container.style.display="block";
      spinner.setAttribute('hidden', '');
    })
    .catch((e) => {
      console.warn(e);
    });
});

$(document).ready(() => {
  meal_container.style.display="none";
  spinner.removeAttribute('hidden');
  fetch("https://www.themealdb.com/api/json/v1/1/random.php")
    .then((res) => res.json())
    .then((res) => {
      createMeal(res.meals[0]);
      meal_container.style.display="block";

      spinner.setAttribute('hidden', '');
    });
});

const createMeal = (meal) => {
  const ingredients = [];
  for (let i = 1; i <= 20; i++) {
    if (meal[`strIngredient${i}`]) {
      ingredients.push(
        `${meal[`strIngredient${i}`]} - ${meal[`strMeasure${i}`]}`
      );
    } else {
      break;
    }
  }

  const newInnerHTML = `
  <div class="container">
    <div class="row">
      <h1>${meal.strMeal}</h1>
    </div>
		<div class="row" id="main-recipe-section">
			<div class="col-5">
        <img src="${meal.strMealThumb}" alt="Meal Image">
        <hr>
				${
          meal.strCategory
            ? `<p><strong>Category:</strong> ${meal.strCategory}</p>`
            : ""
        }
				${meal.strArea ? `<p><strong>Area:</strong> ${meal.strArea}</p>` : ""}
        <hr>
				<h5>Ingredients:</h5>
				<ul>
					${ingredients.map((ingredient) => `<li>${ingredient}</li>`).join("")}
				</ul>
			</div>
      <div class="col-7">
        <h5>Instructions:</h5>
        <div>
        <p>${meal.strInstructions}</p>
        ${meal.strYoutube ? `
          <hr>
          <h5>Video Recipe:</h5>
          <div class="videoWrapper">
            <iframe width="420" height="315"
            src="https://www.youtube.com/embed/${meal.strYoutube.slice(-11)}">
            </iframe>
          </div>
        ` : ''}
        </div>
			</div>
    </div>
  </div>
	`;

  meal_container.innerHTML = newInnerHTML;
};


