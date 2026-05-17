# Decision Report

- generated_at: 2026-05-17T14:33:32.342929+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4404**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4404, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.48% | **-0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.86% | **+0.57%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.38% | **+0.30%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.21% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.89% | **+1.32%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.50% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| MARKET_LONG | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.83% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$118.52** / 初期 $100.00 (+18.52%)
- 確定: 401件 (Win 103 / Loss 137 / Flat 161) / skip 564件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $118.52

## 4. Latest Market Context

- 更新: 2026-05-17T14:33:29.919917+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=77960.6
- Funnel: target 760 → liquid 122 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.8 >= 65=1, 4h RSI 78.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +55.77% | $1,395,090.02 |
| BSB/USDT:USDT | +54.16% | $15,959,685.67 |
| AIA/USDT:USDT | +35.11% | $17,150,372.47 |
| CGPT/USDT:USDT | +17.95% | $2,413,029.52 |
| KAIA/USDT:USDT | +17.09% | $3,114,873.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +3.19% | +3.45% |
| DUSK/USDT:USDT | below_1h_threshold | +2.59% | +2.85% |
| ORDI/USDT:USDT | below_1h_threshold | +1.39% | +1.65% |
| GUA/USDT:USDT | below_1h_threshold | +1.20% | +1.46% |
| RUNE/USDT:USDT | below_1h_threshold | +1.09% | +1.35% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
