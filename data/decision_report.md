# Decision Report

- generated_at: 2026-05-19T15:23:51.302342+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4474**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4474, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.03% | **+0.02%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.18% | **-0.13%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.26% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +3.17% | **+2.11%** |
| MARKET_LONG | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.53% | **+0.83%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.08% | **+0.76%** |
| ASK_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.71** / 初期 $100.00 (+22.71%)
- 確定: 471件 (Win 124 / Loss 162 / Flat 185) / skip 564件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.043% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $122.71

## 4. Latest Market Context

- 更新: 2026-05-19T15:23:46.570674+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=76471.9
- Funnel: target 764 → liquid 134 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +31.59% | $14,798,418.95 |
| PLAY/USDT:USDT | +30.81% | $6,054,698.56 |
| EDEN/USDT:USDT | +25.85% | $3,916,392.38 |
| ENJ/USDT:USDT | +15.31% | $1,536,352.70 |
| ONT/USDT:USDT | +11.59% | $2,314,279.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +2.52% | +2.38% |
| KITE/USDT:USDT | below_1h_threshold | +0.89% | +0.75% |
| ZEC/USDT:USDT | below_1h_threshold | +0.65% | +0.51% |
| ONDO/USDT:USDT | below_1h_threshold | +0.64% | +0.50% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +0.61% | +0.47% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
