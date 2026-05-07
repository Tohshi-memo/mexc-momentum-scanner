# Decision Report

- generated_at: 2026-05-07T01:52:37.288446+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3529**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3529, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.36% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.89% | **+1.70%** |
| MARKET_LONG | 20/20 | 100.0% | +1.63% | **+1.63%** |
| ASK_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.75% | **+1.31%** |
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +2.73% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$101.63** / 初期 $100.00 (+1.63%)
- 確定: 24件 (Win 8 / Loss 9 / Flat 7) / skip 66件
- 成長率目線: 平均log +0.000675 / 幾何平均 +0.068% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $101.63

## 4. Latest Market Context

- 更新: 2026-05-07T01:52:32.900894+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=81124.6
- Funnel: target 770 → liquid 189 → pre 50 → checked 50 → surge 6 → strict 0
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1, 4h RSI 78.9 >= 65=1, 4h RSI 77.5 >= 65=1, 4h RSI 70.4 >= 65=1, 4h RSI 97.4 >= 65=1, 4h RSI 74.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +131.67% | $1,042,455.26 |
| DOGS/USDT:USDT | +59.85% | $6,855,956.31 |
| PENGUIN/USDT:USDT | +30.35% | $1,055,289.53 |
| FHE/USDT:USDT | +28.39% | $16,315,973.10 |
| ZEREBRO/USDT:USDT | +14.71% | $2,032,266.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +3.58% | +3.38% |
| SIREN/USDT:USDT | below_1h_threshold | +1.60% | +1.40% |
| AR/USDT:USDT | below_1h_threshold | +1.40% | +1.21% |
| SILVER/USDT:USDT | below_1h_threshold | +1.33% | +1.14% |
| ALBSTOCK/USDT:USDT | below_1h_threshold | +1.16% | +0.97% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
