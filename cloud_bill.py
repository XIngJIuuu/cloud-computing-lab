"""云服务器（ECS）费用估算小工具。"""

# 按小时计费的规格单价（元/小时），数据仅作演示
ECS_PRICES = {
    "1c2g": 0.09,
    "2c4g": 0.18,
    "4c8g": 0.36,
}

DISK_PRICE = 0.0004  # 云盘 元/GB/小时
DISK_GB = 40  # 默认系统盘大小
HOURS_PER_MONTH = 730  # 平均每月小时数


def monthly_cost(spec: str) -> float:
    compute = ECS_PRICES[spec] * HOURS_PER_MONTH
    disk = DISK_PRICE * DISK_GB * HOURS_PER_MONTH
    return round(compute + disk, 2)


def main() -> None:
    print(f"系统盘按 {DISK_GB}GB 估算")
    for spec in ECS_PRICES:
        print(f"{spec}\t包月 {monthly_cost(spec):.2f} 元")


if __name__ == "__main__":
    main()