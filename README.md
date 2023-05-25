# Learning basics of data analytics and entering to this world.

I am learning finance under master **Ayoub Goudarzi** and he told me to start with some small data.

So, what I had inside my mind was to work on **tmctse** but most of people use it and it has many pre created stuff. I changed my mind and worked on internet usage with **VPN**.

## VPN

I created a simple v2ray vpn with x-ui just for my project and give people configs to connect and use that I be able to make some analytics with usage.

## Project

Inside project you can see notebooks and a script.

### Notebooks

These notebooks are each for one perpose.

#### `Total` notebook

The `total` notebook is where it collect all data and give you **treemap**, **bar chart** and **pie chart**.

|                 Treemap                 |               Bar               |               Pie               |
| :-------------------------------------: | :-----------------------------: | :-----------------------------: |
| ![Treemap](./assets/total/treemap.jpeg) | ![Bar](./assets/total/bar.jpeg) | ![Pie](./assets/total/pie.jpeg) |

#### `User` notebook

In `user` notebook we analyze single user usage. We have **line chart**,and **pie chart** here.

|               Bar               |              Pie               |
| :-----------------------------: | :----------------------------: |
| ![Bar](./assets/user/line.jpeg) | ![Pie](./assets/user/pie.jpeg) |

#### `Collect` notebook

With with notebook we collect usage and save in database. But we created that notebook in a script that it is placed in a server that runs every 1 hour with crontab.
