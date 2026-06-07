# Decision Report

- generated_at: 2026-06-07T16:46:54.935284+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5983**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5983, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.04% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +3.53% | **+2.47%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +4.04% | **+2.22%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| ASK_LONG | 20/20 | 100.0% | +1.53% | **+1.53%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +3.14% | **+1.26%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.05** / 初期 $100.00 (+52.05%)
- 確定: 1100件 (Win 267 / Loss 329 / Flat 504) / skip 1444件
- 成長率目線: 平均log +0.000381 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $152.05

## 4. Latest Market Context

- 更新: 2026-06-07T16:46:45.939961+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=62160.0
- Funnel: target 768 → liquid 122 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=44, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.9 >= 65=1, 4h RSI 92.1 >= 65=1, 4h RSI 80.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +21.23% | $1,549,860.78 |
| VELVET/USDT:USDT | +14.63% | $2,549,493.86 |
| ESPORTS/USDT:USDT | +7.84% | $3,505,918.46 |
| SKYAI/USDT:USDT | +6.76% | $45,930,851.74 |
| LAB/USDT:USDT | +6.57% | $62,443,160.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_relative_strength | +5.14% | +4.99% |
| ALLO/USDT:USDT | below_1h_threshold | +4.20% | +4.06% |
| BLESS/USDT:USDT | below_1h_threshold | +4.08% | +3.94% |
| PIPPIN/USDT:USDT | below_1h_threshold | +3.72% | +3.58% |
| H/USDT:USDT | below_1h_threshold | +3.48% | +3.34% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
