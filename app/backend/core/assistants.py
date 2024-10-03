
def assistant():

    if 'client' not in st.session_state:
        # Initialize the client
        st.session_state.client = openai.OpenAI()

        st.session_state.file = st.session_state.client.files.create(
            file=open("../../../data/essays/wilberforce-slavery.txt", "rb"),
            purpose='assistants'
        )

        # Step 1: Create an Assistant
        st.session_state.assistant = st.session_state.client.beta.assistants.create(
            name="Knowledge QNA Assistant",
            instructions="You are a knowledge based assistant that support chatbot. Use your knowledge base to best respond to user queries.",
            # model="gpt-4-1106-preview",
            model="gpt-3.5-turbo-0613",
            file_ids=[st.session_state.file.id],
            tools=[{"type": "retrieval"}]
        )

        # Step 2: Create a Thread
        st.session_state.thread = st.session_state.client.beta.threads.create()

    user_query = st.text_input("Please Enter your query:", "Why did Wilberforce feel Great Britain had reason to be seriously uneasy that God might bring judgment on the nation? What did he do to help end slavery?")

    if st.button('Submit'):
        # Step 3: Add a Message to a Thread
        message = st.session_state.client.beta.threads.messages.create(
            thread_id=st.session_state.thread.id,
            role="user",
            content=user_query
        )

        # Step 4: Run the Assistant
        run = st.session_state.client.beta.threads.runs.create(
            thread_id=st.session_state.thread.id,
            assistant_id=st.session_state.assistant.id,
            instructions="Please address the user as Peter"
        )

        while True:
            # Wait for 5 seconds
            time.sleep(5)

            # Retrieve the run status
            run_status = st.session_state.client.beta.threads.runs.retrieve(
                thread_id=st.session_state.thread.id,
                run_id=run.id
            )

            # If run is completed, get messages
            if run_status.status == 'completed':
                messages = st.session_state.client.beta.threads.messages.list(
                    thread_id=st.session_state.thread.id
                )

                # Loop through messages and print content based on role
                for msg in messages.data:
                    role = msg.role
                    content = msg.content[0].text.value
                    st.write(f"{role.capitalize()}: {content}")
                break
            else:
                st.write("Waiting for the Assistant to process...")
                time.sleep(5)


    else:
        st.write("Please enter a query") if not st.session_state.client.beta.assistants.retrieve(
            assistant_id=st.session_state.assistant.id
        ) else st.write("Please wait for the Assistant to process...")

    st.write("---")
    st.write("")

