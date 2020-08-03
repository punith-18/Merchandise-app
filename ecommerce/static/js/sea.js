
const searchIcon = document.getElementById("search-icon");
const seacrhbox = document.getElementById("searchbox");

searchIcon.addEventListener('click', function(){
    if(searchbox.style.display == 'block'){
        searchbox.style.display = 'none';
        searchbox.style.pointerEvents = 'none';
    } else {
        searchbox.style.display = 'block';
        searchbox.style.pointerEvents = 'auto';
    }
})