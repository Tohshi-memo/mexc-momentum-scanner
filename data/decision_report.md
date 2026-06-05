# Decision Report

- generated_at: 2026-06-05T00:57:20.929280+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5687**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.24% / filled 20/20。**
- 全期間 MARKET基準: n=5687, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.24% | **+1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.59% | **+1.59%** |
| ASK | 20/20 | 100.0% | +1.30% | **+1.30%** |
| MARKET | 20/20 | 100.0% | +1.24% | **+1.24%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.62% | **+0.50%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.81% | **+1.35%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +3.43% | **+1.20%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.48% | **+0.89%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.07% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$98.05** / 初期 $100.00 (-1.95%)
- 確定トレード: 99件 (TP 30 / SL 66 / EXP 3)
- 最新: MONAD/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1008件 (Win 239 / Loss 312 / Flat 457) / skip 1240件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-05T00:57:15.261285+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.63% price=63450.1
- Funnel: target 771 → liquid 168 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +69.78% | $11,175,354.85 |
| HOME/USDT:USDT | +28.06% | $7,334,298.51 |
| OPN/USDT:USDT | +15.63% | $37,899,538.60 |
| AAOISTOCK/USDT:USDT | +9.05% | $1,287,481.50 |
| MEME/USDT:USDT | +8.31% | $2,020,825.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.84% | +4.47% |
| MYX/USDT:USDT | below_1h_threshold | +3.72% | +4.35% |
| SIREN/USDT:USDT | below_1h_threshold | +2.19% | +2.82% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.04% | +2.67% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.11% | +1.74% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
