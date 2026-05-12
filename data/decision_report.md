# Decision Report

- generated_at: 2026-05-12T13:38:04.504363+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4124**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4124, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.27% | **-1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.21% | **+0.10%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.11% | **+0.95%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.35% | **+0.94%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.81% | **+0.90%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.90% | **+0.86%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.39% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$115.06** / 初期 $100.00 (+15.06%)
- 確定: 260件 (Win 70 / Loss 88 / Flat 102) / skip 425件
- 成長率目線: 平均log +0.000540 / 幾何平均 +0.054% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.06

## 4. Latest Market Context

- 更新: 2026-05-12T13:38:01.091492+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.34% price=80576.4
- Funnel: target 763 → liquid 194 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.8 >= 65=1, 4h RSI 76.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +85.40% | $23,873,406.66 |
| GIGA/USDT:USDT | +54.49% | $6,909,678.62 |
| USELESS/USDT:USDT | +41.70% | $10,303,888.65 |
| SKYAI/USDT:USDT | +40.92% | $43,813,661.87 |
| GUA/USDT:USDT | +33.97% | $3,633,125.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +4.36% | +4.69% |
| SOLV/USDT:USDT | below_1h_threshold | +3.65% | +3.99% |
| USELESS/USDT:USDT | below_1h_threshold | +3.22% | +3.56% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.89% | +3.23% |
| B/USDT:USDT | below_1h_threshold | +2.33% | +2.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
