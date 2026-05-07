# Decision Report

- generated_at: 2026-05-07T06:37:33.755728+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3580**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3580, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_BB3S | 5/18 | 27.8% | +2.00% | **+0.55%** |
| ASK | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.21% | **+0.91%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.99% | **+0.89%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.95% | **+0.58%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.97% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.76** / 初期 $100.00 (+7.76%)
- 確定: 74件 (Win 28 / Loss 29 / Flat 17) / skip 67件
- 成長率目線: 平均log +0.001010 / 幾何平均 +0.101% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $107.76

## 4. Latest Market Context

- 更新: 2026-05-07T06:37:30.474815+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=81248.4
- Funnel: target 770 → liquid 187 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.0 >= 65=1, 4h RSI 81.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +291.35% | $1,817,074.61 |
| B3/USDT:USDT | +84.83% | $9,639,571.26 |
| DOGS/USDT:USDT | +71.71% | $12,585,697.09 |
| PENGUIN/USDT:USDT | +57.86% | $1,423,473.27 |
| FHE/USDT:USDT | +31.13% | $17,086,950.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +4.23% | +3.98% |
| SIREN/USDT:USDT | below_1h_threshold | +4.14% | +3.89% |
| PENGUIN/USDT:USDT | below_1h_threshold | +2.84% | +2.59% |
| IO/USDT:USDT | below_1h_threshold | +2.08% | +1.84% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +1.68% | +1.43% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
