# Decision Report

- generated_at: 2026-06-15T14:31:05.391498+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6786**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=6786, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| ASK | 20/20 | 100.0% | +1.43% | **+1.43%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.56% | **+1.41%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.62% | **+1.21%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.02% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -0.10% | **-0.04%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.14% | **-0.07%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | -0.32% | **-0.22%** |

## 2. $100 Live Portfolio

- 残高: **$104.05** / 初期 $100.00 (+4.05%)
- 確定トレード: 7件 (TP 5 / SL 2 / EXP 0)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$172.74** / 初期 $100.00 (+72.74%)
- 確定: 1659件 (Win 431 / Loss 516 / Flat 712) / skip 1688件
- 成長率目線: 平均log +0.000329 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: USELESS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $172.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.16** / 初期 $100.00 (-1.84%)
- 確定: 147件 (Win 28 / Loss 28 / Flat 91) / skip 50件
- 成長率目線: 平均log -0.000126 / 幾何平均 -0.013% per trade / maxDD +2.48%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0154 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $98.16

## 5. Latest Market Context

- 更新: 2026-06-15T14:31:00.489643+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=66467.7
- Funnel: target 772 → liquid 154 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.0 >= 65=1, 4h RSI 86.6 >= 65=1, 4h RSI 78.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +87.37% | $37,326,146.27 |
| ASTEROID/USDT:USDT | +65.38% | $5,687,493.18 |
| CLO/USDT:USDT | +38.86% | $2,314,788.50 |
| JTO/USDT:USDT | +37.89% | $2,925,182.74 |
| BSB/USDT:USDT | +32.84% | $9,691,772.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EIGEN/USDT:USDT | below_1h_threshold | +3.28% | +3.20% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.77% | +2.69% |
| INJ/USDT:USDT | below_1h_threshold | +2.62% | +2.54% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.15% | +2.07% |
| FHE/USDT:USDT | below_1h_threshold | +2.09% | +2.00% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
