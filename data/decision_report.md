# Decision Report

- generated_at: 2026-07-22T11:31:27.263138+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9275**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=9275, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.81% | **+1.81%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.21% | **+1.02%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.93% | **+0.56%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.59% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$429.93** / 初期 $100.00 (+329.93%)
- 確定: 3272件 (Win 1032 / Loss 1050 / Flat 1190) / skip 2564件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $429.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1526件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1541 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.62** / 初期 $100.00 (+2.62%)
- 確定: 413件 (Win 142 / Loss 170 / Flat 101) / pending 6件 / skip 332件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000374 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BNCSTOCK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $102.62

## 6. Latest Market Context

- 更新: 2026-07-22T11:31:15.433814+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=65999.9
- Funnel: target 888 → liquid 177 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +51.94% | $3,356,330.42 |
| RE/USDT:USDT | +27.81% | $8,991,632.26 |
| SMCISTOCK/USDT:USDT | +18.39% | $4,489,757.44 |
| UB/USDT:USDT | +17.75% | $1,531,079.40 |
| BNCSTOCK/USDT:USDT | +14.21% | $2,932,591.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.21% | +3.24% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +3.12% | +3.15% |
| BOTSTOCK/USDT:USDT | below_1h_threshold | +2.62% | +2.64% |
| DODO/USDT:USDT | below_1h_threshold | +2.58% | +2.60% |
| BANK/USDT:USDT | below_1h_threshold | +2.52% | +2.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
