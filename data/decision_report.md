# Decision Report

- generated_at: 2026-05-30T14:34:50.647440+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5131**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.09% / filled 20/20。**
- 全期間 MARKET基準: n=5131, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.11% | **+1.05%** |
| LIMIT_BB3S | 7/17 | 41.2% | +2.40% | **+0.99%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.17% | **+0.82%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.14% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.48% | **+1.39%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.73% | **+0.51%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.54% | **+0.38%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.54% | **+0.27%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.39% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.00** / 初期 $100.00 (+24.00%)
- 確定: 786件 (Win 183 / Loss 240 / Flat 363) / skip 906件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +5.48%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $124.00

## 4. Latest Market Context

- 更新: 2026-05-30T14:34:48.082871+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=74007.8
- Funnel: target 773 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +62.80% | $3,780,176.10 |
| LAB/USDT:USDT | +35.98% | $144,070,615.31 |
| STG/USDT:USDT | +34.28% | $2,134,566.36 |
| H/USDT:USDT | +27.89% | $7,241,460.63 |
| NFP/USDT:USDT | +27.53% | $3,703,601.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +3.81% | +3.54% |
| STG/USDT:USDT | below_1h_threshold | +3.33% | +3.05% |
| DYDX/USDT:USDT | below_1h_threshold | +2.85% | +2.58% |
| ID/USDT:USDT | below_1h_threshold | +1.63% | +1.36% |
| UB/USDT:USDT | below_1h_threshold | +1.54% | +1.26% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
