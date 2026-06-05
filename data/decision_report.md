# Decision Report

- generated_at: 2026-06-05T14:56:49.678338+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5724**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=5724, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.99% | **+1.99%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.48% | **+1.11%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.42% | **+0.35%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.39% | **+1.04%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.21% | **+0.67%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.81% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1010件 (Win 239 / Loss 313 / Flat 458) / skip 1275件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-05T14:56:46.648316+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=60747.7
- Funnel: target 773 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +79.60% | $29,448,099.41 |
| BABY/USDT:USDT | +33.71% | $12,747,830.99 |
| BEAT/USDT:USDT | +21.48% | $32,464,774.47 |
| AAOISTOCK/USDT:USDT | +15.11% | $3,710,951.23 |
| CLO/USDT:USDT | +12.71% | $1,407,880.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.77% | +4.69% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +4.24% | +4.17% |
| CLO/USDT:USDT | below_1h_threshold | +3.18% | +3.11% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +3.01% | +2.93% |
| BEAT/USDT:USDT | below_1h_threshold | +2.89% | +2.82% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
