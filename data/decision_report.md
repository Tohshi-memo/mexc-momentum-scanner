# Decision Report

- generated_at: 2026-06-17T13:16:00.376403+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6940**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.55% / filled 20/20。**
- 全期間 MARKET基準: n=6940, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |
| ASK | 20/20 | 100.0% | +1.53% | **+1.53%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.94% | **+0.66%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.54% | **+0.41%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.63% | **+0.32%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_BB3S_LONG | 5/10 | 50.0% | +0.45% | **+0.22%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$196.04** / 初期 $100.00 (+96.04%)
- 確定: 1812件 (Win 493 / Loss 572 / Flat 747) / skip 1689件
- 成長率目線: 平均log +0.000371 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $196.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.54** / 初期 $100.00 (+1.54%)
- 確定: 213件 (Win 52 / Loss 49 / Flat 112) / skip 138件
- 成長率目線: 平均log +0.000072 / 幾何平均 +0.007% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0784 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ID/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $101.54

## 5. Latest Market Context

- 更新: 2026-06-17T13:15:55.661385+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=65012.6
- Funnel: target 790 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.5 >= 65=1, 4h RSI 76.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +68.76% | $1,886,233.37 |
| ESPORTS/USDT:USDT | +56.37% | $11,137,061.53 |
| XPL/USDT:USDT | +26.54% | $8,684,571.65 |
| BP/USDT:USDT | +26.22% | $1,075,427.33 |
| HIGH/USDT:USDT | +22.81% | $3,635,010.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COAI/USDT:USDT | below_1h_threshold | +3.61% | +3.60% |
| BLESS/USDT:USDT | below_1h_threshold | +1.96% | +1.95% |
| LIT/USDT:USDT | below_1h_threshold | +1.31% | +1.30% |
| BP/USDT:USDT | below_1h_threshold | +1.14% | +1.13% |
| STG/USDT:USDT | below_1h_threshold | +1.14% | +1.13% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
