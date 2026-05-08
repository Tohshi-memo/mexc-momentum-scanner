# Decision Report

- generated_at: 2026-05-08T14:47:41.725476+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3792**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.35% / filled 20/20。**
- 全期間 MARKET基準: n=3792, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.47% | **+1.47%** |
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.59% | **+0.87%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.92% | **+0.78%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.21% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +2.92% | **+2.92%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.31% | **+0.72%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.04% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 191件 (Win 48 / Loss 64 / Flat 79) / skip 162件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T14:47:38.419323+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.79% price=80246.5
- Funnel: target 773 → liquid 184 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +47.88% | $13,661,087.81 |
| PHAROS/USDT:USDT | +47.12% | $12,766,595.28 |
| PLAY/USDT:USDT | +37.62% | $13,669,324.27 |
| COLLECT/USDT:USDT | +32.07% | $1,223,078.11 |
| AGT/USDT:USDT | +27.81% | $5,946,044.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TIA/USDT:USDT | below_1h_threshold | +4.99% | +4.19% |
| SIREN/USDT:USDT | below_1h_threshold | +4.31% | +3.51% |
| GALA/USDT:USDT | below_1h_threshold | +3.41% | +2.62% |
| EIGEN/USDT:USDT | below_1h_threshold | +3.26% | +2.47% |
| ICP/USDT:USDT | below_1h_threshold | +3.19% | +2.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
