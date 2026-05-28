# Decision Report

- generated_at: 2026-05-28T11:19:53.630796+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4959**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=4959, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.91% | **+1.53%** |
| ASK | 20/20 | 100.0% | +1.42% | **+1.42%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.91% | **+1.24%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.44% | **+1.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.34% | **+0.23%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.16% | **+0.23%** |
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +0.46% | **+0.20%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.04% | **+0.01%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.69% | **-0.27%** |

## 2. $100 Live Portfolio

- 残高: **$98.12** / 初期 $100.00 (-1.88%)
- 確定トレード: 69件 (TP 20 / SL 46 / EXP 3)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.12
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 694件 (Win 172 / Loss 220 / Flat 302) / skip 826件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GENIUS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T11:19:48.765527+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=73381.1
- Funnel: target 777 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +35.65% | $9,107,014.39 |
| PRL/USDT:USDT | +19.03% | $1,773,323.25 |
| ONDSSTOCK/USDT:USDT | +12.98% | $1,067,938.78 |
| NBISSTOCK/USDT:USDT | +12.36% | $1,975,405.64 |
| XLM/USDT:USDT | +9.48% | $122,862,689.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BUILDONBOB/USDT:USDT | below_1h_threshold | +1.94% | +1.94% |
| SNOWSTOCK/USDT:USDT | below_1h_threshold | +1.31% | +1.30% |
| PLAY/USDT:USDT | below_1h_threshold | +1.12% | +1.11% |
| XLM/USDT:USDT | below_1h_threshold | +1.07% | +1.07% |
| TXNSTOCK/USDT:USDT | below_1h_threshold | +0.78% | +0.77% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
