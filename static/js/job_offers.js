$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        let searchText = $('#search-box').val();
        $.ajax( {
            url: '?leit=' + searchText,
            type: 'GET',
            success: function(resp){
                let newHtml = resp.data.map(d => {
                    return `<div class="well_job">
                                <a href="/lausstorf/${d.id}">
                                    <img class="employer-profile-photo" src="${d.employer_photo}" alt="#"/>
                                    <h4 class="job-title">${d.title}</h4>
                                    <p>Umsóknarfrestur: ${d.due_date}</p>
                                </a>
                            </div>`
                    });
                    $('.job_offers').html(newHtml.join(''));
                    $('#search-box').val('');
                },
            error: function (xhr, status, error) {
            //finna betri leið, show toastr?
            console.error(error);
            }
        });
    });
});