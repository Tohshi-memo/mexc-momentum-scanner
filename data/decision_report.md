# Decision Report

- generated_at: 2026-05-22T17:14:04.274484+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4723**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4723, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.34% | **+1.21%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.80% | **+1.08%** |
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.84% | **+0.75%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.82% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.89% | **+1.14%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.39% | **+0.69%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.01% | **+0.40%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.40% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.04** / 初期 $100.00 (+23.04%)
- 確定: 569件 (Win 146 / Loss 187 / Flat 236) / skip 715件
- 成長率目線: 平均log +0.000364 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_8PCT_LONG` TP_HIT account +1.00% 残高後 $123.04

## 4. Latest Market Context

- 更新: 2026-05-22T17:14:01.722211+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=76930.3
- Funnel: target 768 → liquid 135 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +53.94% | $27,267,863.23 |
| GENIUS/USDT:USDT | +7.29% | $5,526,591.11 |
| GUA/USDT:USDT | +4.17% | $1,046,518.56 |
| USELESS/USDT:USDT | +3.12% | $1,152,374.03 |
| GRASS/USDT:USDT | +2.96% | $8,590,504.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +1.93% | +1.91% |
| GENIUS/USDT:USDT | below_1h_threshold | +1.28% | +1.26% |
| NEX/USDT:USDT | below_1h_threshold | +1.21% | +1.19% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.13% | +1.10% |
| GUA/USDT:USDT | below_1h_threshold | +0.97% | +0.95% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
