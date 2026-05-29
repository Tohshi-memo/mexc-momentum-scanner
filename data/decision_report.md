# Decision Report

- generated_at: 2026-05-29T06:29:35.396743+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5020**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.78% / filled 20/20。**
- 全期間 MARKET基準: n=5020, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +3.40% | **+1.02%** |
| ASK | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.52% | **+0.34%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.16% | **+0.17%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.18% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 841件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T06:29:30.764220+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=73740.1
- Funnel: target 777 → liquid 145 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +115.37% | $45,040,158.22 |
| DELLSTOCK/USDT:USDT | +36.41% | $8,367,218.18 |
| CTR/USDT:USDT | +29.74% | $1,252,179.39 |
| CLO/USDT:USDT | +19.57% | $1,613,078.68 |
| AIGENSYN/USDT:USDT | +17.62% | $1,264,983.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +3.18% | +3.07% |
| INJ/USDT:USDT | below_1h_threshold | +2.74% | +2.64% |
| LIT/USDT:USDT | below_1h_threshold | +2.53% | +2.43% |
| ALLO/USDT:USDT | below_1h_threshold | +2.25% | +2.14% |
| BSB/USDT:USDT | below_1h_threshold | +1.58% | +1.48% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
