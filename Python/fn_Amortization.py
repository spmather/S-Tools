#!/bin/python3

# spmather
# 2025-11-23
# Updated 2025-12-23

def amortizationmonthly(principal,rate,periods):
    """Amortization for monthly payment is A = P ( (r(1+r)^n) / ((1+r)^n - 1) )"""
    # solve for A
    rate_p_1      = rate + 1                   # (1+r)
    rate_x_period = rate_p_1 ** periods        # (1+r)^n
    rate_t_rp     = rate * rate_x_period       # (r(1+r)^n)
    rp_m_1        = rate_x_period - 1          # ((1+r)^n - 1)
    divisionpart  = rate_t_rp / rp_m_1         # (r(1+r)^n) / ((1+r)^n - 1)
    monthly       = principal * divisionpart   # P ( (r(1+r)^n) / ((1+r)^n - 1) )
    print(f"Ones monthly payment on a loan of {principal} is: ")
    return monthly

# fin