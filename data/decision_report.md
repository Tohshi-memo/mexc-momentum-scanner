# Decision Report

- generated_at: 2026-06-05T01:19:54.814215+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5689**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.35% / filled 20/20。**
- 全期間 MARKET基準: n=5689, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.42% | **+1.35%** |
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.75% | **+0.60%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.78% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.67% | **+1.25%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +3.43% | **+1.20%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.29% | **+0.78%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.97% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$98.05** / 初期 $100.00 (-1.95%)
- 確定トレード: 99件 (TP 30 / SL 66 / EXP 3)
- 最新: MONAD/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1008件 (Win 239 / Loss 312 / Flat 457) / skip 1242件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-05T01:19:51.852951+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=63346.6
- Funnel: target 771 → liquid 163 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.8 >= 65=1, 4h RSI 75.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +83.77% | $11,580,538.84 |
| HOME/USDT:USDT | +23.96% | $7,410,973.26 |
| OPN/USDT:USDT | +23.92% | $36,637,094.27 |
| MEME/USDT:USDT | +9.32% | $2,018,949.25 |
| AAOISTOCK/USDT:USDT | +7.57% | $1,285,641.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +3.66% | +3.74% |
| RIVER/USDT:USDT | below_1h_threshold | +3.18% | +3.26% |
| BEAT/USDT:USDT | below_1h_threshold | +2.72% | +2.81% |
| AIA/USDT:USDT | below_1h_threshold | +2.29% | +2.37% |
| ALLO/USDT:USDT | below_1h_threshold | +2.05% | +2.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
