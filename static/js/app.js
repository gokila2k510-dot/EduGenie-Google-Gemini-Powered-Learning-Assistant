document.addEventListener("DOMContentLoaded", () => {

    const task = document.getElementById("task");
    const level = document.getElementById("level");
    const inputText = document.getElementById("inputText");
    const inputLabel = document.getElementById("inputLabel");
    const timelineGroup = document.getElementById("timeline-group");
    const timeline = document.getElementById("timeline");

    const submitButton = document.getElementById("submitButton");
    const buttonText = document.getElementById("buttonText");
    const spinner = document.getElementById("spinner");

    const resultSection = document.getElementById("resultSection");
    const result = document.getElementById("result");
    const copyButton = document.getElementById("copyButton");


    /* ============================= */
    /* Task change                    */
    /* ============================= */

    function updateTaskUI() {

        if (task.value === "qa") {

            inputLabel.textContent = "Your question";
            inputText.placeholder = "Type your question here...";
            timelineGroup.style.display = "none";
            buttonText.textContent = "Ask EduGenie";

        } else if (task.value === "explain") {

            inputLabel.textContent = "Topic to explain";
            inputText.placeholder = "Example: What is Python?";
            timelineGroup.style.display = "none";
            buttonText.textContent = "Explain Topic";

        } else if (task.value === "quiz") {

            inputLabel.textContent = "Text for quiz";
            inputText.placeholder = "Enter the topic or text...";
            timelineGroup.style.display = "none";
            buttonText.textContent = "Generate Quiz";

        } else if (task.value === "summarize") {

            inputLabel.textContent = "Text to summarize";
            inputText.placeholder = "Paste your text here...";
            timelineGroup.style.display = "none";
            buttonText.textContent = "Summarize";

        } else if (task.value === "learn") {

            inputLabel.textContent = "Topic to learn";
            inputText.placeholder = "Example: Python Programming";
            timelineGroup.style.display = "block";
            buttonText.textContent = "Create Learning Path";
        }
    }


    task.addEventListener("change", updateTaskUI);


    /* ============================= */
    /* Submit                         */
    /* ============================= */

    submitButton.addEventListener("click", async () => {

        const text = inputText.value.trim();
        const selectedTask = task.value;
        const selectedLevel = level.value;

        if (text === "") {
            alert("Please enter something!");
            return;
        }

        buttonText.textContent = "Thinking...";
        spinner.classList.remove("hidden");
        submitButton.disabled = true;

        resultSection.classList.remove("hidden");
        result.innerHTML = "<p>Loading...</p>";


        try {

            let url = "";
            let body = {};


            /* ============================= */
            /* Q&A                            */
            /* ============================= */

            if (selectedTask === "qa") {

                url = "/api/qa";

                body = {
                    question: text,
                    level: selectedLevel
                };
            }


            /* ============================= */
            /* Explain                        */
            /* ============================= */

            else if (selectedTask === "explain") {

                url = "/api/explain";

                body = {
                    topic: text,
                    level: selectedLevel
                };
            }


            /* ============================= */
            /* Quiz                           */
            /* ============================= */

            else if (selectedTask === "quiz") {

                url = "/api/quiz";

                body = {
                    text: text,
                    level: selectedLevel
                };
            }


            /* ============================= */
            /* Summary                        */
            /* ============================= */

            else if (selectedTask === "summarize") {

                url = "/api/summary";

                body = {
                    text: text,
                    level: selectedLevel
                };
            }


            /* ============================= */
            /* Learning Path                  */
            /* ============================= */

            else if (selectedTask === "learn") {

                url = "/api/learning-path";

                body = {
                    topic: text,
                    level: selectedLevel,
                    timeline: timeline.value
                };
            }


            const response = await fetch(url, {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(body)
            });


            const data = await response.json();


            if (!response.ok) {

                throw new Error(
                    data.detail || "Server error"
                );
            }


            /* ============================= */
            /* Display result                 */
            /* ============================= */

            if (typeof data === "string") {

                result.textContent = data;

            } else if (data.answer) {

                result.textContent = data.answer;

            } else if (data.summary) {

                result.textContent = data.summary;

            } else {

                result.textContent =
                    JSON.stringify(data, null, 2);
            }


        } catch (error) {

            console.error(error);

            result.innerHTML =
                `<p>Error: ${error.message}</p>`;

        } finally {

            buttonText.textContent = "Ask EduGenie";
            spinner.classList.add("hidden");
            submitButton.disabled = false;
        }

    });


    /* ============================= */
    /* Copy result                    */
    /* ============================= */

    copyButton.addEventListener("click", async () => {

        const text = result.innerText;

        if (!text) {
            return;
        }

        try {

            await navigator.clipboard.writeText(text);

            copyButton.textContent = "Copied!";

            setTimeout(() => {
                copyButton.textContent = "Copy";
            }, 1500);

        } catch (error) {

            console.error(error);

        }

    });


    /* Initial UI */

    updateTaskUI();

});