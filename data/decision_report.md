# Decision Report

- generated_at: 2026-05-21T15:54:37.434122+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4647**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4647, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.23% | **+0.17%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.05% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.54% | **+0.69%** |
| MARKET_LONG | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| ASK_LONG | 20/20 | 100.0% | +0.50% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 547件 (Win 138 / Loss 185 / Flat 224) / skip 661件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPOTSTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T15:54:34.532922+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=77165.2
- Funnel: target 766 → liquid 139 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.1 >= 65=1, 4h RSI 67.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +58.38% | $2,569,596.46 |
| FIDA/USDT:USDT | +54.57% | $16,355,631.88 |
| NEX/USDT:USDT | +52.36% | $1,965,413.72 |
| EDEN/USDT:USDT | +46.63% | $34,568,614.83 |
| PROVE/USDT:USDT | +44.30% | $7,225,795.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.00% | +3.71% |
| BSB/USDT:USDT | below_1h_threshold | +3.46% | +3.17% |
| ONDO/USDT:USDT | below_1h_threshold | +3.30% | +3.01% |
| MONAD/USDT:USDT | below_1h_threshold | +3.11% | +2.82% |
| NEAR/USDT:USDT | below_1h_threshold | +3.08% | +2.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
