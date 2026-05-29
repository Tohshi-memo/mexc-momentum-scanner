# Decision Report

- generated_at: 2026-05-29T00:19:33.542648+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4996**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.62% / filled 20/20。**
- 全期間 MARKET基準: n=4996, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.05% | **+0.82%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.40% | **+0.70%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.76% | **+0.34%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.69% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.23** / 初期 $100.00 (+28.23%)
- 確定: 727件 (Win 175 / Loss 222 / Flat 330) / skip 830件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $128.23

## 4. Latest Market Context

- 更新: 2026-05-29T00:19:30.809129+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=73816.6
- Funnel: target 773 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +44.57% | $20,021,519.73 |
| DELLSTOCK/USDT:USDT | +32.51% | $7,001,966.47 |
| CLO/USDT:USDT | +22.57% | $1,210,200.45 |
| ALGO/USDT:USDT | +12.47% | $3,342,987.79 |
| BSB/USDT:USDT | +11.21% | $13,312,979.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +2.98% | +2.68% |
| RIF/USDT:USDT | below_1h_threshold | +2.89% | +2.58% |
| JTO/USDT:USDT | below_1h_threshold | +2.03% | +1.72% |
| ALGO/USDT:USDT | below_1h_threshold | +1.47% | +1.17% |
| FIDA/USDT:USDT | below_1h_threshold | +1.39% | +1.09% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
