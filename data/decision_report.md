# Decision Report

- generated_at: 2026-06-10T04:14:01.455018+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6184**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=6184, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +4.06% | **+1.42%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.55% | **+0.50%** |
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |
| ASK | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.33% | **+0.93%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| MARKET_LONG | 20/20 | 100.0% | +0.91% | **+0.91%** |
| ASK_LONG | 20/20 | 100.0% | +0.74% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.52** / 初期 $100.00 (+48.52%)
- 確定: 1200件 (Win 299 / Loss 376 / Flat 525) / skip 1545件
- 成長率目線: 平均log +0.000330 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $148.52

## 4. Latest Market Context

- 更新: 2026-06-10T04:13:58.269940+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=61439.9
- Funnel: target 778 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +21.57% | $26,798,755.20 |
| STG/USDT:USDT | +15.36% | $4,589,227.33 |
| UB/USDT:USDT | +11.58% | $1,592,315.26 |
| HOME/USDT:USDT | +11.06% | $4,251,240.28 |
| OPN/USDT:USDT | +10.71% | $2,179,379.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.50% | +3.63% |
| BLESS/USDT:USDT | below_1h_threshold | +1.32% | +1.45% |
| RUNE/USDT:USDT | below_1h_threshold | +0.75% | +0.88% |
| NEAR/USDT:USDT | below_1h_threshold | +0.70% | +0.83% |
| UAI/USDT:USDT | below_1h_threshold | +0.63% | +0.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
