//Search bar event listener
document.getElementById('search-box').addEventListener('input', function () {
    doSearchJobs()
})

//Dropdown filters event listeners
document.getElementById('unique-employers').addEventListener('change', function () {
    filterEmployer()
})
document.getElementById('unique-categories').addEventListener('change', function () {
    filterCategory()
})

//Order buttons event listeners
document.getElementById('order-publish-date').addEventListener('click', function () {
    updateURL('publish_date');
    orderJobs('publish_date');
})
document.getElementById('order-due-date').addEventListener('click', function () {
    updateURL('due_date');
    orderJobs('due_date');
})

//Checkbox event listener
document.getElementById('checkbox').addEventListener('change', function () {
    filterApplied()
})

const doSearchJobs = () => {
    const jobs = document.querySelectorAll(".well-job");
    const query = document.getElementById("search-box").value;

    jobs.forEach((job) => {
        let job_title = job.innerText.trim().split('\n')
        if (job_title[0].toLowerCase().includes(query.trim().toLowerCase())) {
            job.classList.remove("hidden");
        }
        else {
            job.classList.add("hidden");
        }
    });
};

const filterEmployer = () => {
    const company = document.getElementById('unique-employers').value;
    const jobs = document.querySelectorAll(".well-job");

    jobs.forEach((job) => {
        let job_title = job.innerText.trim().split('\n')
        if (job_title[2].includes(company)) {
            job.classList.remove("hidden")
        }
        else {
            job.classList.add("hidden");
        }
    });
}

const filterCategory = () => {
    const category = document.getElementById('unique-categories').value;
    const jobs = document.querySelectorAll(".well-job");

    jobs.forEach((job) => {
        let job_category = job.innerText.trim().split('\n')
        if (job_category[1].includes(category)) {
            job.classList.remove("hidden")
        }
        else {
            job.classList.add("hidden");
        }
    });
}

const orderJobs = (order_by) => {
    fetch('/lausstorf/?order_by=' + encodeURIComponent(order_by))
        .then(response =>
            response.text()
        )
        .then(data => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(data, 'text/html');
            const ordered_job_offers = doc.querySelector('#job-offers-for');
            const current_job_offers = document.querySelector('#job-offers-for');
            if (current_job_offers.innerHTML && ordered_job_offers.innerHTML) {
                current_job_offers.innerHTML = ordered_job_offers.innerHTML;
            }
        })

}

function updateURL(order_by) {
    const url = new URL(window.location.href);
    url.searchParams.set('order_by', order_by);
    window.history.pushState({}, '', url);
}

const filterApplied = () => {
    const checkbox = document.getElementById("checkbox")
    const application_ids = document.querySelectorAll(".application")
    const applied_jobs = application_ids[0].innerText.slice(2, -1).split(", ")
    const jobs = document.querySelectorAll(".well-job");

    jobs.forEach((job) => {
        if (checkbox.checked === true && applied_jobs.indexOf(job.id) !== -1) {
            job.classList.remove("hidden")
        }
        else if (checkbox.checked === false) {
            job.classList.remove("hidden")
        }
        else {
            job.classList.add("hidden");
        }
    });
}
