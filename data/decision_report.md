# Decision Report

- generated_at: 2026-05-28T08:30:20.805565+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4956**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.10% / filled 20/20。**
- 全期間 MARKET基準: n=4956, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +3.10% | **+2.64%** |
| LIMIT_3PCT | 14/20 | 70.0% | +3.22% | **+2.25%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.04% | **+1.83%** |
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |
| LIMIT_4PCT | 9/20 | 45.0% | +1.86% | **+0.84%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.03% | **+1.21%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.17% | **+1.03%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.91% | **+0.98%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.76% | **+0.38%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.40% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$98.12** / 初期 $100.00 (-1.88%)
- 確定トレード: 69件 (TP 20 / SL 46 / EXP 3)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.12
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 691件 (Win 172 / Loss 220 / Flat 299) / skip 826件
- 成長率目線: 平均log +0.000344 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T08:30:18.732613+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=73240.8
- Funnel: target 777 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +34.20% | $8,274,078.75 |
| NBISSTOCK/USDT:USDT | +13.92% | $1,787,483.89 |
| PRL/USDT:USDT | +12.77% | $1,236,532.74 |
| ONDSSTOCK/USDT:USDT | +12.59% | $1,044,982.09 |
| BILL/USDT:USDT | +10.31% | $11,041,891.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.66% | +4.96% |
| ONDSSTOCK/USDT:USDT | below_1h_threshold | +3.09% | +3.39% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.25% | +1.55% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +0.94% | +1.24% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.94% | +1.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
