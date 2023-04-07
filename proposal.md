# final project
 This is the Final Project of oim3640 for amanda
1. The Big Idea: What is the main idea of your project? What topics will you explore and what will you accomplish? Describe your minimum viable product (MVP) and your stretch goal.

    The primary objective of this project is to provide a user-friendly tool that investors can use to monitor their stock portfolio on a daily basis. Currently, existing software such as Bloomberg provides a complex interface that requires high levels of expertise to navigate effectively. The proposed project seeks to simplify this process by enabling users to input multiple stock tickers and obtain an overall return, individual stock trends, prices, and volatility, as well as related news that may impact their investments.

    The minimum viable product (MVP) will consist of a web page that allows users to input stock tickers and an output page that presents customers with an overview of their overall return and risk. This simplified interface will enable users to quickly and easily understand the performance of their investment portfolio.

    
    The stretch goal of this project includes the development of an error page that handles incorrect stock ticker inputs, a page that provides users with current news related to a particular stock, a page that returns individual stock performance if the user wants to search for a specific stock, and an overall historical tracking chart of the portfolio's performance over the past 15 days. These additional features will provide users with a more comprehensive view of their investments and enable them to make informed decisions regarding their portfolios.

    Overall, the project aims to provide a simplified and accessible interface for investors to monitor their stock portfolios, which will enable them to make informed decisions regarding their investments. The proposed MVP and stretch goals will ensure that the tool meets the needs of a wide range of users and provides a comprehensive view of their investments.


2. Learning Objectives: Since this is a team project, you may want to articulate both shared and individual learning goals.

    My primary learning objective is to leverage Python as a robust tool to enhance my existing knowledge and skill set, particularly in the context of my interdisciplinary project. The project, which will be of immense help in my pursuit of a master's degree, will involve integrating my finance domain knowledge with the Python skills I have gained so far.

    I aim to utilize my knowledge of APIs, Flask, sentiment analysis, and Python's data visualization capabilities to create a comprehensive and cohesive solution that combines multiple disciplines. This interdisciplinary approach would not only strengthen my Python skills but also allow me to apply them in real-world scenarios.

    Moreover, I am keen to explore the integration of these diverse concepts and their applications in finance, thereby expanding my overall understanding of the subject. By leveraging the skills acquired in this class, I hope to develop a practical and efficient solution that will be instrumental in my future academic pursuits and professional career.


3. Implementation Plan: This part may be somewhat ambiguous initially. You might have identified a library or a framework that you believe would be helpful for your project at this early stage. If you're uncertain about executing your project plan, provide a rough plan describing how you'll investigate this information further.

    My detailed implementation plan involves several steps to ensure the successful completion of the project. Firstly, I plan to create a basic HTML template, similar to the one used in Assignment 3, to establish the foundation of the project. Alongside this, I will also develop a Flask app file and some auxiliary Python files to perform the necessary calculations and fetch data from various sources.

    Python helper files will be utilized to calculate stock returns and analyze related news. To calculate the stock returns, I will utilize APIs to capture the stock ticker symbols inputted by the user and obtain the individual stock returns. Subsequently, I will use finance functions to calculate the overall weighted return of the investment portfolio.

    For the news helper Python file, I plan to use a news API to gather relevant news articles related to the inputted stock ticker symbols. Additionally, I will employ sentiment analysis techniques to analyze the news articles' sentiment and determine whether the current news signals a good or bad time for investing in the respective stocks.

    Lastly, I will research and identify suitable Python tools that enable me to track and visualize the investment portfolio's performance. The tool will be used to draw graphs to provide users with a clear representatio

    Tools I'm gonna use:
    Flask
    Api Keys
    json



4. Project Schedule: You have 6 weeks (roughly) to finish the project. Draft a general timeline for your project. Depending on your project, you might be able to provide a detailed schedule or only an overview. Preparation of a longer project is also accompanied by present uncertainty, and this schedule will likely require revisions as the project progresses.

    week ends on 4/9： write the project proposal; design the initial html, and app.py
    week ends on 4/16: write the initial calculating return helper function, make sure the input html. works well with the output html. finishe the news part
    week ends on 4/23: finish the graphing part, individual stock return part, and other designs. finish most of the project
    week ends on 4/30: formatting the web into more presentable version, finish writing the reflction and web page describing the project. submit the project at 4/29,

5. Collaboration Plan: How will you collaborate with your teammates on this project? Will you divide tasks and then incorporate them separately? Will you undertake a comprehensive pair program? Explain how you'll ensure effective team collaboration. This may also entail information on any software development methodologies you anticipate using (e.g. agile development). Be sure to clarify why you've picked this specific organizational structure.

    I'm working this project on myself so I'll try to monitor myself and use a task tracker. 

6. Risks and Limitations: What do you believe is the most significant threat to this project's success?

    There are several risks related with this project. The first risk pertains to the utilization of open API keys for accessing data from various sources such as Yahoo Finance and Wall Street Journal

    Another significant risk relates to the potential limitations posed by my current coding skills, which may pose challenges in effectively executing the project. To mitigate this risk, I plan to visit  office hours to seek guidance and support on any issues I encounter.
    
    Furthermore, there is a risk associated with the task of plotting the tracking graph, which may require specialized skills and knowledge. As I currently lack experience in this area, I plan to undertake additional research and training to ensure that I acquire the necessary skills to successfully complete this task.

7. Additional Course Content: What topics do you believe will be beneficial to your project?
    Connect api gathered data with graphing tools 