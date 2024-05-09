$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        const searchText = $('#search-box').val();
        $ajax( {
            url: 'lausstorf?leit=' + searchText,
            type: 'GET',
            success: function(resp){
                const newHtml = resp.data.map(d => {
                    return `<div class="well job">
                                <a href="/lausstorf/${d.id}">
                                    <img class="job-image" src="#" alt="#"/>
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