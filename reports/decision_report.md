# Decision Report

- generated_at: 2026-05-29T15:44:00.415090+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5055**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5055, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.19% | **+1.02%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.07% | **+0.96%** |
| ASK | 20/20 | 100.0% | +0.90% | **+0.90%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_BB3S | 7/12 | 58.3% | +1.05% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.96% | **+1.33%** |
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +1.90% | **+0.95%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.28% | **+0.33%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.27% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定トレード: 74件 (TP 22 / SL 49 / EXP 3)
- 最新: LIT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 876件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T15:35:19.482035+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.31% price=74020.1
- Funnel: target 777 → liquid 151 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=3, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +147.43% | $125,149,428.94 |
| HEI/USDT:USDT | +99.64% | $3,789,058.72 |
| ID/USDT:USDT | +43.87% | $3,192,617.13 |
| DELLSTOCK/USDT:USDT | +25.53% | $11,102,975.52 |
| LAB/USDT:USDT | +24.40% | $95,230,625.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AR/USDT:USDT | below_relative_strength | +5.75% | +4.44% |
| LIT/USDT:USDT | below_relative_strength | +5.56% | +4.25% |
| NEAR/USDT:USDT | below_relative_strength | +5.03% | +3.73% |
| DYDX/USDT:USDT | below_1h_threshold | +4.89% | +3.58% |
| INJ/USDT:USDT | below_1h_threshold | +4.70% | +3.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
