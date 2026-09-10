# Decision Report

- generated_at: 2026-09-10T23:36:20.371538+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14191**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14191, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.92% | **+0.39%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.18% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +1.87% | **+1.87%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.47% | **+1.10%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.04% | **+0.47%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.36% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,053.34** / 初期 $100.00 (+953.34%)
- 確定: 5364件 (Win 1612 / Loss 1734 / Flat 2018) / skip 5388件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,053.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.08** / 初期 $100.00 (+108.08%)
- 確定: 2785件 (Win 767 / Loss 650 / Flat 1368) / skip 4817件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0298 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CHIP/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $208.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.93** / 初期 $100.00 (+21.93%)
- 確定: 2696件 (Win 794 / Loss 1031 / Flat 871) / pending 2件 / skip 2963件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000196 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CHIP/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.93

## 6. Latest Market Context

- 更新: 2026-09-10T23:36:09.127055+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=76696.0
- Funnel: target 1067 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +26.75% | $5,996,060.93 |
| RAY/USDT:USDT | +11.83% | $5,075,090.08 |
| BTW/USDT:USDT | +11.09% | $2,719,703.67 |
| SAGA/USDT:USDT | +9.17% | $6,080,659.10 |
| CNPY/USDT:USDT | +8.54% | $2,417,343.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAY/USDT:USDT | below_1h_threshold | +2.27% | +2.40% |
| 4/USDT:USDT | below_1h_threshold | +1.65% | +1.77% |
| NES/USDT:USDT | below_1h_threshold | +1.54% | +1.67% |
| 4STOCK/USDT:USDT | below_1h_threshold | +1.48% | +1.61% |
| VVV/USDT:USDT | below_1h_threshold | +1.29% | +1.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
