# Decision Report

- generated_at: 2026-05-19T08:18:36.555002+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4465**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4465, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +1.04% | **+0.73%** |
| ASK | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.24% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.44% | **+1.08%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.37% | **+0.83%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +1.55% | **+0.78%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +2.01% | **+0.50%** |
| MARKET_LONG | 20/20 | 100.0% | +0.29% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.06** / 初期 $100.00 (+23.06%)
- 確定: 462件 (Win 122 / Loss 158 / Flat 182) / skip 564件
- 成長率目線: 平均log +0.000449 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $123.06

## 4. Latest Market Context

- 更新: 2026-05-19T08:18:34.336355+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=77110.4
- Funnel: target 763 → liquid 137 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +32.23% | $2,360,088.75 |
| RON/USDT:USDT | +26.48% | $8,946,261.77 |
| PLAY/USDT:USDT | +21.64% | $2,337,018.37 |
| ONDO/USDT:USDT | +12.48% | $53,932,596.87 |
| ONT/USDT:USDT | +12.30% | $1,064,840.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +0.47% | +0.59% |
| ONT/USDT:USDT | below_1h_threshold | +0.31% | +0.43% |
| INJ/USDT:USDT | below_1h_threshold | +0.28% | +0.40% |
| LIT/USDT:USDT | below_1h_threshold | +0.14% | +0.26% |
| NICKEL/USDT:USDT | below_1h_threshold | +0.10% | +0.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
