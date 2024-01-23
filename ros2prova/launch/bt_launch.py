from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='alarm_battery_low_skill',
            executable='alarm_battery_low_skill',
            output='screen',
            arguments=['--ros-args', '--log-level', 'debug']
        ),
        Node(
            package='battery_drainer_skill',
            executable='battery_drainer_skill',
            output='screen',
            arguments=['--ros-args', '--log-level', 'debug']
        ),
        Node(
            package='battery_level_skill',
            executable='battery_level_skill',
            arguments=['--ros-args', '--log-level', 'debug']
        ),
        Node(
            package='battery_drainer_component',
            executable='battery_drainer_component',
            arguments=['--ros-args', '--log-level', 'debug']
        ),
        Node(
            package='bt_executable',
            executable='bt_executable',
            arguments=[ './BT/simple_bt.xml','--ros-args', '--log-level', 'debug']
        )
    ])

