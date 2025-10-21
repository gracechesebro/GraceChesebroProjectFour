import dearpygui.dearpygui as dpg
import comp151Colors

my_file = open("ProjectFour.txt", "r")
lines = my_file.readlines()

initial_states = ["Oklahoma", "Georgia", "Texas", "Ohio", "Pennsylvania"]
state_data = []
# Pulling out data
for line in lines:
    parts = line.strip().split(";")
    state_name = parts[1]
    if state_name in initial_states:
        income = int(parts[4].replace(";", ""))
        price = int(parts[5].replace(";", ""))
        state_data.append([state_name, income, price])

# drawing
dpg.create_context()
dpg.create_viewport(title="5 States Housing Affordability Bar Graph",
                    width = 800, height=900)

with dpg.window(label="Housing Affordability Bar Graph", width=800, height=900):
    with dpg.drawlist(width=750, height=850):
        # X and Y axis
        dpg.draw_line((50, 50), (50, 800), color=comp151Colors.WHITE,
                      thickness=2)
        dpg.draw_line((50, 50), (700, 50), color=comp151Colors.WHITE,
                      thickness=2)
        #labels for every 100k
        for i in range(1,9):
            y = i*100+50
            dpg.draw_text((10, y), f"${i*100}k", size=15,
                          color=comp151Colors.WHITE)
        #bars
        x=100
        bar_width=50
        gap=130

        for state in state_data:
            name = state[0]
            income = state[1]
            price = state[2]
            #had to flip bars to match dpg coordinate plane
            chart_bottom = 800
            base_line = 50
            height = price // 1000
            top_y = chart_bottom - height
            #color
            ratio = price / income
            if ratio <= 3:
                color = comp151Colors.BLUE
            elif ratio <= 4:
                color = comp151Colors.YELLOW
            else:
                color = comp151Colors.RED
            #draw bar
            dpg.draw_rectangle((x, top_y), (x + bar_width, chart_bottom), color=comp151Colors.WHITE, fill=color)
            #state name
            dpg.draw_text((x, 30), name, size=15, color=comp151Colors.WHITE)
            x+= gap
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
