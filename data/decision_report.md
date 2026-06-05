# Decision Report

- generated_at: 2026-06-05T14:17:52.913204+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5723**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.18% / filled 20/20。**
- 全期間 MARKET基準: n=5723, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.76% | **+1.76%** |
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.48% | **+1.11%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.94% | **+0.66%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.39% | **+1.04%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.65% | **+0.91%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.24% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1010件 (Win 239 / Loss 313 / Flat 458) / skip 1274件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-05T14:17:50.631849+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=60796.8
- Funnel: target 773 → liquid 160 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +77.13% | $28,712,168.51 |
| BABY/USDT:USDT | +45.27% | $12,235,449.90 |
| BEAT/USDT:USDT | +19.22% | $29,758,679.05 |
| HEI/USDT:USDT | +15.11% | $2,576,482.09 |
| AAOISTOCK/USDT:USDT | +12.36% | $3,603,360.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +4.92% | +4.76% |
| LIT/USDT:USDT | below_1h_threshold | +3.31% | +3.15% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.56% | +2.40% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.49% | +2.34% |
| MEME/USDT:USDT | below_1h_threshold | +2.11% | +1.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
