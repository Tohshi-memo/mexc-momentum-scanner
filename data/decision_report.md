# Decision Report

- generated_at: 2026-05-28T14:36:05.004110+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4967**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.52% / filled 20/20。**
- 全期間 MARKET基準: n=4967, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.14% | **+1.03%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.87% | **+0.83%** |
| ASK | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_FIB1272 | 13/20 | 65.0% | +0.84% | **+0.55%** |
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.88% | **+0.31%** |
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.21% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.06** / 初期 $100.00 (+28.06%)
- 確定: 702件 (Win 173 / Loss 220 / Flat 309) / skip 826件
- 成長率目線: 平均log +0.000352 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_8PCT_LONG` TP_HIT account +1.00% 残高後 $128.06

## 4. Latest Market Context

- 更新: 2026-05-28T14:36:02.046305+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=72921.5
- Funnel: target 776 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +33.78% | $11,438,931.50 |
| ESPORTS/USDT:USDT | +25.35% | $3,373,647.55 |
| ONDSSTOCK/USDT:USDT | +25.09% | $1,184,242.67 |
| XLM/USDT:USDT | +24.09% | $229,652,514.90 |
| PRL/USDT:USDT | +14.02% | $2,519,663.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.39% | +3.48% |
| DRAM/USDT:USDT | below_1h_threshold | +2.90% | +2.99% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +2.62% | +2.71% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.39% | +2.48% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.28% | +2.37% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
