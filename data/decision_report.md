# Decision Report

- generated_at: 2026-07-17T08:46:15.805174+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8834**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.83% / filled 20/20。**
- 全期間 MARKET基準: n=8834, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_5PCT | 6/20 | 30.0% | +4.02% | **+1.21%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.33% | **+1.13%** |
| LIMIT_BB3S | 4/15 | 26.7% | +2.94% | **+0.78%** |
| LIMIT_4PCT | 9/20 | 45.0% | +1.48% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.55% | **+0.64%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.93% | **+0.33%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.24% | **+0.05%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | -0.29% | **-0.23%** |

## 2. $100 Live Portfolio

- 残高: **$110.71** / 初期 $100.00 (+10.71%)
- 確定トレード: 110件 (TP 41 / SL 65 / EXP 4)
- 最新: AERO/USDT:USDT SL_HIT PnL -3.73% 残高後 $110.71
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.42** / 初期 $100.00 (+242.42%)
- 確定: 2949件 (Win 917 / Loss 947 / Flat 1085) / skip 2446件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LRC/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $342.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.95** / 初期 $100.00 (+7.95%)
- 確定: 796件 (Win 184 / Loss 171 / Flat 441) / skip 1449件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0211 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LRC/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.95

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定: 101件 (Win 32 / Loss 65 / Flat 4) / pending 4件 / skip 200件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000229 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LRC/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.69

## 6. Latest Market Context

- 更新: 2026-07-17T08:46:08.539750+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=62790.5
- Funnel: target 885 → liquid 184 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.9 >= 65=1, 4h RSI 74.2 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUMIA/USDT:USDT | +32.89% | $2,233,327.20 |
| SOXS/USDT:USDT | +16.20% | $1,800,763.95 |
| AKE/USDT:USDT | +15.56% | $42,433,612.93 |
| LRC/USDT:USDT | +15.32% | $1,394,278.12 |
| KAITO/USDT:USDT | +14.64% | $4,160,871.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +3.08% | +3.09% |
| VELVET/USDT:USDT | below_1h_threshold | +2.58% | +2.59% |
| SOXS/USDT:USDT | below_1h_threshold | +2.26% | +2.26% |
| MYX/USDT:USDT | below_1h_threshold | +2.14% | +2.14% |
| POL/USDT:USDT | below_1h_threshold | +2.09% | +2.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
