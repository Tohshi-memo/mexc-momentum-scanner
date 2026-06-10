# Decision Report

- generated_at: 2026-06-10T02:43:13.049265+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6180**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6180, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +3.90% | **+1.56%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_10PCT | 4/20 | 20.0% | +4.36% | **+0.87%** |
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_BB3S | 5/20 | 25.0% | +1.34% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| ASK_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.79% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.52** / 初期 $100.00 (+48.52%)
- 確定: 1197件 (Win 299 / Loss 376 / Flat 522) / skip 1544件
- 成長率目線: 平均log +0.000330 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_5PCT_LONG` EXPIRED account +0.00% 残高後 $148.52

## 4. Latest Market Context

- 更新: 2026-06-10T02:43:09.191054+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.52% price=61360.1
- Funnel: target 778 → liquid 149 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +69.33% | $19,465,513.11 |
| STG/USDT:USDT | +22.01% | $4,058,589.46 |
| HOME/USDT:USDT | +13.42% | $4,386,788.20 |
| JCT/USDT:USDT | +11.85% | $3,819,423.93 |
| SENT/USDT:USDT | +10.17% | $1,741,647.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +2.47% | +2.99% |
| UAI/USDT:USDT | below_1h_threshold | +1.06% | +1.58% |
| OPN/USDT:USDT | below_1h_threshold | +0.54% | +1.06% |
| IO/USDT:USDT | below_1h_threshold | +0.30% | +0.82% |
| SENT/USDT:USDT | below_1h_threshold | +0.30% | +0.82% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
