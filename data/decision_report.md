# Decision Report

- generated_at: 2026-06-14T14:13:37.025466+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6668**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.28% / filled 20/20。**
- 全期間 MARKET基準: n=6668, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.28% | **+2.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.28% | **+2.28%** |
| ASK | 20/20 | 100.0% | +1.94% | **+1.94%** |
| LIMIT_1PCT | 14/20 | 70.0% | +0.34% | **+0.24%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.43% | **+0.22%** |
| ASK_LONG | 20/20 | 100.0% | +0.07% | **+0.07%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: H/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$169.52** / 初期 $100.00 (+69.52%)
- 確定: 1541件 (Win 408 / Loss 488 / Flat 645) / skip 1688件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $169.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 58件 (Win 19 / Loss 12 / Flat 27) / skip 21件
- 成長率目線: 平均log -0.000173 / 幾何平均 -0.017% per trade / maxDD +2.00%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $99.00

## 5. Latest Market Context

- 更新: 2026-06-14T14:13:28.933485+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64250.3
- Funnel: target 770 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRADOOR/USDT:USDT | +29.58% | $8,444,196.61 |
| ZKC/USDT:USDT | +28.36% | $1,456,097.95 |
| CLO/USDT:USDT | +26.87% | $1,071,805.59 |
| OPG/USDT:USDT | +22.38% | $1,671,513.62 |
| BANANAS31/USDT:USDT | +18.86% | $1,467,687.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRADOOR/USDT:USDT | below_1h_threshold | +4.13% | +4.18% |
| BSB/USDT:USDT | below_1h_threshold | +2.53% | +2.58% |
| ZKC/USDT:USDT | below_1h_threshold | +2.03% | +2.08% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.69% | +1.74% |
| JASMY/USDT:USDT | below_1h_threshold | +1.18% | +1.23% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
