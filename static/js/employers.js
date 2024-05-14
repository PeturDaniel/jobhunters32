const workplaces = document.getElementsByClassName("employers")


const doSearch = () => {
    const workplaces = document.querySelectorAll(".well_job");
    const query = document.getElementById("search-box").value;

    workplaces.forEach((workplace) => {
        employer_title = workplace.innerText.trim().split('\n')
        if (employer_title[0].toLowerCase().includes(query.trim().toLowerCase())) {
            workplace.classList.remove("hidden");
        }
        else {
            workplace.classList.add("hidden");
        }
    });
};




//$(document).ready(function(){
//    $('#search-btn').on('click', function(e) {
//        e.preventDefault();
//        let searchText = $('#search-box').val();
//        if (searchText.trim() !== '')  {
//            $.ajax( {
//                url: '?leit=' + searchText.trim(),
//                type: 'GET',
//                success: function(resp){
//                    let newHtml = resp.data.map(d => {
//                        return `<div class="well_job">
//                                    <a href="/vinnustadir/${d.id}" class="card-link">
//                                        <img class="employer-profile-photo" src="${d.profile_photo}" alt="#"/>
//                                        <h4 class="employer-title">${d.name}</h4>
//                                        <p>${d.address}</p>
//                                    </a>
//                                </div>`
//                        });
//                        $('.employers').html(newHtml.join(''));
//                        $('#search-box').val('');
//                    },
//                error: function (xhr, status, error) {
//                //finna betri leið, show toastr?
//                console.error(error);
//                }
//            });
//        }
//        $('#search-box').val('');
//    });
//});