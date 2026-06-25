# Decision Report

- generated_at: 2026-06-25T09:48:27.977918+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7540**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7540, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.42% | **-0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/16 | 25.0% | +1.03% | **+0.26%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| ASK | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.95% | **+2.21%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.71% | **+1.76%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.14% | **+1.61%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.33% | **+1.50%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.89% | **+1.42%** |

## 2. $100 Live Portfolio

- 残高: **$102.94** / 初期 $100.00 (+2.94%)
- 確定トレード: 39件 (TP 15 / SL 24 / EXP 0)
- 最新: MUSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.24** / 初期 $100.00 (+119.24%)
- 確定: 2132件 (Win 629 / Loss 715 / Flat 788) / skip 1969件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $219.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.38** / 初期 $100.00 (+6.38%)
- 確定: 352件 (Win 98 / Loss 96 / Flat 158) / skip 599件
- 成長率目線: 平均log +0.000176 / 幾何平均 +0.018% per trade / maxDD +3.03%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_robust_growth_score) / robust_score +0.0578 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $106.38

## 5. Latest Market Context

- 更新: 2026-06-25T09:48:21.651203+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=61735.6
- Funnel: target 807 → liquid 162 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.6 >= 65=1, 4h RSI 72.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +30.49% | $17,087,886.91 |
| BAS/USDT:USDT | +22.66% | $8,949,422.56 |
| RESOLV/USDT:USDT | +19.79% | $3,178,723.08 |
| MUSTOCK/USDT:USDT | +17.32% | $125,902,068.00 |
| KORU/USDT:USDT | +16.87% | $5,557,246.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +2.60% | +2.52% |
| AERO/USDT:USDT | below_1h_threshold | +2.45% | +2.37% |
| APE/USDT:USDT | below_1h_threshold | +1.78% | +1.70% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.19% | +1.11% |
| AAVE/USDT:USDT | below_1h_threshold | +1.10% | +1.02% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
