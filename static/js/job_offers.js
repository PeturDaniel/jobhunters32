$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        let searchText = $('#search-box').val();
        if (searchText.trim() !== '') {
            $.ajax( {
                url: '?leit=' + searchText.trim(),
                type: 'GET',
                success: function(resp){
                    let newHtml = resp.data.map(d => {
                        return `<div class="well_job">
                                    <a href="/lausstorf/${d.id}" class="card-link">
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
        }
    });
});

$(document).ready(function() {
    $('#companySelect').on('change', function() {
        var companyName = $(this).val(); // Get the selected company name
        if (companyName) {
            $.ajax({
                url: '/getCompanyData?company=' + encodeURIComponent(companyName),
                type: 'GET',
                success: function(resp) {
                    let newHtml = resp.data.map(d => {
                        return `<div class="company-info">
                                    <img src="${d.logo}" alt="Logo of ${d.name}" class="company-logo">
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                </div>`;
                    });
                    $('#companyData').html(newHtml.join('')); // Assuming companyData is the ID of the container for company info
                },
                error: function(xhr, status, error) {
                    console.error("Error fetching data: ", error);
                    // Implement error handling, e.g., show a notification or message to the user
                }
            });
        }
    });
});