# Decision Report

- generated_at: 2026-06-10T05:39:31.217264+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6185**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.54% / filled 20/20。**
- 全期間 MARKET基準: n=6185, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +4.06% | **+1.42%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| ASK | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.60% | **+0.54%** |
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.33% | **+0.93%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| MARKET_LONG | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.89% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.52** / 初期 $100.00 (+48.52%)
- 確定: 1201件 (Win 299 / Loss 376 / Flat 526) / skip 1545件
- 成長率目線: 平均log +0.000329 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $148.52

## 4. Latest Market Context

- 更新: 2026-06-10T05:39:25.866819+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=61195.6
- Funnel: target 780 → liquid 148 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +28.29% | $5,076,779.14 |
| BTW/USDT:USDT | +26.36% | $28,409,549.58 |
| UB/USDT:USDT | +9.57% | $1,750,989.73 |
| HOME/USDT:USDT | +8.99% | $4,163,116.06 |
| OPN/USDT:USDT | +8.12% | $2,233,044.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.95% | +3.07% |
| BLESS/USDT:USDT | below_1h_threshold | +1.70% | +1.82% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.39% | +1.51% |
| OPN/USDT:USDT | below_1h_threshold | +1.32% | +1.44% |
| HOME/USDT:USDT | below_1h_threshold | +0.74% | +0.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
