# Decision Report

- generated_at: 2026-05-20T18:33:48.087995+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4566**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4566, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-2.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.48% | **-2.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.42% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.24% | **+2.24%** |
| ASK_LONG | 20/20 | 100.0% | +1.72% | **+1.72%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.28% | **+1.50%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.37% | **+1.30%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +2.09% | **+1.25%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.95** / 初期 $100.00 (+24.95%)
- 確定: 528件 (Win 137 / Loss 177 / Flat 214) / skip 599件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $124.95

## 4. Latest Market Context

- 更新: 2026-05-20T18:33:43.495288+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=77443.0
- Funnel: target 759 → liquid 127 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +50.68% | $42,841,227.34 |
| EDEN/USDT:USDT | +9.67% | $28,391,490.85 |
| LAB/USDT:USDT | +8.93% | $43,825,095.23 |
| NIL/USDT:USDT | +8.34% | $1,687,322.84 |
| JTO/USDT:USDT | +7.70% | $1,160,503.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.95% | +3.07% |
| JTO/USDT:USDT | below_1h_threshold | +2.59% | +2.71% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.53% | +2.65% |
| BANANAS31/USDT:USDT | below_1h_threshold | +2.46% | +2.58% |
| SATO/USDT:USDT | below_1h_threshold | +2.34% | +2.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
