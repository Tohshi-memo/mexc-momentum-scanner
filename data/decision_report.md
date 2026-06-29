# Decision Report

- generated_at: 2026-06-29T00:33:13.009605+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7779**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.09% / filled 20/20。**
- 全期間 MARKET基準: n=7779, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+3.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.09% | **+3.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.09% | **+3.09%** |
| ASK | 20/20 | 100.0% | +3.07% | **+3.07%** |
| LIMIT_BB3S | 7/15 | 46.7% | +2.69% | **+1.25%** |
| LIMIT_1PCT | 14/20 | 70.0% | +1.71% | **+1.19%** |
| LIMIT_2PCT | 11/20 | 55.0% | +2.07% | **+1.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.46% | **+0.26%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.28% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$258.80** / 初期 $100.00 (+158.80%)
- 確定: 2283件 (Win 694 / Loss 762 / Flat 827) / skip 2057件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: POWR/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.50% 残高後 $258.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 735件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0219 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T00:33:05.018879+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.82% price=59061.9
- Funnel: target 805 → liquid 124 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NES/USDT:USDT | +13.72% | $2,898,126.53 |
| POWR/USDT:USDT | +11.14% | $6,610,202.67 |
| BAS/USDT:USDT | +10.30% | $5,080,090.43 |
| G/USDT:USDT | +9.85% | $1,140,348.61 |
| SYN/USDT:USDT | +9.68% | $8,252,192.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APDSTOCK/USDT:USDT | below_1h_threshold | +2.14% | +2.96% |
| BAS/USDT:USDT | below_1h_threshold | +1.52% | +2.34% |
| BSB/USDT:USDT | below_1h_threshold | +1.44% | +2.26% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +0.87% | +1.69% |
| HEI/USDT:USDT | below_1h_threshold | +0.81% | +1.63% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
