# Decision Report

- generated_at: 2026-06-27T08:28:35.729400+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7680**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7680, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.23% | **-1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.46% | **+0.07%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 2/16 | 12.5% | -2.10% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.08% | **+1.35%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.55% | **+1.24%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.19% | **+1.10%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.55% | **+1.02%** |
| MARKET_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$237.23** / 初期 $100.00 (+137.23%)
- 確定: 2205件 (Win 662 / Loss 735 / Flat 808) / skip 2036件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $237.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.76** / 初期 $100.00 (+8.76%)
- 確定: 411件 (Win 113 / Loss 102 / Flat 196) / skip 680件
- 成長率目線: 平均log +0.000204 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0724 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $108.76

## 5. Latest Market Context

- 更新: 2026-06-27T08:28:29.924903+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=60440.8
- Funnel: target 806 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +41.67% | $64,439,350.80 |
| MYX/USDT:USDT | +37.83% | $10,177,572.10 |
| PUNDIX/USDT:USDT | +19.02% | $6,197,392.08 |
| SYRUP/USDT:USDT | +16.91% | $1,680,451.44 |
| SLX/USDT:USDT | +15.05% | $10,694,482.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +3.44% | +3.58% |
| ARX/USDT:USDT | below_1h_threshold | +1.81% | +1.94% |
| MYX/USDT:USDT | below_1h_threshold | +1.52% | +1.65% |
| JTO/USDT:USDT | below_1h_threshold | +1.23% | +1.36% |
| PUNDIX/USDT:USDT | below_1h_threshold | +1.03% | +1.17% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
