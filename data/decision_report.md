# Decision Report

- generated_at: 2026-05-07T13:20:14.130958+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3631**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3631, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.35% | **-0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.42% | **+0.64%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +5.66% | **+1.98%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.11% | **+1.58%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.94% | **+1.47%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.25% | **+1.13%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.82** / 初期 $100.00 (+8.82%)
- 確定: 125件 (Win 40 / Loss 48 / Flat 37) / skip 67件
- 成長率目線: 平均log +0.000676 / 幾何平均 +0.068% per trade / maxDD +2.62%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $108.82

## 4. Latest Market Context

- 更新: 2026-05-07T13:20:10.372728+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=81025.5
- Funnel: target 771 → liquid 181 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.3 >= 65=1, 4h RSI 70.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +89.14% | $11,516,190.95 |
| SATO/USDT:USDT | +77.66% | $2,937,815.98 |
| PENGUIN/USDT:USDT | +75.44% | $3,976,033.95 |
| DOGS/USDT:USDT | +52.83% | $16,920,897.65 |
| SIREN/USDT:USDT | +38.88% | $19,698,823.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +2.77% | +2.88% |
| PENGUIN/USDT:USDT | below_1h_threshold | +2.66% | +2.78% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.52% | +2.63% |
| DYDX/USDT:USDT | below_1h_threshold | +2.36% | +2.47% |
| SIREN/USDT:USDT | below_1h_threshold | +2.31% | +2.43% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
