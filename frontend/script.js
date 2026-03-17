const API_URL = "http://localhost:8000";

async function fetchMovies() {
    const res = await fetch(`${API_URL}/movies`);
    const movies = await res.json();
    const container = document.getElementById("movies");
    container.innerHTML = "";
    movies.forEach((movie, index) => {
        const div = document.createElement("div");
        div.className = "movie-card";
        div.innerHTML = `
            <h3>${movie.title} (${movie.year})</h3>
            <img src="${movie.image_url}" alt="${movie.title}">
            <p><strong>Gênero:</strong> ${movie.genre}</p>
            <p>${movie.description || ""}</p>
            <button onclick="deleteMovie(${index})">Deletar</button>
        `;
        container.appendChild(div);
    });
}

async function addMovie() {
    const movie = {
        title: document.getElementById("title").value,
        year: parseInt(document.getElementById("year").value),
        genre: document.getElementById("genre").value,
        image_url: document.getElementById("image_url").value,
        description: document.getElementById("description").value
    };
    await fetch(`${API_URL}/movies`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(movie)
    });
    fetchMovies();
}

async function deleteMovie(id) {
    await fetch(`${API_URL}/movies/${id}`, { method: "DELETE" });
    fetchMovies();
}

async function getRecommendation() {
    const res = await fetch(`${API_URL}/recommend`);
    const movie = await res.json();
    const container = document.getElementById("recommendation");
    container.innerHTML = `
        <h3>${movie.title} (${movie.year})</h3>
        <img src="${movie.image_url}" alt="${movie.title}" width="200">
        <p><strong>Gênero:</strong> ${movie.genre}</p>
        <p>${movie.description || ""}</p>
    `;
}

fetchMovies();
