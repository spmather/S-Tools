#!/bin/python3

# spmather
# 2025-11-23
# Updated 2025-12-23


def compoundinterest(principal,rate,periods,years):
    """Compound interest is A = P(1+(r/n))^nt)"""
    # Solve for A.  Vars P,r,n,t 
    rate_d_period  = rate / periods                   # (r/n)
    rate_d_period  = rate_d_period + 1                # 1+(r/n)
    years_t_period = periods * years                  # nt
    growth         = rate_d_period ** years_t_period  # 1+(r/n))^nt
    amount         = principal * growth               # P(1+(r/n))^nt)
    print(f"Ones compounded interest on {principal} is: ")
    return amount

# fin