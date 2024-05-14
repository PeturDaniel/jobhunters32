const jobs = document.getElementsByClassName("job_offers")

const doSearchJobs = () => {
    const jobs = document.querySelectorAll(".well_job");
    const query = document.getElementById("search-box").value;

    jobs.forEach((job) => {
        job_title = job.innerText.trim().split('\n')
        if (job_title[0].toLowerCase().includes(query.trim().toLowerCase())) {
            job.classList.remove("hidden");
        }
        else {
            job.classList.add("hidden");
        }
    });
};


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